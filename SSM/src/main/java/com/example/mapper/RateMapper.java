package com.example.mapper;

import com.example.pojo.Rate;
import org.apache.ibatis.annotations.Param;

public interface RateMapper {
    Rate selectRateById(@Param("userId") Integer userId,@Param("movieId") Integer movieId);
    int insertRate(Rate rate);
    int updateRate(Rate rate);
}
