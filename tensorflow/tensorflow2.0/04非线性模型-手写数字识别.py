import os
import tensorflow as tf # 导入TF 库
from tensorflow import keras # 导入TF 子库keras
from tensorflow.keras import layers, optimizers, datasets # 导入TF 子库等

# 0、手写图片数据集
(x, y), (x_val, y_val) = datasets.mnist.load_data() # 加载MNIST 数据集
x = 2*tf.convert_to_tensor(x, dtype=tf.float32)/255.-1 # 转换为浮点张量，并缩放到-1~1
y = tf.convert_to_tensor(y, dtype=tf.int32) # 转换为整形张量
y = tf.one_hot(y, depth=10) # one-hot 编码
print(x.shape, y.shape)
train_dataset = tf.data.Dataset.from_tensor_slices((x, y)) # 构建数据集对象
train_dataset = train_dataset.batch(512) # 批量训练

# 1、搭建3层非线性神经网络
# 创建一层网络，设置输出节点数为256，激活函数类型为ReLU
layers.Dense(256, activation='relu')
# 利用Sequential 容器封装3 个网络层，前网络层的输出默认作为下一层的输入
model = keras.Sequential([ # 3 个非线性层的嵌套模型
layers.Dense(256, activation='relu'), # 隐藏层1
layers.Dense(128, activation='relu'), # 隐藏层2
layers.Dense(10)]) # 输出层，输出节点数为10
optimizer = optimizers.SGD(learning_rate=0.001)

# 2、训练过程
def train_epoch(epoch):
    # Step4.loop
    for step, (x, y) in enumerate(train_dataset):
        with tf.GradientTape() as tape:
            # [b, 28, 28] => [b, 784]
            x = tf.reshape(x, (-1, 28*28))
            # Step1. compute output
            # [b, 784] => [b, 10]
            out = model(x)
            # Step2. compute loss
            loss = tf.reduce_sum(tf.square(out - y)) / x.shape[0]

        # Step3. optimize and update w1, w2, w3, b1, b2, b3
        grads = tape.gradient(loss, model.trainable_variables)
        # w' = w - lr * grad
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

        if step % 100 == 0:
            print(epoch, step, 'loss:', loss.numpy())
# 3、训练模型
def train():

    for epoch in range(30):

        train_epoch(epoch)

if __name__ == '__main__':
    train()