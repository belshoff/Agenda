// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import VueI18n from 'vue-i18n'
import axios from 'axios'
import VueAxios from 'vue-axios'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

/* eslint-disable no-new */

let i18n = new VueI18n(
  {
    locale: 'pt-br',
    fallbackLocale: 'pt-br',
    localeDir: '@/i18n',
    enableInSFC: false
  }
);

new Vue({
  el: '#app',
  router,
  i18n,
  components: { App },
  template: '<App/>'
})
