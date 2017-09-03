#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student objcet(name: %s)' % self.name

    __repr__ = __str__

print(Student('Michael'))