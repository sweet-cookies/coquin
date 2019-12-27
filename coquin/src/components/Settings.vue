

<template>

<v-container pa-0>

    <!-- Soft deck selection overlay -->
    <DeckSelectionOverlay :decks="Decks" deckType="soft" v-bind:selectedDeck.sync="selectedSoftDeck" v-bind:decksOverlay.sync="softDecksOverlay" />
    <!-- Hot deck selection overlay -->
    <DeckSelectionOverlay :decks="Decks" deckType="hot" v-bind:selectedDeck.sync="selectedHotDeck" v-bind:decksOverlay.sync="hotDecksOverlay" />
    <!-- Coquin deck selection overlay -->
    <DeckSelectionOverlay :decks="Decks" deckType="coquine" v-bind:selectedDeck.sync="selectedCoquinDeck" v-bind:decksOverlay.sync="coquineDecksOverlay" />
    <!-- Positions deck selection overlay -->
    <DeckSelectionOverlay :decks="Decks" deckType="positions" v-bind:selectedDeck.sync="selectedPositionsDeck" v-bind:decksOverlay.sync="positionsDecksOverlay" />

    <v-row justify="center">
        <v-col cols="12" sm="10" md="8" lg="6">
            <v-card ref="form">
                <v-card-text>
                    <v-img max-width="200" src="../assets/logo.svg"></v-img>
                    <v-spacer class="pt-4"></v-spacer>

                    <v-spacer class="pt-2"></v-spacer>

                    <!-- Player configuration -->
                    <p class="body-1 blue-grey--text">Nombre de joueurs</p>
                    <v-text-field outlined dense shaped readonly v-model="numberOfPlayers" prepend-icon="mdi-star-circle" :max="maxPlayers" min="1" step="1" style="width: 130px" :rules="[rules.required, rules.number, rules.numberMax]">
                        <template slot="prepend">
                            <v-btn @click="decPlayer()" color="grey" outlined fab x-small>
                                <v-icon>mdi-minus</v-icon>
                            </v-btn>
                        </template>

                        <template slot="append-outer">
                            <v-btn @click="incPlayer()" color="grey" outlined fab x-small>
                                <v-icon>mdi-plus-outline</v-icon>
                            </v-btn>
                        </template>
                    </v-text-field>
                    <v-text-field dense style="width: 200px" :key="playerId" v-for="playerId in Array(playerList.length).keys()" :ref="'player_'+playerId" v-model="playerList[playerId]" :rules="[rules.required, rules.maxChar, rules.playerName]" :label="'Num du joueur '+(playerId+1)"
                    placeholder="Nom du joueur" required></v-text-field>

                    <v-spacer class="pt-8"></v-spacer>

                    <!-- Mode configuration -->
                    <p class="body-1 blue-grey--text">Selection le mode de jeu</p>
                    <v-radio-group v-model="gameMode" :mandatory="true">
                        <p>Lancer des dés ou tirer des cartes d'un jeu classique. Le perdant est le joueur avec le plus petit score, le gagnant sera le joueur avec le plus haut score. Si vous n'avez pas cela, utiliser tout moyen qui vous passe par la tête
                            pour désigner un gagnant et un perdant.
                            <v-radio color="success" label="Classique" value="standard"></v-radio>
                        </p>
                        <p>Chacun son tour, un joueur tire une carte gage, il est considéré comme perdant.
                            <v-radio color="success" label="Chacun son tour" value="turn"></v-radio>
                        </p>
                        <p>Un perdant est défini aléatoirement chaque tour.
                            <v-radio color="success" label="Aléatoire" value="random"></v-radio>
                        </p>
                    </v-radio-group>

                    <v-spacer class="pt-4"></v-spacer>

                    <!-- Decks selection -->
                    <p class="body-1 blue-grey--text">Choix des étapes</p>
                    <p>Sélectionner les decks pour les différentes étapes que vous souhaitez utiliser pendant votre partie.</p>
                    <v-row>
                        <v-col md="2" align="end">Soft
                        </v-col>
                        <v-col md="auto" align="center">
                            <v-btn :color="getColor('soft')" @click="softDecksOverlay = !softDecksOverlay" rounded outlined>{{ getDeckProperty(Decks, selectedSoftDeck, "name")}}</v-btn>
                        </v-col>
                        <v-col>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col md="2" align="end">Coquin
                        </v-col>
                        <v-col md="auto" align="center">
                            <v-btn :color="getColor('coquine')" @click="coquineDecksOverlay = !coquineDecksOverlay" rounded outlined>{{getDeckProperty(Decks, selectedCoquinDeck, "name")}}</v-btn>
                        </v-col>
                        <v-col>
                        </v-col>
                    </v-row>

                    <v-row>
                        <v-col md="2" align="end">Hot
                        </v-col>
                        <v-col md="auto" align="left">
                            <v-btn :color="getColor('hot')" @click="hotDecksOverlay = !hotDecksOverlay" rounded outlined>{{getDeckProperty(Decks, selectedHotDeck, "name")}}</v-btn>
                        </v-col>
                        <v-col>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col md="2" align="end">Positions
                        </v-col>
                        <v-col md="auto" align="center">
                            <v-btn :color="getColor('positions')" @click="positionsDecksOverlay = !positionsDecksOverlay" rounded outlined>{{getDeckProperty(Decks, selectedPositionsDeck, "name")}}</v-btn>
                        </v-col>
                        <v-col>
                        </v-col>
                    </v-row>

                    <v-spacer class="pt-8"></v-spacer>

                    <!-- End game cards -->
                    <p class="body-1 blue-grey--text">Selection des cartes de fin de partie</p>
                    <p>Si vous souhaitez jouer avec des cartes de fin de partie, indiquer dans quelle étape les ajouter.</p>

                    <v-select v-model="endStep" style="width: 200px" :items="selectedSteps()" label="étape"></v-select>

                    <v-container class="pa-0" v-show="endStep != 'aucune'">
                        <v-row align="center" no-gutters>
                            <v-col align="start" sm>
                                <v-switch color="success" v-model="randomEnd" label="Carte de fin de partie aléatoire"></v-switch>
                            </v-col>
                            <v-col md="auto" align="start">
                                <v-text-field :disabled="!randomEnd" label="Nombre de carte" dense rounded readonly v-model="randomEndCardNumber" prepend-icon="mdi-star-circle" :max="getNumberOfEndCards" min="1" step="1" style="width: 230px">
                                    <template slot="prepend">
                                        <v-btn :disabled="!randomEnd" @click="decRandomEndCardNumber()" color="grey" outlined fab x-small>
                                            <v-icon>mdi-minus</v-icon>
                                        </v-btn>
                                    </template>

                                    <template slot="append-outer">
                                        <v-btn :disabled="!randomEnd" @click="incRandomEndCardNumber()" color="grey" outlined fab x-small>
                                            <v-icon>mdi-plus-outline</v-icon>
                                        </v-btn>
                                    </template>
                                </v-text-field>
                            </v-col>
                        </v-row>

                        <!-- Select end game cards -->
                        <v-card class="mx-auto" max-width="500" v-show="!randomEnd">
                            <v-container class="py-0">
                                <v-row align="center" justify="start">
                                    <!-- Selected cards -->
                                    <v-col v-for="(cardIndex, i) in selectedEndGameCards" :key="cardIndex" class="shrink">
                                        <v-chip color="success" class="ma-0" close @click:close="selectedEndGameCards.splice(i, 1)">
                                            {{ cardIndex }}
                                        </v-chip>
                                    </v-col>
                                </v-row>
                            </v-container>

                            <v-divider v-if="!allEndCardsSelected"></v-divider>

                            <!-- Available cards list -->
                            <v-list>
                                <template v-for="(card, cardId) in EndCards">
                                    <v-list-item v-if="!selectedEndGameCards.includes(cardId)" :key="cardId" @click="selectedEndGameCards.push(cardId)">
                                        <v-list-item-avatar>
                                            <v-chip color="grey">
                                                {{cardId}}
                                            </v-chip>
                                        </v-list-item-avatar>
                                        <div class="pb-3" v-text="card.text"></div>
                                    </v-list-item>
                                </template>
                            </v-list>
                        </v-card>
                    </v-container>
                </v-card-text>
                <v-divider class="mt-12"></v-divider>

                <v-divider></v-divider>
                <!-- Summit button -->
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="pink" @click="startNewGame()" outlined>Lancer la partie</v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>

