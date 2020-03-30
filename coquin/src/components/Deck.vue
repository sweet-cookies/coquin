<style scoped>

.picker-slider >>> .v-slider {
    width: 90px;
}

</style>

<template>

<v-container pa-0>

    <!-- Deck -->
    <v-container>
        <v-card elevation="24" max-width="444" class="mx-auto">
            <v-system-bar lights-out></v-system-bar>
            <v-carousel ref="pickedCards" v-model="carouselPickedIndex" :continuous="true" show-arrows-on-hover :cycle="false" height="auto" :show-arrows="true" progress progress-color="grey" hide-delimiter-background hide-delimiters>
                <v-carousel-item v-for="(card, i) in decks[deck].pickedCards" :key="i">
                    <!-- <v-sheet :color="cards[card].image" height="100%" tile> -->

                    <!-- Regular deck -->
                    <v-sheet v-if="!cards[card].image_content" color="#484848" tile>
                        <v-row dense tile no-gutters>
                            <v-col align="start" class="mt-5">
                                <v-icon large v-if="cards[card].for" :color="getColor(cards[card].for)">{{ getIcon(cards[card].for) }}</v-icon>
                                <v-badge v-if="cards[card].timer" :color="getColor('timer-badge')">
                                    <template v-slot:badge>{{cards[card].timer}}min</template>
                                    <v-btn @click="startTimer(cards[card].timer)" :color="getColor('timer')" fab x-small>
                                                                  <v-icon>{{ getIcon("timer") }}</v-icon>
                                    </v-btn>
                                </v-badge>
                            </v-col>

                            <v-col align="end">
                                <v-container>
                                    <img width="50" height="50" :src="cards[card].image">
                                </v-container>
                            </v-col>
                        </v-row>
                        <!-- style="background: #121212" -->
                        <v-row dense no-gutters class="fill-height">
                            <v-col justify-self="center">
                                <v-container>
                                    <!-- here to add some padding -->
                                    <v-responsive min-height="220px">
                                        <div class="headline">
                                            {{ cards[card].text }}
                                        </div>
                                    </v-responsive>
                                </v-container>
                            </v-col>
                        </v-row>
                    </v-sheet>

                    <!-- Positions -->
                    <v-sheet v-if="cards[card].image_content" color="#484848" tile>
                        <v-row dense tile no-gutters>
                            <v-col align="right">
                                <v-container>
                                    <img height="50" width="50" :src="cards[card].image">
                                </v-container>
                            </v-col>
                        </v-row>
                        <!-- style="background: #121212" -->
                        <v-row dense no-gutters class="fill-height">
                            <v-col align="center">
                                <!-- here to add some padding -->
                                <v-responsive min-height="350px">
                                    <img contain width="100%" :src="cards[card].image_content">
                                </v-responsive>
                            </v-col>
                        </v-row>
                    </v-sheet>
                </v-carousel-item>
            </v-carousel>
            <v-container>
                <v-responsive min-height="130px">
                    <v-system-bar color="#1E1E1E"></v-system-bar>
                    <v-row v-show="decks[deck].cards.length > 0 && persistent.currentPlayer" align="center" justify="start" no-gutters>
                        <v-col justify-self="center">
                            <div class="ma-0">
                                <v-btn class="ma-2" outlined @click="drawCard(deck)" color="warning" small rounded>
                                    <v-icon left>mdi-cursor-pointer</v-icon>Piocher
                                </v-btn>
                            </div>
                        </v-col>
                        <v-col ld="auto">
                        </v-col>
                        <v-col justify-self="end">
                            <v-slider v-model="decks[deck].drawNumber" :tick-labels="[1,2,3]" thumb-color="warning" track-fill-color="warning" thumb-size="22" max="3" min="1" step="1" ticks="always" tick-size="5" thumb-label="always" class="picker-slider"></v-slider>
                        </v-col>
                    </v-row>
                    <v-row align="center" no-gutters>
                        <v-col>
                            <v-btn class="ma-1" v-show="decks[deck].pickedCards.length > 0 && pickedCardInfo(deck).type == 'action'" @click="takeCardInHand(deck)" outlined color="warning" rounded small>
                                <v-icon left>mdi-arrange-bring-forward</v-icon>Conserver</v-btn>
                        </v-col>
                        <v-col ld>
                        </v-col>
                        <v-col>
                            <v-btn v-show="decks[deck].pickedCards.length > 0 && pickedCardInfo(deck).type == 'end'" class="ma-2" outlined color="blue-grey" @click="backInTheDeck(deck)" small rounded>
                                <v-icon left>mdi-redo-variant</v-icon>Reposer</v-btn>
                        </v-col>
                    </v-row>
                </v-responsive>

            </v-container>
        </v-card>
    </v-container>


    <!-- Discarded Deck -->
    <v-container>
        <v-card elevation="24" max-width="444" class="mx-auto">
            <!-- <v-system-bar lights-out></v-system-bar> -->

            <v-list two-line style="background: #353535">
                <v-list-item>
                    <v-list-item-avatar>
                        <v-img src="../assets/discarded.svg"></v-img>
                    </v-list-item-avatar>
                    <v-list-item-content>
                        <v-list-item-title>Défausse</v-list-item-title>
                        <!-- <v-list-item-subtitle>discarded</v-list-item-subtitle> -->
                    </v-list-item-content>
                </v-list-item>
            </v-list>

            <!-- hide-delimiters -->
            <v-carousel ref="DiscardedDeck" v-model="carouselDiscardedIndex" :continuous="true" :cycle="false" height="auto" show-arrows-on-hover :show-arrows="true" progress progress-color="grey" hide-delimiter-background hide-delimiters>
                <v-carousel-item v-for="(card, i) in decks[deck].discardedCards" :key="i">

                    <!-- Regular deck -->
                    <v-sheet v-if="!cards[card].image_content" color="#484848" height="300" tile>
                        <v-row dense tile no-gutters>
                            <v-col align="start" class="mt-5">
                                <v-icon large v-if="cards[card].for" :color="getColor(cards[card].for)">{{ getIcon(cards[card].for) }}</v-icon>
                                <v-badge v-if="cards[card].timer" :color="getColor('timer-badge')">
                                    <template v-slot:badge>{{cards[card].timer}}min</template>
                                    <v-btn @click="startTimer(cards[card].timer)" :color="getColor('timer')" fab x-small>
                                                                  <v-icon>{{ getIcon("timer") }}</v-icon>
                                    </v-btn>
                                </v-badge>
                            </v-col>
                            <v-col align="end">
                                <v-container>
                                    <img width="50" height="50" :src="cards[card].image">
                                </v-container>
                            </v-col>
                        </v-row>
                        <!-- style="background: #121212" -->
                        <v-row dense no-gutters class="fill-height">
                            <v-col justify-self="center">
                                <v-container>
                                    <!-- here to add some padding -->
                                    <div class="headline">{{ cards[card].text }}</div>
                                </v-container>
                            </v-col>
                        </v-row>
                    </v-sheet>

                    <!-- Positions -->
                    <v-sheet v-if="cards[card].image_content" color="#484848" tile>
                        <v-row dense tile no-gutters>
                            <v-col align="right">
                                <v-container>
                                    <img height="50" width="50" :src="cards[card].image">
                                </v-container>
                            </v-col>
                        </v-row>
                        <!-- style="background: #121212" -->
                        <v-row dense no-gutters class="fill-height">
                            <v-col align="center">
                                <!-- here to add some padding -->
                                <v-responsive min-height="350px">
                                    <img contain width="100%" :src="cards[card].image_content">
                                </v-responsive>

                            </v-col>
                        </v-row>
                    </v-sheet>
                </v-carousel-item>
            </v-carousel>
        </v-card>
    </v-container>
