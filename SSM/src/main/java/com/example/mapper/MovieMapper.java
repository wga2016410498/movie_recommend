package com.example.mapper;

import com.example.pojo.Movie;
import org.apache.ibatis.annotations.Param;


import java.util.List;


public interface MovieMapper {
    //分类查询

    List<Movie> getAllMovies(@Param(value="tag")String tag);

    List<Movie> getAllMoviesByName(@Param(value= "search")String search);

    int deleteMoiveById(@Param(value= "id")Integer movieId);

    int updataMovieById(Movie movie);

    List<Movie> getMovieByList(@Param(value = "movielist") List<Integer> movieList);

    List<Movie> getHotMovies();

    List<Movie> getNewMovies();
}
