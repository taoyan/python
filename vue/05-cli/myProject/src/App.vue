
<template>
  <div>
    <h3>{{ msg }}</h3>
    <div class="app2">
    </div>

    <vheader></vheader>
    <vcenter></vcenter>
    <vfooter></vfooter>
  </div> 
  
</template>
  

<script>
import vheader from "./components/header.vue"
import vcenter from "./components/center.vue"
import vfooter from "./components/footer.vue"

export default{
  name: "App",
  data:function(){
    return{
      msg:"hello 组件"
    }
  },
  methods:{

  },
  created:{

  },
  components:{
    vheader:vheader,
    vcenter,
    vfooter,
  }
}
</script>


<style>
</style>