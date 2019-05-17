<template>
    <div>
        我是音乐
        <button @click="goMovie">跳转到电影</button>
        <button @click="goBack">向上</button>
        <button @click="go">向下</button>
    </div>
</template>


<script>
export default {
    data(){
        return{

        }
    },
    methods:{
        goMovie(){
            this.$router.push('/movie')
        },
        goBack(){
            this.$router.go(-1);
        },
        go(){
            this.$router.go(1);
        }
    }
}
</script>
