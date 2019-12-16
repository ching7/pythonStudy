#coding:utf-8
# 神经网络的实现过程
# 1、准备数据级，提取特征，作为输入喂给神经网络（Neural NetWork,NN）
# 2、搭建NN结构，从输入到输出（先搭建计算图，再用会话执行）
# （NN前向传播算法 ---> 计算输出）
# 3、大量特征数据喂给NN，迭代优化NN参数
# （NN反向传播算法 ---> 优化参数训练模型）
# 4、使用训练好的模型进行预测和分类

# 前3步为训练、4为使用

# 两层简单神经网络（全连接）
import tensorflow  as tf

# 定义输入和参数
# x = tf.placeholder (tf.float32,shape =(2))
x = tf.constant([[0.7,0.5]])
w1=tf.Variable(tf.random.normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random.normal([3,1],stddev=1,seed=1))

# 前向传播过程
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)
# 得出结果
print("w1: \n",w1)
print("w2: \n",w2)

print(y)
y1 = x@w1+x@w2
y2 = tf.nn.relu(y2)
print(y1)

# 反向传播过程：训练模型参数，在所有的参数上用梯度下降
# 使NN模型在训练数据上的损失函数最小

# 损失函数（loss）:预测值y和已知答案y_的差距
# 均方误差MSE (tf.reduce_mean)
y_= tf.constant([[1.2]])
loss = tf.reduce_mean(tf.square(y_-y))
print(loss)
# 反向传播训练方法：以减少loss值为优化目标（优化器）
# train_step = tf.train.function(learning_rate)
# learning_rate:学习率，每次梯度下降的幅度