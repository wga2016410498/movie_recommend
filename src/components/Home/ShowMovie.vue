<template>
    <!--对于不同的用户，显示的电影格子应该是不一样的。对于管理员，有删除，修改的操作  -->
    <!-- 对于普通的用户，有电影评分展示和点击查看详情的操作 -->
    <el-card :title="movie.name" :body-style="{padding:'0px'}">
      <img :src="movie.url" class="movie-img">
      <div style="padding-left:8px;padding-right: 5px;">
          <p class="movie-name line-limit-length">{{movie.name}}</p>
          <div class="bottom clearfix">
              <p class="movie-type line-limit-length">{{ movie.tag }}</p>
          </div>
          <el-rate
            v-model="movie.rate"
            disabled
            show-score
            text-color="#ff9900"
            score-template="{value} 分"
          />
          <!-- <p>{{ movie.rate }}</p> -->
      </div>
    </el-card>
  </template>
  
  <script>
  export default {
      name:'ShowMovie',
      props:['movie']
  }
  </script>
  
  <style scoped>
  .el-card {
    height: 350px;
    width: 200px;
    cursor: pointer;
  }
  .movie-img {
    height: 250px;
    width: 100%;
  }
  .movie-name {
    font-size: 14px;
    color: rgba(0, 0, 0, 0.87);
    text-align: left;
  }
  .movie-type {
    font-size: 12px;
    color: rgba(0, 0, 0, 0.34);
    text-align: left;
  }
  .line-limit-length {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin: 0px;
  }
  </style>