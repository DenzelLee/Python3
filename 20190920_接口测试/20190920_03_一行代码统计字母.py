#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-20 and 10:46
FileName:20190920_03_一行代码统计字母.py
Description：...
第三题
尽量用一行代码统计中字符串中重复出现的字符（大小写敏感）,要求输出格式{字符：字符出现的次数}
输入：str1='AIDlkdiDKIiLLLLLdli'
输出：{'I': 2, 'D': 2, 'l': 2, 'd': 2, 'i': 3, 'L': 5}
'''

from collections import Counter
str1 = 'AIDlkdiDKIiLLLLLdli'

# 方法一：结果乱序
print(str(Counter((str1))).replace("Counter(", "").replace(")", ""))

# 方法二：结果顺序
print(dict(zip([i for i in str1], [str1.count(j) for j in str1])))


# --结果：{'L': 5, 'i': 3, 'I': 2, 'D': 2, 'l': 2, 'd': 2, 'A': 1, 'k': 1, 'K': 1}
# --结果：{'A': 1, 'I': 2, 'D': 2, 'l': 2, 'k': 1, 'd': 2, 'i': 3, 'K': 1, 'L': 5}

# --备注：想把结果字典类型做一个字母从小到大排序，但是半个小时也没搞出来，放弃了。


