import tensorflow as tf
print(tf.__version__)
# 创建4 个张量，并赋值
a = tf.constant(1.)
b = tf.constant(2.)
c = tf.constant(3.)
w = tf.constant(4.)

with tf.GradientTape() as  tape:# 构建梯度环境
    tape.watch([w])# 将w 加入梯度跟踪列表
    # 构建计算过程，函数表达式
    y =  a*w**2 + b*w + c
# 自动求导
[dy_dw] = tape.gradient(y,[w])
print(dy_dw)