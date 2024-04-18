package com.example.pojo;

import java.util.Date;

public class Rate {
    Integer userId;
    Integer movieId;
    Integer rate;
    String rateTime;

    public Integer getUserId() {
        return userId;
    }

    public void setUserId(Integer userId) {
        this.userId = userId;
    }

    public Integer getMovieId() {
        return movieId;
    }

    public void setMovieId(Integer movieId) {
        this.movieId = movieId;
    }

    public Integer getRate() {
        return rate;
    }

    public void setRate(Integer rate) {
        this.rate = rate;
    }

    public String getRateTime() {
        return rateTime;
    }

    public void setRateTime(String rateTime) {
        this.rateTime = rateTime;
    }

    @Override
    public String toString() {
        return "Rate{" +
                "userId=" + userId +
                ", movieId=" + movieId +
                ", rate=" + rate +
                ", rateTime='" + rateTime + '\'' +
                '}';
    }
}
