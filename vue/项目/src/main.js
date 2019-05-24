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
//拦截器加loading
Axios.interceptors.request.use(function(config){
    Mint.Indicator.open({
      text: '加载中...',
      spinnerType: 'fading-circle'
    });
    return config;
});
Axios.interceptors.response.use(function(config){
    Mint.Indicator.close();
    return config;
});

//moment全局过滤器
import Moment from 'moment'
Vue.filter('convertDate',function(value){
    return Moment(value).format('YYYY-MM-DD');
})

//vue-preview
import VuePreview from 'vue-preview'
Vue.use(VuePreview)


//全局组件
import Navbar from './components/common/Navbar.vue'
import Comment from './components/common/Comment.vue'
Vue.component('navBar', Navbar) //使用最好以nav-bar
Vue.component('comment', Comment)

import App from './App.vue'
import Home from './components/home/Home.vue'
import Member from './components/member/Member.vue'
import Shopcart from './components/shopcart/Shopcart.vue'
import Search from './components/search/Search.vue'
import NewsList from './components/news/NewsList.vue'
import NewsDetail from './components/news/NewsDetail.vue'
import PhotoShare from './components/photo/PhotoShare.vue'
import PhotoDetail from './components/photo/PhotoDetail.vue'
import GoodsList from './components/goods/GoodsList.vue'
import GoodsDetail from './components/goods/GoodsDetail.vue'

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
    {name:'news.detail', path:"/news/detail", query:{id:1}, component:NewsDetail},
    
    {name:'photo.share', path:"/photo/share", component:PhotoShare},
    {name:'photo.detail', path:"/photo/detail/:id", component:PhotoDetail},

    {name:'goods.list', path:"/goods/list/", component:GoodsList},
    {name:'goods.detail', path:"/goods/detail/", component:GoodsDetail},
  ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
