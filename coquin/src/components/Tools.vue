

<template>

<v-container pa-0>
</v-container>

</template>

<script>

export default {
    name: 'Tools',
    getDeckProperty: function(decks, deckName, property,
        defaultValue = "...") {
        if (decks.hasOwnProperty(deckName)) {
            return decks[deckName][property]
        }
        return defaultValue
    },
    getIcon: function(name) {
        if (name == "timer") return 'mdi-alarm'
        else if (name == "women") return 'mdi-gender-female'
        else if (name == "men") return 'mdi-gender-male'
        else return 'mdi-dots-horizontal'
    },
    getColor: function(type) {
        if (type == "background") return 'brown lighten-1'
        else if (type == "timer") return 'blue-grey lighten-3'
        else if (type == "timer-badge") return 'blue-grey darken-1'
        else if (type == "women") return 'pink lighten-1'
        else if (type == "men") return 'blue lighten-1'
        else if (type == "hand") return 'blue-grey'
        else if (type == "all") return 'deep-purple darken-1'
        else if (type == "question") return 'light-green'
        else if (type == "action") return 'green'
        else if (type == "soft") return 'cyan'
        else if (type == "coquine") return 'light-blue'
        else if (type == "coquin") return 'light-blue'
        else if (type == "hot") return 'deep-purple lighten-1'
        else if (type == "hard") return 'pink lighten-2'
        else if (type == "soumis") return 'pink lighten-2'
        else if (type == "positions") return 'red lighten-2'
        else if (type == "end") return 'teal'
        else if (type == "undress") return 'green accent-3'
        else if (type == "0") return 'red lighten-3'
        else if (type == "1") return 'pink lighten-3'
        else if (type == "2") return 'purple lighten-3'
        else if (type == "3") return 'deep-purple lighten-3'
        else if (type == "4") return 'indigo lighten-3'
        else if (type == "5") return 'blue lighten-3'
        else if (type == "6") return 'light-blue lighten-3'
        else if (type == "7") return 'cyan lighten-3'
        else if (type == "8") return 'teal lighten-3'
        else if (type == "9") return 'green lighten-3'
        else if (type == "10") return 'light-green lighten-3'
        else if (type == "11") return 'lime lighten-3'
        else if (type == "12") return 'yellow lighten-3'
        else if (type == "13") return 'amber lighten-3'
        else if (type == "14") return 'orange lighten-3'
        else if (type == "15") return 'deep-orange lighten-3'
        else if (type == "16") return 'brown lighten-3'
        else if (type == "17") return 'blue-grey lighten-3'
        else if (type == "18") return 'grey lighten-3'
        else return 'grey'
    },
};

</script>
