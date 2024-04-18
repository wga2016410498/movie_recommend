package com.example.controller;


import com.example.config.Result;
import com.example.mapper.RateMapper;
import com.example.pojo.Rate;
import com.example.service.RateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class RateController {
    @Autowired
    RateMapper rateMapper;

    @Autowired
    RateService rateService;

    @PostMapping("/addmovie")
    public Result<?> addMovie(@RequestBody Rate rate) {
        System.out.println(rate);
        //如果能够查询到有关的评分，就更新。如果不能查询到，就插入。
        rateService.addRate(rate);
        return Result.success();
    }
}
