package com.example.pojo;

import java.util.Date;

public class Movie {
    private Integer movieId;
    private String name;
    private String url;
    private String tag;
    private Double rate;
    private String describe;
    private String duration;
    private String language;
    private String director;
    private String actor;
    private String location;
    private String releaseTime;

    private String outUrl;

    public String getOutUrl() {
        return outUrl;
    }

    public void setOutUrl(String outUrl) {
        this.outUrl = outUrl;
    }

    public Integer getMovieId() {
        return movieId;
    }

    public void setMovieId(Integer movieId) {
        this.movieId = movieId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public Double getRate() {
        return rate;
    }

    public void setRate(Double rate) {
        this.rate = rate;
    }

    public String getDescribe() {
        return describe;
    }

    public void setDescribe(String describe) {
        this.describe = describe;
    }

    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public String getActor() {
        return actor;
    }

    public void setActor(String actor) {
        this.actor = actor;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getReleaseTime() {
        return releaseTime;
    }

    public void setReleaseTime(String release_time) {
        this.releaseTime = release_time;
    }

    @Override
    public String toString() {
        return "Movie{" +
                "movieId=" + movieId +
                ", name='" + name + '\'' +
                ", url='" + url + '\'' +
                ", tag='" + tag + '\'' +
                ", rate=" + rate +
                ", describe='" + describe + '\'' +
                ", duration='" + duration + '\'' +
                ", language='" + language + '\'' +
                ", director='" + director + '\'' +
                ", actor='" + actor + '\'' +
                ", location='" + location + '\'' +
                ", releaseTime='" + releaseTime + '\'' +
                ", outUrl='" + outUrl + '\'' +
                '}';
    }
}
//package com.example.pojo;
//
//        import java.util.Date;
//
//public class Movie {
//    private Integer movieId;
//    private String name;
//    private String url;
//    private Date year;
//    private String tag;
//    private String describe;
//
//    public Integer getMovieId() {
//        return movieId;
//    }
//
//    public void setMovieId(Integer movieId) {
//        this.movieId = movieId;
//    }
//
//    public String getName() {
//        return name;
//    }
//
//    public void setName(String name) {
//        this.name = name;
//    }
//
//    public String getUrl() {
//        return url;
//    }
//
//    public void setUrl(String url) {
//        this.url = url;
//    }
//
//    public Date getYear() {
//        return year;
//    }
//
//    public void setYear(Date year) {
//        this.year = year;
//    }
//
//    public String getTag() {
//        return tag;
//    }
//
//    public void setTag(String tag) {
//        this.tag = tag;
//    }
//
//    public String getDescribe() {
//        return describe;
//    }
//
//    public void setDescribe(String describe) {
//        this.describe = describe;
//    }
//
//    @Override
//    public String toString() {
//        return "Movie{" +
//                "movieId=" + movieId +
//                ", name='" + name + '\'' +
//                ", url='" + url + '\'' +
//                ", year=" + year +
//                ", tag='" + tag + '\'' +
//                ", describe='" + describe + '\'' +
//                '}';
//    }
//}