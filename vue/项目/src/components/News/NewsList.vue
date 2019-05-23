<template>
    <div class="tmpl">
        <!-- 头 -->
        <nav-bar title="新闻列表"></nav-bar>

        <!-- mui 图文列表 -->
        <ul v-for="index in times" :key="index" class="mui-table-view">
            <li v-for="news in newsList" :key="news.id" class="mui-table-view-cell" >
                <router-link :to="{name:'news.detail', query:{id:news.id}}" class="mui-navigate-right">
                    <img class="mui-media-object mui-pull-left" src="../../static/images/test.png">
                    <div class="mui-media-body">
                        <span v-text="news.title"></span>
                        <div class="sub">
                            <p>点击数:{{ news.click }}</p>
                            <p>发表时间:{{ news.add_time | convertDate }}</p>
                        </div>
                    </div>
                </router-link>
            </li>
		</ul>
    </div>
</template>

<script>
export default {
    data(){
        return{
            times:[1,2,3,4],
            newsList:[
                {
                    id:'1',
                    title:'CBD',
                    add_time:'2019-04-16T04:54:20.000Z',
                    zhaiyao:'烤炉模式的城，到黄昏，如同打翻的调色盘一般.',
                    click:20,
                    img_url:''
                },
                {
                    id:'2',
                    title:'在星巴克中国第一家手语店里，我们看见沟通方式可以多种多样',
                    add_time:'2019-04-16T04:54:20.000Z',
                    zhaiyao:'',
                    click:20,
                    img_url:''
                },
                {
                    id:'3',
                    title:'29岁女行长挂职副县长引质疑：其父系九江财政局原副调研员',
                    add_time:'2019-05-16T04:54:20.000Z',
                    zhaiyao:'',
                    click:20,
                    img_url:''
                },
            ]
        }
    },
    created(){
        this.$axios.get('getnewslist')
        .then(res =>{

        })
    }
}
</script>

<style>
.mui-table-view-cell {
    transform-style: preserve-3d;
}

.mui-table-view .mui-media-object {
    line-height: 42px;
    max-width: 42px;
    height: 42px;
}

.mui-pull-left {
    float: left;
}
.sub p{
    font-size: 10px;
}

</style>
