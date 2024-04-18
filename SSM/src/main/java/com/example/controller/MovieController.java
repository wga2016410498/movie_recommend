package com.example.controller;

import com.example.config.Result;
import com.example.mapper.MovieMapper;
import com.example.pojo.Movie;
import com.example.service.MovieService;
import com.github.pagehelper.Page;
import com.github.pagehelper.PageInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/movies")
public class MovieController {
    @Autowired
    MovieService movieService;

    @Autowired
    MovieMapper movieMapper;
    @GetMapping
    public Result<?> findMoviePage(@RequestParam Integer pageNum,
                                   @RequestParam Integer pageSize,
                                   @RequestParam String tag)
                                   {
        PageInfo page = movieService.findAllMovie(pageNum,pageSize,tag);
        return Result.success(page);
    }

    @GetMapping("/getbyname")
    public Result<?> findMovieByNamePage(@RequestParam Integer pageNum,
                                         @RequestParam Integer pageSize,
                                         @RequestParam String search)
    {
        PageInfo page = movieService.findAllMovieByName(pageNum,pageSize,search);
        return Result.success(page);
    }
    @GetMapping("/hotmovies")
    public Result<?> getHotMovies(){
        List<Movie> hotMovies = movieMapper.getHotMovies();
        return Result.success(hotMovies);
    }
    @GetMapping("/newmovies")
    public Result<?> getNewMovies(){
        List<Movie> newMovies = movieMapper.getNewMovies();
        return Result.success(newMovies);
    }
    @PostMapping("/getbymovielist")
    public Result<?> getMovieByMovieList(@RequestBody Map<String,List<Integer>> movieList){

        List<Integer> movielist = movieList.get("movielist");
        List<Movie> movies= movieMapper.getMovieByList(movielist);
//        System.out.println(movielist);
        return Result.success(movies);
    }
    //删除电影
    @DeleteMapping("/{id}")
    public Result<?> deleteById(@PathVariable Integer id) {
        movieMapper.deleteMoiveById(id);
        return Result.success();
    }
    //修改电影信息
    @PutMapping
    public Result<?> saveMovieInfo(@RequestBody Movie movie){
        movieMapper.updataMovieById(movie);
        return Result.success();
    }

    @PostMapping("/addmovie")
    public Result<?> addMovie(@RequestBody Movie movie){
        movieMapper.insertMovie(movie);
        return Result.success();
    }
}
