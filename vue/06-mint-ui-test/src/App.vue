<template>
  <div id="app">
    <div class="h">头部
      <!-- <a href="#/music">进入音乐</a>
      <a href="#/movie">进入电影</a>
      <a href="#/music">进入音乐</a>
      <a href="#/movie">进入电影</a>

      to字符串
      <router-link to="/music">进入音乐</router-link>
      <router-link to="/movie">进入电影</router-link>

      :to绑定变量
      <router-link :to="{name:'music'}">进入音乐</router-link>
      <router-link :to="{name:'movie'}">进入电影</router-link> -->


      
    </div>

    <router-view class="c"></router-view>
  <div class="b">底部</div> 
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
     return {
        
     }
  },
}
</script>


<style>
.h{
  height: 100px;
  background-color: yellowgreen;
}
.c{
  height: 100px;
  background-color: green;
}
.b{
  height: 100px;
  background-color: yellow;
}
</style>
