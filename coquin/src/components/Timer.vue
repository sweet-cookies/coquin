<style scoped>

.timer-slider >>> .v-slider {
    height: 350px;
}

</style>

<template>

<!-- timer overlay -->
<v-overlay :value="timerOverlay" opacity="0.6">
    <v-card class="d-inline-block mx-auto" color="#303030" shaped raised width="350">
        <v-container fill-height fluid>
            <v-row>
                <v-col>
                    <v-row>
                        <v-col justify-self="start">
                            <div class="overline mb-4">Timer</div>
                        </v-col>
                    </v-row>
                    <v-row align="stretch" justify="start" no-gutters>
                        <v-col justify-self="start">
                            <v-slider vertical v-model="timerValue" :tick-labels="timerLabels" track-fill-color="pink" max="12" min="0" thumb-size="55" step="1" label="minute" ticks="always" tick-size="5" class="timer-slider"></v-slider>
                        </v-col>
                        <v-col ld="auto">
                        </v-col>
                        <v-col justify-self="end">
                            <div class="text-center">
                                <v-progress-circular :rotate="90" :size="100" :width="15" :value="timerProgress" color="pink">
                                    {{ Math.round(timerProgress) }}
                                </v-progress-circular>
                            </div>
                        </v-col>
                    </v-row>
                    <v-row align="end" justify="start" no-gutters>
                        <v-col justify-self="end">
                            <v-btn text color="primary" @click="timerStart()">Start</v-btn>
                            <v-btn text color="error" @click="timerStop()">Stop</v-btn>
                            <v-btn text @click="timerClose()">Close</v-btn>
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
        if (localStorage.timerValue) {
            this.timerValue = localStorage.timerValue;
        }

        // Register a listener on automatic timer triger.
        // If sent we expect the timer to popup and automatically start with the expected value.
        // The value should be emit from a card displayed by Deck or Hand
        this.$root.$on('startAutomaticTimer', (newTimerNumber) => {
            this.timerValue = this.timerLabels.indexOf(parseFloat(newTimerNumber))
            this.timerOverlay = true
            this.timerStop()
            this.timerStart()
        });

    },
    watch: {
        timerValue(newTimerNumber) {
            localStorage.timerValue = newTimerNumber;
        },
    },
    data: () => ({
        timerAudio: new Audio("./timer.mp3"),
        timerOverlay: false,
        timerValue: 0,
        timerLabels: [0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        timerProgressTick: null,
        timerInterval: {},
        timerProgress: 0,
    }),
    methods: {
        timerPlaySound: function() {
            window.console.log("--timerPlaySound")
            this.timerAudio.play();
        },
        timerStart: function() {
            this.timerProgressTick = 100 / (this.timerLabels[this.timerValue] * 60)
            this.timerProgress = 0
            this.timerInterval = setInterval(() => {
                this.timerProgress += this.timerProgressTick
                if (this.timerProgress >= 100) {
                    this.timerPlaySound()
                    clearInterval(this.timerInterval)
                    return (this.timerProgress = 100)
                }
            }, 1000)
        },
        timerStop: function() {
            this.timerAudio.pause()
            clearInterval(this.timerInterval)
            this.timerProgress = 0
        },
        timerClose: function() {
            this.timerOverlay = false
        }
    }
}

</script>
