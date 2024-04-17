package com.example.mapper;

import com.example.pojo.Authentication;
import com.example.pojo.User;
import org.apache.ibatis.annotations.Param;


import javax.lang.model.element.NestingKind;
import java.util.List;


public interface UserMapper {
    List<User> SelectAllUsers();

    Authentication UserLogin(@Param(value="username")String username);

    int UserRegister(@Param(value="username")String username,@Param(value="password")String password);
}
