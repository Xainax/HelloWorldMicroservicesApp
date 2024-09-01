package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloMicroservice {
    @GetMapping("/hello")
    public String returnHello() {
        return "Hello";
    }
}
