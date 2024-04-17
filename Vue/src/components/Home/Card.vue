<template>
  <el-card :title="card.name" :body-style="{padding:'0px'}">
    <img :src="card.url" class="card-img" @click="showMovieInfo(card)">
    <div style="padding-left:8px;padding-right: 5px;">
        <p class="card-name line-limit-length">{{card.name}}</p>
        <div class="bottom clearfix">
            <p class="card-type line-limit-length">{{ card.tag }}</p>
        </div>
    </div>
  </el-card>
</template>

<script>
export default {
    name:'Card',
    props:['card'],
    
    created(){
      // console.log(this.card)
    },
    methods:{
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
    }
}
</script>

<style scoped>
.el-card {
  /* height: 185px;
  width: 300px; */
  height: 300px;
  width: 200px;
  cursor: pointer;
}
.card-img {
  /* height: 400px;
  width: 200px; */
  height: 250px;
  width: 100%;
}
.card-name {
  font-size: 14px;
  color: rgba(0, 0, 0, 0.87);
  text-align: left;
}
.card-type {
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