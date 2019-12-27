<style scoped>

.picker-slider >>> .v-slider {
    width: 90px;
}

</style>

<template>

<v-container pa-0>

    <!-- Hand -->
    <v-container>
        <v-card elevation="24" max-width="444" class="mx-auto">
            <v-system-bar lights-out></v-system-bar>
            <v-carousel ref="pickedCards" v-model="carouselHandIndex" :continuous="true" show-arrows-on-hover :cycle="false" height="300" :show-arrows="true">
                <v-carousel-item v-for="(card, i) in playerCards" :key="i">
                    <v-sheet :color="cards[card.card_id].image" height="100%" tile>
                        <v-row dense tile no-gutters>
                            <v-col align="start" class="mt-5">
                                <v-icon large v-if="cards[card.card_id].for" :color="getColor(cards[card.card_id].for)">{{ getIcon(cards[card.card_id].for) }}</v-icon>
                                <v-badge v-if="cards[card.card_id].timer" :color="getColor('timer-badge')">
                                    <template v-slot:badge>{{cards[card.card_id].timer}}min</template>
                                    <v-btn @click="startTimer(cards[card.card_id].timer)" :color="getColor('timer')" fab x-small>
                                        <v-icon>{{ getIcon("timer") }}</v-icon>
                                    </v-btn>
                                </v-badge>
                            </v-col>

                            <v-col align="end">
                                <v-container>
                                    <img width="50" height="50" :src="cards[card.card_id].image">
                                </v-container>
                            </v-col>
                        </v-row>
                        <!-- style="background: #121212" -->
                        <v-row dense no-gutters class="fill-height">
                            <v-col justify-self="center">
                                <v-container>
                                    <!-- here to add some padding -->
                                    <div style="width: 340px" class="headline">{{ cards[card.card_id].text }}</div>
                                </v-container>
                            </v-col>
                        </v-row>
                    </v-sheet>
                </v-carousel-item>
            </v-carousel>

            <v-container>
                <v-system-bar color="#424242"></v-system-bar>

                <!-- regular hand display -->
                <v-row v-if="popupModePlayerName == null && persistent.players[persistent.currentPlayer]['hand'].length > 0 && getCardType() != 'hand'" align="center" justify="start" no-gutters>
                    <v-col justify-self="center">
                        <div class="ma-0">
                            <v-btn class="ma-2" outlined @click="playAcard()" color="warning" small rounded>
                                <v-icon left>mdi-star-circle</v-icon>Jouer
                            </v-btn>
                        </div>
                    </v-col>
                    <v-col ld="auto">
                    </v-col>
                </v-row>

                <!-- In popup mode -->
                <v-row v-if="popupModePlayerName != null" align="center" justify="start" no-gutters>
                    <v-col justify-self="center" v-show="persistent.players[popupModePlayerName]['hand'].length > 0 && getCardType() != 'hand'">
                        <div class="ma-0">
                            <v-btn class="ma-2" outlined @click="playAcard()" color="warning" small rounded>
                                <v-icon left>mdi-star-circle</v-icon>Jouer
                            </v-btn>
                        </div>
                    </v-col>
                    <v-col ld="auto" align="end">
                        <div class="ma-0">
                            <v-btn class="ma-2" outlined @click="$emit('update:popupModePlayerName', null)" color="grey" small rounded>
                                <v-icon left>mdi-close</v-icon>Close
                            </v-btn>
                        </div>
                    </v-col>
                </v-row>

            </v-container>
        </v-card>
    </v-container>
</v-container>

</template>

<script>

import Tools from './Tools';

export default {
    name: 'Decks',
    props: {
        popupModePlayerName: {
            type: String,
            default: null
        },
        decks: Object,
        cards: Object,
        persistent: Object,
    },
    created() {},
    watch: {
        persistent: {
            handler: function() {
                this.$forceUpdate(); // adding some force refresh of the object cause vuetify in some case don't refresh it. Even it this.persistent changed
            },
            deep: true
        }
    },
    computed: {
        playerCards: function() {
            if (!this.popupModePlayerName) {
                return this.persistent.players[this.persistent.currentPlayer]['hand']
            } else {
                return this.persistent.players[this.popupModePlayerName]['hand']
            }
        }
    },

    methods: {
        getIcon: Tools.getIcon,
        getColor: Tools.getColor,
        getCardType: function() {
            var card_id
            if (!this.popupModePlayerName) {
                card_id = this.persistent.players[this.persistent.currentPlayer]['hand'][this.carouselHandIndex].card_id

            } else {
                card_id = this.persistent.players[this.popupModePlayerName]['hand'][this.carouselHandIndex].card_id
            }
            return this.cards[card_id].type
        },
        // Play a card from the hand, then place it into the discarded
        playAcard: function() {
            window.console.log("--playAcard")

            var cards
            if (!this.popupModePlayerName) {
                cards = this.persistent.players[this.persistent.currentPlayer]["hand"].splice(this.carouselHandIndex, 1)
            } else {
                cards = this.persistent.players[this.popupModePlayerName]["hand"].splice(this.carouselHandIndex, 1)
            }

            this.carouselHandIndex = 0
            this.$forceUpdate(); // adding some force refresh of the object cause vuetify in some case don't refresh it. Even it this.persistent changed
            if (cards.length > 0) {
                var card = cards[0]
                this.decks[card.deck].discardedCards.push(card.card_id)
            }

        },
    },
    data: () => ({
        carouselHandIndex: 0,
    }),
};

</script>
