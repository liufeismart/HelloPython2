#coding=utf-8
#__author__='liufeismart'

#缓存装饰器
def cache(function):
    cached_values = {}  # Contains already computed values
    def wrapping_function(*args):
        if args not in cached_values:
            # Call the function only if we haven't already done it for those parameters
            cached_values[args] = function(*args)
        print('not calling fibonacci(%d)' % n)
        return cached_values[args]
    return wrapping_function

@cache
def fibonacci(n):
    print('calling fibonacci(%d)' % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print([fibonacci(n) for n in range(1, 9)])


from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    print('calling fibonacci(%d)' % n)
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(1, 9)])