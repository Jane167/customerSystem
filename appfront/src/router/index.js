import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import login from '@/page/login/login'
import member from '@/page/member/index'
import customer from '@/page/customer/index'
import manager from '@/page/manager/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: 'member',
      name: 'member',
      component: member
    },
    {
      path: 'customer',
      name: 'customer',
      component: customer
    },
    {
      path: 'manager',
      name: 'manager',
      component: manager
    },
  ]
})
