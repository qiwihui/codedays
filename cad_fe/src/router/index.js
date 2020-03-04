import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import Confirmation from '@/views/Confirmation.vue'
import Unsubscription from '@/views/Unsubscription.vue'
import Home from '@/views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  { 
    path: '/subscribe/confirm', 
    name: 'subscription_confirmation', 
    component: Confirmation,
  },
  { 
    path: '/unsubscribe', 
    name: 'unsubscription', 
    component: Unsubscription,
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
