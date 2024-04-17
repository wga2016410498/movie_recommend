<template>
    <router-view />
</template>
<script>
export default {
  name:'App',
  components:{

  },
}
</script>
<style>
  * {
      margin: 0;
      padding: 0;
      box-sizing: border-box; /* 使得元素的宽度和高度包括内边距和边框 */
  }
  body{
    font: 12px / 1.5 Helvetica Neue, Helvetica, Arial, Microsoft Yahei, Hiragino Sans GB, Heiti SC, WenQuanYi Micro Hei, sans-serif;
    color: #333;
    background-color: #fff;
    min-width: 1226px;
  }
  li{
    list-style-type: none; /* 移除列表项的默认小点点 */
  }
  a{
    /* color: #fff; */
    text-decoration: none;
    /* padding: 5px; 设置内边距 */
    white-space: nowrap; /* 防止文字换行 */
    color: inherit;
  }
</style>


