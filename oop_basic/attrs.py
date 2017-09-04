#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print('hasattr(obj,\'x\') =', hasattr(obj, 'x'))  # 有属性'X'吗？
print('hasattr(obj,\'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'


