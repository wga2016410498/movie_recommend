<template>
    <el-container>
        <el-header>
            <nav-head :user="user"></nav-head>
            <h1 style="margin-top:20px;margin-left: 70px;">最新上映</h1>
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
            this.user = userStr;
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