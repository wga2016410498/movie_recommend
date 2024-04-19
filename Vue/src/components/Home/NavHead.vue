<template>
  <el-row class="head-container">
    <el-col :span="8" >
        <div class="grid-content left">
            <img class="nav-img" src="../../assets/sun.gif">
            <span class="web-span" style="font-size: 20px;">
                {{ title }}
            </span>
            </div>
        
    </el-col>
   
    <el-col :span="16" v-if="userflag==0 ">
        <div class="grid-content right">            
            <div class="nav-item" style="margin-right:50px">
                <el-dropdown :hide-on-click="false">
                    <span class="el-dropdown-link">
                      <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
                    </span>
                    <template #dropdown>
                      <el-dropdown-menu >
                        <el-dropdown-item @click="$router.push('/person')">个人信息</el-dropdown-item>
                        <el-dropdown-item @click="logout">退出系统</el-dropdown-item>
                      </el-dropdown-menu>
                      <!-- <el-dropdown-menu v-else>
                        <el-dropdown-item @click="$router.push('/login')">登录</el-dropdown-item>
                      </el-dropdown-menu> -->
                    </template>
                </el-dropdown>
            </div>
        </div>
    </el-col>
  </el-row>
</template>

<script>
export default {
    name:'NavHead',
    props: ['user'],
    data(){
        return{
            title:'电影推荐系统',
            searchContent: '',
            circleUrl:'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
            userflag:''
        }
    },
    methods:{
        goLogin(){
            this.$router.push('/')
        },
        logout(){
          sessionStorage.removeItem('user');
          this.$router.push('/')
        }
    },
    created(){
      let userStr =JSON.parse(sessionStorage.getItem("user"));
      this.userflag = userStr.role
      console.log(this.userflag)
    }
}
</script>

<style scoped lang="scss">
.head-container{
    display: flex;
    justify-content: center;
    background: #fff;
    height: 100%;
}
.el-col {
  border-radius: 4px;
  height: 100%;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content:space-around;
}
.left {
  float: left;
}
.right {
  float: right;
}
.web-span {
  font-size: 16px;
  padding: 8px;
  color: rgba(0, 0, 0, 0.87);
  margin-left: 5px;
  cursor: pointer;
}
.nav-img {
  width: 36px;
  height: 36px;
  border-radius: 4px;
  cursor: pointer;
  margin-left:50px;
}
.nav-item {
  margin-left: 14px;
  margin-right: 14px;
}
.el-input {
  border-radius: 15px;
}
.nav-span {
  font-size: 14px;
  padding: 8px;
  color: rgba(0, 0, 0, 0.87);
}
.nav-span:hover {
  color: #d88911;
  cursor: pointer;
}
</style>

<!-- <span class="el-dropdown-link" @click="goPersonCenter">
  <el-avatar :size="30" :src="circleUrl" />
</span>
<template #dropdown>
<el-dropdown-menu v-if="user">
  <el-dropdown-item>修改信息</el-dropdown-item>
  <el-dropdown-item>退出</el-dropdown-item>
  
</el-dropdown-menu>
<el-dropdown-menu v-else>
  <el-dropdown-item @click="goLogin">登录</el-dropdown-item>
</el-dropdown-menu>
</template>
<el-dropdown> -->