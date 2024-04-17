<template>
    <div class="slide">
        <div class="slide-prev" @click="prev"></div>
        <div class="slide-next" @click="next"></div>
        <ul class="slide-container" >
            <li class="image-container" v-for="(item, index) in slides"  v-show="index === imgIndex" :key="index">
                <a class="img-box" :href="item.url" target="_blank">
                    <img :src="item.src">
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name:'SlideShow',
    props:['slides'],
    data(){
        return{
            imgIndex:0,
            timer:'',
        }
    },
    methods:{
        prev(){
            const lastPage = this.slides.length -1;
            if(this.imgIndex>0){
                this.imgIndex -= 1;
            }else{
                this.imgIndex = lastPage;
            }
        },
        next () {
            const lastPage = this.slides.length - 1;
            if (this.imgIndex < lastPage) {
                this.imgIndex += 1;
            } else {
                this.imgIndex = 0;
            }
        },
    }
}
</script>

<style scoped>
.slide{
    background-color:rgba(0,0,0,0.3);
    position: relative;
    /* top: 10px; */
}
img{ 
    width: 100%;
    height: 100%;
}
.slide-prev{
    position: absolute;
    background: url(../assets/image/icon-slides.png) no-repeat -84px 50%;
    width: 41px;
    height: 69px;
    top: 40%;
    cursor: pointer;
}
.slide-prev:hover{
    background: url(../assets/image/icon-slides.png) no-repeat 0px 50%;
}
.slide-next{
    position: absolute;
    background: url(../assets/image/icon-slides.png) no-repeat -125px 50%;
    width: 41px;
    height: 69px;
    top: 40%;
    right: 0;
    cursor: pointer;
}
.slide-next:hover{
    background: url(../assets/image/icon-slides.png) no-repeat -43px 50%;
}
</style>

