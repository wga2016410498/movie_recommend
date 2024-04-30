<template>
    <!-- 这个是一个下拉列表的轮子 -->
    <div class="zq-drop-list" @mouseover="onDplOver($event)" @mouseout="onDplOut($event)">
        <span>{{dplLable}}<i></i></span>
        <ul v-dpl>
            <li v-for="(item, index) in dataList" :key="index" @click="onLiClick(index, $event)">{{item[labelProperty]}}</li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "DropDownList",
    data(){
        return {
            activeIndex:0
        }
    },
    props:{
        dataList:{
            type:Array,
            default(){
                return [
                    {name: "中文"},
                    {name: "英文"}
                ]
            }
        },
        labelProperty:{
            type:String,
            default(){ return "name" }
        }
    },
    directives:{
        dpl:{
            bind(el){
                el.style.display = "none";
            }
        }
    },
    methods:{
        onDplOver(event){
            let ul = event.currentTarget.childNodes[1];
            ul.style.display = "block";
        },
        onDplOut(event){
            let ul = event.currentTarget.childNodes[1];
            ul.style.display = "none";
        },
        onLiClick(index){
            let path = event.path || (event.composedPath && event.composedPath()) //兼容火狐和safari
            path[1].style.display = "none";
            this.activeIndex = index;
            this.$emit("change", {
                index:index,
                value:this.dataList[index]
            })
        }
    },
    computed:{
        dplLable(){
            return this.dataList[this.activeIndex][this.labelProperty]
        }
    }
}
</script>


<style scoped lang="scss">
    .zq-drop-list{
        display: inline-block;
        min-width: 100px;
        position: relative;
        span{
            display: block;
            height: 30px;
            line-height: 30px;
            background: #f1f1f1;
            font-size: 14px;
            text-align: center;
            color: #333333;
            border-radius: 4px;
            i{
                background: url(https://www.easyicon.net/api/resizeApi.php?id=1189852&size=16) no-repeat center center;
                margin-left: 6px;
                display: inline-block;
            }
        }
        ul{
            position: absolute;
            top: 30px;
            left: 0;
            width: 100%;
            margin: 0;
            padding: 0;
            border: solid 1px #f1f1f1;
            border-radius: 4px;
            overflow: hidden;
            li{
                list-style: none;
                height: 30px;
                line-height: 30px;
                font-size: 14px;
                border-bottom: solid 1px #f1f1f1;
                background: #ffffff;
            }
            li:last-child{
                border-bottom: none;
            }
            li:hover{
                background: #f6f6f6;
            }
        }
    }
</style>