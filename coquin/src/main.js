import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import store from './store'

Vue.config.productionTip = false

new Vue({
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')

//new Vue({
//  el: '#app',
//  render: h => h(App),
//  vuetify: new vuetify({
//    theme: { dark: true },
//  }),
//  data: () => ({
//    drawer: null,
//  })
//})
