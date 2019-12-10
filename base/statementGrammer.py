#coding:utf-8

# 条件语句
# input获取输入值返回的是str
# age=input("输入年龄\n")
age = 23
if int(age) > 18:
    print("你成年")
elif int(age)>20:
    print("你成年20岁")
else:
    print("你未成年")

# 循环语句
for i in range(0,5):
    print("hello")

arr = ["a","b","c","d"]
for j in arr:
    print(j)
    
x=1
y=1
while x<5 and y<5:
    x+=1
    y+=1
    print(x)
    print(y)
