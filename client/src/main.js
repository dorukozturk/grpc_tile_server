import Vue from 'vue'
import App from './App.vue'
import VueLayers from 'vuelayers'
import 'vuelayers/lib/style.css' // needs css-loader

Vue.config.productionTip = false

Vue.use(VueLayers)

new Vue({
  render: h => h(App),
}).$mount('#app')
