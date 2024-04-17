package com.example.pojo;

import java.util.Date;
import java.util.Set;

public class Authentication {



    private Integer userId;
    private String userName;
    private String password;
    private String email;
    private Date createdAt;
    private Integer role;

    private Set<Permission> permissions;
    private String token;//token

    public String getToken() {
        return token;
    }
    public Integer getUserId() {
        return userId;
    }

    public Integer getRole(){return role;}

    public void setRole(int role){
        this.role = role;
    }
    public void setUserId(Integer userId) {
        this.userId = userId;
    }
    public void setToken(String token) {
        this.token = token;
    }
    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Date createdAt) {
        this.createdAt = createdAt;
    }

    public Set<Permission> getPermissions() {
        return permissions;
    }

    public void setPermissionSet(Set<Permission> permissions) {
        this.permissions = permissions;
    }

    @Override
    public String toString() {
        return "Authentication{" +
                "userId=" + userId +
                ", userName='" + userName + '\'' +
                ", password='" + password + '\'' +
                ", email='" + email + '\'' +
                ", createdAt=" + createdAt +
                ", role=" + role +
                ", permissionSet=" + permissions +
                ", token='" + token + '\'' +
                '}';
    }
}
