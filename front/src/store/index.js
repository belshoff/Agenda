import Vue from 'vue'
import Vuex from 'vuex'
import VeeValidate from 'vee-validate'

import example from './module-example'

Vue.use(Vuex)
Vue.use(VeeValidate)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      example
    }
  })

  return Store
}
