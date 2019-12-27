



<script>

export default {
    getDeck() {
            window.console.log("--getDeck");
            return this.deck
        },
        deck: {
            'soft_soumis': {
                'defaultDrawNumber': 1, // Default card to pick on the deck
                'name': "Soft soumis 2 et plus",
                'description': "Deck soft pour jouer à deux ou à plusieurs avec un joueur soumis (attaché et / ou yeux bandés)",
                'tags': ["soft", "soumis"],
                'type': 'standard',
                'icon': "mdi-heart-outline",
                'background': "bgSm",
                'pickedCards': [], // Drawed cards before going to hand or discard
                'discardedCards': [], // Discarded cards
                'drawNumber': null,
                'cards': [], // Deck cards
                // ++GENERATED CARDS++
deckCards:{"sm1": 1, "sm10": 1, "sm11": 1, "sm12": 3, "sm13": 1, "sm14": 1, "sm15": 1, "sm16": 1, "sm17": 1, "sm18": 1, "sm19": 1, "sm2": 1, "sm21": 1, "sm25": 1, "sm26": 1, "sm27": 1, "sm3": 3, "sm32": 3, "sm37": 1, "sm4": 1, "sm41": 1, "sm42": 1, "sm43": 2, "sm44": 1, "sm5": 1, "sm51": 2, "sm52": 1, "sm6": 1, "sm61": 2, "sm62": 2, "sm7": 1, "sm8": 1, "sm9": 2}
// --GENERATED CARDS--

            },
        }
}

</script>
