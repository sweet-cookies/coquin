<style scoped>

.timer-slider >>> .v-slider {
    height: 350px;
}

</style>

<template>

<!-- timer overlay -->
<v-overlay :value="positionOverlay" opacity="0.6">
    <v-card class="d-inline-block mx-auto" color="#303030" shaped raised width="350">
        <v-container fill-height fluid>
            <v-row>
                <v-col>
                    <v-row>
                        <v-col justify-self="start">
                            <div class="overline mb-4">Position</div>
                        </v-col>
                    </v-row>
                    <v-img src="https://picsum.photos/id/11/500/300" aspect-ratio="1" class="grey lighten-2" max-width="500" max-height="300"></v-img>
                    <v-row align="end" justify="start" no-gutters>
                        <v-col justify-self="end">
                            <v-btn text color="warning" @click="positionDraw()">Piocher</v-btn>
                            <v-btn text @click="positionClose()">Close</v-btn>
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</v-overlay>
<!-- END timer overlay -->

</template>

<script>

export default {
    name: 'Timer',
    props: {},
    mounted() {

    },
    watch: {

    },
    data: () => ({
        positionOverlay: false,
    }),
    methods: {
        positionDraw: function() {},
        positionClose: function() {
            this.positionOverlay = false
        },
    }
}

</script>
