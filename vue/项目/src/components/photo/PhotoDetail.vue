<template>
    <div class="tmpl">
        <navBar title="图文详情"></navBar>
        <div>
            <ul>
                <!-- <li v-for="(img, index) in imgs" :key="index">
                    <img :src="img.src">    
                </li> -->
                <li>
                    <vue-preview :slides="imgs" @close="handleClose"></vue-preview>
                </li>
            </ul>
        </div>

        <comment pid="pid"></comment>

        <!-- <div class="photo-bottom">
            <ul>
                <li class="photo-comment">
                    <div>
                        <span>提交评论</span>
                        <span><a href="">返回</a></span>
                    </div>
                </li>
                <li class="txt-comment">
                    <textarea v-model="msg" id="" cols="30" rows="3"></textarea>
                </li>
                <li>
                    <mt-button @click="sendComment" type="primary" size="large">发表评论</mt-button>
                </li>
                <li class="photo-comment">
                    <div>
                        <span>评论列表</span>
                        <span>{{ comments.length }}条评论</span>
                    </div>
                </li>

                <li v-for="(comment, index) in comments" :key="index">
                    <p>{{ comment.title}}</p>
                </li>

                <button @click="loadByPage">load more</button>
                
            </ul>
        </div> -->
    </div>
</template>

<script>
export default {
    data(){
        return{
            imgs:[
                {
                    src: 'https://farm6.staticflickr.com/5591/15008867125_68a8ed88cc_b.jpg',
                    msrc: 'https://farm6.staticflickr.com/5591/15008867125_68a8ed88cc_m.jpg',
                    alt: 'picture1',
                    title: 'Image Caption 1',
                    w: 600,
                    h: 400
                },
                {
                    src: 'https://farm4.staticflickr.com/3902/14985871946_86abb8c56f_b.jpg',
                    msrc: 'https://farm4.staticflickr.com/3902/14985871946_86abb8c56f_m.jpg',
                    alt: 'picture2',
                    title: 'Image Caption 2',
                    w: 1200,
                    h: 900
                },
            ],
            // comments:[
            //     {
            //         title:"评论内容123",
            //     },
            //     {
            //         title:"评论内容dwaindlawmdlkmwakl",
            //     },
            //     {
            //         title:"评论内容d[pwad,oawmdo;awmd'kq'wpdlaw;kd;awmd;wka\ndskakdmlk",
            //     }
            // ],
            // pageIndex:1,    //页码
            pid:this.$route.params.id,
            // msg:"",
        }   
    },
    created(){
        let id = this.$route.params.id;
        console.log(id)
    },
    methods: {
      handleClose () {
        console.log('close event')
      },
    //   loadByPage(){
    //       console.log('concat')
    //       this.comments = this.comments.concat({title:"评论内容2222"})
    //   },
    //   sendComment(){
    //       this.comments.unshift({title:this.msg});
    //       this.msg = "";
    //   }
    }
}
</script>

<style>

</style>
