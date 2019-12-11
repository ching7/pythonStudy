import tensorflow as tf
a = tf.constant([1.0,2.0])
b = tf.constant([3.0,4.0])
result = a+b
print(result)
print(tf.__version__)
# tf.Tensor([4. 6.], shape=(2,), dtype=float32)-张量
# 输出参数：[4.6]为结果输出 ，shape(2,)为维度信息-一维数组长度2，dtype为数据类型
# 上述代码描述的就是一个计算图
# 什么是计算图（Graph）:搭建神经网络的计算过程，只搭建不运算

x = tf.constant([[1.0,2.0]])
w = tf.constant([[3.0],[4.0]])
y = tf.matmul(x,w)
print(y)
# 会话（Session）：执行计算图中的节点计算 ，例：[4.6]结果输出：为计算图的结果

# 参数：即单个神经元的线上的权重w，用变量表示，随机给初始值
wt = tf.Variable(tf.random.normal([4,5],stddev=2,mean=0,seed=1))
# random.normal:正态分布
# [2,3]：产生2x3矩阵
# stddev=2：标准差2
# mean=0: 均值为0
# seed=1：随机种子为1
print(wt)