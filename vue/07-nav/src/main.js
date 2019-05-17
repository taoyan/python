import Vue from 'vue'
import App from './App.vue'

import Music from './components/Music.vue'
import Movie from './components/Movie.vue'
import NotFound from './components/NotFound.vue'

import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

import VueRouter from 'vue-router'
Vue.use(VueRouter)


let router = new VueRouter({
  routes:[
    {path:'/', components:{header:Header, default:Footer, footer:Footer}},
    // {path:'/', redirect:{name:'home'}},
    // {name:'home', path:"/home", component:App},
    // {name:'music', path:"/music", component:Music},
    // {name:'movie', path:"/movie", component:Movie},
    // {path:'*', component:NotFound},

    //路由嵌套
    // {path:'/music', children:[
    //     {name:'music_oumei', path:"oumei", component:OuMei},
    // ]},
  ]
})


// 注册全局组件
Vue.component('headerVue', Header)
Vue.component('footerVue', Footer)

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
