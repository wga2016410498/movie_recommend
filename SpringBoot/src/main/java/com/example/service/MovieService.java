package com.example.service;

import com.github.pagehelper.Page;
import com.github.pagehelper.PageInfo;

public interface MovieService {
    PageInfo findAllMovie(Integer currentPage, Integer pageSize,String tag);

    PageInfo findAllMovieByName(Integer currentPage, Integer pageSize,String search);
}
