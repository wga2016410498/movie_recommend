<template>
  <div class="product">
    <div class="image-container">
        <a :href="url" target="_blank">
            <img :src="src" />
        </a>
    </div>
    <GoodsBox :goodsItem="goodsItem"></GoodsBox>
    <GoodsBox :goodsItem="goodsItemA"></GoodsBox>
    <GoodsBox :goodsItem="goodsItemB"></GoodsBox>
  </div>
</template>

<script>
import GoodsBox from '@/parts/GoodsBox.vue'

export default {
    name:'HotSale',
    components:{
        'GoodsBox':GoodsBox
    },
    data() {
        return {
            src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/2656295f6c067f48a04a425acf15a096.jpg?thumb=1&w=1839&h=180&f=webp&q=90',
            goodsItem: {
                boxTitle: '手机',
                isHot: false,
                vertical: true,
                listData: {
                promo: [{
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/059f14c9ba134897be7db7a7286f1bb5.jpg?thumb=1&w=351&h=921&f=webp&q=90',
                }],
                goods: [
                    {
                    value: 'Redmi Note 8 Pro',
                    desc: '6400万全场景四摄',
                    sub: true,
                    newPrice: '1199',
                    oldPrice: '',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202210262033_ef39fca0e37395d07682124770fd3ad9.png?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: 'Redmi Note 8',
                    desc: '千元4800万四摄',
                    sub: true,
                    newPrice: '1699',
                    oldPrice: '',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202210262012_94dd4ca657adcebec0d11ea09dac8a03.png?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: 'Redmi K20 Pro 6GB+128GB',
                    desc: '骁龙855， 弹出全面屏',
                    sub: false,
                    newPrice: '2199',
                    oldPrice: '2599',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202210262024_83bfd34bb3f733d69d342acaf34aea58.png?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: 'Redmi Note 7',
                    desc: '4800万拍照千元机',
                    sub: false,
                    newPrice: '1099',
                    oldPrice: '1199',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/50da95e9e4496dcac8704da2deb94f6e.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: 'Redmi 7',
                    desc: '4000mAh超长续航',
                    sub: true,
                    newPrice: '2299',
                    oldPrice: '2399',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/28c14106b688ac7ae88e761564789b37.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米MIX 3 8GB+128GB',
                    desc: 'DxO百分拍照手机',
                    sub: false,
                    newPrice: '1569',
                    oldPrice: '1799',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/5713971c4bb6512743dfd06023080268.png?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米CC9',
                    desc: '3200万自拍，4800万三摄',
                    sub: true,
                    newPrice: '4399',
                    oldPrice: '4699',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202207012000_0b9df066c110f201154013ac373df1d9.png?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米9 SE',
                    desc: '索尼4800万三摄，骁龙712',
                    sub: true,
                    newPrice: '2999',
                    oldPrice: '',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202208101511_488638d8f8d5dbcf3b66cd82703ecfb9.png?thumb=1&w=300&h=300&f=webp&q=90',

                    }
                ]
                }
            },
            goodsItemA: {
            boxTitle: '智能穿戴',
            isHot: true,
            vertical: false,
            tabList: [
            {value: '耳机', type: 'hots', },
            {value: '穿戴', type: 'trip', }
            ],
            listData: {
            promo: [
                {
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/45c23f5b9a927b2dc49c25277e07727c.jpg?w=468&h=600',

                },
                {
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/a660ce095e8f553a9ed1515265f4e9fc.jpg?w=468&h=600',

                }
            ],
            hots: [
                {
                value: 'Xiaomi Buds 4 Pro',
                desc: '48dB智能动态降噪',
                sub: true,
                newPrice: '1049',
                oldPrice: '1099',
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202208111200_c1016839eae2c1f5bb79d5afde498e81.png?thumb=1&w=300&h=300&f=webp&q=90',

                },
                {
                value: 'Xiaomi Buds 3 Pro',
                desc: '48dB智能动态降噪',
                sub: false,
                newPrice: '499',
                oldPrice: '699',
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202204211422_ce41ed00fe7fb79df35101222880121d.png?thumb=1&w=300&h=300&f=webp&q=90',

                },
                {
                value: 'Xiaomi Buds 4 ',
                desc: '48dB智能动态降噪',
                sub: false,
                newPrice: '299',
                oldPrice: '199',
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/0b271a074e087848357aa61ae665b214.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                },
                {
                value: 'Xiaomi Buds 4 ',
                desc: '48dB智能动态降噪',
                sub: false,
                newPrice: '169',
                oldPrice: '99',
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202205241527_fb27e27e6587254da27de5ba9c889512.png?thumb=1&w=300&h=300&f=webp&q=90',

                },
                {
                value: 'Xiaomi Buds 3',
                desc: '48dB智能动态降噪',
                sub: false,
                newPrice: '109',
                oldPrice: '169',
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/11570d5371f16d2d9b19f504e09d01f0.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                },
                {
                value: 'Xiaomi Buds 4 青春版',
                desc: '48dB智能动态降噪',
                sub: false,
                newPrice: '169',
                oldPrice: '',
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/2fcf24e40ff09a254857ac8b4ace25b8.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                },
                {
                value: '小米无线蓝牙耳机',
                desc: '48dB智能动态降噪',
                sub: false,
                newPrice: '999',
                oldPrice: '',
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202111052007_e8e92e67988ebaff6e075412a54c3c66.png?thumb=1&w=300&h=300&f=webp&q=90',

                },
                {
                value: '骨传导耳机',
                desc: '',
                sub: false,
                newPrice: '99',
                oldPrice: '',
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202210191430_3ad0e4809ce06a126dea9755adbb2a1b.png?thumb=1&w=150&h=150&f=webp&q=90',

                }
            ],
            trip: [
                {
                value: '小米米家电动滑板车',
                desc: '便携折叠，自由穿行',
                sub: false,
                newPrice: '1999',
                oldPrice: '',
                src: 'https://i8.mifile.cn/v1/a1/768992ca-4136-92f1-244a-0194a81a6360.jpg',

                },
                {
                value: '米兔折叠婴儿推车',
                desc: '出发去向往的地方',
                sub: false,
                newPrice: '669',
                oldPrice: '699',
                src: 'https://i8.mifile.cn/b2c-mimall-media/18a82e7cda6ecbc22ecee7ac927d6ff9.jpg',

                },
                {
                value: '米兔遥控小飞机',
                desc: '迷你酷玩具，溜到飞起',
                sub: false,
                newPrice: '399',
                oldPrice: '',
                src: 'https://i8.mifile.cn/b2c-mimall-media/553b5c01820c844565abe64e50bba323.jpg',

                },
                {
                value: '米家车载空气净化器',
                desc: '高效净化车内空气',
                sub: false,
                newPrice: '449',
                oldPrice: '',
                src: 'https://i8.mifile.cn/v1/a1/cdc5c77b-d7e9-5a42-f848-3ff1808a139a.jpg',

                },
                {
                value: 'AMAZFIT 运动手表',
                desc: '扔掉手机去跑步',
                sub: false,
                newPrice: '769',
                oldPrice: '799',
                src: 'https://i8.mifile.cn/v1/a1/aaa1593d-9ca7-2944-3b62-380cc3427d82.jpg',

                },
                {
                value: '九号平衡车 Plus',
                desc: '一个形影不离的新伙伴',
                sub: false,
                newPrice: '3499',
                oldPrice: '',
                src: 'https://i8.mifile.cn/v1/a1/877d3ce8-68ab-7506-2a78-55a8c0fba946.png',

                },
                {
                value: '米家车载逆变器',
                desc: '双USB充电口，国际组合插孔',
                sub: false,
                newPrice: '199',
                oldPrice: '',
                src: 'https://i8.mifile.cn/b2c-mimall-media/61472c3fcd181959055551e5c73aafec.jpg',

                },
                {
                value: '米家充气宝',
                desc: '',
                sub: false,
                newPrice: '199',
                oldPrice: '',
                src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/0294e2f3997bf0cffb7bf48361d03588.jpg',

                }
            ]
            }
            },
            goodsItemB: {
                boxTitle: '家电',
                isHot: true,
                vertical: false,
                tabList: [
                {value: '热门', type: 'hots', },
                {value: '电视音影', type: 'television', }
                ],
                listData: {
                promo: [
                    {
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/3d47879ec183e25a36e67e0219636e60.jpg?thumb=1&w=351&h=450&f=webp&q=90',

                    },
                    {
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/229bbaccda43f32f464c0a810b800106.jpg?thumb=1&w=351&h=450&f=webp&q=90',

                    }
                ],
                hots: [
                    {
                    value: '小米电视6 65 OLED',
                    desc: 'OLED自发光屏|百万级对比度',
                    sub: false,
                    newPrice: '6699',
                    oldPrice: '6999',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/82ff5ea76730fdf6f91aba5d3b2e5739.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米电视6 至尊版 65英寸',
                    desc: '百万分区背光|双120Hz高刷',
                    sub: false,
                    newPrice: '7199',
                    oldPrice: '7999',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/c7c15101f2c8a652a4a0d069501d1e53.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米电视 ES55 2022款',
                    desc: '百万分区背光|双120Hz高刷',
                    sub: false,
                    newPrice: '2999',
                    oldPrice: '',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/388b13bf52ab0d6a56bc9f195b5f1dd5.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '巨省电 小米空调 1.5匹新1级能效',
                    desc: '百万分区背光|双120Hz高刷',
                    sub: false,
                    newPrice: '2199',
                    oldPrice: '2499',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/21429638bdd453e8c1cb5c357ff4835b.png?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: 'Redmi全自动波轮洗衣机1A 8kg',
                    desc: '百万分区背光|双120Hz高刷',
                    sub: false,
                    newPrice: '2499',
                    oldPrice: '2699',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/2ff20ac3e305cee9e9cd2ac269f1b488.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '米家新风空调 立式3匹',
                    desc: '全面屏设计，人工智能语音',
                    sub: false,
                    newPrice: '6999',
                    oldPrice: '7299',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/9cd8a5a447b4f84faeb3791811a179f9.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '米家直驱洗烘一体机',
                    desc: '安静护衣',
                    sub: false,
                    newPrice: '4899',
                    oldPrice: '',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/74d58c933744cca5fce7e198a90bf364.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: 'Air 13.3" 2019款 ',
                    desc: '',
                    sub: true,
                    newPrice: '4699',
                    oldPrice: '',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/b649a329983ad590fde607472f73e55a.jpg?thumb=1&w=150&h=150&f=webp&q=90',

                    }
                ],
                television: [
                    {
                    value: '小米电视4A 32英寸',
                    desc: '人工智能系统，高清液晶屏',
                    sub: false,
                    newPrice: '699',
                    oldPrice: '799',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/363bf63e1ca2c6b21a0e5e21cd284368.png?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米全面屏电视E55A',
                    desc: '全面屏设计，人工智能语音',
                    sub: false,
                    newPrice: '1999',
                    oldPrice: '2099',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/9d8674cd21c486feff5328772ab9cf01.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米全面屏电视E65A',
                    desc: '全面屏设计，人工智能语音',
                    sub: false,
                    newPrice: '2999',
                    oldPrice: '3999',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/ecbe6a6c0d4950b78b086d7ada654e3b.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米电视4X 43英寸',
                    desc: 'FHD全高清屏，人工智能语音',
                    sub: false,
                    newPrice: '1299',
                    oldPrice: '1499',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/a5572d6d4adea2e8e9f936ef19024dd4.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米电视4C 55英寸',
                    desc: '4K HDR，人工智能系统',
                    sub: false,
                    newPrice: '1699',
                    oldPrice: '1799',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/03a9e7e96a09d256ca1badeec186c859.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米电视4A 65英寸',
                    desc: '4K HDR，人工智能语音系统',
                    sub: false,
                    newPrice: '2699',
                    oldPrice: '2999',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/f674ced205c2e81125dfd2d6659aabfc.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米壁画电视 65英寸',
                    desc: '壁画外观，全面屏，远场语音',
                    sub: false,
                    newPrice: '6999',
                    oldPrice: '',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/5f8be2fa1f60f81a0cfbfa3f6e0a5723.jpg?thumb=1&w=300&h=300&f=webp&q=90',

                    },
                    {
                    value: '小米盒子4',
                    desc: '',
                    sub: false,
                    newPrice: '299',
                    oldPrice: '',
                    src: 'https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/4769d147d65c64de4fd808e0d5229b5e.jpg?thumb=1&w=150&h=150&f=webp&q=90',

                    }
                ]
            }
            }
        }
        
    },
}
</script>

<style>
.product{
    
    width: 1226px;
    margin-left: auto;
    margin-right: auto;
    margin-top:10px
}

img{
   width: 100%;
}
</style>