#coding=utf-8
#__author__='liufeismart'

def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield  n

    n += 1
    print('This is printed thrid')
    yield n


# for item in my_gen():
#     print(item)

# print(my_gen().next())
# print(my_gen().next())
# print(my_gen().next())


a = (x * x for x in range(100))

# print(a.next())
# print(a.next())
# print(a.next())
# print(a.next())
# print(a.next())
# print(a.next())


def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
            yield my_str[i]

print(rev_str("hello").next())
print(rev_str("hello").next())
print(rev_str("hello").next())

for char in rev_str("hello python"):
    print(char)