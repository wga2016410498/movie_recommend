// import router from "@/router";

// export function activeRouter(){
//     const userStr = sessionStorage.getItem("user")
//     if(userStr){
//         const user = JSON.parse(userStr)
//         user.permissions.forEach(p => {
//             let obj = {
//                 path: p.path,
//                 name: p.name,
//                 component: () => import("@/views/"+p.name)
//             };
//             router.addRoute(obj);
//         })
//     }
// }