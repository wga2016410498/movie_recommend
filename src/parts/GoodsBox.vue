<template>
    <div class="good-box">
        <div class="box-header">
            <h2 class="box-title">{{ goodsItem.boxTitle }}</h2>
            <div class="type-select" v-if="goodsItem.isHot">
                <ul class="tab-list">
                    <li class="tab-item" v-for="(item,index) in goodsItem.tabList" 
                    :key="index"
                    :class="{'active': item.type === selectItem.type}"
                    @mouseenter="selectType(item)">
                        {{ item.value }}
                    </li>
                </ul>
            </div>
            <div class="type-more" v-else>
                <a :href="goodsItem.url" target="_blank">
                    <span>查看全部</span>
                    <i class="fa fa-angle-right"></i>
                </a>
            </div>
        </div>
        <div class="box-content">
            <div class="promo-content">
                
                <div class="promo-one" v-if="goodsItem.listData.promo.length === 1">
                    <a class="brick-item" target="_blank" :href="goodsItem.listData.promo[0].url">
                    <img :src="goodsItem.listData.promo[0].src">
                    </a>
                </div>
                
                <div class="promo-two" v-if="goodsItem.listData.promo.length === 2">
                    <a class="brick-item" target="_blank"
                        :href="item.url"
                        v-for="(item, index) in goodsItem.listData.promo"
                        :key="index">
                        <img :src="item.src">
                    </a>
                </div>
            </div>
            <div class="goods-content">
                <div class="goods-one" v-if="!goodsItem.isHot">
                    <div class="goods-item" v-for="(item, index) in goodsItem.listData.goods" :key="index">
                        <a :href="item.url" target="_blank">
                            <img :src="item.src" :alt="item.value">
                            <h3 class="name">{{item.value}}</h3>
                            <span class="desc">{{item.desc}}</span>
                            <div class="price">
                                <span>{{item.newPrice}}元</span>
                                <span v-if="item.sub">起</span>
                                <del v-if="item.oldPrice">{{item.oldPrice}}元</del>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="goods-two" v-else>
                    <template v-for="(item, index) in goodsData">
                        <!-- 如果是最后一张图片 -->
                        <div class="goods-item-end" :key="index" v-if="index === goodsData.length - 1 && goodsData.length % 2 === 0">
                            <a class="brick-item" :href="item.url" target="_blank">
                                <div class="text-container">
                                    <h3 class="name">{{item.value}}</h3>
                                    <div class="price">
                                    <span>{{item.newPrice}}元</span>
                                    <span v-if="item.sub">起</span>
                                    </div>
                                </div>
                                <img :src="item.src" :alt="item.value">
                            </a>
                            <!-- 点击浏览更多会跳转到别的页面 -->
                            <a class="brick-more" :href="selectItem.url" target="_blank">
                                <div class="look-more">
                                    <h3 class="name">浏览更多</h3>
                                    <span class="desc">{{selectItem.value}}</span>
                                </div>
                                <img src="../assets/image/right.png">
                            </a>
                        </div>
                        <!-- 非最后一张图片 -->
                        <div class="goods-item" :key="index" v-if="index < goodsData.length - 1">
                            <a class="brick-items" :href="item.url" target="_blank">
                                <img :src="item.src" :alt="item.value">
                                <h3 class="name">{{item.value}}</h3>
                                <span class="desc">{{item.desc}}</span>
                                <div class="price">
                                    <span>{{item.newPrice}}元</span>
                                    <span v-if="item.sub">起</span>
                                    <del v-if="item.oldPrice">{{item.oldPrice}}元</del>
                                </div>
                            </a>
                        </div>
                    </template>
                </div>
            </div>
        </div>
        
        
    </div>
</template>

<script>
export default {
    name:'GoodsBox',
    props:['goodsItem'],
    data(){
        return{
            selectItem: '',
            goodsData: ''
        }
    },
    methods:{
        selectType (item) {
            this.selectItem = item;
            this.goodsData = this.goodsItem.listData[item.type];
        },
        init(){
            if (this.goodsItem.tabList) {
                this.selectItem = this.goodsItem.tabList[0];
                this.goodsData = this.goodsItem.listData.hots;
            } else {
                this.selectItem = '';
                this.goodsData = '';
            }  
        }
    },
    mounted(){
        this.init();
    }
}
</script>

<style lang="scss">
.good-box{
    width: 1226px;
    margin-left: auto;
    margin-right: auto;
}
.box-header{
    display: flex;
    justify-content: space-between;
    .type-select{
        .tab-list{
            display: flex;
            .tab-item{
                display: inline-block;
                margin-right: 10px;
                font-size: 15px;
                color: #424242;
                border-bottom: 2px solid transparent;//渐变颜色
                transition: all .3s;
                cursor: pointer;
            }
            .active {
                border-bottom: 2px solid #ff6709;
                color: #ff6709;
            }
        }
    }
    .type-more{
        a {
            font-size: 16px;
            display: flex;
            align-items: center;
            span {
                color: #424242;
                transition: all .4s;
            }
            i {
                width: 20px;
                height: 20px;
                margin-left: 8px;
                border-radius: 16px;
                font-size: 15px;
                line-height: 20px;
                background: #b0b0b0;
                color: #fff;
                text-align: center;
                transition: all .4s;
            }
            &:hover {
                span {
                color: #ff6709;
                }

                i {
                background: #ff6709;
                }
            }
        }
    }
}

.box-content{
    display: flex;
    .promo-content{
        .promo-one{
            width: 200px;
        }
        .promo-two{
            width: 200px;
            .brick-item{
                img{
                    width: 100%;
                }
            }

        }
    }
}
.goods-content{
    .goods-one{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr; 
        grid-row-gap: 10px;
        flex-wrap: wrap;
        .goods-item {
            margin-left: 50px;
            cursor: pointer;
            a{
                display: flex;
                flex-direction: column;
                text-align: center;
                img{
                    width: 200px;
                }
            }
        }
    }
    .goods-two{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr; 
        grid-row-gap: 10px;
        flex-wrap: wrap;
        .goods-item-end{
            // display: grid;
            // grid-row-gap: 100px;
            margin-left: 50px;
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            .brick-item{
                width: 100px;
                display: flex;
                .text-container{
                    // background-color: red;
                    text-align: center;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                }
            }
            .brick-more{
               
                width: 100px;
                display: flex;
                // text-align: center;
                .look-more{
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                }
                
            }
        }
        .goods-item {
            margin-left: 50px;
            cursor: pointer;
            a{
                display: flex;
                flex-direction: column;
                text-align: center;
                img{
                    width: 200px;
                }
            }
        }
    }
}
.brick-items{
    transition: all .2s linear;
    &:hover {
        transform: translate3d(0, -2px, 0);
        box-shadow: 0 15px 30px rgba(0, 0, 0, .1);
    }
}

</style>