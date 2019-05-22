<template>
  <div>
		<!-- mint ui header  -->
    <mt-header title="头部"></mt-header>

    <router-view></router-view>

		<!-- mui tabbar -->
    <nav class="mui-bar mui-bar-tab">
			<router-link class="mui-tab-item" :to="{name:'home'}">
				<span class="mui-icon mui-icon-home"></span>
				<span class="mui-tab-label">首页</span>
			</router-link>
			<router-link class="mui-tab-item" :to="{name:'member'}">
				<span class="mui-icon icon-huiyuan"></span>
				<span class="mui-tab-label">会员</span>
			</router-link>
			<router-link class="mui-tab-item" :to="{name:'shopcart'}">
				<span class="mui-icon icon-gouwuche"><span class="mui-badge">9</span></span>
				<span class="mui-tab-label">购物车</span>
			</router-link>
			<router-link class="mui-tab-item" :to="{name:'search'}">
				<span class="mui-icon mui-icon-search"></span>
				<span class="mui-tab-label">查找</span>
			</router-link>
		</nav>
  </div>
</template>

<script>
export default {
  data(){
    return{

    }
  },
  created(){
    // this.$axios.get('http://182.254.146.100:8899/api/getlunbo')
    // .then(res=>{
    //   console.log(res)
    // })
  }
}
</script>

<style>

</style>
