<template>
    <el-container>
        <el-header>
            <nav-head :user="user"></nav-head>
            <carousel :carousels="carousels"></carousel>
        </el-header>

        <!-- 主体部分 -->
        
        <el-main>
            <el-row class="common-content-row">
                <el-col>
                    <div class="common-content">
                        <recommend :recommondItems="recommondItems" :rankinglist="rankinglist">
                        </recommend> 
                    </div>
                </el-col>
            </el-row>
        </el-main>

       
        <el-footer>
            <footer-bar></footer-bar>
        </el-footer>
    </el-container>
  
</template>

<script>
import NavHead from '@/components/Home/NavHead.vue'
import Carousel from '@/components/Home/Carousel.vue'
import Recommend from '@/components/Home/Recommend.vue'
import FooterBar from '@/components/Home/FooterBar.vue'
import request from '@/utils/request'
export default {
    name: 'home',
    components: {
        NavHead,
        Carousel,
        Recommend,
        FooterBar,
    },
    data(){
        return{
            user: null,
            carousels: [
            {
                movie_id: '26425063',
                name: '无双',
                url: 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',
                tag: '动作',
                rate: 3,
                describe: '身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
                duration: '130分钟',
                language: '汉语普通话, 粤语, 英语, 泰语, 波兰语',
                director: '庄文强',
                actor: '周润发 郭富城 张静初',
                location: '中国大陆, 香港',
                release_time: '2018-09-30(中国大陆)'
            },
            {
                movie_id: '26425063',
                name: '无双',
                url: 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',
                tag: '动作',
                rate: 3,
                describe: '身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
                duration: '130分钟',
                language: '汉语普通话, 粤语, 英语, 泰语, 波兰语',
                director: '庄文强',
                actor: '周润发 郭富城 张静初',
                location: '中国大陆, 香港',
                release_time: '2018-09-30(中国大陆)'
            },
            {
                movie_id: '26425063',
                name: '无双',
                url: 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',
                tag: '动作',
                rate: 3,
                describe: '身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
                duration: '130分钟',
                language: '汉语普通话, 粤语, 英语, 泰语, 波兰语',
                director: '庄文强',
                actor: '周润发 郭富城 张静初',
                location: '中国大陆, 香港',
                release_time: '2018-09-30(中国大陆)'
            },
            {
                movie_id: '26425063',
                name: '无双',
                url: 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',
                tag: '动作',
                rate: 3,
                describe: '身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
                duration: '130分钟',
                language: '汉语普通话, 粤语, 英语, 泰语, 波兰语',
                director: '庄文强',
                actor: '周润发 郭富城 张静初',
                location: '中国大陆, 香港',
                release_time: '2018-09-30(中国大陆)'
            },
            {
                movie_id: '26425063',
                name: '无双',
                url: 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',
                tag: '动作',
                rate: 3,
                describe: '身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
                duration: '130分钟',
                language: '汉语普通话, 粤语, 英语, 泰语, 波兰语',
                director: '庄文强',
                actor: '周润发 郭富城 张静初',
                location: '中国大陆, 香港',
                release_time: '2018-09-30(中国大陆)'
            },
            {
                movie_id: '26425063',
                name: '无双',
                url: 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',
                tag: '动作',
                rate: 3,
                describe: '身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
                duration: '130分钟',
                language: '汉语普通话, 粤语, 英语, 泰语, 波兰语',
                director: '庄文强',
                actor: '周润发 郭富城 张静初',
                location: '中国大陆, 香港',
                release_time: '2018-09-30(中国大陆)'
            },
            {
                movie_id: '26425063',
                name: '无双',
                url: 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',
                tag: '动作',
                rate: 3,
                describe: '身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
                duration: '130分钟',
                language: '汉语普通话, 粤语, 英语, 泰语, 波兰语',
                director: '庄文强',
                actor: '周润发 郭富城 张静初',
                location: '中国大陆, 香港',
                release_time: '2018-09-30(中国大陆)'
            }, 
                
            ],
            data:require('../data.json'),
            recommondItems: [
            ],
            rankinglist: [
            ],
            recommendlist:[],
        }
    },
    created(){
        let userStr = sessionStorage.getItem("user")? JSON.parse(sessionStorage.getItem("user")) : {}
        //还有一个排行榜数据，这个排行榜打算做个热榜，把用户访问最多的加载过来。
        if(userStr){
            this.user = true;
            let userid = userStr.userId
            this.recommendlist = this.data[userid]
            this.getMoviesByRecommendList()
            this.getHotMovie()
            this.getNewMovie()
        }
    },
    methods:{
        getMoviesByRecommendList(){
            request.post('/movies/getbymovielist',{
                movielist:this.recommendlist
            }).then(res=>{
                this.recommondItems = res.data.data
            })
        },
        getHotMovie(){
            request.get('/movies/hotmovies').then(res=>{
                this.rankinglist = res.data.data
                // console.log(this.rankinglist)
            })
        },
        getNewMovie(){
            request.get('/movies/newmovies').then(res=>{
                this.carousels = res.data.data
            })
        }
    }

}
</script>

<style scoped>
.common-content-row {
  display: flex;
  justify-content: center;
}
.common-content {
  width: 1280px;
}
.el-header {
  padding: 0;
  height: auto;
}
</style>