



<script>

// Types
// Soft : questions, caresses, massages, retirer des vétements
// Coquin caresses, massages à des endroits plus intimes (poitrine, fesses)
// Hot Sex, pénétration et mélangisme pour plusieurs
// Hard Fessée, anal, ...
// Soumis Une personne attachée/soumise regroupement de tout
// Question
// Actions

import CardsSoft from './cards/Soft';
import CardsCoquin from './cards/Coquin';
import CardsHot from './cards/Hot';
import CardsHard from './cards/Hard';
import CardsQuestion from './cards/Question';
import CardsAction from './cards/Action';
import CardsSoumis from './cards/Soumis';
import CardsEnd from './cards/End';
import CardsUndress from './cards/Undress';

var SpecialCards = {
    "hbg1": {
        "type": "hand",
        "image": "/img/back.svg",
        "text": ""
    },
    "bgS": {
        "type": "background",
        "image": "/img/soft_bg.svg",
        "text": ""
    },
    "bgC": {
        "type": "background",
        "image": "/img/coquin_bg.svg",
        "text": ""
    },
    "bgH": {
        "type": "background",
        "image": "/img/hot_bg.svg",
        "text": ""
    },
    "bgSm": {
        "type": "background",
        "image": "/img/handcuffs_bg.svg",
        "text": ""
    },
    "bgP": {
        "type": "background",
        "image": "/img/position_bg.svg",
        "text": ""
    },
    "randomQuestion": {
        "image": "/img/question.svg",
        "text": "Carte question aléatoire",
        "type": "question"
    },
}

export default {
    numberOfDuoPositions: 90, // from 0 to 89
    numberOfDuoFFPositions: 15,
    numberOfQuadPositions: 4,
    numberOfTrioFFHPositions: 34,
    numberOfTrioHHFPositions: 20,
    _initPosCards: function() {
        window.console.log("--_initPosCards");
        for (const x of Array(this.numberOfDuoPositions).keys()) {
            this.cards["p_duo".concat(x)] = {
                "type": "position",
                "image": "/img/position.svg",
                "image_content": "/img/pos/duo/".concat(x).concat(".jpg"),
                "text": ""
            }
        }
        for (const x of Array(this.numberOfDuoFFPositions).keys()) {
            this.cards["p_duo_ff".concat(x)] = {
                "type": "position",
                "image": "/img/position.svg",
                "image_content": "/img/pos/duo_ff/".concat(x).concat(".jpg"),
                "text": ""
            }
        }
        for (const x of Array(this.numberOfQuadPositions).keys()) {
            this.cards["p_quad".concat(x)] = {
                "type": "position",
                "image": "/img/position.svg",
                "image_content": "/img/pos/quad/".concat(x).concat(".jpg"),
                "text": ""
            }
        }
        for (const x of Array(this.numberOfTrioFFHPositions).keys()) {
            this.cards["p_trio_ffh".concat(x)] = {
                "type": "position",
                "image": "/img/position.svg",
                "image_content": "/img/pos/trio_ffh/".concat(x).concat(".jpg"),
                "text": ""
            }
        }
        for (const x of Array(this.numberOfTrioHHFPositions).keys()) {
            this.cards["p_trio_hhf".concat(x)] = {
                "type": "position",
                "image": "/img/position.svg",
                "image_content": "/img/pos/trio_hhf/".concat(x).concat(".jpg"),
                "text": ""
            }
        }

    },
    getEndCards: function() {
        return CardsEnd.getCards()
    },
    getQuestionCards: function() {
        return CardsQuestion.getCards()
    },
    getCards() {
        window.console.log("--getCards");
        this._initPosCards()
        return this.cards
    },
    cards: Object.assign(SpecialCards,
        CardsSoft.getCards(),
        CardsCoquin.getCards(),
        CardsHot.getCards(),
        CardsHard.getCards(),
        CardsQuestion.getCards(),
        CardsAction.getCards(),
        CardsSoumis.getCards(),
        CardsEnd.getCards(),
        CardsUndress.getCards()),
}

</script>
