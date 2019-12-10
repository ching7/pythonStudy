# 函数
# input-print函数
# a=input('输入值\n')
# print(a)
# 自定义函数
def  add(a,b):
    return a+b
c = add(2,3)
print(c)
# 内建函数
# abs()绝对值
print(abs(-10))

# 模块-函数的集合
import time
print(time.asctime())

# 包-多个模块放在同一个目录
from PIL import Image
#  PIL为包 Image为模块