import Vue from 'vue'
// 第三方包
//mint-ui
import Mint from 'mint-ui'
import 'mint-ui/lib/style.css'
Vue.use(Mint)
//Mui
// import './static/vendor/mui/dist/css/mui.css'
// //全局css
// import './static/css/global.css'


//axios
import Axios from 'axios'
//挂载到原型
Vue.prototype.$axios = Axios


import Moment from 'moment'
//moment全局过滤器
Vue.filter('convertDate',function(value){
    return Moment(value).format('YYYY-MM-DD');
})




import App from './App.vue'
import Home from './components/home/Home.vue'
import Member from './components/member/Member.vue'
import Shopcart from './components/shopcart/Shopcart.vue'
import Search from './components/search/Search.vue'
import NewsList from './components/News/NewsList.vue'

import VueRouter from 'vue-router'
Vue.use(VueRouter)
//路由
let router = new VueRouter({
  linkActiveClass:'mui-active',
  routes:[
    {path:'/', redirect:{name:'home'}},
    {name:'home', path:"/home", component:Home},
    {name:'member', path:"/member", component:Member},
    {name:'shopcart', path:"/shopcart", component:Shopcart},
    {name:'search', path:"/search", component:Search},

    {name:'news_list', path:"/news/list", component:NewsList},
  ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