</v-container>

</template>

<script>

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

import DeckSelectionOverlay from './DeckSelectionOverlay';
import Tools from './Tools';

export default {
    name: 'Settings',
    props: {
        Persistent: Object,
        EndCards: Object,
        Decks: Object,
        PersistentTemplate: Object,
    },
    components: {
        DeckSelectionOverlay,
    },
    mounted() {
        window.console.log("--Settings-mounted")
        if (this.Persistent.playerList) {
            this.numberOfPlayers = this.Persistent.playerList.length
            this.playerList = this.Persistent.playerList
        }
        if (this.Persistent.gameMode) {
            this.gameMode = this.Persistent.gameMode
        }
        if (this.Persistent.endStep) {
            this.endStep = this.Persistent.endStep
        }
        if (this.Persistent.randomEnd) {
            this.randomEnd = this.Persistent.randomEnd
        }
        if (this.Persistent.randomEndCardNumber) {
            this.randomEndCardNumber = this.Persistent.randomEndCardNumber
        }
        if (this.Persistent.selectedDecks) {
            // if (this.Persistent.selectedDecks.hasOwnProperty('coquine')) {
            this.selectedCoquinDeck = this.Persistent.selectedDecks['coquine'] || null
                // }
                // if (this.Persistent.selectedDecks.hasOwnProperty('soft')) {
            this.selectedSoftDeck = this.Persistent.selectedDecks['soft'] || null
                // }

            // if (this.Persistent.selectedDecks.hasOwnProperty('hot')) {
            this.selectedHotDeck = this.Persistent.selectedDecks['hot'] || null
                // }
                //
                // if (this.Persistent.selectedDecks.hasOwnProperty('positions')) {
            this.selectedPositionsDeck = this.Persistent.selectedDecks['positions'] || null
                // }
        }
        if (this.Persistent.endGameCards) {
            this.selectedEndGameCards = this.Persistent.endGameCards
        }
    },
    created() {},
    computed: {
        allEndCardsSelected() {
            return this.selectedEndGameCards.length === this.EndCards.length
        },
    },
    data: () => ({
        selectedEndGameCards: [],
        softDecksOverlay: false,
        hotDecksOverlay: false,
        positionsDecksOverlay: false,
        coquineDecksOverlay: false,
        selectedPositionsDeck: null,
        selectedHotDeck: null,
        selectedCoquinDeck: null,
        selectedSoftDeck: null,
        gameMode: 'standard',
        randomEnd: true,
        randomEndCardNumber: 2,
        endStep: 'aucune',
        maxPlayers: 10,
        configError: null,
        numberOfPlayers: 2,
        // Using an Object to be able to do dynamic set like playerList[playerId]
        playerList: [],
        rules: {
            required: value => !!value || 'This field is required.',
            numberMax: value => Number(value) <= 10 || 'Max 10',
            maxChar: value => {
                if (value && value.length <= 15) {
                    return true
                } else {
                    return 'Max 15'
                }
            },
            number: value => {
                return Number.isInteger(Number(value)) || 'Entrez un nombre.'
            },
            playerName: value => {
                const pattern = /^([0-9a-zA-Z -]+)$/
                return pattern.test(value) || 'Should not contain any special char.'
            },
        }
    }),
    watch: {
        numberOfPlayers: {
            handler: function(val) {
                if (this.rules.number(val) == true && this.rules.numberMax(val) == true) {
                    if (this.playerList.length > val) {

                        if (this.playerList.length > val) {
                            this.playerList.splice(val, this.playerList.length - val)
                        }

                    } else if (this.playerList.length < val) {
                        for (var i = 0; i < val; i++) {
                            if (!this.playerList[i]) {
                                this.playerList[i] = "Joueur ".concat(i + 1)
                            }
                        }
                    }
                }
            },
        },
    },
    methods: {
        selectedSteps: function() {
            var steps = ['aucune']
            if (this.selectedSoftDeck) {
                steps.push("soft")
            }
            if (this.selectedCoquinDeck) {
                steps.push("coquine")
            }
            if (this.selectedHotDeck) {
                steps.push("hot")
            }
            return steps
        },
        startNewGame: function() {
            window.console.log("--startNewGame");
            var newPersistent = this.PersistentTemplate
            newPersistent.playerList = this.playerList
            newPersistent.gameMode = this.gameMode
            newPersistent.randomEnd = this.randomEnd
            newPersistent.endStep = this.endStep
            newPersistent.randomEndCardNumber = this.randomEndCardNumber

            if (!this.randomEnd) {
                newPersistent.endGameCards = this.selectedEndGameCards
            } else {
                var randomEndGameCards = shuffle(Object.keys(this.EndCards))
                var endGameCards = randomEndGameCards.splice(0, this.randomEndCardNumber)
                newPersistent.endGameCards = endGameCards
            }

            newPersistent.selectedDecks = {}
            if (this.selectedSoftDeck) {
                newPersistent.selectedDecks["soft"] = this.selectedSoftDeck
            }
            if (this.selectedHotDeck) {
                newPersistent.selectedDecks["hot"] = this.selectedHotDeck
            }
            if (this.selectedCoquinDeck) {
                newPersistent.selectedDecks["coquine"] = this.selectedCoquinDeck
            }
            if (this.selectedPositionsDeck) {
                newPersistent.selectedDecks["positions"] = this.selectedPositionsDeck
            }

            // Redirect and start new game
            newPersistent.currentPage = '/game'

            // Reset local storage with new configuration and reset cache expire
            localStorage.clear()
            var now = new Date().getTime();
            localStorage.setItem('setupTime', now)

            this.$emit('update:persistent', newPersistent)
            location.reload(true)
        },
        getColor: Tools.getColor,
        getDeckProperty: Tools.getDeckProperty,
        getNumberOfEndCards: function() {
            window.console.log("--getNumberOfEndCards");
            return Object.keys(this.EndCards).length
        },
        incRandomEndCardNumber: function() {
            if (this.randomEndCardNumber < this.getNumberOfEndCards()) {
                this.randomEndCardNumber++
            }
        },
        decRandomEndCardNumber: function() {
            if (this.randomEndCardNumber > 1) {
                this.randomEndCardNumber--
            }
        },
        incPlayer: function() {
            if (this.numberOfPlayers < this.maxPlayers) {
                this.numberOfPlayers++
            }
        },
        decPlayer: function() {
            if (this.numberOfPlayers > 1) {
                this.numberOfPlayers--
            }
        },
    },
};

</script>
