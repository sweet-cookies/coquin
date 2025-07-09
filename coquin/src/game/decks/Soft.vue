



<script>

export default {
    getDeck() {
            window.console.log("--getDeck");
            return this.deck
        },
        deck: {
            'soft': {
                'defaultDrawNumber': 1, // Default card to pick on the deck
                'name': "Soft duo standard",
                'description': "Deck soft par defaut pour couple",
                'tags': ["soft"],
                'type': 'standard',
                'icon': "mdi-heart-outline",
                'background': "bgS",
                'pickedCards': [], // Drawed cards before going to hand or discard
                'discardedCards': [], // Discarded cards
                'drawNumber': null,
                'cards': [], // Deck cards
                // ++GENERATED CARDS++
deckCards:{"a1": 1, "a12": 1, "a2": 1, "a3": 1, "a7": 1, "c11": 1, "c14": 1, "c19": 1, "c29": 1, "c33": 1, "c4": 1, "c41": 1, "c42": 1, "c46": 1, "c47": 1, "c48": 1, "c49": 1, "c5": 1, "c6": 1, "c63": 1, "c8": 1, "randomQuestion": 0, "s14": 1, "s17": 1, "s19": 1, "s2": 1, "s21": 1, "s22": 1, "s24": 1, "s28": 1, "s3": 1, "s35": 1, "s38": 1, "s41": 1, "s42": 1, "s46": 1, "s47": 1, "s5": 1, "s50": 1, "s51": 1, "s54": 1, "s55": 1, "s57": 1, "s58": 1, "s59": 1, "s66": 1, "s75": 1, "s78": 1, "u12": 1, "u14": 2, "u15": 2, "u17": 1, "u19": 1, "u2": 1, "u20": 1, "u5": 2, "u6": 1, "u7": 1, "u8": 1, "u9": 1}
// --GENERATED CARDS--

            },
        }
}

</script>
