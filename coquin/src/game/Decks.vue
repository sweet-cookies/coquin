



<script>

import SoftPlus from './decks/SoftPlus';
import HotPlusMel from './decks/HotPlusMel';
import HotPlusEch from './decks/HotPlusEch';
import CoquinPlus from './decks/CoquinPlus';
import Soft from './decks/Soft';
import Coquin from './decks/Coquin';
import Hot from './decks/Hot';
import SoftSoumis from './decks/SoftSoumis';
import HotSoumis from './decks/HotSoumis';

var decksPositions = {
    'positions': {
        'defaultDrawNumber': 1, // Default card to pick on the deck
        'drawNumber': null,
        'name': "Positions duo",
        'description': "Deck de positions par defaut pour couple",
        'icon': "mdi-account-multiple",
        'background': "bgP",
        'pickedCards': [],
        'discardedCards': [],
        'cards': [],
        'deckCards': {},
        'type': 'positions',
        'tags': ["2"],
        // Special template to generate deck of positions
        // Just a way to automate it because there is quite a lot of positions.
        // You can also specify directly as standard deck the position as regular cards if needed see _initPosCards
        // Just don't forgot to set the deck to type standard to do so
        'deckCardsTemplate': [{
            'prefix': 'p_duo',
            'start': 0,
            'stop': 87
        }],
    },
    'positions_3_plus': {
        'defaultDrawNumber': 1, // Default card to pick on the deck
        'drawNumber': null,
        'name': "Selection de positions duo, trio et plus",
        'description': "Deck de positions de 2 à 4 personnes",
        'icon': "mdi-account-multiple",
        'background': "bgP",
        'type': 'positions',
        'tags': ["3+"],
        'pickedCards': [],
        'discardedCards': [],
        'cards': [],
        'deckCards': {
            "p_duo1": 1,
            "p_duo3": 1,
            "p_duo4": 1,
            "p_duo8": 1,
            "p_duo11": 1,
            "p_duo12": 1,
            "p_duo13": 1,
            "p_duo14": 1,
            "p_duo15": 1,
            "p_duo16": 1,
            "p_duo25": 1,
            "p_duo27": 1,
            "p_duo28": 1,
            "p_duo30": 1,
            "p_duo43": 1,
            "p_duo45": 1,
            "p_duo49": 1,
            "p_duo51": 1,
            "p_duo54": 1,
            "p_duo69": 1,
            "p_duo72": 1,
            "p_duo78": 1,
            "p_duo87": 1,
        },
        // Special template to generate deck of positions
        // Just a way to automate it because there is quite a lot of positions.
        // You can also specify directly as standard deck the position as regular cards if needed see _initPosCards
        // Just don't forgot to set the deck to type standard to do so
        'deckCardsTemplate': [{
            'prefix': 'p_duo_ff',
            'start': 0,
            'stop': 5
        }, {
            'prefix': 'p_quad',
            'start': 0,
            'stop': 3
        }, {
            'prefix': 'p_trio_ffh',
            'start': 0,
            'stop': 26
        }, {
            'prefix': 'p_trio_hhf',
            'start': 0,
            'stop': 15
        }],
    },
    'positions_3_plus_only': {
        'defaultDrawNumber': 1, // Default card to pick on the deck
        'drawNumber': null,
        'name': "Positions trio et plus",
        'description': "Deck de positions 3 et 4 personnes uniquement",
        'icon': "mdi-account-multiple",
        'background': "bgP",
        'pickedCards': [],
        'discardedCards': [],
        'cards': [],
        'deckCards': {},
        'type': 'positions',
        'tags': ["3"],
        // Special template to generate deck of positions
        // Just a way to automate it because there is quite a lot of positions.
        // You can also specify directly as standard deck the position as regular cards if needed see _initPosCards
        // Just don't forgot to set the deck to type standard to do so
        'deckCardsTemplate': [{
            'prefix': 'p_duo_ff',
            'start': 0,
            'stop': 5
        }, {
            'prefix': 'p_quad',
            'start': 0,
            'stop': 3
        }, {
            'prefix': 'p_trio_ffh',
            'start': 0,
            'stop': 26
        }, {
            'prefix': 'p_trio_hhf',
            'start': 0,
            'stop': 15
        }],
    },
}

export default {
    // Feed position decks of positions cards
    _feedPositions: function(prefix, start, stop) {
        window.console.log("--_feedPositions");
        var pos = {}
        for (var i = start; i <= stop; i++) {
            pos[prefix.concat(i)] = 1
        }
        return pos
    },
    getDecks() {
        window.console.log("--getDecks");
        var deck
        var templateIdx
        var pos
        for (deck in this.decks) {
            if (this.decks[deck].type == "positions") {
                for (templateIdx in this.decks[deck].deckCardsTemplate) {
                    pos = this._feedPositions(this.decks[deck].deckCardsTemplate[templateIdx].prefix, this.decks[deck].deckCardsTemplate[templateIdx].start, this.decks[deck].deckCardsTemplate[templateIdx].stop)
                    this.decks[deck].deckCards = Object.assign(pos, this.decks[deck].deckCards)
                }
            }
        }
        return this.decks
    },
    decks: Object.assign(SoftPlus.getDeck(),
        HotPlusMel.getDeck(),
        HotPlusEch.getDeck(),
        CoquinPlus.getDeck(),
        Soft.getDeck(),
        Coquin.getDeck(),
        Hot.getDeck(),
        SoftSoumis.getDeck(),
        HotSoumis.getDeck(), decksPositions),
}

</script>
