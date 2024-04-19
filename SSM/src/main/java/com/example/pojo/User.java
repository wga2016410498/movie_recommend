package com.example.pojo;

import java.util.Date;
import java.util.Set;

public class User {

    private Integer userId;
    private String userName;
    private String password;
    private String email;
    private Date createdAt;
    private Integer role;

    private Set<Permission> permissions;
    private String token;//token

    private String gender;
    private Integer age;
    private String occupation;
    private String zipCode;

    public void setRole(Integer role) {
        this.role = role;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public String getOccupation() {
        return occupation;
    }

    public void setOccupation(String occupation) {
        this.occupation = occupation;
    }

    public String getZipCode() {
        return zipCode;
    }

    public void setZipCode(String zipCode) {
        this.zipCode = zipCode;
    }

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
        return "User{" +
                "userId=" + userId +
                ", userName='" + userName + '\'' +
                ", password='" + password + '\'' +
                ", email='" + email + '\'' +
                ", createdAt=" + createdAt +
                ", role=" + role +
                ", permissions=" + permissions +
                ", token='" + token + '\'' +
                ", gender='" + gender + '\'' +
                ", age=" + age +
                ", occupation='" + occupation + '\'' +
                ", zipCode='" + zipCode + '\'' +
                '}';
    }
}
