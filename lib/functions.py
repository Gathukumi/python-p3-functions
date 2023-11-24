#!/usr/bin/env python3

def greet_programmer(name = "Hello, programmer!"):
    print(f"{name}")

def greet(name="david"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("Denis");

greet_with_default()

def add(num1, num2):
    return num1 + num2

result = add(5, 7)
print(result)

def halve(number):
    return number / 2

result = halve(20)
print(result)
