package com.example.service.Impl;

import com.example.mapper.UserMapper;
import com.example.pojo.Authentication;
import com.example.pojo.User;
import com.example.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service("userService")
public class UserServiceImpl implements UserService {
    @Autowired
    private UserMapper userMapper;
    @Override
    public List<User> SelectAllUsers() {
        return userMapper.SelectAllUsers();
    }

}
