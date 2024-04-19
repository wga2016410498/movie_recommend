<template>
  <div>
    <el-table :data="movies" :table-layout="tableLayout">
        <el-table-column type="expand">
            <template #default="props">
                <div>
                    <p>导演: {{ props.row.director }}</p>
                    <p>演员: {{ props.row.actor }}</p>
                    <p>上映时间: {{ props.row.release_time }}</p>
                    <span>简介: {{ props.row.describe.substring(0, 100) + (props.row.describe.length > 100 ? '...' : '') }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column label="id" prop="movieId"  />
        <el-table-column label="名称" prop="name" />
        <el-table-column label="类型" prop="tag" />
        <el-table-column label="评分" prop="rate" />
        <el-table-column label="时长" prop="duration" />
        <el-table-column>
        <el-table-column label="图片">
            <template v-slot="{ row }">
                <img :src="row.url" alt="图片" style="width: 40px;">
            </template>
        </el-table-column>
        </el-table-column>
        
        <el-table-column width="200px">
            <template #header>
                <el-input v-model="search" size="small" placeholder="请输入..." @keyup.enter="searchByName"/>
            </template>
            <template #default="scope">
                <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
                >修改</el-button
                >
                <el-button
                size="small"
                type="danger"
                @click="handleDelete(scope.row.movieId)"
                >删除</el-button
                >
            </template>
        </el-table-column>
  </el-table>
  <!-- 下面有一个分页 -->
  <el-button type="success" style="position:fixed;bottom:0px;width: 200px;height: 50px;" @click="insertMovie">新增电影</el-button>
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
            @current-change="handleCurrentChange"
            />
        </div>
    </div>
  </div>
  <!-- 设置一个下拉框，负责电影信息的修改 -->
  <el-dialog title="电影信息" v-model="dialogVisible" width="50%" center>
        <el-form :model="movieInfo" label-width="120px">
          <!-- <el-form-item label="电影ID">
            <el-input v-model="movieInfo.movieId" style="width: 80%"></el-input>
          </el-form-item> -->
          <el-form-item label="电影名称">
            <el-input v-model="movieInfo.name" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影类型">
            <el-input v-model="movieInfo.tag" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影评分">
            <el-input v-model="movieInfo.rate" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影时长">
            <el-input v-model="movieInfo.duration" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影导演">
            <el-input v-model="movieInfo.director" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影演员">
            <el-input v-model="movieInfo.actor" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影简介">
            <el-input v-model="movieInfo.describe" style="width: 80%"></el-input>
          </el-form-item>
        </el-form>

        <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="save">确 定</el-button>
          </span>
        </template> 
      </el-dialog>

    <!--这个下拉框负责新增电影的时候使用  -->
      <el-dialog title="电影信息" v-model="insertDialog" width="50%" center>
        <el-form :model="movieInfo" label-width="120px">
          <el-form-item label="电影ID">
            <el-input v-model="movieInfo.movieId" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影名称">
            <el-input v-model="movieInfo.name" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影链接">
            <el-input v-model="movieInfo.url" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影类型">
            <el-input v-model="movieInfo.tag" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影评分">
            <el-input v-model="movieInfo.rate" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影简介">
            <el-input v-model="movieInfo.describe" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影时长">
            <el-input v-model="movieInfo.duration" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影语言">
            <el-input v-model="movieInfo.language" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影导演">
            <el-input v-model="movieInfo.director" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="电影演员">
            <el-input v-model="movieInfo.actor" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="上映地点">
            <el-input v-model="movieInfo.location" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="上映时间">
            <el-input v-model="movieInfo.releaseTime" style="width: 80%"></el-input>
          </el-form-item>
          <el-form-item label="购买链接">
            <el-input v-model="movieInfo.outUrl" style="width: 80%"></el-input>
          </el-form-item>
          
        </el-form>

        <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="add">确 定</el-button>
          </span>
        </template> 
      </el-dialog>
</template>

       
<script>
import request from '@/utils/request';
export default {
    data(){
        return{
            currentPage:1,
            pageSize:7,
            total:10,
            search:'',
            movies:[],
            dialogVisible:false,
            movieInfo:{},
            insertDialog:false,

        };
    },
    created() {
        this.getMovieData()
    },
    methods:{
        getMovieData(){
            request.get('/movies/getbyname',{
                params:{
                    pageNum:this.currentPage,
                    pageSize:this.pageSize,
                    search:this.search,
                }
            }).then(res=>{
                this.movies = res.data.data.list,
                this.total = res.data.data.total
            })
        },
        searchByName(){
            this.getMovieData();
        },
        handleSizeChange(){

        },
        handleCurrentChange(newPage){
            this.pageNum = newPage
            this.getMovieData()
        },
        handleEdit(index, row){
            this.movieInfo = JSON.parse(JSON.stringify(row))
            this.dialogVisible = true;
        },
        handleDelete(id){
            request.delete("/movies/" + id).then(res =>{
                if (res.data.code === '0') {
                    this.$message({
                        type: "success",
                        message: "删除成功"
                    })
                    } 
                else {
                    this.$message({
                        type: "error",
                        message: res.data.msg
                    })
                }
                    // this.getMovieData // 删除之后重新加载表格的数据
            })
            this.getMovieData()
        },
        save(){
            request.put("/movies",this.movieInfo).then(res=>{
                if (res.data.code === '0') {
                    this.$message({
                    type: "success",
                    message: "更新成功"
                    })
                } else {
                    this.$message({
                    type: "error",
                    message: res.data.msg
                    })
                }
                this.getMovieData() // 刷新表格的数据
                this.dialogVisible = false  // 关闭弹窗
            })
        },
        //新增操作
        insertMovie(){
          this.movieInfo={}
          this.insertDialog = true
        },
        add()
        {
          request.post("/movies/addmovie",this.movieInfo).then(res=>{
            if (res.data.code === '0') {
                    this.$message({
                    type: "success",
                    message: "更新成功"
                    })
                } else {
                    this.$message({
                    type: "error",
                    message: res.data.msg
                    })
                }
                this.insertVisible = false  // 关闭弹窗
          })
        }
    },
}
</script>

<style>
.pagination-fixed-bottom {
        position: fixed;
        left:40%;
        bottom: 0;
        background-color: #fff; /* 可根据需要设置背景颜色 */
        border-top: 1px solid #ebeef5; /* 可根据需要设置顶部边框 */
        padding: 10px; /* 可根据需要设置内边距 */
        box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1); /* 可根据需要设置阴影效果 */
    }
