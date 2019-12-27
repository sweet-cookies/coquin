<style scoped>

.timer-slider>>>.v-slider {
    height: 350px;
}

</style>

<template>

<v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app clipped>
        <v-list dense>
            <v-list-item link @click="persistent.currentPage = '/game'">
                <v-list-item-action>
                    <v-icon>mdi-gamepad-variant</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Jeu</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item link @click="persistent.currentPage = '/settings'">
                <v-list-item-action>
                    <v-icon>mdi-settings</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Configuration</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item link @click="persistent.currentPage = '/decks'">
                <v-list-item-action>
                    <v-icon>mdi-view-module</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Liste des decks</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item link @click="persistent.currentPage = '/cards'">
                <v-list-item-action>
                    <v-icon>mdi-relative-scale</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Liste des cartes</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item link @click="flushCache()">
                <v-list-item-action>
                    <v-icon color="grey">mdi-eraser</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title><font color="grey">Remise à zéro</font></v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item link @click="persistent.currentPage = '/rules'">
                <v-list-item-action>
                    <v-icon>mdi-library-books</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Règles du jeu</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-left>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" />

        <!-- Page name if not playing -->
        <div v-show="!persistent.currentPlayer">
            {{pages[persistent.currentPage].name}}
        </div>

        <!-- Game top menu player name-->
        <v-toolbar-title v-show="persistent.currentPlayer">
            <v-menu offset-y open-on-hover>
                <template v-slot:activator="{ on }">
                    <v-container no-gutters v-on="on">
                        {{persistent.currentPlayer}}</v-container>
                </template>
                <v-list>
                    <v-list-item v-for="name in persistent.playerList.filter(name => name != persistent.currentPlayer)" :key="name" @click="showPlayerHand(name)">
                        <v-list-item-title>{{ name }}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-toolbar-title>

        <!-- Game top menu -->
        <v-row v-if="persistent.currentPage == '/game'" no-gutters justify="end">
            <v-col align="right">
                <v-btn class="mx-1" @click="$refs.timer.timerOverlay = !$refs.timer.timerOverlay" color="primary" fab x-small>
                    <v-icon>mdi-alarm</v-icon>
                </v-btn>

                <!-- Finally disabled features, not that useful
                <v-btn class="mx-1" v-show="persistent.currentPlayer" @click="$refs.P.positionOverlay = !$refs.positionpopup.positionOverlay" color="primary" fab x-small>
                    <v-icon>mdi-account-multiple</v-icon>
                </v-btn> -->

                <!-- Next turn buttons mode standard-->
                <v-menu v-if="persistent.gameMode === 'standard' && !persistent.currentPlayer" offset-y open-on-hover>
                    <template v-slot:activator="{ on }">
                        <v-btn class="mx-1" color="success" v-on="on" :fab="false" rounded small>
                            <v-badge :color="persistent.turnNumberColor">
                                <template v-slot:badge>
                                    <span>{{persistent.turnNumber}}</span>
                                </template>
                                Suivant
                                <v-icon>mdi-arrow-right-bold</v-icon>
                            </v-badge>
                        </v-btn>
                    </template>
                    <v-list>
                        <v-list-item v-for="(player, name) in persistent.players" :key="name" @click="nextPlayer(name)">
                            <v-list-item-title>{{ name }}</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>

                <v-btn class="mx-1" color="error" v-if="persistent.gameMode === 'standard' && persistent.currentPlayer" @click="endTurn()" :fab="false" small>
                    <v-badge :color="persistent.turnNumberColor">
                        <template v-slot:badge>
                            <span>{{persistent.turnNumber}}</span>
                        </template>
                        Fin
                        <v-icon>mdi-arrow-right-bold</v-icon>
                    </v-badge>
                </v-btn>

                <!-- Next turn buttons mode random -->
                <v-btn v-if="persistent.gameMode === 'random' && !persistent.currentPlayer" @click="nextPlayer(null)" class="mx-1" color="success" fab x-small>
                    <v-badge :color="persistent.turnNumberColor">
                        <template v-slot:badge>
                            <span>{{persistent.turnNumber}}</span>
                        </template>
                        <v-icon>mdi-arrow-right-bold</v-icon>
                    </v-badge>
                </v-btn>

                <v-btn v-if="persistent.gameMode === 'random' && persistent.currentPlayer" @click="endTurn()" class="mx-1" color="error" fab x-small>
                    <v-badge :color="persistent.turnNumberColor">
                        <template v-slot:badge>
                            <span>{{persistent.turnNumber}}</span>
                        </template>
                        <v-icon>mdi-arrow-right-bold</v-icon>
                    </v-badge>
                </v-btn>

                <!-- Next turn buttons mode turn -->
                <v-btn v-if="persistent.gameMode === 'turn' && !persistent.currentPlayer" @click="nextPlayer(null)" class="mx-1" color="success" fab x-small>
                    <v-badge :color="persistent.turnNumberColor">
                        <template v-slot:badge>
                            <span>{{persistent.turnNumber}}</span>
                        </template>
                        <v-icon>mdi-arrow-right-bold</v-icon>
                    </v-badge>
                </v-btn>

                <v-btn v-if="persistent.gameMode === 'turn' && persistent.currentPlayer" @click="endTurn()" class="mx-1" color="error" fab x-small>
                    <v-badge :color="persistent.turnNumberColor">
                        <template v-slot:badge>
                            <span>{{persistent.turnNumber}}</span>
                        </template>
                        <v-icon>mdi-arrow-right-bold</v-icon>
                    </v-badge>
                </v-btn>
            </v-col>
        </v-row>
    </v-app-bar>

    <!-- Settings content -->
    <v-content v-if="persistent.currentPage == '/settings'">
        <v-container fluid>
            <Settings v-bind:Persistent.sync="persistent" :PersistentTemplate="persistentTemplate" :EndCards="endCards" :Decks="decks" />
        </v-container>
    </v-content>

    <!-- Game content -->
    <v-content v-if="persistent.currentPage == '/game'">
        <v-container class="fill-height" fluid>
            <Timer ref="timer" />
            <!-- Finally disabled features, not that useful
            <PositionPopup ref="positionpopup" /> -->

            <v-overlay :value="handPopupPlayerName != null" opacity="0.6">
                <!-- https://vuejs.org/v2/guide/components-custom-events.html#Binding-Native-Events-to-Components -->
                <Hand v-if="handPopupPlayerName != null" v-bind:popupModePlayerName.sync="handPopupPlayerName" :persistent="persistent" :cards="cards" :decks="persistentDecks" />
            </v-overlay>

            <Decks :decks="persistentDecks" :cards="cards" :persistent="persistent" v-if="resetHack" />
        </v-container>
    </v-content>

    <!-- Rules content -->
    <v-content v-if="persistent.currentPage == '/rules'">
        <v-container fluid>
            <Rules/>
        </v-container>
    </v-content>

    <!-- DecksList content -->
    <v-content v-if="persistent.currentPage == '/decks'">
        <v-container fluid>
            <DecksList :cards="cards" :decks="decks" />
        </v-container>
    </v-content>

    <!-- CardsList content -->
    <v-content v-if="persistent.currentPage == '/cards'">
        <v-container fluid>
            <CardsList :decks="decks" :cards="cards" />
        </v-container>
    </v-content>


    <!-- Game footer -->
    <v-footer app padless v-if="persistent.currentPage == '/game'">
        <v-tabs background-color="#303030" v-model="persistent.selectedDeck" grow centered height=50 icons-and-text show-arrows>
            <v-tabs-slider></v-tabs-slider>

            <v-tab v-if="persistent.handEnabled" href="#tab-hand">
                <p class="text-capitalize">Main</p>
                <v-icon>mdi-checkbox-multiple-blank-outline</v-icon>
            </v-tab>



            <v-tab v-for="ingameType in deckTypeOrdering.filter(value => Object.keys(persistent.selectedDecks).includes(value))" :key="ingameType" :href="'#tab-' + ingameType">
                <p class="text-capitalize">{{ingameType}}</p>
                <v-icon>{{persistentDecks[persistent.selectedDecks[ingameType]].icon}}</v-icon>
            </v-tab>

        </v-tabs>

    </v-footer>
