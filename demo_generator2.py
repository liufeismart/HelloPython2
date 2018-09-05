#coding=utf-8
#__author__='liufeismart'

# generator的好处：
def generate_square1(n):
    i = 0
    while i < n:
        yield i * i
        i += 1

result = generate_square1(10)
print(result)
print(list(result))


def generate_square2(n):
    i = 0
    result = []
    while i < n:
        result.append(i * i)
        i += 1
    return result

result = generate_square2(10)
print(result)