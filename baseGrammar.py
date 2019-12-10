# 基础语法
print("hello world");
print(5+3*2)

# 占位符演示
a = 100
b= "hello"
print("%s, %s"%(a,b)) 

# 数组操作
c = [1,2,3,4,5,6,7,8]
print(c[2:])
print(c[2:3])
# print(c.insert(3,2))
# del c[4]
print(c)
print(c[3:6:1])
print(c[-3:-8:1])
# 元组-定义后无法改变
f = (1,2,3,4)
print(f)

# 字段-{key:value.key:value}
dic = {1:"123","name":"张三"}
print(dic)
print(dic["name"])
# dic["nam2","test"]
print(dic)
