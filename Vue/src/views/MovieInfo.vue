<template>
  <!-- 当用户点击电影的时候，会跳转到当前电影详情页面 -->
  <el-card class="movie-card">
    <div class="rating-container">
      <img :src="$route.query.url" class="movie-image" alt="movie poster">
      <div class="rating-box">
       
          <h1>评价这个电影</h1>
          <el-rate
            v-model="value"
            :texts="['很差', '较差', '还行', '推荐', '力荐']"
            show-text
          />
        
        <div class="rating-footer">
          <el-button type="primary" @click="saveRating($route.query.movieId)">保存</el-button>
        </div>
      </div>
    </div>
    

    <div class="movie-info">
      <h2>{{ $route.query.name }}</h2>
      <el-tag>{{ $route.query.tag }}</el-tag>
      <el-rate
        v-model="$route.query.rate"
        disabled
        show-score
        text-color="#ff9900"
        score-template="{value} 分"
      />
      <el-divider></el-divider>
      <p>{{ $route.query.describe }}</p>
      <el-divider></el-divider>
      <p><b>电影时长:</b> {{ $route.query.duration }}</p>
      <p><b>电影语言:</b> {{ $route.query.language }}</p>
      <p><b>导演:</b> {{ $route.query.director }}</p>
      <p><b>演员:</b> {{ $route.query.actor }}</p>
      <p><b>上映地点:</b> {{ $route.query.location }}</p>
      <p><b>上映时间:</b> {{ $route.query.release_time }}</p>
    </div>
  </el-card>
</template>

<script>
import request from '@/utils/request';

export default {
  name:'MovieInfo',
  data() {
    return { 
      value:'',
    };
  },
  created(){
  },
  methods:{
    saveRating(movieId){
      // 先查看用户对于当前电影是否做过评价，没有做过评价就插入一条评价。
      let user =  JSON.parse(sessionStorage.getItem("user"))
      let timestamp = new Date().getTime()
      console.log(timestamp)
      const Rate = {
        userId:user.userId,
        movieId:movieId,
        rate:this.value,
        rateTime:timestamp
      }
      request.post("/addmovie",Rate).then(res=>{
        if (res.data.code === '0') {
            this.$message({
            type: "success",
            message: "更新成功"
            })
        }else{
            this.$message({
            type: "error",
            message: res.data.msg
            })
        }
      })
    },
  }
};
</script>

<style>
.movie-card {
  display: flex;
  width: 70%;
  margin: auto;
}

.movie-image {
  width: 200px;
  height: auto;
}

.movie-info {
  padding: 20px;
}

.movie-info h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.movie-info p {
  margin-bottom: 5px;
}

.movie-info b {
  font-weight: bold;
}
.rating-box {
  width: 500px;
  border-left: 1px solid #ccc;
  /* border-radius: 8px; */
  padding: 50px;
  margin: 20px;
}
.rating-container{
  display: flex;
  /* align-content: space-around; */
  justify-content: space-around;
}




.rating-footer {
  margin-top: 20px;
  margin-left: 150px;
}
</style>

