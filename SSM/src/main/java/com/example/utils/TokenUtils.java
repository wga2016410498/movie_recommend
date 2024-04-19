package com.example.utils;

import cn.hutool.core.date.DateUtil;
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.example.pojo.User;

import java.util.Date;

//@Component
public class TokenUtils {

//    生成token
    public static String genToken(User user) {
        return JWT.create().withExpiresAt(DateUtil.offsetDay(new Date(), 1)).withAudience(user.getUserId().toString())
                .sign(Algorithm.HMAC256(user.getPassword()));
    }
//    解析token
}
