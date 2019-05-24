<template>
    <div class="photo-bottom">
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
        </div>
</template>

<script>
export default {
    data(){
        return{
            pageIndex:1,    //页码
            // cid:this.$route.params.id,
            msg:"",
            comments:[
                {
                    title:"评论内容123",
                },
                {
                    title:"评论内容dwaindlawmdlkmwakl",
                },
                {
                    title:"评论内容d[pwad,oawmdo;awmd'kq'wpdlaw;kd;awmd;wka\ndskakdmlk",
                }
            ],
        }
    },
    methods:{
        loadByPage(){
            console.log('concat')
            this.comments = this.comments.concat({title:"评论内容2222"})
        },
        sendComment(){
            this.comments.unshift({title:this.msg});
            this.msg = "";
        }
    },
    props:['pid']
}
</script>

<style>

</style>
