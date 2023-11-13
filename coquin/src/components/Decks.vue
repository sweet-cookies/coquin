<style scoped>

.picker-slider >>> .v-slider {
    width: 90px;
}

</style>

<template>

<v-container pa-0>

    <v-container pa-0>

        <v-tabs-items v-model="persistent.selectedDeck" touchless style="background: rgba(0, 0, 0, 0);">
            <v-tab-item value="tab-hand">

                <Hand v-if="persistent.currentPlayer != null" :persistent="persistent" :cards="cards" :decks="decks" />

            </v-tab-item>

            <v-tab-item v-for="ingameType in Object.keys(persistent.selectedDecks)" :key="ingameType" :value="'tab-' + ingameType">

                <Deck :persistent="persistent" :cards="cards" :decks="decks" :deck="persistent.selectedDecks[ingameType]" />

            </v-tab-item>
        </v-tabs-items>

    </v-container>

</v-container>

</template>

<script>

import Deck from './Deck';
import Hand from './Hand';

export default {
    name: 'Decks',
    props: {
        persistent: Object,
        decks: Object,
        cards: Object,
    },
    components: {
        Deck,
        Hand,
    },
    methods: {
    },
    data: () => ({
        colors: [
            'green',
            'secondary',
            'yellow darken-4',
            'red lighten-2',
            'orange darken-1',
        ],
    }),
};

</script>
