import Vue from 'vue'
import App from './App.vue'

// 引入全部组件
import Mint from 'mint-ui';
import 'mint-ui/lib/style.css';
Vue.use(Mint);


import Home from './components/Home.vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter);//安装插件，挂载属性
//路由规则
let router = new VueRouter({
  routes:[
    {path:'/home',component:Home},
    {path:'/',component:Home}
  ]
})

new Vue({
  el: '#app',
  //让vue知道路由
  router:router,
  render: h => h(App)
})
