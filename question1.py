#coding=utf-8
#__author__='liufeismart'
#1.默认参数与函数
def func(var1, var2=[]):
    var2.append(var1)
    return var2
func(1)
func(2)
func(3)
func(1,[4])

#2.类 与 变量
class URLCatcher(object):
    urls = []

    def add_url(self, url):
        self.urls.append(url)

a = URLCatcher()
a.add_url('http://www.google.com')
b = URLCatcher()
b.add_url('http://www.sina.com')
a
b

class URLCatcher2(object):
    def __init__(self):
        self.urls = []
    def add_url(self, url):
        self.urls.append(url)

a = URLCatcher2()
a.add_url('http://www.google.com')
b = URLCatcher2()
b.add_url('http://www.sina.com')
a
b


#3.可变的分配
a = ['one', 'two', 'three']
b = a
a[0] = 'ONE'
b
