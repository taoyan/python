<template>
    <div class="tmpl">
        <nav-bar title="新闻详情"></nav-bar>
        <div class="news-title">
            <p v-text="newsDetail.title"></p>
            <div>
                <span>{{newsDetail.click }}次点击</span>
                <span>分类：民生经济</span>
                <span>添加时间：{{ newsDetail.add_time | convertDate }}</span>
            </div>
        </div>
        <div v-html="newsDetail.detail" class="news-content"></div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            newsDetail:{
                title:"又是猝不及防，苹果悄悄上架多款新品",
                click:300,
                add_time:"2019-05-23T04:54:20.000Z",
                detail:'<div class="article-content"><p><span class="bjh-p">今天，苹果突然发布了新品，没错是自家的MacBook Pro系列进行了更新，其换上了速度更快的Intel第九代处理器。</span></p><p><span class="bjh-p">从配置上来说，这次苹果为新MacBook Pro配备了速度更快的第八代和第九代英特尔核心处理器，而新款8核MacBook Pro比4核MacBook Pro快两倍，比6核MacBook Pro快40%。</span></p><div class="img-container"><img class="large" data-loadfunc="0" src="https://pics6.baidu.com/feed/f3d3572c11dfa9ec7488002e8e0d2b07908fc14c.jpeg?token=3484b76d46cb4c23f67142144813278c&amp;s=0041FA0489002966DE770F810300A08C" data-loaded="0"></div><p><span class="bjh-p">除了配备速度更快的处理器以外，新款MacBook Pros还采用了升级换代后的蝴蝶（Butterfly）键盘技术。苹果将在今日发布的13英寸和15英寸版MacBook Pro上配备这种新键盘，但该公司并未提供任何细节以说明这种新的键盘设计是否也将适用于MacBook Air等其他蝴蝶键盘Mac电脑。</span></p><p><span class="bjh-p">针对之前用户吐槽多次的MacBook Pro显示屏问题，苹果终于出面进行了公开回应。</span></p><div class="img-container"><img class="large" data-loadfunc="0" src="https://pics0.baidu.com/feed/d833c895d143ad4bcc8d7b0e69df86aba60f06ba.jpeg?token=5eea077e5c1c16683097a47cf8aec365&amp;s=9FA1E90446CA972C18E8A5D3010050B2" data-loaded="0"></div><p><span class="bjh-p">苹果给出的公告显示，2016年10月至2018年2月之间售出的部分13英寸MacBook Pro，将可能存在一些问题，主要来说有两点，第一显示屏背光沿整个屏幕底部持续或间歇性显示垂直的明亮区域，第二是显示屏背光完全停止工作。</span></p><p><span class="bjh-p">对于这个问题，拆解机构iFixit给出的说法是，背光不均匀问题是因为，苹果使用了更薄的柔性线缆，上一代MacBook Pro中使用的线缆更厚。</span></p><div class="img-container"><img class="large" data-loadfunc="0" src="https://pics5.baidu.com/feed/6c224f4a20a44623c6f0337e75ffae0a0df3d7d3.jpeg?token=5dc3807c9676b3009d9e52e095295d8a&amp;s=4B80E50A14F85588147DADDA000010B0" data-loaded="0"></div><p><span class="bjh-p">此外，iFixit还强调，这个问题对于用户来说很难承担，由于苹果更改了Touch Bar MacBook Pro的设计，原本只需6美元就可以完成的修理，现在需要花费600美元。</span></p><p><span class="bjh-p">具体来说，相应的机型包含了：</span></p><p><span class="bjh-p">MacBook Pro (13--inch, 2016, Four Thunderbolt 3 Ports)</span></p><p><span class="bjh-p">MacBook Pro (13--inch, 2016, Two Thunderbolt 3 Ports)</span></p><p><span class="bjh-p">不过惊喜不止这些，除了全新的MacBook Pro之外，苹果官网还上架了一款LG 4K显示器。</span></p><div class="img-container"><img class="large" data-loadfunc="0" src="https://pics7.baidu.com/feed/f31fbe096b63f6242e0035446a9937fc1b4ca37e.jpeg?token=fdb44ee00a6b755a2f979fd3ecd1a605&amp;s=5498749288A1330B61509DDE0300D021" data-loaded="0"></div><p><span class="bjh-p">这款显示器名为LG UltraFine 4K显示屏，大小为23.7英寸，分辨率为3840x2160，覆盖P3广色域，亮度500尼特，苹果称其可显示超过800万个像素，比普通1080p HD显示屏高出4倍。</span></p><p><span class="bjh-p">至于I/O接口，LG UltraFine 4K显示屏搭载了2个雷电3接口用来视频驶入，也可以反向为笔记本或主机供电，最大功率85W，此外还有3个USB-C接口。</span></p><div class="img-container"><img class="large" data-loadfunc="0" src="https://pics7.baidu.com/feed/2f738bd4b31c870129b139fad6a2422b0608ff8e.jpeg?token=3f7f7f34ecd07309a3dfe8d28d2d9ff7&amp;s=F001D614BE72378A4C3ECCEC0300A0A3" data-loaded="0"></div><p><span class="bjh-p">LG UltraFine 4K显示屏内置立体声扬声器，三围为41.8x55.6x23cm，重7kg。</span></p><p><span class="bjh-p">外观上，LG UltraFine 4K显示屏非常朴素，并没有采用流行的窄边框设计，看起来与一般的办公用显示器无异。</span></p><p><span class="bjh-p">至于价格，LG UltraFine 4K显示屏售价5356元，现货可买，免费送货，支持分期。</span></p><div class="img-container"><img class="large" data-loadfunc="0" src="https://pics0.baidu.com/feed/63d0f703918fa0ec620fa932d74a85ea3c6ddb2c.jpeg?token=2dbe243bbf193b193d50456c074f33dc&amp;s=1600F40204909F8A42148DF503000021" data-loaded="0"></div><p><span class="bjh-p">另外据外媒报道称，苹果在2013年左右曾“认真地出价”收购特斯拉，价格大约在每股240美元左右。至于双方的谈判进入到哪一阶段，外界并不清楚。</span></p><p><span class="bjh-p">根据之前的资料看，2013年苹果CEO蒂姆·库克的确曾与特斯拉CEO埃隆·马斯克进行过一次会谈。与苹果当时给出的每股约240美元的报价相比，特斯拉当前股价仅徘徊在每股205美元左右。</span></p><p><span class="bjh-p">在过去的6个月里，特斯拉股价遭遇重创，当前股价已接近去年12月13日创下的376.79美元最高纪录的一半。对于特斯拉而言，这种痛苦可能还要持续一段时间，因为摩根士丹利今日曾发布投资研究报告，认为在最糟糕的情况下，特斯拉股价可能跌至10美元。</span></p><div class="img-container"><img class="normal" width="468px" data-loadfunc="0" src="https://pics2.baidu.com/feed/728da9773912b31b9c16effe6cc5ea7ed8b4e1d5.jpeg?token=db9051ed33257cb19dc4722391b32e8b&amp;s=5820347240B3539049C098ED0300E023" data-loaded="0"></div><p><span class="bjh-p">至于苹果的自动驾驶汽车项目，虽然其规模已被缩减，但苹果仍不死心。路透社上个月曾援引多位知情人士的消息称，苹果正与至少四家公司谈判，商讨为其供应用于自动驾驶汽车的下一代LiDAR（激光雷达）传感器。</span></p><p><span class="bjh-p">自2015年以来，苹果还与豪华汽车制造商宝马和梅赛德斯-奔驰进行了零星谈判，商讨共同开发全电动自动驾驶汽车事宜。但出于知识产权方面的担忧，这些谈判最终以失败告终。</span></p></div>',
            },
        }
    },
    created(){
        //获取参数，发起请求，返回后渲染页面
        let id = this.$toute.query.id;
        this.$axios.get('getnews/'+id)
        .then(res=>{
            this.newsDetail = res.data.messages[0];
        })
        .catch(err=>{
            console.log(err);
        })
    }
}
</script>

<style scoped>
.news-title p{
    color: #0a87f8;
    font-size: 20px;
    font-weight: bold;
}


</style>
