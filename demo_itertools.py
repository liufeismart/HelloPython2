#coding=utf-8
#__author__='liufeismart'

import itertools

#排列
print("排列\n")
from itertools import permutations
for p in permutations([1,2,3]):
    print(p)
print("\n")
#组合
print("组合\r\n")
from itertools import combinations
for c in combinations([1,2,3,4], 2):
    print(c)
print("\n")

#链表
print("链表\n")
from itertools import chain
for c in chain(range(3), range(12, 15)):
    print(c)