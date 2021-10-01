



<script>

export default {
    getDeck() {
            window.console.log("--getDeck");
            return this.deck
        },
        deck: {
            'coquin': {
                'defaultDrawNumber': 1, // Default card to pick on the deck
                'name': "Coquin duo standard",
                'description': "Deck coquin par defaut pour couple",
                'tags': ["coquin"],
                'type': 'standard',
                'icon': "mdi-heart-outline",
                'background': "bgC",
                'pickedCards': [], // Drawed cards before going to hand or discard
                'discardedCards': [], // Discarded cards
                'drawNumber': null,
                'cards': [], // Deck cards
                // ++GENERATED CARDS++
deckCards:{"a1": 1, "a12": 1, "a2": 1, "a3": 1, "a5": 1, "a7": 1, "a9": 1, "c11": 1, "c19": 1, "c25": 1, "c29": 1, "c3": 1, "c35": 1, "c4": 1, "c41": 1, "c42": 1, "c43": 1, "c44": 1, "c45": 1, "c46": 1, "c47": 1, "c48": 1, "c49": 1, "c5": 1, "c50": 1, "c53": 1, "c54": 1, "c55": 1, "c6": 1, "c79": 1, "c8": 1, "h1": 1, "h12": 1, "h17": 1, "h21": 1, "h22": 1, "h30": 1, "h31": 1, "h37": 1, "h39": 1, "h4": 1, "h41": 1, "h43": 1, "h54": 1, "h55": 1, "h70": 1, "h82": 1, "hd23": 1, "hd6": 1, "randomQuestion": 0, "s14": 1, "s22": 1, "s24": 1, "s35": 1, "s37": 1, "s38": 1, "s43": 1, "s45": 1, "s46": 1, "s47": 1, "s49": 1, "s5": 1, "s50": 4, "s55": 1, "s58": 1, "s59": 1, "s66": 1, "s73": 1, "s78": 1, "u14": 1, "u15": 1, "u17": 1, "u2": 1, "u20": 1, "u5": 1, "u9": 1}
// --GENERATED CARDS--

            },
        }
}

</script>
