



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
deckCards:{"a1": 1, "a12": 1, "a2": 1, "a3": 1, "a7": 1, "c14": 1, "c29": 1, "c3": 1, "c33": 1, "c41": 1, "c42": 1, "c46": 1, "c47": 1, "c48": 1, "c49": 1, "c56": 1, "c63": 1, "c8": 1, "randomQuestion": 5, "s14": 1, "s17": 1, "s18": 1, "s19": 1, "s2": 1, "s21": 1, "s22": 1, "s23": 1, "s24": 1, "s27": 1, "s28": 1, "s3": 1, "s30": 1, "s35": 1, "s41": 1, "s42": 1, "s46": 1, "s47": 1, "s49": 1, "s50": 1, "s51": 1, "s52": 1, "s53": 1, "s54": 1, "s55": 1, "s57": 1, "s59": 1, "s61": 1, "s75": 1, "s78": 1, "u12": 1, "u14": 1, "u15": 1, "u19": 1, "u5": 1, "u6": 1, "u7": 1, "u8": 1}
// --GENERATED CARDS--

            },
        }
}

</script>
