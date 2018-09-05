#coding=utf-8
#__author__='liufeismart'
import pip
import pip._internal
import sys

# args = ["pip","setuptools", "wheel", "install", "--upgrade", "--force-reinstall"]
# pip._internal.main(args)

from pip._internal import main
main(['install']+ ['matplotlib'])



for y in range(15,-15,-1):
    for x in range(-30, 30):
        str = ''.join('AndyLove'[(x-y)%8])
        if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0:
            str = ''.join('AndyLove'[(x - y) % 8])