</style>

<!-- {
    movie_id:'26425063',
    name:'无双',
    url:'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',	
    tag:'动作',	
    rate:'3',
    describe:'身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
    duration:'130分钟',
    language:'汉语普通话, 粤语, 英语, 泰语, 波兰语',
    director:'庄文强',
    actor:'周润发 郭富城 张静初',
    location:'中国大陆, 香港',
    release_time:'2018-09-30(中国大陆)',
},
{
    movie_id:'26425063',
    name:'无双',
    url:'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',	
    tag:'动作',	
    rate:'3',
    describe:'身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
    duration:'130分钟',
    language:'汉语普通话, 粤语, 英语, 泰语, 波兰语',
    director:'庄文强',
    actor:'周润发 郭富城 张静初',
    location:'中国大陆, 香港',
    release_time:'2018-09-30(中国大陆)',
},
{
    movie_id:'26425063',
    name:'无双',
    url:'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',	
    tag:'动作',	
    rate:'3',
    describe:'身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
    duration:'130分钟',
    language:'汉语普通话, 粤语, 英语, 泰语, 波兰语',
    director:'庄文强',
    actor:'周润发 郭富城 张静初',
    location:'中国大陆, 香港',
    release_time:'2018-09-30(中国大陆)',
},
{
    movie_id:'26425063',
    name:'无双',
    url:'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',	
    tag:'动作',	
    rate:'3',
    describe:'身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
    duration:'130分钟',
    language:'汉语普通话, 粤语, 英语, 泰语, 波兰语',
    director:'庄文强',
    actor:'周润发 郭富城 张静初',
    location:'中国大陆, 香港',
    release_time:'2018-09-30(中国大陆)',
},
{
    movie_id:'26425063',
    name:'无双',
    url:'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',	
    tag:'动作',	
    rate:'3',
    describe:'身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
    duration:'130分钟',
    language:'汉语普通话, 粤语, 英语, 泰语, 波兰语',
    director:'庄文强',
    actor:'周润发 郭富城 张静初',
    location:'中国大陆, 香港',
    release_time:'2018-09-30(中国大陆)',
},
{
    movie_id:'26425063',
    name:'无双',
    url:'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',	
    tag:'动作',	
    rate:'3',
    describe:'身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
    duration:'130分钟',
    language:'汉语普通话, 粤语, 英语, 泰语, 波兰语',
    director:'庄文强',
    actor:'周润发 郭富城 张静初',
    location:'中国大陆, 香港',
    release_time:'2018-09-30(中国大陆)',
},
{
    movie_id:'26425063',
    name:'无双',
    url:'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535260806.webp',	
    tag:'动作',	
    rate:'3',
    describe:'身陷囹圄的李问（郭富城饰）被引渡回港，他原本隶属于一个的跨国假钞制贩组织。该组织曾犯下过多宗恶性案件，而首脑“画家”不仅始终逍遥法外，连真面目都没人知道。为了逼迫李问吐露“画家”真实身份，警方不惜用足以判死刑的假罪证使其就范。就在此时，富有的遗孀阮文（张静初饰）申请保释李问，而警方提出的条件依然是“画家”的真面目。原来早在十数年前，李问和阮文是一对画家情侣，无奈女友的作品受人青睐，李问的画作却被贬得一文不值。就在此困顿期间，他制作假画的才能被“画家”（周润发饰）发掘，进而成为对方美元假币团伙中的一员……',
    duration:'130分钟',
    language:'汉语普通话, 粤语, 英语, 泰语, 波兰语',
    director:'庄文强',
    actor:'周润发 郭富城 张静初',
    location:'中国大陆, 香港',
    release_time:'2018-09-30(中国大陆)',
}, -->