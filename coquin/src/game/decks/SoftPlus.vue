



<script>

export default {
    getDeck() {
            window.console.log("--getDeck");
            return this.deck
        },
        deck: {
            'soft_plus': {
                'defaultDrawNumber': 1, // Default card to pick on the deck
                'name': "Soft 3 et plus",
                'description': "Deck soft pour 3 joueurs et plus",
                'tags': ["soft", "decouverte"],
                'type': 'standard',
                'icon': "mdi-heart-outline",
                'background': "bgS",
                'pickedCards': [], // Drawed cards before going to hand or discard
                'discardedCards': [], // Discarded cards
                'drawNumber': null,
                'cards': [], // Deck cards
                // ++GENERATED CARDS++
deckCards:{"a1": 1, "a11": 2, "a2": 1, "a3": 1, "a4": 1, "a6": 2, "a7": 2, "a8": 1, "c47": 2, "c67": 1, "c68": 1, "c69": 1, "c71": 1, "c8": 2, "randomQuestion": 47, "s1": 3, "s10": 1, "s11": 1, "s15": 1, "s16": 1, "s17": 1, "s18": 1, "s19": 1, "s2": 1, "s20": 1, "s23": 1, "s26": 1, "s27": 1, "s31": 1, "s33": 1, "s34": 1, "s4": 1, "s40": 1, "s44": 1, "s46": 1, "s47": 1, "s49": 4, "s5": 1, "s50": 4, "s51": 2, "s52": 1, "s53": 1, "s56": 1, "s57": 1, "s58": 1, "s59": 1, "s6": 1, "s62": 1, "s63": 1, "s64": 1, "s65": 2, "s66": 2, "s69": 1, "s7": 1, "s70": 1, "s71": 2, "s73": 1, "s74": 2, "s78": 1, "s8": 1, "s80": 2, "s81": 2, "u1": 1, "u10": 2, "u12": 2, "u14": 5, "u15": 2, "u16": 1, "u17": 2, "u18": 1, "u19": 1, "u2": 2, "u3": 1, "u4": 2, "u6": 2, "u7": 2, "u8": 2}
// --GENERATED CARDS--

            },
        }
}

</script>
