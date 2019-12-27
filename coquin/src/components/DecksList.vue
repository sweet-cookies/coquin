

<template>

<v-container pa-0>
    <v-container v-for="(deck, name) in decks" :key="name">
        <DeckContent :cards="cards" :deck="decks[name]" />
    </v-container>
</v-container>

</template>

<script>

import DeckContent from './DeckContent';

export default {
    name: 'DecksList',
    props: {
        cards: Object,
        decks: Object
    },
    mounted() {},
    watch: {},
    methods: {},
    components: {
        DeckContent,
    },
    data: () => ({
    }),
};

</script>
