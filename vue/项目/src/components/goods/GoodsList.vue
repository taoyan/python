<template>
    <div class="tmpl">
        <nav-bar title="商品列表"></nav-bar>
        <div class="mui-content" style="background-color:#fff">
            <mt-loadmore :bottom-method="loadBottom" :bottom-all-loaded="allLoaded" :auto-fill="autoFill">
                <ul class="mui-table-view mui-grid-view">
                    <li v-for="(item, index) in list" :key="index" class="mui-table-view-cell mui-media mui-col-xs-6">
                        <router-link :to="{name:'goods.detail', query:{id:index}}">
                            <img class="mui-media-object" src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2153937626,1074119156&fm=27&gp=0.jpg">
                            <div class="mui-media-body">幸福就是可以一起睡觉</div>
                        </router-link>
                    </li>
		        </ul>   
            </mt-loadmore>
		     
		</div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            list:[1,2,3,4,5,6,7,8, 9, 10],
            allLoaded:false,
            autoFill:false,
        }
    },
    methods:{
        loadBottom(){
            console.log("loadmore");
        }
    }
}
</script>

<style>

</style>
