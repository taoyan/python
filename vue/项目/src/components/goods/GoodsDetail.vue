<template>
    <div class="tmpl">
        <nav-bar title="商品详情"></nav-bar>

        <div class="mui-card">
            <div class="mui-card-header mui-card-media">
                <img src="../../assets/logo.png">
                <div class="mui-media-body">
                    小M
                    <p>发表于 2016-06-30 15:30</p>
                </div>
            </div>
            <div class="mui-card-content">
                <mt-swipe :auto="2000" style="height:200px; width=100%">
                    <mt-swipe-item v-for="(item, index) in imgs" :key="index">
                        <a :href="item.url"><img :src="item.img"></a>
                    </mt-swipe-item>
                </mt-swipe>
                <!-- <img src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2153937626,1074119156&fm=27&gp=0.jpg" alt="" width="100%"> -->
                <span>购买数量</span>
                <input type="text" v-model="num">
            </div>
            <div class="mui-card-footer">
                <a class="mui-card-link">Like</a>
                <a class="mui-card-link">Read more</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            imgs:[{
                url:'https://www.baidu.com',
                img:'http://img5.imgtn.bdimg.com/it/u=1979198230,3799788659&fm=26&gp=0.jpg',
            },
            {
                url:'https://www.baidu.com',
                img:'http://img5.imgtn.bdimg.com/it/u=3300305952,1328708913&fm=26&gp=0.jpg',
            },
            ],
            num: 10,
        }
    }
}
</script>

<style>

</style>
