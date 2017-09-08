#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

d = dict(name='Bob', age=20, score=88)
print(d)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)

