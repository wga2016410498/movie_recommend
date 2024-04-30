import { createRouter, createWebHistory } from 'vue-router'
import Manage from '@/views/Manage.vue'
const routes = [
  {
    path:'/',
    name:'Home',
    component:() => import('../views/Home'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path:'/movieinfo',
    name:'MovieInfo',
    component: () => import('../views/MovieInfo'),
    props:true //将路由参数作为组件的props传递
  },
  //想要在导航栏当中显示路由，需要把要访问的路由添加在子路由下面。
  // {
  //   path:'/manage',
  //   name:'manage',
  //   component:() => import('../views/Manage'),
  //   children:[{
  //     path:'/managemovie',
  //     name:'ManageMovie',
  //     component:()=>import('../views/ManageMovies')
  //   }]
  // },
  // {
  //   path:'/person',
  //   name:'Person',
  //   component:() => import('../views/Person')
  // },
  // {
  //   path:'/password',
  //   name:'Password',
  //   component:() => import('../views/Password')
  // },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// 在刷新页面的时候重置当前路由
activeRouter()

// 动态生成路由
export function activeRouter(){
  const userStr = sessionStorage.getItem("user")
  if(userStr){
      const user = JSON.parse(userStr)
      //如果身份是管理员，就把管理员能访问的路由添加在管理的路径下
      if(user.role===1){
        let root={
          path:'/manage',
          name:'Manage',
          component:Manage,
          children:[]
        }
        user.permissions.forEach(p => {
          let obj = {
              path: p.path,
              name: p.name,
              component: () => import("@/views/" + p.name)
          };
          if(p.path!=='/manage'){
            root.children.push(obj)
          }
        })
        if (router) {
            router.addRoute(root)
        }
      }
      //如果是普通用户，就把普通用户能访问的路由添加在
      else{
          user.permissions.forEach(p => {
            let obj = {
                path: p.path,
                name: p.name,
                component: () => import("@/views/"+p.name)
            };
            router.addRoute(obj);
        })
      }
      
  }
}

// 路由前置守卫
router.beforeEach((to,from,next)=>{
  if(to.path === '/login' || to.path === '/register'||to.path === '/'||to.path==='/movieinfo'){
    next()
    return
  }
  let user = sessionStorage.getItem("user")? JSON.parse(sessionStorage.getItem("user")) : {}
  if(!user.permissions || !user.permissions.length){
    next('/login')
  }else if(!user.permissions.find(p=> p.path === to.path)){
    next('/login')
  }else{
    next()
  }
})
export default router

