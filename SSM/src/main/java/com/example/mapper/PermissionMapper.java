package com.example.mapper;

import com.example.pojo.Permission;

import java.util.Set;

public interface PermissionMapper {
    Set<Permission> SelectPermissionByRole(int role);
}
