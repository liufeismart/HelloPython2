#coding=utf-8
#__author__='liufeismart'
import collections

print("Counter\n")
from collections import Counter
a = Counter('blue')
b = Counter('yellow')

print(a)
print(b)
print((a+b).most_common(3))

print("\n")


print("defaultdict\n")
from collections import defaultdict
import json
def tree():
    """
    Factory that creates a defaultdict that also uses this factory
    :return:
    """
    return defaultdict(tree)

root = tree()
root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None

print(json.dumps(root, indent=4))
