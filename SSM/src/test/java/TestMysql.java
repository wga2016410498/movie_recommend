import com.example.mapper.MovieMapper;
import com.example.mapper.PermissionMapper;
import com.example.mapper.ProductMapper;
import com.example.mapper.UserMapper;
import com.example.pojo.*;
import com.example.service.Impl.MovieServiceImpl;
import com.github.pagehelper.Page;
import com.github.pagehelper.PageInfo;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class TestMysql {


    @Test
    public void testMapper(){
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
        MovieMapper movieMapper = applicationContext.getBean("movieMapper", MovieMapper.class);
        List<Integer> arr = new ArrayList<>();
        arr.add(1);
        arr.add(2);
        List<Movie> allMovie = movieMapper.getNewMovies();
        System.out.println(allMovie.size());
        for (Movie movie : allMovie){
            System.out.println(movie);
        }
    }
}
//        Set<Permission> permissionSet = permissionMapper.SelectPermissionByRole(1);
//        for(Permission permission : permissionSet){
//            System.out.println(permission);
//        }
//        UserServiceImpl userServiceimpl= applicationContext.getBean("userService", UserServiceImpl.class);
//        UserServiceImpl userService = applicationContext.getBean("userService",UserServiceImpl.class);
//        userService.UserLogin("wangguangan");
//        List<User> userList = userMapper.SelectAllUsers();
//        for (User user : userList) {
//            System.out.println(user);
//        }
//        Authentication authentication = userMapper.UserLogin("wangguangan","111111");
//        System.out.println(authentication);
//        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("spring.xml");
//        ProductMapper productMapper = applicationContext.getBean("productMapper", ProductMapper.class);
//        List<Product> productList = productMapper.getAllProduct();
//        for (Product product : productList) {
//            System.out.println(product);
//        }