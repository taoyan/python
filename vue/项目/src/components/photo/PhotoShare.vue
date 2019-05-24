<template>
    <div class="tmpl">
        <nav-bar title="图文分享"></nav-bar>
        <div class="photo-header">
            <ul>
                <li v-for="category in categorys" :key="category.id">
                    <a href="javascript:;" @click="loadImg(category.id)">{{category.title}}</a>
                </li>
            </ul>
        </div>
        <div class="photo-list">
            <ul>
                <li v-for="img in imgs" :key="img.id">
                    <router-link :to="{name:'photo.detail', params:{id:img.id}}">
                        <!-- mint ui提供的懒加载 -->
                        <!-- <img :src="img.img_url"> -->
                        <img v-lazy="img.img_url">
                        <p>
                            <span v-text="img.title"></span>
                            <br>
                            <span v-text="img.content"></span>
                        </p>
                    </router-link >
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            categorys:[
                {
                    id:"1",
                    title:"清纯可爱",
                },
                {
                    id:"2",
                    title:"古典美女",
                },
                {
                    id:"3",
                    title:"名模",
                },
                {
                    id:"4",
                    title:"小猫小狗",
                },
                {
                    id:"5",
                    title:"大话西游",
                },
                {
                    id:"6",
                    title:"全部图书",
                },
            ],
            imgs:[
                {
                    id:'1',
                    img_url:'http://img5.imgtn.bdimg.com/it/u=3300305952,1328708913&fm=26&gp=0.jpg',
                    title:'白马王子？',
                    content:'你是天使中的魔鬼，让我收拾收拾收拾，才发现信我的心头插了一把刀子',
                },
                {
                    id:'2',
                    img_url:'http://img2.imgtn.bdimg.com/it/u=1451330793,2242997567&fm=26&gp=0.jpg',
                    title:'霸道总裁爱上你？',
                    content:'你是天使中的魔鬼，让我收拾收拾收拾，才发现信我的心头插了一把刀子',
                },
                {
                    id:'3',
                    img_url:'http://img2.imgtn.bdimg.com/it/u=1451330793,2242997567&fm=26&gp=0.jpg',
                    title:'白马王子？',
                    content:'你是天使中的魔鬼，让我收拾收拾收拾，才发现信我的心头插了一把刀子',
                },
                {
                    id:'4',
                    img_url:'http://img5.imgtn.bdimg.com/it/u=3300305952,1328708913&fm=26&gp=0.jpg',
                    title:'小狐狸与小王子',
                    content:'你是天使中的魔鬼，让我收拾收拾收拾，才发现信我的心头插了一把刀子',
                },
                {
                    id:'5',
                    img_url:'http://img2.imgtn.bdimg.com/it/u=1451330793,2242997567&fm=26&gp=0.jpg',
                    title:'白马王子？',
                    content:'你是天使中的魔鬼，让我收拾收拾收拾，才发现信我的心头插了一把刀子',
                },
            ],
        }
    },
    created(){
        this.categorys.unshift({
            id:0,
            title:"全部",
        })
        // this.$axios.get('getimagecategory')
        // .then(res=>{
        //     this.categorys = res.data.message;
        //     this.categorys.unshift({
        //         id:0,
        //         title:"全部",
        //     })
        // })
        // .catch(err=>{
        //     console.log(err);
        // })

        this.loadImg(0)
    },
    methods:{
        loadImg(id){
            //获取类别下的图片
            // this.$axios.get('getimages/'+id)
            // .then(res=>{
            //     this.imgs = res.data.message;
            // })
            // .catch(err=>{
            //     console.log(err);
            // })
        }
    }
}
</script>

<style>
.photo-header li{
    list-style: none;
    display: inline-block;
    margin-left: 10px;
}

.photo-list img{
    width: 100%;
    height: 100;
}
</style>
