<template>
    <div class="nav">
        <h2>我是center</h2>

        <ul>
            <li v-for = "(hero, index) in heros" :key="index" :class="{'A':'red','B':'yellow','C':'green'}[hero.score]">
                {{ hero.name }},{{hero.score}}
                <button @click="del(index)">删除</button>
            </li>
        </ul>

    </div>
</template>



<script>
export default {
    name:"vcenter",
    data(){
        return{
            heros:[{
                id:1,
                name:"奥利安啦",
                score:"A"
            },{
                id:2,
                name:"崔斯特",
                score:"B"
            },{
                id:3,
                name:"雷锋",
                score:"C"
            },{
                id:4,
                name:"阿拉斯加",
                score:"D"
            }]
        }
    },
    methods:{
        del(index){
            this.heros.splice(index, 1);
        }
    }
}
</script>


<style scoped>
h2 {
    background-color: yellow;
}
.red{
    background-color: red;
}
.yellow{
    background-color: yellow;
}
.green{
    background-color: green;
}
</style>