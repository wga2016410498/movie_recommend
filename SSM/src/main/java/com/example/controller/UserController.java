package com.example.controller;

import com.example.config.Result;
import com.example.mapper.PermissionMapper;
import com.example.mapper.UserMapper;
import com.example.pojo.Authentication;
import com.example.pojo.Permission;
import com.example.pojo.User;
import com.example.service.UserService;
import com.example.utils.TokenUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Set;

@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @Autowired
    private UserMapper userMapper;

    @Autowired
    private PermissionMapper permissionMapper;
    @RequestMapping("/all")
    public List<User> getAllUsers() {
        List<User> userList = userService.SelectAllUsers();
        System.out.println(userList.isEmpty());
        userList.forEach(user -> System.out.println(user));
        return userList;
    }
    //在用户登陆的过程中，如果发现用户是管理员，就让他进入的时候显示管理界面。如果是普通用户的话就显示主页。而且二者能访问的界面不同。
    @RequestMapping("/login")
    public Result<?> Login(@RequestBody Authentication userParam){
        Authentication authentication = userMapper.UserLogin(userParam.getUserName());
        if(authentication!=null){
            if(authentication.getPassword().equals(userParam.getPassword())){
                String token = TokenUtils.genToken(authentication);
                System.out.println(token);
                authentication.setToken(token);
                Set<Permission> permissions = permissionMapper.SelectPermissionByRole(authentication.getRole());
                authentication.setPermissionSet(permissions);
                return Result.success(authentication);
            }else{
                return Result.error("-1", "密码错误");//0代表账号有，密码无
            }
        }else{
            return Result.error("-1", "用户名错误");
        }
    }

    //注册
    @RequestMapping("/register")
    public Result<?> Register(@RequestBody Authentication userParam){
        Authentication authentication = userMapper.UserLogin(userParam.getUserName());
        if(authentication!=null){
            return Result.error("-1","用户名已被注册");
        }
        else
        {
            int count = userMapper.UserRegister(userParam.getUserName(), userParam.getPassword());
            if (count == 0) return Result.error("-1", "注册失败");
            return Result.success();
        }
    }

    //修改个人信息

}
