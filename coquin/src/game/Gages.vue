

<template>

<v-container pa-0>

    <v-card>
        <v-card-title>
            Gages
            <v-spacer></v-spacer>
        </v-card-title>
        <v-card-subtitle>
        </v-card-subtitle>
        <v-card-text>
            <v-spacer class="pt-4"></v-spacer>
            {{gage}}
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="pink" @click="pickGage()" outlined>Piochez un gage</v-btn>
        </v-card-actions>
    </v-card>



</v-container>

</template>

<script>
function shuffle(a) {
    window.console.log("--shuffle");
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}


export default {
    name: 'Gages',
    props: {
        cards: Object,
    },
    mounted() {
            window.console.log(this.cards);
            this.gageCardsShuffled = shuffle(Object.keys(this.cards))
    },
    watch: {},
    methods: {
        pickGage: function() {
            // newPersistent.endGameCards = endGameCards
            this.gage = ""
            window.console.log("--pickGage");
            var gageCardId = this.gageCardsShuffled.splice(0, 1)

              if (gageCardId == "") {
                return
              }
            this.gage = this.cards[gageCardId]["text"]
        }
},
    data: () => ({
        gage: "",
        gageCardsShuffled: null
}),
};

</script>
