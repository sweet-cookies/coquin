

<template>

<v-overlay :value="decksOverlay">
    <v-container pa-0>
        <!--
    <div>
      <v-container
        id="scroll-target"
        style="max-height: 400px"
        class="overflow-y-auto"
      >
        <v-row
          align="start"
          justify="center"
          style="height: 1000px"
        >
          <v-col><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p><p>ddd</p></v-col>
        </v-row>
      </v-container>
    </div>
                <v-btn @click="$emit('update:decksOverlay', false)" icon>

-->
        <v-card v-show="true" max-width="350" class="mx-auto">
            <v-app-bar dark :color="getColor(deckType)">
                <v-toolbar-title>Decks {{deckType}}</v-toolbar-title>
                <v-spacer></v-spacer>

                <v-btn @click="$emit('update:decksOverlay', false)" icon>
                    <v-icon>mdi-close</v-icon>
                </v-btn>
            </v-app-bar>

            <v-container id="scroll-target" style="max-height: 450px; min-width: 350px" class="overflow-y-auto">
                <v-row dense>

                    <!-- Selected deck -->
                    <v-col cols="12">
                        <v-card :disabled="true" color="grey darken-1" dark>
                            <v-card-title class="bod">{{getDeckProperty(decks, selectedDeck, "name", "Aucun deck sélectionné")}}</v-card-title>

                            <v-card-subtitle>{{getDeckProperty(decks, selectedDeck, "description")}}</v-card-subtitle>

                            <v-chip small filter filter-icon="mdi-minus" :input-value="tag == filterTag" v-for="tag in getDeckProperty(decks, selectedDeck, 'tags', [])" :color="getColor(tag)" :key="tag" class="ma-1">
                                {{tag}}
                            </v-chip>

                            <v-card-actions>
                                <v-row dense no-gutters>
                                    <v-col align="end">
                                        <v-btn text>selectionner</v-btn>
                                    </v-col>
                                </v-row>

                            </v-card-actions>
                        </v-card>
                    </v-col>

                    <!-- available decks -->
                    <v-col cols="12" v-for="(deck, deckId) in filterUnselectedDeck" :key="deckId">
                        <v-card :disabled="false" color="blue-grey darken-2" dark>
                            <v-card-title class="bod">{{deck.name}}</v-card-title>

                            <v-card-subtitle>{{deck.description}}</v-card-subtitle>

                            <v-chip small filter filter-icon="mdi-minus" :input-value="tag == filterTag" @click="enableDisableFilter(tag)" v-for="tag in getDeckProperty(decks, deckId, 'tags')" :color="getColor(tag)" :key="tag" class="ma-1">
                                {{tag}}
                            </v-chip>

                            <v-card-actions>
                                <v-row dense no-gutters>
                                    <v-col align="end">
                                        <v-btn text @click="selectDeck(deckId)">selectionner</v-btn>
                                    </v-col>
                                </v-row>

                            </v-card-actions>
                        </v-card>
                    </v-col>

                    <!-- Disable deck -->
                    <v-col cols="12">
                        <v-card :disabled="false" color="blue-grey lighten-1" dark>
                            <v-card-title class="bod">Aucun</v-card-title>

                            <v-card-subtitle></v-card-subtitle>

                            <v-card-actions>
                                <v-row dense no-gutters>
                                    <v-col align="end">
                                        <v-btn text @click="selectDeck(null)">selectionner</v-btn>
                                    </v-col>
                                </v-row>

                            </v-card-actions>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-card>

    </v-container>
</v-overlay>

</template>

<script>

import Tools from './Tools';

export default {
    name: 'DeckSelectionOverlay',
    props: {
        decks: Object,
        deckType: String,
        selectedDeck: String,
        decksOverlay: {
            type: Boolean,
            default: false
        },
    },
    created() {},
    computed: {
        filterUnselectedDeck: function() {
            window.console.log("--filterUnselectedDeck");
            var unselectedDeck = {}
            for (let [deckId, deck] of Object.entries(this.decks)) {

                if (deckId != this.selectedDeck && !this.isFiltered(deckId)) {
                    // In case of position, just display positions decks, else don't display positions
                    if (this.getDeckProperty(this.decks, deckId, 'type') == "positions" && this.deckType == "positions") {
                        unselectedDeck[deckId] = deck
                    } else if (this.getDeckProperty(this.decks, deckId, 'type') != "positions" && this.deckType != "positions") {
                        unselectedDeck[deckId] = deck
                    }
                }
            }
            return unselectedDeck
        }
    },
    data: () => ({
        filterTag: null,
        items: [{
            color: '#1F7087',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Supermodel',
            artist: 'Foster the People',
        }, {
            color: '#952175',
            src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
            title: 'Halcyon Days',
            artist: 'Ellie Goulding',
        }],
    }),
    watch: {},
    methods: {
        isFiltered: function(deckId) {
            var tags
            if (this.filterTag != null) {
                tags = this.getDeckProperty(this.decks, deckId, 'tags')
                if (!tags.includes(this.filterTag)) {
                    return true
                }
            }
            return false
        },
        enableDisableFilter: function(tag) {
            if (tag == this.filterTag) {
                this.filterTag = null
            } else {
                this.filterTag = tag
            }
        },
        getDeckProperty: Tools.getDeckProperty,
        getColor: Tools.getColor,
        selectDeck: function(deckId) {
            window.console.log("--selectDeck");
            this.$emit('update:selectedDeck', deckId)
            this.$emit('update:decksOverlay', false)
        }
    },
};

</script>
