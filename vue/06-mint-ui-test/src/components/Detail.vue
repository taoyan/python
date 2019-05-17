<template>
    <div>
        详情
    </div>
</template>

<script>
export default {
    data(){
        return{

        }
    },
    created(){
        // vue-router挂载两个对象属性
        // $route(信息数据) $router(功能函数)
        console.log(this.$route.query)
        // console.log(this.$route.params)
    }

}
</script>
