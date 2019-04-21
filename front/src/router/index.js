import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: () => import('@/pages/Index')
    },
    {
      path: '/form',
      name: 'Form',
      component: () => import('@/pages/Form')
    }
  ]
})
