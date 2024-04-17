<template>
  <div class="topheader">
    <!-- 显示小米logo和菜单栏部分 -->
    <div class="header-container">
        <div class="logo">
            <a class="mi-logo">
                <svg data-v-777bda80="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 808 808" class="mi-logo">
                    <g data-v-777bda80=""><path data-v-777bda80="" fill="#ff6900" d="M723.79,84.42C647.55,8.48,537.94,0,404,0,269.89,0,160.12,8.58,83.92,84.72S0,270.43,0,404.39,7.74,648,84,724.14,269.9,808,404,808s243.85-7.71,320-83.86,84-185.78,84-319.75C808,270.25,800.16,160.54,723.79,84.42Z"></path>
                    <path data-v-777bda80="" fill="#fff" d="M374.26,553.72a5,5,0,0,1-5.06,5H300.3a5.05,5.05,0,0,1-5.12-5V373.53a5.05,5.05,0,0,1,5.12-5h68.9a5,5,0,0,1,5.06,5Z"></path>
                    <path data-v-777bda80="" fill="#fff" d="M509.18,553.72a5.05,5.05,0,0,1-5.09,5H438.5a5,5,0,0,1-5.1-5V398.26c-.07-27.15-1.62-55-15.64-69.06-12-12.09-34.51-14.86-57.88-15.44H241a5,5,0,0,0-5.07,5v235a5.07,5.07,0,0,1-5.12,5H165.16a5,5,0,0,1-5.06-5V254.31a5,5,0,0,1,5.06-5H354.52c49.49,0,101.22,2.26,126.74,27.81s27.92,77.3,27.92,126.85Z"></path>
                    <path data-v-777bda80="" fill="#fff" d="M644.29,553.72a5.06,5.06,0,0,1-5.09,5H573.57a5,5,0,0,1-5.08-5V254.31a5,5,0,0,1,5.08-5H639.2a5.06,5.06,0,0,1,5.09,5Z"></path>
                    </g>
                </svg>
            </a>
        </div>
        <div class="navs-container">
            <ul class="navs">
                <li class="navs-item" v-for="(item,index) in navsData" :key="index">
                    <a v-if="item.type" @mouseenter="menusListShow(item.type)"
                    @mouseout="menuListHide()">{{ item.value }}</a>
                </li>
            </ul>
        </div>
        <div class="search">
            <input class="search-input" type="search">
            <button class="search-btn" :class="{'active':foucusFlag}">
                <i class="fa fa-search"></i>
            </button>
        </div>
        <div class="menus-list" v-show="menusListFlag">
            <ul class="menus">
                <li class="menus-item" v-for="(item,index) in menusItemData" :key="index">
                    <a :href="item.src">
                        <img class="item-img" :src="item.url">
                    </a>
                    <div class="item-value">{{ item.value }}</div>
                    <div class="item-type" v-if="item.type">{{ item.type }}</div>
                    <div class="item-price" v-if="item.price&&item.sub">{{ item.price }}元起</div>
                    <div class="item-price" v-if="item.price&&!item.sub">{{ item.price }}</div>
                </li>
            </ul>
        </div>
    </div>

  </div>
</template>

