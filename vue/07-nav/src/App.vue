<template>
  <div>
    <!-- <div class="h">header
      <button @click="goMusic">跳转到音乐</button>
    </div>

    <router-view class="c"></router-view>
    <div class="b">bottom</div>
    <button @click="testParams">测试传递参数</button> -->

  <headerVue></headerVue>
  <div>我是头部啊</div>
  <hr>

  <router-view class="c" name="header"></router-view>
  <router-view class="c" ></router-view>
  <router-view class="c" name="footer"></router-view>

  <hr>
  <!-- <footerVue></footerVue> -->
  <div>我是底部啊</div>

  </div>
</template>


<script>
export default {
  data(){
    return{

    }
  },
  methods:{
    goMusic(){
      this.$router.push('/music')
    },
    testParams(){
      this.$router.push({
        name:'music',query:{id:1}
      })
    }
  }
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
