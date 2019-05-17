<template>
    <div>
        我是电影
        <button @click="goMusic">跳转到音乐</button>
        <button @click="goBack">向上</button>
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
            this.$router.push(
                {name:'music'}
            )
        },
        goBack(){
            this.$router.go(-1);
        }
    }
}
</script>
