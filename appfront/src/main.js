// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
// import axios from 'axios'
import VueAxios from 'vue-axios'

import App from './App'
import router from './router'
import './assets/css/reset.css'
import bkMagic from 'bk-magic-vue'
import 'bk-magic-vue/dist/bk-magic-vue.min.css'
import axios from 'axios'
//其他vue组件中就可以this.$axios调用使用
Vue.prototype.$axios = axios
Vue.use(bkMagic)
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
