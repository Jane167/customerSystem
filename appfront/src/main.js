// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

import App from './App'
import router from './router'
import './assets/css/reset.css'
// 全局变量引入bk-magin-vue
import bkMagic from 'bk-magic-vue'
// 全局变量引入bk-magic-vue样式
import 'bk-magic-vue/dist/bk-magic-vue.min.css'

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
