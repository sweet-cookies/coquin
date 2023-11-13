

<template>

<v-container pa-0>

    <v-card>
        <v-card-title>
            All cards
            <v-spacer></v-spacer>
            <v-text-field v-model="search" append-icon="mdi-magnify" label="Search" single-line hide-details></v-text-field>
        </v-card-title>
        <v-data-table dense :items-per-page="-1" :footer-props="{
              itemsPerPageOptions: [25,50,100,-1],
            }" :headers="headers" :items="formatCards" :search="search">

            <template v-slot:item.text="{ item }">

                <v-tooltip v-if="item.timer" bottom>
                    <template v-slot:activator="{ on }">
                        <v-icon :color="getColor('timer')" v-on="on">{{getIcon('timer')}}</v-icon>
                    </template>
                    <span>{{item.timer}} min</span>
                </v-tooltip>

                <v-icon v-if="item.for" :color="getColor(item.for)">{{ getIcon(item.for) }}</v-icon>
                {{ item.text }}
            </template>
            <template v-slot:item.type="{ item }">
                <v-chip :color="getColor(item.type)" dark>{{ item.type }}</v-chip>
            </template>
            <template v-slot:item.decks="{ item }">
                <v-chip class="mr-1" :key="deckId" v-for="(deckId, index) in item.decks" :color="getColor(index)" dark>{{ deckId }}</v-chip>
                <!-- :ref="'player_'+playerId" v-model="playerList[playerId]" :rules="[rules.required, rules.maxChar, rules.playerName]" :label="'Num du joueur '+(playerId+1)" -->

            </template>
        </v-data-table>
    </v-card>

</v-container>

</template>

<script>

import Tools from './Tools';

export default {
    name: 'CardsList',
    props: {
        cards: Object,
        decks: Object,
    },
    computed: {
        formatCards: function() {
            window.console.log("--formatCards")

            var formattedCards = []
            for (let [cardId, card] of Object.entries(this.cards)) {
                if (card.type == "position") {
                    continue
                }
                formattedCards.push({
                    id: cardId,
                    type: card.type,
                    text: card.text,
                    for: card.for,
                    timer: card.timer,
                    decks: this.decksContaining(cardId),
                })
            }
            return formattedCards
        }
    },
    methods: {
        decksContaining: function(card_id) {
            var decks = []
            for (var deck in this.decks) {
                if (this.decks[deck].type == "positions") {
                    continue
                }
                if (Object.keys(this.decks[deck].deckCards).includes(card_id)) {
                    decks.push(deck)
                }
            }
            return decks
        },
        getColor: Tools.getColor,
        getIcon: Tools.getIcon,
    },
    data: () => ({
        search: '',
        headers: [{
            text: 'Carte',
            align: 'left',
            sortable: true,
            value: 'id',
        }, {
            text: 'Type',
            value: 'type'
        }, {
            text: 'Text',
            value: 'text'
        }, {
            text: 'Decks',
            value: 'decks'
        }],
    }),
};

</script>
