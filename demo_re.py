#coding=utf-8
#__author__='liufeismart'

import re

# 转义
print('That is Carol\'s cat.')
# 原始字符串
print(r'That is Carol\'s cat.')

# ''' 多行字符串
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
             Sincerely,
             Bob''')


#
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())