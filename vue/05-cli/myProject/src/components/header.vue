<template>
<div>
    <h1 class="nav">
        我是header    
        {{textone}}
    </h1>
    <button @click="show()">从js获取父组件值</button>
</div>
</template>



<script>
export default {
    name:"vheader",
    data(){
        return{

        }
    },
    // 组件参数
    props:['textone'],
    methods:{
        show(){
            console.log(this.textone)
        }
    }
}
</script>

<style scoped>
h1{
    background-color: aqua;
}

</style>
