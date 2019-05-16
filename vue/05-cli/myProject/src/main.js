import Vue from 'vue'
import App from './App.vue'

// 全局组件
import vcenter from "./components/center.vue"
Vue.component('vcenter', vcenter)

//全局过滤器
Vue.filter('myFilter', function(value){
  return "我是全局过滤器"
})

new Vue({
  el: '#app',
  render: h => h(App)
})
