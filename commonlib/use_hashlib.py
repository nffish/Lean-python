#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

sha3 = hashlib.sha3_512()
sha3.update('how to use sha3 in python hashlib?'.encode('utf-8'))
print(sha3.hexdigest())


# 原味MD5
def get_md5(str):
    md = hashlib.md5()
    md.update(str.encode('utf-8'))
    return md.hexdigest()


# 加盐
def calc_md5(password):
    return get_md5(password + 'the-Salt')


def calc_md5(username, password):
    return get_md5(username + password + 'the-Salt')


username = 'name'
password = '123456'
print(get_md5('123456'))
print(calc_md5(username, password))
