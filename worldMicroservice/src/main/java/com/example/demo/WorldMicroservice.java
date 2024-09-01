package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WorldMicroservice {
    @GetMapping("/world")
    public String returnWorld() {
        return "World";
    }
}
