import Vue from 'vue'
// 第三方包
//mint-ui
import Mint from 'mint-ui'
import 'mint-ui/lib/style.css'
Vue.use(Mint)

//axios
import Axios from 'axios'
//挂载到原型
Vue.prototype.$axios = Axios


import App from './App.vue'
import Home from './components/home/Home.vue'

import VueRouter from 'vue-router'
Vue.use(VueRouter)
//路由
let router = new VueRouter({
  routes:[
    {path:'/', redirect:{name:'home'}},
    {name:'home', path:"/home", component:Home},
  ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
