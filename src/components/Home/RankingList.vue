<template>
    <div style="padding-left:20px">
        <el-row class="title">
            <el-col :span="15">
                <h2 style="text-align:left;font-weight:700;">排行榜</h2>
            </el-col>
            <el-col :span="8">
                <p class="more-span" @click="this.$router.push('/movies')">更多></p>
            </el-col>
        </el-row>
        <div v-for="(rank,id) in rankinglist" :key="id" @mouseenter="onMouseEnter(id)" @click="showMovieInfo(rank)" style="margin-top:40px">
            <el-row class="rank-item" v-show="flag[id]">
                <el-col :span="4">
                <p :class="id<3?'id-p-gold':'id-p'">{{id+1}}</p>
                </el-col>
                <el-col :span="12">
                <p class="name-p">{{rank.name}}</p>
                </el-col>
                <el-col :span="8">
                <p class="update-p">{{rank.releaseTime}}</p>
                </el-col>
            </el-row>

            <!-- 显示图像 -->
            <el-container class="rank-item img-item" style="height:250px" v-show="!flag[id]">
                <el-aside width="240px" style="overflow-y:hidden;">
                    <img :src="rank.url" height="250px" width="100%">
                </el-aside>

                <el-container>
                    <el-main class="img-name">
                        <p :title="rank.name" class="line-limit-length">{{ rank.name }}</p>
                        <p :title="rank.author" class="img-word line-limit-length">{{ rank.director }}</p>
                        <p :title="rank.type" class="img-word line-limit-length">{{ rank.tag }}</p>
                    </el-main>
                    <el-footer style="padding-right:0px">
                        <el-row>
                            <el-col :span="12"
                                    :class="id<3?'img-id-gold':'img-id'">
                                {{rank.id}}
                            </el-col>
                        </el-row>
                    </el-footer>
                </el-container>
            </el-container>
        </div>
    </div>
</template>

<script>
export default {
    name: 'RankingList',
    props: ['rankinglist'],
    data(){
      return{
        flag:[false,true,true,true,true,true,true,true,true,true],
      };
    },
    methods: {
    onMouseEnter: function (id) {      
      this.flag.fill(true);
      this.flag[id] = false
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
    // onMouseLeave: function(id) {
    //   this.flag[id] = true
    // }
  }
}
</script>

<style>
.title {
  margin-bottom: 10px;
}
.more-span {
  font-size: 16px;
  color: rgba(0, 0, 0, 0.56);
  margin-top: 25px;
  cursor: pointer;
}
.more-span:hover {
  color: #d88911;
}
.rank-item {
  cursor: pointer;
  margin-bottom: 20px;
}
.id-p-gold {
  font-size: 18px;
  font-weight: 700;
  color: #cf9870;
  text-align: left;
}
.id-p {
  font-size: 18px;
  color: rgba(0, 0, 0, 0.34);
  text-align: left;
}
.name-p {
  font-size: 16px;
  color: rgba(0, 0, 0, 0.87);
  text-align: left;
}
.update-p {
  font-size: 12px;
  color: rgba(0, 0, 0, 0.34);
  text-align: right;
  line-height: 22px;
}
.img-id-gold {
  font-size: 64px;
  font-weight: 700;
  color: #cf9870;
  text-align: right;
  margin: 0px;
  line-height: 50px;
}
.img-id {
  font-size: 64px;
  color: rgba(0, 0, 0, 0.34);
  text-align: right;
  margin: 0px;
  line-height: 50px;
}
.img-name {
  font-size: 18px;
  color: rgba(0, 0, 0, 0.87);
  text-align: left;
  padding-top: 0px;
}
.img-word {
  font-size: 12px;
  color: rgba(0, 0, 0, 0.34);
  text-align: left;
  margin: 0px;
  margin-top: 10px;
}
.line-limit-length {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin: 0px;
}
</style>