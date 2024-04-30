<template>
  <!-- <el-carousel :interval="4000"
                type="card"
                height="480px">
      <el-carousel-item v-for="(item,index) in carousels"
                          :key="index">
          <img :src="item.url"
              height="480px"
              width="100%" />
      </el-carousel-item>
  </el-carousel> -->
  
  <el-carousel height="320px" motion-blur>
      <el-carousel-item v-for="(carouselItem, index) in Math.ceil(carousels.length / 5)" :key="index" style="display:flex;justify-content: space-around;">
        <div class="carousel-slide" v-for="(item, i) in carousels.slice(index * 5, index * 5 + 5)" :key="i" style="display:flex;">
          <Card :card="item"></Card>
          <!-- <el-card >
            <img :src="item.url" height="100%" width="100%" />
          </el-card> -->
        </div>
      </el-carousel-item>
  </el-carousel>


</template>
<script>
import Card from './Card.vue';
export default {
  name: 'Carousel',
  components:{
    Card
  },
  data: function () {
    return {
    }
  },
  props: ['carousels']
}
</script>
<style scoped>
.el-carousel {
  background-image: linear-gradient(
    to right,
    rgba(0, 0, 0, 1),
    rgba(0, 0, 0, 0.34),
    rgba(0, 0, 0, 1)
  );
  /* background-color: rgba(0, 0, 0, 0.8); */
}
.el-carousel__item h3 {
  /* color: #475669; */
  font-size: 14px;
  /* opacity: 0.75; */
  /* line-height: 200px; */
  margin: 0;
}


</style>
