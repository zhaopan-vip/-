#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@auth: zhaopan
@time: 2020/8/12 17:33
@desc: str 字符串
"""


# https://docs.python.org/3.6/tutorial/introduction.html#strings
# 字符串属于不可变变量(immutable)
s = 'abcdefg'
# 切片操作
s = s[:]            # 拷贝
s = s[::-1]         # 反转
print('line1\n2')   # 转义字符
print(r'line1\n2')  # raw strings
# 多行字符
"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""
print(len(s))       # 取长度
s += 'hijk'         # 支持加号运算符

# Text Sequence Type - str
# https://docs.python.org/3.6/library/stdtypes.html#textseq
b = b'1234567890'       # class bytes
s = str(b)              # class str, but not real string, print "b'1234567890'"
p = str(b, 'utf-8')     # class str, real string, print "1234567890"
q = b.decode()          # class bytes => class str, print "1234567890"
# str(bytes, encoding, errors) is equivalent to bytes.decode(encoding, errors)
assert p == q
