<template>
    <div class="bar">
        <div class="top-bar">
            <!-- 内容栏 -->
            <div class="nav-container">
                <ul class="nav">
                    <li class="nav-item" v-for ="(item,index) in navData" :key="index">
                        <a v-bind:href="item.url">{{ item.value }}</a>
                        <span class="nav-span" v-show="index !== navData.length - 1">|</span>
                    </li>
                </ul>
            </div>
            <!-- 登陆注册栏 -->
            <div class="nav-login">
                <ul class="login-register">
                    <li class="login-register-item" v-for="(item,index) in loginData" :key="index">
                        <a v-bind:href="item.url">{{ item.value }}</a>
                        <span class="nav-span" v-show="index !== loginData.length - 1">|</span>
                    </li>
                </ul>

            </div>
            <!-- 购物车栏 -->
            <div class="nav-cart" v-on:mouseenter="cartListShow" v-on:mouseleave="carListHide">
                <div class="cart-container" >
                    <i class="icon-cart fa fa-shopping-cart"></i>
                    <a href="https://static.mi.com/cart/">
                        购物车（0）
                    </a>
                </div>
                <!-- transation -->
                <transition name="fade-in">
                    <div class="cart-content" v-show="showFlag">
                        <div class="content-word">购物车还没有商品，赶快选购吧！</div>
                    </div>
                </transition>
                
            </div>
            
        </div>
    </div>
    

</template>

<script>
export default {
    name:'TopBar',
    data(){
        return{
            navData :[
            {value: '小米官网', url: 'https://www.mi.com/index.html'},
            {value: '小米商城', url: 'https://www.mi.com/index.html'},
            {value: 'MIUI', url: 'https://www.miui.com/'},
            {value: 'loT', url: 'https://iot.mi.com/index.html'},
            {value: '云服务', url: 'https://i.mi.com/'},
            {value: '天星数科', url: 'https://jr.mi.com?from=micom'},
            {value: '有品', url: 'https://youpin.mi.com/'},
            {value: '小爱开放平台', url: 'https://xiaoai.mi.com/'},
            {value: '企业团购', url: 'https://qiye.mi.com/'},
            {value: '资质证照', url: 'https://www.mi.com/aptitude/list/?id=41'},
            {value: '协议规则', url: 'https://www.mi.com/aptitude/list/'},
            {value: '下载app', url: 'https://www.mi.com/appdownload/'},
            {value: 'Select Location', url: 'javascript:void(0);'}
            ] ,
            loginData: [
            {value: '登陆', url: '/login'},
            {value: '注册', url: '/register'},
            {value: '消息通知', url: 'https://order.mi.com/message/list'}
            ],
            
            showFlag : false,
        }
    },
    methods:{
        cartListShow(){
            this.showFlag = true;
        },
        carListHide(){
            this.showFlag = false;
        }
    }
}
</script>

<style scoped>
.bar{
    width: 100%;
    background-color: #333;
}
a{
    color: #fff;
}
.top-bar{
    width: 1400px;
    height: 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-right: auto;
    margin-left: auto;
}
.nav{
    display: flex;
}
.nav-item{
    align-items: center;
}
.nav-item:hover a{
    color:#ff6700
}
.nav-span{
    color: #fff;
    margin: 0 10px;
}
.login-register{
    display: flex;
}
.login-register-item:hover a{
    color: #ff6700;
}
.nav-cart{
    width: 120px;
    background:#424242;
    margin-left: 25px;
    cursor: pointer;  /*鼠标在上面变成一个小手，也可以变成一个？啥的*/
    height: 40px;
    position: relative;
}
.nav-cart:hover a,.nav-cart:hover i{
    color: #ff6700;
}
.cart-container{
    height: 40px;
    display: flex;
    justify-content: center; /* 水平居中对齐 */
    align-items: center; /* 垂直居中对齐 */
}
.cart-container a{
    margin: 10px;
}

.cart-content{
    width: 300px;
    position: absolute;
    top:100%;
    right: 0;
    background-color: #fff;
    box-shadow: 0 0 5px -1px #ccc;
    z-index: 1;
}
.content-word{
    line-height: 96px;
    text-align: center;
}
/* 过渡效果 */
.fade-in-enter-active, .fade-in-leave-active {
    transition: opacity 1s; /* 过渡持续时间为 0.5 秒 */
}
.fade-in-enter, .fade-in-leave-to {
    opacity: 0; /* 开始时和结束时设置透明度为 0 */
}
</style>