package com.example.utils;

import cn.hutool.core.date.DateUtil;
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.example.pojo.Authentication;
import org.springframework.stereotype.Component;
import java.util.Date;

//@Component
public class TokenUtils {

//    生成token
    public static String genToken(Authentication authentication) {
        return JWT.create().withExpiresAt(DateUtil.offsetDay(new Date(), 1)).withAudience(authentication.getUserId().toString())
                .sign(Algorithm.HMAC256(authentication.getPassword()));
    }
//    解析token
}
