package com.example.mapper;

import com.example.pojo.User;
import org.apache.ibatis.annotations.Param;


import java.util.List;


public interface UserMapper {
    List<User> SelectAllUsers();

    User UserLogin(@Param(value="username")String username);

    int UserRegister(@Param(value="username")String username,@Param(value="password")String password);

    int updataUserInfo(User user);
}
