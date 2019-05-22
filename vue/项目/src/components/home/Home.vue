<template>
    <div>
        <!-- 轮播图 -->
        <mt-swipe :auto="2000">
            <mt-swipe-item v-for="(item, index) in imgs" :key="index">
                <a :href="item.url"><img :src="item.img"></a>
            </mt-swipe-item>
        </mt-swipe>
        
        <!-- 九宫格 -->
        <div class="mui-content">
		        <ul class="mui-table-view mui-grid-view mui-grid-9">
		            <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3">
                        <router-link :to="{name:'news_list'}">
		                    <span class="mui-icon mui-icon-home"></span>
		                    <div class="mui-media-body">新闻资讯</div>
                        </router-link></li>
		            <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3">
                        <a href="#">
		                    <span class="mui-icon mui-icon-email"></span>
		                    <div class="mui-media-body">图文分享</div>
                        </a></li>
		            <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><a href="#">
		                    <span class="mui-icon mui-icon-chatbubble"></span>
		                    <div class="mui-media-body">商品展示</div></a></li>
		            <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><a href="#">
		                    <span class="mui-icon mui-icon-location"></span>
		                    <div class="mui-media-body">留言反馈</div></a></li>
		            <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><a href="#">
		                    <span class="mui-icon mui-icon-search"></span>
		                    <div class="mui-media-body">搜索资讯</div></a></li>
		            <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><a href="#">
		                    <span class="mui-icon mui-icon-phone"></span>
		                    <div class="mui-media-body">联系我们</div></a></li>
		            
		        </ul> 
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
            {
                url:'https://www.baidu.com',
                img:'http://img2.imgtn.bdimg.com/it/u=1451330793,2242997567&fm=26&gp=0.jpg',
            }]
        }
    },
    created(){
        console.log('home created')
        this.$axios.get('http://182.254.146.100:8899/api/getlunbo')
        .then(res=>{
            console.log(res)
        })
    }
}
</script>

<style scoped>
.mint-swipe{
    max-height: 187px;
    height: 187px;
}
.mint-swipe img{
    height: 100%;
}

/* 九宫格 */
.mui-table-view.mui-grid-view.mui-grid-9{
    background-color: white;
    border: 0px;
    margin-top: 0px;
}

.mui-table-view.mui-grid-view.mui-grid-9 li{
    border: 0px;
}

.mui-table-view.mui-grid-view.mui-grid-9 ul{
    border: 0px;
}

/* 九宫格清除字体图标 */
.mui-icon-chatbubble:before,
.mui-icon-location:before,
.mui-icon-email:before{
    content: '';
}

/* 九宫格背景图片 */
.mui-icon-email{
    background-image: url('../../static/images/test.png');
    background-repeat: round;
}
.mui-icon-chatbubble{
    background-image: url('../../static/images/telegram.png');
    background-repeat: round;
}
.mui-icon-location{
    background-image: url('../../static/images/talk.png');
    background-repeat: round;
}

/* 九宫格图标宽高 */
.mui-icon{
    height: 50px;
    width: 50px;
}
</style>
