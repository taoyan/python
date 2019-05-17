import Vue from 'vue'
import App from './App.vue'

// 引入全部组件
import Mint from 'mint-ui';
import 'mint-ui/lib/style.css';
Vue.use(Mint);


import Home from './components/Home.vue'
import Music from './components/Music.vue'
import Movie from './components/Movie.vue'

import List from './components/List.vue'
import Detail from './components/Detail.vue'

import VueRouter from 'vue-router'
Vue.use(VueRouter);//安装插件，挂载属性
//路由规则
let router = new VueRouter({
  routes:[
    // {path:'/home',component:Home},
    // {path:'/',component:Home},
    {name:'music', path:'/music',component:Music},
    {name:'movie', path:'/movie',component:Movie},
    {name:'list', path:'/list',component:List},
    //查询字符串不用改，参数方式设置参数id
    {name:'detail', path:'/detail',component:Detail},
    // {name:'detail', path:'/detail/:id',component:Detail},
  ]
})

new Vue({
  el: '#app',
  //让vue知道路由
  router:router,
  render: h => h(App)
})
