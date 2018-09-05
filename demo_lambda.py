#coding=utf-8
#__author__='liufeismart'
#匿名函数
add = lambda x, y : x+y
print(add(1,2))

# 应用在函数式编程
list1 = [3, 5, -4, -1, 0, -2, -6]
print(sorted(list1, cmp = lambda x,y:cmp(x,y)))


# 应用在闭包
def get_y(a,b):
    return lambda x:a*x+b

y1 = get_y(1,10)
print(y1(3))