<script>
export default {
    name:'TopHeader',
    data(){
        return{
            menusListFlag:false,
            timer:'',
            focusFlag:false,
            navsData: [
                {value: 'Xiaomi手机', type: 'xiaomi'},
                {value: 'Redmi手机', type: 'redmi'},
                {value: '电视', type: 'tv'},
                {value: '笔记本', type: 'laptop'},
                {value: '平板', type: 'hardware'},
                {value: '家电', type: 'household'},
                {value: '路由器', type: 'router'},
                {value: '服务中心', },
                {value: '社区', }
            ],
            xiaomi: [
            {value: 'Xiaomi Civi2', price: '1799', sub: true, src: 'https://www.mi.com/micc9/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/4ef3713521fb9d7f114aa8bb152e220d.png?thumb=1&w=240&h=165&f=webp&q=90'},
            {value: 'Xiaomi MIX Fold 2', price: '1299', sub: true, src: 'https://www.mi.com/micc9e/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/581f3a690e6803add02e4c9fde98cb78.png?thumb=1&w=240&h=165&f=webp&q=90'},
            {value: 'Xiaomi 12S ULtra', price: '2599', sub: false, src: 'https://www.mi.com/xiaomicc9mt/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/d7a15df55e98e4163390096ed05b1ef5.png?thumb=1&w=240&h=165&f=webp&q=90'},
            {value: 'Xiaomi 12S Pro', price: '2599', sub: true, src: 'https://www.mi.com/mi9/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/b01bb7ee0f8c9865c11eeb2c483015e2.png?thumb=1&w=240&h=165&f=webp&q=90'},
            {value: 'Xiaomi 12S', price: '2599', sub: false, src: 'https://item.mi.com/10000123.html', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/e1f5a30b6e9e29c7f4ad6ed26023f4de.png?thumb=1&w=240&h=165&f=webp&q=90'},
            {value: 'Xiaomi 12 Pro 天玑版', price: '1799', sub: true, src: 'https://www.mi.com/mix2s/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/a811f07a4e13510b23ada8e2eca473ae.png?thumb=1&w=240&h=165&f=webp&q=90'}
            ],
            redmi: [
                {value: 'Redmi Note 12 5G', price: '2299', sub: true, src: 'https://www.mi.com/redmik20pro/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/570184de014d26516f4c334f7132878a.png?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: 'Redmi Note 12 5G', price: '2299', sub: true, src: 'https://www.mi.com/redmik20/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/93e23b29e03f62164c5494a31dbbed25.png?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: 'Redmi Note 12 5G', price: '2299', sub: false, src: 'https://www.mi.com/redminote7pro/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/86122140712f0f645e42934d07d262a8.png?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: 'Redmi Note 12 5G', price: '2299', sub: true, src: 'https://www.mi.com/redmi7a/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/ee06a9131e93619c75c49b88c740203b.png?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: 'Redmi Note 12 5G', price: '2299', sub: true, src: 'https://www.mi.com/redminote7/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/1e1f915167554e99916273b5269da1b5.png?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: 'Redmi Note 12 5G', price: '2299', sub: true, src: 'https://www.mi.com/redmi7/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/f11d7da9517953d11e02d0b459003f19.png?thumb=1&w=240&h=165&f=webp&q=90'}
            ],
            tv: [
                {value: '小米壁画电视 65英寸', price: '6999', sub: false, src: 'https://www.mi.com/arttv/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/00f597a8725eee9245e383c35cd4f7b6.jpg'},
                {value: '小米全面屏电视E55A', price: '1999', sub: false, src: 'https://www.mi.com/mitvall-screen/e55a/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/a40904b6a053b73b631a152334388d0e.jpg'},
                {value: '小米电视4A 32英寸', price: '699', sub: false, src: 'https://www.mi.com/mitv4A/32/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/e8f4e22f6d591825f8f150b3309c750b.png'},
                {value: '小米电视4A 55英寸', price: '1799', sub: false, src: 'https://www.mi.com/mitv4A/55/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/bf72a3e9a6e799cb71ecfa7d80465351.jpg'},
                {value: '小米电视4A 65英寸', price: '2699', sub: false, src: 'https://www.mi.com/mitv4A/65', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/bd922870295a97a0972eaba5af92129e.jpg'},
                {value: '查看全部', type: '小米电视', sub: false, src: 'https://www.mi.com/a/h/9819.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/cd4dafd1461a006f161d00924bf692e9.png'},
            ],
            laptop: [
                {value: 'RedmiBook 14 独显版', price: '3999', sub: true, src: 'https://item.mi.com/10000153.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/be5ddca319f92a508a6e3b3bac4d5fb2.png'},
                {value: '小米笔记本Air 12.5"', price: '3599', sub: true, src: 'https://item.mi.com/10000145.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/95c4329ce2c454e2a5fa1e0931528a46.png'},
                {value: '小米笔记本 Air 13.3"', price: '4999', sub: true, src: 'https://item.mi.com/10000142.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/96108a8feee8e790389b09b8b949fa7d.png'},
                {value: '小米笔记本 15.6"', price: '3799', sub: true, src: 'https://item.mi.com/10000141.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/bb159dbe860ee434b52d8eed9e9fd424.png'},
                {value: '小米笔记本Pro 15.6"', price: '4999', sub: true, src: 'https://item.mi.com/10000144.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/d712f71b3c4a3b562601c2b956a660ad.png'},
                {value: '小米游戏本', price: '5999', sub: true, src: 'https://item.mi.com/10000113.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/60b99f44108d4cf5967bb614cf1e8690.png'}
            ],
            household: [
                {value: '米家互联网空调C1（一级能效）', price: '2299', sub: false, src: 'https://www.mi.com/airconditionc1/v1c1/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/03dc85cd792904ddc8027b2d781beed8.png'},
                {value: '米家互联网空调（一级能效）', price: '2199', sub: false, src: 'https://www.mi.com/airenergy/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/e06b219c5bced9256467b17738a943c6.png'},
                {value: 'Redmi全自动波轮洗衣机1A', price: '699', sub: false, src: 'https://item.mi.com/9509.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/c5d772b7c2a159c3ed7d4e31bd293f18.jpg'},
                {value: '米家互联网洗烘一体机10kg', price: '1899', sub: false, src: 'https://www.mi.com/washer-dryer-10/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/11b8bca444aba2994fe852993eac9203.png'},
                {value: '小米净水器', price: '1999', sub: false, src: 'https://www.mi.com/water2', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/486a2a7359b6bda95b3dbd4e45b9c50a.jpg'},
                {value: '米家扫地机器人', price: '1499', sub: false, src: 'https://www.mi.com/roomrobot/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/4ae019eebf10a55f8df2fee8d19b4e1f.jpg'}
            ],
            router: [
                {value: '小米路由器 Mesh', price: '999', sub: false, src: 'https://www.mi.com/mesh/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/ec5be5f93ac0118aeec27b8df4337fc9.jpg'},
                {value: '小米路由器4A 千兆版', price: '149', sub: false, src: 'https://www.mi.com/miwifi4ac/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/026a28fc18eff2cfa4d26a799a2da9cc.jpg'},
                {value: '小米路由器 4C', price: '59', sub: false, src: 'https://item.mi.com/8645.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/28efac56ef4c4942077dac7e30e8c624.jpg'},
                {value: '小米路由器 4A', price: '99', sub: false, src: 'https://www.mi.com/miwifi4a/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/3c3e9f61cc72ccd2a37fc90fed215b66.jpg'},
                {value: '小米路由器 HD/Pro', price: '399', sub: false, src: 'https://www.mi.com/miwifihd/', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/5fc5ee374e5306aa5513be4f3b560531.png'},
                {value: '查看全部', type: '小米路由器', sub: false, src: 'https://www.mi.com/a/h/8363.html', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/2ddc6a2789c5f5ff78fa4ca1402417c8.png'}
            ],
            hardware: [
                {value: '小米平板5', price: '189', sub: false, src: 'https://www.mi.com/camera-360/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/a887139f3995c4cac2a167e014ffd91e.jpg?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: '小米平板5', price: '489', sub: true, src: 'https://www.mi.com/aiteacher-wifi/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/1ba211a988be47d7ae5a1a448ecf0b67.jpeg?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: '小米平板5', price: '1299', sub: false, src: 'https://www.mi.com/mj-smartlock/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/33de34a4caf2834a1828dc51203dc922.png?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: '小米平板5', price: '299', sub: false, src: 'https://www.mi.com/aispeaker-touch/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/03892b203a6413bcd8ef3f92d77df79c.gif?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: '小米平板5', price: '179', sub: false, src: 'https://www.mi.com/aispeaker-control/', url: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/03892b203a6413bcd8ef3f92d77df79c.gif?thumb=1&w=240&h=165&f=webp&q=90'},
                {value: '小米平板5', type: '智能硬件', sub: false, src: 'https://www.mi.com/p/3469.html?client_id=180100041086&masid=17409.0245', url: 'https://cdn.cnbj0.fds.api.mi-img.com/b2c-mimall-media/c1016ddffd2ac5808c4bebcdbefd413a.jpg'}
            ],
            menusItemData:[],
        }
    },
    methods:{
        menusListShow(type){
            if(type){
                this.menusItemData = this[type]
            }
            this.menusListFlag = true;
            clearTimeout(this.timer);//取消之前设置的定时器，确保在菜单显示时立即隐藏时不会触发之前设置的延迟隐藏操作
        },
        menuListHide(){
            //通过setTimeout设置了一个延迟隐藏的定时器，
            this.timer = setTimeout(()=>{
                this.menusListFlag = false; 
            },300)
        }
    }

}
</script>

<style scoped>
a{
    font-size:15px;
}
.topheader{
    width: 100%;
}
.header-container{
    width: 1226px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    align-items: center;
    position: relative;
}
.logo{
    margin: 30px;
}
.mi-logo{
    width: 50px;
}
.navs{
    width: 800px;
    display: flex;
    margin-left: 120px;
    justify-content: space-between;
}
.search{
    display: flex;
}
.search-input{
    width: 160px;
    height: 40px;
    outline: none;
    font-size: 15px;
    border: 1px solid #e0e0e0;
}
.search-btn{
    height: 40px;
    width: 40px;
}
.search-btn:hover i{
    background:#ff6700;
    color: #fff;
    transition: all .20s ease;
}
.menus-list{
    position:absolute;
    width: 100%;
    left: 0;
    top: 100%;
    z-index: 1;
    background-color: whitesmoke;
}
.menus{
    display: flex;
    padding: 30xp 0 30px 110px;
    justify-content: space-between;
}
.menus-item a{ 
    text-decoration: none;
    display: block;
    padding: 0 20px;
    border-right:1px gray solid ;
}
.item-img{
    width:160px;
    height: 110px;
}
.item-value{
    width: 100%;
    height:16px;
    margin-top:16px;
    text-align: center;
    font-size: 12px;
}
.item-price{
    font-size: 10px;
    text-align: center;
    color: #ff6700;
}

</style>