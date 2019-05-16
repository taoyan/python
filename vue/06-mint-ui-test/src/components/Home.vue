<template>
    <div>
        我是主页
        <h1>123</h1>
        <mt-swipe :auto="4000">
        <mt-swipe-item>1</mt-swipe-item>
        <mt-swipe-item>2</mt-swipe-item>
        <mt-swipe-item>3</mt-swipe-item>
        </mt-swipe>

        <mt-progress :value="60">
        <div slot="start">0%</div>
        <div slot="end">100%</div>
        </mt-progress>

        <mt-button type="default">default</mt-button>
        <mt-button type="primary">primary</mt-button>
        <mt-button type="danger" @click="clickDanger()">显示弹出框</mt-button>
    </div>
</template>

<script>
import { Toast } from 'mint-ui';

export default {
    name: 'home',
    data () {
    return {
      
    }
  },
  methods:{
        clickDanger(){
            Toast({
                message: 'Upload Complete',
                position: 'bottom',
                duration: 5000
            });
        }
    }
}
</script>
