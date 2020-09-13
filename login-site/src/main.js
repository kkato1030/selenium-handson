import Vue from 'vue'
import App from './App.vue'
import '@aws-amplify/ui-vue'
import Amplify from 'aws-amplify'
import awsconfig from './aws-exports'
import Buefy from 'buefy'
import './assets/scss/app.scss'

Vue.use(Buefy)

Vue.config.productionTip = false
Amplify.configure(awsconfig)

new Vue({
  render: h => h(App),
}).$mount('#app')
