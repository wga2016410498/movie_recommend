<template>
    <div class="container">
        <div class="main">
            <el-tabs class="tabs" @tab-click="handleTabClick" v-model="activeName" stretch>
                <el-tab-pane class="tabs-item"  v-for="(item, index) in tabs" :key="index" :label="item.label" :name="item.name">
                    <el-row>
                        <el-col :span="5"
                            v-for="(movie, movieIndex) in filteredMoviesByTag(item.label)" :key="movieIndex"
                            style="margin-left: 30px;margin-bottom: 20px;">
                            <ShowMovie :movie="movie" @click="showMovieInfo(movie)"></ShowMovie>
                        </el-col>
                    </el-row>
                    <!-- 下面有一个分页 -->
                    <div class="pagination-fixed-bottom">
                        <div class="pagination-block">
                            <el-pagination
                            v-model:current-page="currentPage"
                            v-model:page-size="pageSize"
                            :small="small"
                            :disabled="disabled"
                            :background="background"
                            layout="prev, pager, next, jumper"
                            :total="total"
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange"
                            />
                        </div>
                    </div>
                   
                </el-tab-pane>
            </el-tabs>
        </div>
    </div>
</template>
<script>
import ShowMovie from '@/components/Home/ShowMovie.vue';
import request from '@/utils/request';
export default {
    data(){
        return{
            currentPage:1,
            pageSize:12,
            total:10,
            tag:'爱情',
            activeName:'love',
            tabs: [
                { label: '爱情', name: 'love' },
                { label: '喜剧', name: 'comdy' },
                { label: '动作', name: 'action' },
                { label: '悬疑', name: 'suspense' },
                { label: '惊悚', name: 'panic' },
                { label: '动画', name: 'cartoon' },
                { label: '传记', name: 'biography' },  
                { label: '犯罪', name: 'crime' },
                { label: '科幻', name: 'technology' },
                { label: '家庭', name: 'family' },
                { label: '历史', name: 'history' },
                // { label: '两性', name: 'both' },
                // 如果要是等于其他
                // { label: '其他', name: 'other'},
            ],
            movies:[],  
        };
    },
    created() {
        this.getMovieData()
    },
    components: {
        ShowMovie
    },
    
    methods:{
        getMovieData(){
            request.get('/movies',{
                params:{
                    pageNum:this.currentPage,
                    pageSize:this.pageSize,
                    tag:this.tag
                }
            }).then(res=>{
                this.movies = res.data.data.list,
                this.total = res.data.data.total
            })
        },
        handleSizeChange(){

        },
        handleCurrentChange(newPage){
            this.pageNum = newPage
            this.getMovieData()
        },
        handleTabClick(tab) {
            this.tag = tab.props.label
            this.getMovieData()
            // console.log(tab.props.label)
        },
       showMovieInfo(movie){
            this.$router.push({ 
                name: 'MovieInfo', // 使用路由名称而不是路径
                query: { 
                    movieId: movie.movieId,
                    name: movie.name,
                    url:movie.url,
                    tag:movie.tag,
                    rate:movie.rate,
                    describe:movie.describe,
                    duration:movie.duration,
                    language:movie.language,
                    director:movie.director,
                    actor:movie.actor,
                    location:movie.location,
                    release_time:movie.releaseTime,
                } 
            });
        },
    },
    computed:{
        filteredMoviesByTag() {
            return (tag) => {
                return this.movies.filter(movie => movie.tag === tag);
            }
        }
    }   

}

</script>

<style scoped lang="scss">
.container{
    width:100%;
    display: flex;
    justify-content: center;
    align-content: center;
    .main{
        width: 1000px;
    }
    .pagination-fixed-bottom {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #fff; /* 可根据需要设置背景颜色 */
        border-top: 1px solid #ebeef5; /* 可根据需要设置顶部边框 */
        padding: 10px; /* 可根据需要设置内边距 */
        box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1); /* 可根据需要设置阴影效果 */
    }
    .pagination-block{
        display: flex;
        justify-content: center;
        align-content: center ;
    }
} 


</style>

<!-- 
<div>
    <div class="movie-item" v-for="(movie, movieIndex) in filteredMoviesByTag(item.label)" :key="movieIndex">
        <img :src="movie.img"/>
        <p>{{ movie.name }}</p>
        <p>{{ movie.describe }}</p>
    </div>
</div> -->


<!-- //     movie_id: '26425063',
//     name: '无双',
//     url: 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',
//     tag: '动作',
//     rate: 3,
//     describe: '身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
//     duration: '130分钟',
//     language: '汉语普通话, 粤语, 英语, 泰语, 波兰语',
//     director: '庄文强',
//     actor: '周润发 郭富城 张静初',
//     location: '中国大陆, 香港',
//     release_time: '2018-09-30(中国大陆)', -->