</v-container>

</template>

<script>

import Tools from './Tools';

function getRandomInt(max) {
    // Gen a number from 0 to < max
    // Adding 1 to max to make it more user friendly and include max as value
    max += 1
    return Math.floor(Math.random() * Math.floor(max));
}

export default {
    name: 'Decks',
    props: {
        decks: Object,
        deck: String,
        cards: Object,
        persistent: Object,
    },
    mounted() {},
    watch: {
        persistent: {
            handler: function() {
                this.$forceUpdate(); // adding some force refresh of the object cause vuetify in some case don't refresh it. Even it this.persistent changed
            },
            deep: true
        }
    },
    methods: {
        getIcon: Tools.getIcon,
        getColor: Tools.getColor,
        startTimer: function(value) {
            this.$root.$emit('startAutomaticTimer', value)
        },
        drawCard: function(deck_name) {
            window.console.log("--drawCard");

            var card = this.decks[deck_name].cards.splice(0, this.decks[deck_name].drawNumber)
            if (card.length <= 0) {
                return
            }
            if (this.decks[deck_name].pickedCards[0] == this.decks[deck_name].background) {
                this.decks[deck_name].pickedCards = card;
            } else {
                this.decks[deck_name].pickedCards = this.decks[deck_name].pickedCards.concat(card);
                // this.decks[deck_name].pickedCards.push(card);
            }
        },
        // Return real card from picked cards
        pickedCardInfo: function(deck_name) {
            window.console.log("--pickedCardInfo " + deck_name);
            var cardId = this.decks[deck_name].pickedCards[this.carouselPickedIndex]
            var card = this.cards[cardId]

            if (card) {
                return this.cards[cardId]
            } else {
                return {
                    "type": "",
                    "image": "",
                    "text": ""
                }
            }
        },
        takeCardInHand: function(deck_name) {
            window.console.log("--takeCardInHand");
            // Remove the card from picked
            var card = this.decks[deck_name].pickedCards.splice(this.carouselPickedIndex, 1)
            this.carouselPickedIndex = 0
            if (card.length > 0) {
                // Add this card in player hand
                this.persistent.players[this.persistent.currentPlayer]["hand"].push({
                    "card_id": card[0],
                    "deck": deck_name
                })
            }
        },
        backInTheDeck: function(deck_name) {
            window.console.log("--backInTheDeck");

            // Remove the card from picked
            var card = this.decks[deck_name].pickedCards.splice(this.carouselPickedIndex, 1)
            this.carouselPickedIndex = 0
            if (card.length > 0) {
                var randomPlace = getRandomInt(this.decks[deck_name].cards.length)
                    // Add this card in deck random place
                this.decks[deck_name].cards.splice(randomPlace, 0, card)
            }
        },
    },
    data: () => ({
        carouselPickedIndex: 0,
        carouselDiscardedIndex: 0,

    }),
};

</script>
