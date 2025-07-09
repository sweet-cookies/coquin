



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
deckCards:{"a1": 1, "a12": 1, "a16": 1, "a2": 1, "a3": 1, "a5": 1, "a7": 1, "a9": 1, "c29": 1, "c35": 1, "c42": 1, "c43": 1, "c44": 1, "c47": 1, "c48": 1, "c49": 1, "c50": 1, "c54": 1, "c55": 1, "c79": 1, "c8": 1, "c80": 1, "c81": 1, "c82": 1, "h1": 1, "h11": 1, "h14": 1, "h17": 1, "h22": 1, "h30": 1, "h31": 1, "h32": 1, "h35": 1, "h37": 1, "h39": 1, "h41": 1, "h43": 1, "h48": 1, "h5": 1, "h54": 1, "h68": 1, "h7": 1, "h70": 1, "h77": 1, "h78": 1, "h82": 1, "h84": 1, "h92": 1, "h93": 1, "h94": 1, "hd14": 1, "hd15": 1, "hd17": 1, "hd21": 1, "hd23": 1, "hd30": 1, "hd6": 1, "hd9": 1, "s35": 1, "s45": 1, "s46": 1, "s47": 1, "s49": 1, "s50": 10, "s78": 1}
// --GENERATED CARDS--

            },
        }
}

</script>
