<template>
  <div class="site-footer">
    <ul class="site-service">
      <li class="service-item"  v-for="(item, index) in serviceInfo"  :key="index">
        <a :href="item.url" target="_blank">
          <i :class="item.font"></i>
          <span>{{item.value}}</span>
        </a>
      </li>
    </ul>
    <div class="service-center">
      <div class="site-link">
        <div class="links">
          <div class="link-container" v-for="(list, key) in serviceLink" :key="key">
            <span class="link-title">
              {{list.value}}
            </span>
            <ul class="link-list">
              <li class="link-item" v-for="(item, index) in list.subLinks" :key="index">
                <a :href="item.url" target="_blank">{{item.value}}</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="link-contact">
        <p class="phone">400-100-5678</p>
        <p class="desc">8:00-18:00<br>（仅收市话费）</p>
        <a href="https://support.kefu.mi.com/" target="_blank">
          <label></label>
          <span>人工客服</span>
        </a>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "SiteFooter",
  data () {
    return {
      serviceInfo: [
        {value: '预约维修服务', font:'icon-buoumaotubiao46', url: 'https://www.mi.com/static/fast/'},
        {value: '7天无理由退货', font:'icon-7tianwuliyoutuihuo', url: 'https://www.mi.com/service/exchange#back'},
        {value: '15天免费换货', font:'icon-15tianwuliyoutuihuo', url: 'https://www.mi.com/service/exchange#back'},
        {value: '满69元包邮', font:'icon-liwu', url: 'https://www.mi.com/service/buy/postage/'},
        {value: '1100余家售后网点', font:'icon-icon-test', url: 'https://www.mi.com/static/maintainlocation/'}
      ],
      serviceLink: [
        {value: '选购指南', subLinks: [
            {value: '手机', url: 'https://www.mi.com/service/account/Account%20registration/'},
            {value: '电视', url: 'https://www.mi.com/service/buy/SalesTime/'},
            {value: '笔记本', url: 'https://www.mi.com/service/order/sendprogress/'},
            {value: '平板', url: 'https://www.mi.com/service/order/sendprogress/'},
            {value: '穿戴', url: 'https://www.mi.com/service/order/sendprogress/'},
            {value: '耳机', url: 'https://www.mi.com/service/order/sendprogress/'},
            {value: '家电', url: 'https://www.mi.com/service/order/sendprogress/'},
            {value: '路由器', url: 'https://www.mi.com/service/order/sendprogress/'},
            {value: '音箱', url: 'https://www.mi.com/service/order/sendprogress/'},
            {value: '配件', url: 'https://www.mi.com/service/order/sendprogress/'}

          ]},
        {value: '服务中心', subLinks: [
            {value: '申请售后', url: 'https://www.mi.com/service/exchange'},
            {value: '售后政策', url: 'https://www.mi.com/service/exchange'},
            {value: '维修服务', url: 'https://www.mi.com/service/exchange'},
            {value: '订单查询', url: 'https://www.mi.com/service/'},
            {value: '以旧换新', url: 'https://www.mi.com/c/service/download/'},
            {value: '保障服务', url: 'https://www.mi.com/c/service/download/'},
            {value: '防伪查询', url: 'https://order.mi.com/service/imei'},
            {value: 'F码通道', url: 'https://www.mi.com/order/fcode'},

          ]},
        {value: '线下门店', subLinks: [
            {value: '小米之家', url: 'https://www.mi.com/c/xiaomizhijia/'},
            {value: '服务网点', url: 'https://www.mi.com/static/maintainlocation/'},
            {value: '授权体验店', url: 'https://www.mi.com/static/familyLocation/'}
          ]},
        {value: '关于小米', subLinks: [
            {value: '了解小米', url: 'https://www.mi.com/about/'},
            {value: '加入小米', url: 'https://hr.xiaomi.com/'},
            {value: '投资者关系', url: 'https://company.mi.com/zh-cn/ir/indexContent/index.html'},
            {value: '环境社会', url: 'https://company.mi.com/zh-cn/ir/indexContent/index.html'},
            {value: '廉洁举报', url: 'https://company.mi.com/zh-cn/ir/indexContent/index.html'}
          ]},
        {value: '关注我们', subLinks: [
            {value: '新浪微博', url: 'https://weibo.com/xiaomishangcheng'},
            {value: '官方微信', url: 'javascript:void(0);'},
            {value: '联系我们', url: 'https://www.mi.com/about/contact/'},
            {value: '公益基金会', url: 'https://www.mi.com/about/contact/'}
          ]},

      ]
    }
  },
}
</script>

