#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    animal.run()


dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

run_twice(dog)
run_twice(Tortoise())
