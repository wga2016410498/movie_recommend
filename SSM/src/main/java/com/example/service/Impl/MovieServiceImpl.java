package com.example.service.Impl;

import com.example.mapper.MovieMapper;
import com.example.pojo.Movie;
import com.example.service.MovieService;
import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service("movieService")
public class MovieServiceImpl implements MovieService {
    @Autowired
    MovieMapper movieMapper;

    @Override    //根据类别查询全部
    public PageInfo findAllMovie(Integer currentPage, Integer pageSize,String tag) {
        PageHelper.startPage(currentPage, pageSize);
        List<Movie> movieList = movieMapper.getAllMovies(tag);
        PageInfo pageInfo = new PageInfo(movieList);
        // 调用 Mapper 的查询方法，这里假设 MovieMapper 中有一个 selectAll 方法用于查询所有电影
        return pageInfo;
    }

    @Override
    public PageInfo findAllMovieByName(Integer currentPage, Integer pageSize, String search) {
        PageHelper.startPage(currentPage, pageSize);
        List<Movie> movieList = movieMapper.getAllMoviesByName(search);
        PageInfo pageInfo = new PageInfo(movieList);
        // 调用 Mapper 的查询方法，这里假设 MovieMapper 中有一个 selectAll 方法用于查询所有电影
        return pageInfo;
    }

}
