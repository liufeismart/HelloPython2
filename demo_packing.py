#coding=utf-8
#__author__='liufeismart'
def repeat(count, name):
    for i in range(count):
        print(name)

print("Call function repeat using a list of arguments:")
args = [4, "cats"]
repeat(*args)

print("Call function repeat using a dictionary of keyword arguments:")
args2 = {'count': 4, 'name': 'cats'}
repeat(**args2)


def f(*args, **kwargs):
    print("Arguments: ", args)
    print("Keyword arguments: ", kwargs)

f(3, 4, 9, 12, 16,foo=42, bar=7)
