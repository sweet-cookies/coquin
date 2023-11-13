

<template>

<v-container pa-0>

    <v-card>
        <v-card-title>
            {{deck.name}}
            <v-spacer></v-spacer>
            <v-text-field v-model="search" append-icon="mdi-magnify" label="Search" single-line hide-details></v-text-field>
        </v-card-title>
        <v-card-subtitle>
            {{deck.description}}
        </v-card-subtitle>

        <v-data-table :items-per-page="15" :footer-props="{
              itemsPerPageOptions: [5,15,25,-1],
            }" :headers="headers" :items="formatCards" :search="search">
            <template slot="footer">
                <td class="pt-2"><strong>Total</strong></td>
                <td class="text-xs-right">{{totalCards}}</td>

                <v-sheet max-width="350">
                    <v-row :key="type" v-for="(average, type) in cardsTypeAverage" >
                        <v-col xs align="end">{{type}}
                        </v-col>
                        <v-col md="6">
                            <v-progress-linear :value="average" :color="getColor(type)" height="25">
                                <template v-slot="{ value }">
                                    <strong>{{ Math.ceil(value) }}%</strong>
                                </template>
                            </v-progress-linear>
                        </v-col>
                        <v-col md="auto">
                        </v-col>
                    </v-row>
                </v-sheet>

            </template>
            <template v-slot:item.type="{ item }">
                <v-chip :color="getColor(item.type)" dark>{{ item.type }}</v-chip>
            </template>

        </v-data-table>

    </v-card>

</v-container>

</template>

<script>

import Tools from './Tools';

export default {
    name: 'DeckContent',
    props: {
        deck: Object,
        cards: Object,
    },
    computed: {
        cardsTypeAverage: function() {
            var total = 0
            var totalPerTypes = {}
            var avgPerTypes = {}
            var type

            // Get totals
            for (let [card, number] of Object.entries(this.deck.deckCards)) {
                type = this.cards[card].type
                total += number
                if (totalPerTypes.hasOwnProperty(type)) {
                    totalPerTypes[type] += number
                } else {
                    totalPerTypes[type] = number
                }
            }

            // Compute averages
            for (let [type, number] of Object.entries(totalPerTypes)) {
                avgPerTypes[type] = 100 * number / total
            }
            return avgPerTypes
        },
        totalCards: function() {
            var total = 0
            for (let number of Object.values(this.deck.deckCards)) {
                total += number
            }
            return total
        },
        formatCards: function() {
            window.console.log("--formatCards")

            var deckCards = []
            var total = this.totalCards
            for (let [cardId, number] of Object.entries(this.deck.deckCards)) {
                if (number <= 0) {
                    continue
                }
                deckCards.push({
                    id: cardId,
                    type: this.cards[cardId].type,
                    number: "".concat(number).concat(" (").concat(Math.round(100 * number / total)).concat("%)"),
                    text: this.cards[cardId].text,
                })
            }
            return deckCards
        }
    },
    watch: {},
    methods: {
        getColor: Tools.getColor
    },
    data: () => ({

        search: '',
        headers: [{
            text: 'Carte',
            align: 'left',
            sortable: true,
            value: 'id',
        }, {
            text: 'Nombre',
            value: 'number'
        }, {
            text: 'Type',
            value: 'type'
        }, {
            text: 'Text',
            value: 'text'
        }],
    }),
};

</script>