<style lang="scss">
.site-footer{
  width: 1226px;
  margin-right: auto;
  margin-left: auto;
  margin-top: 50px;
  .site-service{
    display: flex;
    font-size: 20px;
    justify-content: space-between;
    align-content: center;
    border-bottom: 1px solid #e0e0e0;
    .service-item{
      padding-right: 40px;
      border-right: 1px solid #e0e0e0;
    }
  }
  .service-center{
    display: flex;
    justify-content: space-around;
    justify-content: center;
    text-align: center;
    margin-top: 20px;
    .site-link{
        .links{
          width: 1000px;
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); 
          grid-auto-columns: auto;
          // background-color: red;
          .link-list{
            margin-top:5px;
            .link-item{
              margin-top:5px;
            }
          }
        }
    }
    .link-contact{
        
        .phone {
          font-size: 22px;
          line-height: 1;
          color: #ff6700;
        }
        a{
          display: inline-block; /* 将链接转换为块级元素，以便设置宽度和高度 */
          width: 100px; /* 设置链接的宽度 */
          height: 50px; /* 设置链接的高度 */
          line-height: 50px; /* 行高与链接高度相等，使文本垂直居中 */
          border: 1px solid #ff6700;
          font-size: 15px;
          color: #ff6700;
          &:hover {
            color: #fff;
            background-color: #f25807;
            border-color: #f25807;
          }
        }
    }
  }
}
  // .site-footer{
  //   width: 1226px;
  //   height: auto;
  //   margin: 100px auto;
  //   .site-service{
  //     display: flex;
  //     border-bottom: 1px solid #e0e0e0;
  //     padding: 27px 0;
  //     .service-item{
  //       padding: 0;
  //       margin: 0;
  //       width: 20%;
  //       height: 25px;
  //       text-align: center;
  //       border-left: 1px solid #e0e0e0;

  //       &:first-child{
  //         border-left: none;
  //       }
  //       span{
  //         color: black;
  //       }
  //     }
  //   }
  //   .service-center{
  //     display: flex;
  //     .site-link{
  //       width: 70%;
  //       height: 112px;

  //       .links{
  //         margin-left: 20%;
  //         display: flex;
  //         justify-content: space-between;
  //         .link-container{
  //           .link-title{
  //             color: black;
  //           }
  //           .link-list{
  //             text-align: center;
  //             padding: 0;
  //             .link-item{

  //               line-height: 2;
  //               font-size: 12px;
  //               a{
  //                 color: black;
  //               }
  //             }
  //           }
  //         }
  //       }
  //     }
  //     .link-contact{
  //       width: 30%;
  //       height: 112px;
  //       margin-left: 20px;
  //       border-left: 1px solid #e0e0e0;
  //       text-align: center;
  //       color: #616161;
  //       .phone {
  //         margin: 0 0 5px;
  //         font-size: 22px;
  //         line-height: 1;
  //         color: #ff6700;
  //       }
  //       .desc {
  //         margin: 0 0 16px;
  //         font-size: 12px;
  //       }
  //       a{
  //         font-size: 12px;
  //         line-height: 28px;
  //         border: 1px solid #ff6700;
  //         color: #ff6700;
  //         &:hover {
  //           color: #fff;
  //           background-color: #f25807;
  //           border-color: #f25807;
  //         }
  //       }
  //     }
  //   }
  // }
</style>