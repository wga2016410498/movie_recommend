package com.example.service.Impl;

import com.example.mapper.RateMapper;
import com.example.pojo.Rate;
import com.example.service.RateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class RateServiceImpl implements RateService {
    @Autowired
    RateMapper rateMapper;
    @Override
    public void addRate(Rate rate) {
        //1.如果查询的不为空，就更新
        Rate ratetmp = rateMapper.selectRateById(rate.getUserId(), rate.getMovieId());
        if(ratetmp!=null){
            System.out.println("111");
            rateMapper.updateRate(rate);
        }else{
           rateMapper.insertRate(rate); //2.如果查询的为空，就插入
        }
    }
}
