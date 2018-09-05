#coding=utf-8
#__author__='liufeismart'

import csv




#写
datas = [
         ['Bob', 14],
         ['Tom', 23],
        ['Jerry', '18'] ]
with open('temp.csv', 'w') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)

# 读
filename = '/Users/wenjing/Documents/workspace/python/Hello PyCharm/temp.csv'
with open(filename) as f:
    reader = csv.reader(f)
    print(list(reader))