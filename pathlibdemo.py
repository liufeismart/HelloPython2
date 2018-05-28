#coding=utf-8
#__author__='liufeismart'

from pathlib import Path
import sys

tree_str = ''

def generate_tree(pathname, n=0):
    global tree_str
    print(pathname.name)
    if pathname.is_file():
        tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'
    elif pathname.is_dir():
        tree_str += '    |' * n + '-' * 4 + \
            str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)

#显示指定目录
if __name__ == '__main__':

    generate_tree(Path('/Users/wenjing/Documents/workspace/python/output.txt'))
    print(tree_str)

# Path.cwd() 当前目录
# if __name__ == '__main__':
#     generate_tree(Path.cwd())
#     print(tree_str)
# python pathlibdemo.py /Users/wenjing/Documents/book

if __name__ == '__main__':
    # 命令参数个数为2并且目录存在存在
    if len(sys.argv) == 2 and Path(sys.argv[1]).exists():
        generate_tree(Path(sys.argv[1]), 0)
    else: # 当前路径
        generate_tree(Path.cwd(), 0)
    print(tree_str)