</v-app>

</template>

<script>

// Expire/expire cache 24h on persistent storage
var hours = 6; // Reset when storage is more than 24hours
var now = new Date().getTime();
var setupTime = localStorage.getItem('setupTime');
if (setupTime == null) {
    window.console.log("--setCacheExpire")
    localStorage.setItem('setupTime', now)
} else {
    window.console.log("--CheckCacheExpire")

    if (now - setupTime > hours * 60 * 60 * 1000) {
        window.console.log("--ClearCache")
        localStorage.clear()
        localStorage.setItem('setupTime', now);
    }
}


import Decks from './components/Decks';
import Timer from './components/Timer';
//import PositionPopup from './components/Position';
import Hand from './components/Hand';
import Rules from './game/Rules';
import Cards from './game/Cards';
import GameDecks from './game/Decks';
import DecksList from './components/DecksList';
import CardsList from './components/CardsList';
import Settings from './components/Settings';

function shuffle(a) {
    window.console.log("--shuffle");
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}

function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}

export default {
    name: 'App',
    props: {
        source: String,
    },
    components: {
        Decks,
        Timer,
        Hand,
        Rules,
        DecksList,
        CardsList,
        Settings,
        //PositionPopup,
    },
    mounted() {

        window.console.log("--mounted")
        if (localStorage.persistentDecks) {
            this.persistentDecks = JSON.parse(localStorage.getItem('persistentDecks'))
        }

        if (localStorage.persistent) {
            this.persistent = JSON.parse(localStorage.getItem('persistent'))
        }

        // Set new players from template
        this.initPlayers()
            // Init deck
        this.initDecks()

        // make sure everything work
        //this.triggerResetHack()
    },
    // see deep watch https://vuejs.org/v2/api/#watch
    watch: {
        persistentDecks: {
            handler: function(val) {
                localStorage.setItem('persistentDecks', JSON.stringify(val))
            },
            deep: true
        },
        persistent: {
            handler: function(val) {
                localStorage.setItem('persistent', JSON.stringify(val))
            },
            deep: true
        }
    },

    data: () => ({
        cards: Cards.getCards(),
        endCards: Cards.getEndCards(),
        questionCards: Cards.getQuestionCards(),
        decks: GameDecks.getDecks(),
        persistentDecks: GameDecks.getDecks(),
        handPopupPlayerName: null,
        playerTemplate: {
            "hand": [], // {"card_id": "h1", "deck": "deck1"}
        },
        pages: {
            '/game': {
                'name': ""
                    // 'name': "Tour: 0"
                    // 'name': "Joueur suivant"
            },
            '/settings': {
                'name': "Configuration"
            },
            '/rules': {
                'name': "Règles du jeu"
            },
            '/decks': {
                'name': "Liste des decks"
            },
            '/cards': {
                'name': "Liste des cartes"
            },

        },
        deckTypeOrdering: ['soft', 'coquine', 'hot', 'positions'],
        persistentTemplate: {
            currentPage: '/rules',
            playerList: ["Joueur 1", "Joueur 2"],
            endGameCards: [],
            randomEnd: false,
            turnNumber: 0,
            turnNumberColor: "#303030",
            players: {},
            currentPlayer: null,
            lastPlayer: null,
            gameMode: "standard", // can be "standard" or "turn" or "random"
            selectedDecks: {
                'soft': 'soft_plus',
                'coquine': 'coquin_plus',
                'hot': 'hot_plus_ech',
                'positions': 'positions_3_plus'
            },
            selectedDeck: null,
            handEnabled: true,
        },
        persistent: {},
        drawer: null,
        resetHack: true,
        resetHackTimer: {},
    }),
    methods: {
        triggerResetHack: function() {
            // Reset hack is here to hide and display components. The goal is to rebuild
            // the vue component to get back on his local default values (kind of this.$forceUpdate();).
            this.resetHack = false

            this.resetHackTimer = setInterval(() => {
                clearInterval(this.resetHackTimer)
                this.resetHack = true
            }, 300)

        },
        endTurn: function() {
            window.console.log("--endTurn")

            // Flush deck picked cards and drawer value to set back the default
            this.initDecks()
            this.initPlayers()
            this.prepareDecksForNextPlayer()
                // Reset the selected user
            this.persistent.lastPlayer = this.persistent.currentPlayer
            this.persistent.currentPlayer = null
            this.persistent.turnNumber += 1

            // Directly trigger next player in case of turn mode or random mode.
            // Remove it if you want to get back on default behavior with a pause between each turn
            if (this.persistent.gameMode == "turn" || this.persistent.gameMode == "random") {
                this.nextPlayer(null)
            }
        },

        showPlayerHand: function(playerName) {
            window.console.log("--showPlayerHand")
            this.handPopupPlayerName = playerName
        },
        nextPlayer: function(playerName) {
            window.console.log("--nextPlayer")

            // Standard mode
            if (playerName && this.persistent.gameMode == "standard") {
                this.persistent.currentPlayer = playerName
            } else if (this.persistent.gameMode == "turn") { // turn mode
                var playerIndex = this.persistent.playerList.indexOf(this.persistent.lastPlayer) + 1
                if (playerIndex >= this.persistent.playerList.length) {
                    this.persistent.currentPlayer = this.persistent.playerList[0]
                } else {
                    this.persistent.currentPlayer = this.persistent.playerList[playerIndex]
                }
            } else { // Random mode
                var randomPlayer = Math.floor(Math.random() * (this.persistent.playerList.length))
                this.persistent.currentPlayer = this.persistent.playerList[randomPlayer]
            }

            this.triggerResetHack()
        },
        flushCache: function() {
            window.console.log("--flushCache")
            localStorage.clear()
            location.reload(true)
        },

        initPlayers: function() {
            window.console.log("--initPlayers")
            var playerIndex
            var player

            // Cleanup removed players
            for (player in this.persistent.players) {
                if (!this.persistent.playerList.includes(player)) {
                    delete this.persistent.players[player]
                }
            }
            for (playerIndex in this.persistent.playerList) {
                player = this.persistent.playerList[playerIndex]

                if (!this.persistent.players[player]) {
                    this.persistent.players[player] = Object.assign({}, this.playerTemplate)
                    this.persistent.players[player] = {
                        "hand": [{
                            "card_id": "hbg1",
                            "deck": null
                        }], // {"card_id": "h1", "deck": "deck1"}
                    }
                }
            }
        },
        prepareDecksForNextPlayer: function() {
            var deck
            for (deck in this.persistentDecks) {
                // Put all picked cards into discard
                if (this.persistentDecks[deck].pickedCards.length > 0 && this.persistentDecks[deck].pickedCards[0] != this.persistentDecks[deck].background) {
                    this.persistentDecks[deck].discardedCards = this.persistentDecks[deck].discardedCards.concat(this.persistentDecks[deck].pickedCards)
                    this.persistentDecks[deck].discardedCards = this.persistentDecks[deck].discardedCards.filter(onlyUnique)
                    this.persistentDecks[deck].pickedCards = []
                }
                // Reset card number selector
                this.persistentDecks[deck].drawNumber = this.persistentDecks[deck].defaultDrawNumber
                    // Reset for next player to display the background before draw a card
                if (this.persistentDecks[deck].pickedCards.length == 0) {
                    this.persistentDecks[deck].pickedCards = [this.persistentDecks[deck].background]
                }
            }
        },
        initDecks: function() {
            window.console.log("--initDecks")
            var deck
            var cardId
            var i
            for (deck in this.persistentDecks) {
                if (!Object.values(this.persistent.selectedDecks).includes(deck)) {
                    continue
                }
                // Build the deck cards if the deck is empty
                if (this.persistentDecks[deck].discardedCards.length == 0 && this.persistentDecks[deck].cards.length == 0 && this.persistentDecks[deck].pickedCards.length == 0) {
                    // For each card type
                    for (cardId in this.persistentDecks[deck].deckCards) {

                        if (cardId == "randomQuestion") {
                            // Push as many cards as described into deckCards
                            var questions = shuffle(Object.keys(this.questionCards)).splice(0, this.persistentDecks[deck].deckCards[cardId])
                            for (var questionId of questions) {
                                this.persistentDecks[deck].cards.push(questionId)
                            }
                        } else {
                            // Push as many cards as described into deckCards
                            for (i = 0; i < this.persistentDecks[deck].deckCards[cardId]; i++) {
                                this.persistentDecks[deck].cards.push(cardId)
                            }
                        }
                    }
                    // Add end game card for hot deck, if selceted
                    if (this.persistent.endStep != 'Aucune' && deck == this.persistent.selectedDecks[this.persistent.endStep] && this.persistent.endGameCards) {
                        window.console.log("Adding random cards")
                        window.console.log(deck)

                        for (cardId of this.persistent.endGameCards) {
                            this.persistentDecks[deck].cards.push(cardId)
                        }
                    }

                    // Shuffle the deck
                    this.persistentDecks[deck].cards = shuffle(this.persistentDecks[deck].cards)

                    // Reset for next player to display the background before draw a card
                    if (this.persistentDecks[deck].pickedCards.length == 0) {
                        this.persistentDecks[deck].pickedCards = [this.persistentDecks[deck].background]
                    }
                }
            }
        },
    },
    created() {
        window.console.log("--created")
            // Init persistent from template. It will be filled later by local storage if existing
        this.persistent = Object.assign({}, this.persistentTemplate)
        this.$vuetify.theme.dark = true
    },
}

</script>
