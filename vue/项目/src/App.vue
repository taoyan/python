<template>
  <div>
    <mt-button type="primary">primary</mt-button>
    <hr>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data(){
    return{

    }
  },
  created(){
    this.$axios.get('http://182.254.146.100:8899/api/getlunbo')
    .then(res=>{
      console.log(res)
    })
  }
}
</script>

<style>

</style>
