<template>
<div>
    <h2 class="nav">
        我是footer
    </h2>
    <button @click="callDaddy">打电话给爸爸</button>

    <input type="text" v-model="text" ref="ff">
    <p>{{ text | myFilter }}</p>
</div>
    
</template>



<script>
import connect from '../connector.js'
export default {
    name:"vfooter",
    data(){
        return{
            text : "",
        }
    },
    methods:{
        callDaddy(){
            connect.$emit("phone","60分钟后来")
        }
    },
    filters:{
        myFilter:function(value){
            return value.split("").reverse().join('')
        }
    },
    //组件创建后，数据初始化完成，Dom未生成
    created(){
        console.log("created", this.$refs.ff);
    },
    //数据已装载,dom已渲染完成，dom生效后
    mounted(){
        console.log("mounted", this.$refs.ff)
    }
}
</script>


<style scoped>
h2 {
    background-color: orange
}
</style>

