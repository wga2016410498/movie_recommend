<template>
  

  <!-- 管理电影 -->
  <!-- 管理权限 -->
  <!-- 管理用户 -->
  <el-header>
    <NavHead :user="user"></NavHead>
  </el-header>
  <el-container>
    <el-aside width="170px" style="margin-left:100px;">
      <el-menu
        :default-active="this.$route.path"
        class="el-menu-vertical"
        :router = 'true'
        @open="handleOpen"
        @close="handleClose"
        style="margin-top: 20px;"
      >
        
        <el-menu-item index="/managemovie"  style="margin-bottom: 150px;">
          <el-icon><location /></el-icon>
          <span>电影管理</span>
        </el-menu-item>
        <el-menu-item index="2" style="margin-bottom: 150px;">
          <el-icon><IconMenu/></el-icon>
          <span>用户管理</span>
        </el-menu-item>
        <el-menu-item index="3" style="margin-bottom: 150px;">
          <el-icon><document /></el-icon>
          <span>权限管理</span>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><setting /></el-icon>
          <span>订单管理</span>
        </el-menu-item>
         <!-- <el-sub-menu index="5">
          <template #title>
            <span>信息统计</span>
          </template>
          <el-menu-item-group title="Group One">
            <el-menu-item index="1-1">item one</el-menu-item>
            <el-menu-item index="1-2">item two</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="Group Two">
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          <el-sub-menu index="1-4">
            <template #title>item four</template>
            <el-menu-item index="1-4-1">item one</el-menu-item>
          </el-sub-menu>
        </el-sub-menu> -->
      </el-menu>
    </el-aside>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
  
</template>

<script>
import NavHead from '@/components/Home/NavHead.vue';
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
export default {
   data(){

    },
    components:{
      NavHead,
      Document,
      IconMenu,
      Location,
      Setting
    }
}
</script>

<style>

</style>