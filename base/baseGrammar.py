# 基础语法
print("hello world");
print(5+3*2)

# 占位符演示
a = 100
b= "hello"
print("%s, %s"%(a,b)) 

# 数组操作-[value,value,...]
c = [1,2,3,4,5,6,7,8]
#切边
print(c[2:])
print(c[2:3])
# print(c.insert(3,2))
# del c[4]
print(c)
#步进
print(c[3:6:1])
print(c[-3:-8:1])

# 元组-定义后无法改变-(value,value,...)
f = (1,2,3,4)
print(f)

# 字典-{key:value.key:value}
dic = {1:"123","name":"张三"}
print(dic)
print(dic["name"])
#更新，新增
dic.update(b='23',asd=2)
dic.update(name='张三23')
#修改
dic[1]='2111'
#删除
del dic[1]
# dic["nam2","test"]
print(dic)

