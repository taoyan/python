
<template>
  <div>
    <h3>{{ msg }}</h3>
    <div class="app2">
    </div>

    <vheader :textone='text_header'></vheader>
    <vheader textone='传递常量'></vheader>
    <vcenter></vcenter>
    <vfooter></vfooter>
    <button @click="listen">爸爸监听了</button>
  </div> 
  
</template>
  

<script>
import connect from "./connector.js"
import vheader from "./components/header.vue"
import vfooter from "./components/footer.vue"

export default{
  name: "App",
  data:function(){
    return{
      msg:"hello 组件哈哈哈哈",
      text_header:"大头大头",
    }
  },
  methods:{
    listen(){
      // 监听事件名
      connect.$on("phone",function(msg){
        console.log(msg);
      })
    }
  },
  created:{

  },
  components:{
    vheader:vheader,
    // vcenter,
    vfooter,
  }
}
</script>


<style>
</style>