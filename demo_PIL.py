#coding=utf-8
#__author__='liufeismart'
#操作图像
from PIL import Image

im = Image.open('/Users/wenjing/Documents/workspace/python/Hello PyCharm/cat.jpg')
w, h = im.size
print(w,h)
im.thumbnail((w//2, h//2))
im.save('/Users/wenjing/Documents/workspace/python/Hello PyCharm/cat1.jpg', 'jpeg')