<template>
    <div>
        <el-row>
            <!-- 推荐列表 -->
            <el-col :span="17">
                <div class="title">
                    <h2 style="text-align:left;font-weight:700;">作品推荐</h2>
                </div>
                <el-row>
                    <el-col :span="7"
                        v-for="(movie,index) in recommondItems"
                        :key="index"
                        style="margin-right: 26px;margin-bottom: 30px;"
                        
                    >
                    <card :card="movie"></card>
                    </el-col>
                </el-row>
            </el-col>

            <!-- 排行榜 -->
            <el-col :span="7">
                <ranking-list :rankinglist="rankinglist"></ranking-list>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Card from '@/components/Home/Card.vue'
import RankingList from './RankingList.vue'
export default {
    name:'Recommend',
    props:['recommondItems', 'rankinglist'],
    components: {
    RankingList,
    Card
    },
    methods:{
    }
}
</script>

<style>

</style>

 <!-- <el-row>
                    <el-col :span="7"
                            v-for="id in 3"
                            :key="id+3"
                            style="margin-right: 26px;margin-bottom: 30px;">
                        <card :card="recommondItems[id+2]"></card>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="7"
                            v-for="id in 3"
                            :key="id+6"
                            style="margin-right: 26px;margin-bottom: 30px;">
                        <card :card="recommondItems[id+5]"></card>
                    </el-col>
                </el-row> -->