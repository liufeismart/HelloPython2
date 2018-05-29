#coding=utf-8
#__author__='liufeismart'
#操作图像
from PIL import Image

im = Image.open('cat.jpg')
w, h = im.size
print(w,h)
im.thumbnail((w//2, h//2))
im.save('cat1.jpg', 'jpeg')