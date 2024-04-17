// 请求接口来访问后端的数据。
// 因为如果不封装的话，每次请求都要书写请求代码，造成代码冗余。
import axios from 'axios'
const request = axios.create({
    baseURL:'http://localhost:8081/shore'
})

export default request