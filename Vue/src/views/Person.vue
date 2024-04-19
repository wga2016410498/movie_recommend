<template>
  <div class="root">
    <div class="img-container">
      <img :src="picture_url">
    </div>
    <div class="userinfo">
      <div class="container">
          <el-card style="width: 600px;height: 320px;" shadow="always">
            
            <div class="user-card-header">
              <el-avatar shape="square" :size="250" :fit="fit" :src="user_url" />
            </div>
            <div class="info-item">
              <span class="label">用户名：</span>
              <span class="value">{{ userInfo.userName }}</span>
            </div>
            <div class="info-item">
              <span class="label">邮箱：</span>
              <span class="value">{{ userInfo.email }}</span>
            </div>
            <div class="info-item">
              <span class="label">年龄：</span>
              <span class="value">{{ userInfo.age }}</span>
            </div>
            <div class="info-item">
              <span class="label">性别：</span>
              <span class="value">{{ userInfo.gender }}</span>
            </div>
            <div class="info-item">
              <span class="label">职业：</span>
              <span class="value">{{ userInfo.occupation }}</span>
            </div>
            <div class="info-item">
              <el-tag size="small">{{ userInfo.role ? '管理员' : '普通用户' }}</el-tag>
            </div>
            <el-button type="text" icon="el-icon-edit"  @click="editProfile">编辑</el-button>
          </el-card>
      </div>

      <!-- 用户信息下拉框 -->
      <el-dialog title="用户信息" v-model="dialogVisible" width="50%" center>
        <el-form :model="userInfo" label-width="120px">
          <el-form-item label="用户名">
            <el-input v-model="userInfo.userName" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="邮箱">
            <el-input v-model="userInfo.email" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="年龄">
            <el-input v-model="userInfo.age" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="性别">
            <el-input v-model="userInfo.gender" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="职业">
            <el-input v-model="userInfo.occupation" style="width: 80%"></el-input>
          </el-form-item>
        </el-form>

        <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="save">确 定</el-button>
          </span>
        </template> 
      </el-dialog>

      <!-- 这个是尾部的一些东西 -->
      <div class="copy-right">公司版权所有-京ICP备10046444-京公网安备11010802020134号-京ICP证110507号</div>
   
    </div>
  </div>
</template>

<script>

import request from '@/utils/request'
export default {
  name:'Person',
 
  data(){
    return{
      picture_url:"https://images.wallpapersden.com/image/download/among-us-cool_bGprbmWUmZqaraWkpJRsamWtZm1lZQ.jpg",
      user_url:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      userInfo :{
      },
      dialogVisible:false,
    }
  },
  methods: {
    load()
    {
      this.userInfo  = JSON.parse(sessionStorage.getItem("user"))
    },
    editProfile()
    {
      this.dialogVisible = true;
    },
    save()
    {
        request.put("/updateinfo",this.userInfo).then(res=>{
          if (res.data.code === '0') {
                    this.$message({
                        type: "success",
                        message: "更新成功"
                    })
                    } 
                else {
                    this.$message({
                        type: "error",
                        message: res.data.msg
            })
          }
          this.dialogVisible = false
        }
        )
    }
  },
  created(){
      this.load()
  },


}
</script>

<style scoped lang="scss">
.root{
  height: 793px;
  display: flex;
  justify-content: space-between;
  .img-container{
    img{
      width: 375px;
    }
  }
  .userinfo{
    width: 1105px;
    height: 900px;
    padding-bottom: 40px;
    font-size: 14px;
    display: flex;
    flex-direction: column;
    }
    .container{
      display: flex;
      padding-top: 200px;
      align-items: center; /* 让内容在垂直方向上居中 */
      justify-content: center; /* 可选，如果需要在水平方向上也居中 */
    }
    .copy-right{
        position:fixed;
        bottom: 20px;
        left: 650px;
        // margin-top: 100px;
        text-align: center;
        font-size: 12px;
        font-weight: 500;
        color: rgba(0,0,0,0.3);
    }
    .user-card-header {
      // display: flex;
      // justify-content: space-between;
      // align-items: center;
      float: left;
      margin-right: 20px;
    }

    .info-item {
      margin-bottom: 15px;
    }

    .label {
      font-weight: bold;
    }

    .value {
      margin-left: 10px;
    }
  }
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>