#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 22:05:51 2017

@author: pydemia
"""


import numpy as np
import tensorflow as tf
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import unipy.dataset.api as dm

# %% Load a Dataset

dm.init()

data = dm.load('winequality_red')
data


# %% Scatter plot (Quality & for each)
for _ in data.columns[2:-1]:
    x = data[_]
    y = data['quality']
    plt.scatter(x, y)
    plt.xlabel(_)
    plt.ylabel('quality')
    plt.show()


# %% Correlation
data.corr()


# %% Scatter plot (within X)

x = data['fixed_acidity']
y = data['citric_acid']
plt.scatter(x, y)
plt.xlabel('fixed_acidity')
plt.ylabel('citric_acid')
plt.show()


x = data['volatile_acidity']
y = data['citric_acid']
plt.scatter(x, y)
plt.xlabel('volatile_acidity')
plt.ylabel('citric_acid')
plt.show()

x = data['pH']
y = data['citric_acid']
plt.scatter(x, y)
plt.xlabel('pH')
plt.ylabel('citric_acid')
plt.show()


# %% Linear Regression with `statsmodel`
rowFlag = int(data.shape[0] * 7 /10)
colFlag = int(data.shape[1])
trainSet = data.iloc[:rowFlag, :]
testSet  = data.iloc[rowFlag:, :]

trainX0 = trainSet[['fixed_acidity']].values
trainX1 = trainSet[['fixed_acidity', 'volatile_acidity']].values
trainX2 = trainSet[['fixed_acidity', 'volatile_acidity', 'pH']].values

trainY = trainSet[['citric_acid']].values
testY  = testSet[['citric_acid']].values

ols_trainX1 = trainX1.copy()
ols_trainX1 = sm.add_constant(ols_trainX1)

est = sm.OLS(trainY, ols_trainX1).fit()
est.summary()


# %% 3D Plot

x0 = ols_trainX1.T[0]
x1 = ols_trainX1.T[1]

Z = est.params[0] + est.params[1] * x0 + est.params[2] * x1

fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig, azim=-115, elev=15)
#ax = fig.add_subplot(111, projection='3d')

x0 = ols_trainX1.T[0]
x1 = ols_trainX1.T[1]
xx0, xx1 = np.meshgrid(np.linspace(x0.min(), x0.max(), len(x0)), 
                       np.linspace(x1.min(), x1.max(), len(x1)))

Z0 = est.params[0] + est.params[1] * xx0 + est.params[2] * xx1
Z1 = est.params[0] + est.params[1] * x0 + est.params[2] * x1
surf = ax.plot_surface(xx0, xx1, Z1, cmap=plt.cm.RdBu_r, alpha=.1, linewidth=0)

resid = trainY.T[0] - est.predict(ols_trainX1)
ax.scatter(x0[resid >= 0], x1[resid >= 0], trainY[resid >= 0], color='black', alpha=1.0, facecolor='white')
ax.scatter(x0[resid < 0], x1[resid < 0], trainY[resid < 0], color='black', alpha=1.0)
ax.plot(x0, x1, Z1, color='blue', label='parametric curve')

plt.show()


# %% tensorflow

learning_rate = .01
training_epochs = 10000  #
display_step = 100

rowFlag = int(data.shape[0] * 7 /10)
colFlag = int(data.shape[1])
trainSet = data.iloc[:rowFlag, :]
testSet  = data.iloc[rowFlag:, :]

trainX0 = trainSet[['fixed_acidity']].values
trainX1 = trainSet[['fixed_acidity', 'volatile_acidity']].values
trainX2 = trainSet[['fixed_acidity', 'volatile_acidity', 'pH']].values

trainY = trainSet[['citric_acid']].values
testY  = testSet[['citric_acid']].values

nDim0 = trainX0.shape[1]
nDim1 = trainX1.shape[1]
nDim2 = trainX2.shape[1]

print(trainX0.shape)
print(trainX1.shape)
print(trainX2.shape)
print(trainY.shape)


# Using `ndarray`, calculated by `tensorflow`

# Variables
trainX0
trainY

W0 = tf.Variable(tf.random_uniform([1], -1, 1), name='weight')
b0 = tf.Variable(tf.random_uniform([1], -1, 1), name='bias')


y_0 = trainX0 * W0 + b0
costFunc = tf.reduce_mean(tf.square(y_0 - trainY))  # Mean Squared Error

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
model0 = optimizer.minimize(costFunc)

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
with tf.Session(config=config) as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(training_epochs):
        
        sess.run(model0)

        if step % display_step == 0:
            print(step, sess.run(W0), sess.run(b0))


# %% `tf.placeholder`

# Variables
trainX0
trainY

X0 = tf.placeholder(tf.float32, [None, nDim0])
Y_train = tf.placeholder(tf.float32, [None, 1])

W0 = tf.Variable(tf.random_uniform([nDim0, 1], -1, 1), name='weight')
b0 = tf.Variable(tf.random_uniform([1], -1, 1), name='bias')

y_pred = tf.add(tf.matmul(X0, W0), b0)

costFunc = tf.reduce_mean(tf.square(Y_train - y_pred))  # Mean Squared Error
Y_mean = tf.reduce_mean(Y_train)
rsquareFunc = 1 - (tf.reduce_sum(tf.square(Y_train - y_pred)) /
                   tf.reduce_sum(tf.square(Y_train - Y_mean)))
#rsquareFunc = tf.reduce_sum(tf.square(y_pred - Y_mean)) / tf.reduce_sum(tf.square(y_train - Y_mean))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
model0 = optimizer.minimize(costFunc)


config = tf.ConfigProto()
config.gpu_options.allow_growth = True
with tf.Session(config=config) as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(training_epochs):
        
        feedDict = feedDict = {X0: trainX0, Y_train: trainY}
        sess.run(model0, feed_dict=feedDict)

        if step % display_step == 0:
            print(step, sess.run(W0), sess.run(b0))


config = tf.ConfigProto()
config.gpu_options.allow_growth = True
with tf.Session(config=config) as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(training_epochs):
        
        feedDict = feedDict = {X0: trainX0, Y_train: trainY}
        #sess.run(model0, feed_dict=feedDict)
        model0.run(feedDict)

        if step % display_step == 0:
            cost_step = costFunc.eval(feedDict)
            rsquare = rsquareFunc.eval(feedDict)
            msg0 = 'STEP: {:>3}, MSE: {:02.4f}, R2: {:02.4f}'.format(step, cost_step, rsquare)
            msg1 = 'Weights: {}, Bias: {}'.format(sess.run(W0).reshape((1,1)), sess.run(b0))
            print(msg0)
            print(msg1)
            
            plt.plot(trainX0, trainY, 'o', label='STEP: {step}'.format(step=step))
            plt.plot(trainX0, sess.run(W0) * trainX0 + sess.run(b0))
            plt.show()

# %% `tf.placeholder`, 2 columns

# Variables
X1 = tf.placeholder(tf.float32, [None, nDim1])
Y_train = tf.placeholder(tf.float32, [None, 1])

W1 = tf.Variable(tf.random_normal([nDim1, 1]), name='weight')
b1 = tf.Variable(tf.random_normal([1]), name='bias')


y_pred = tf.add(tf.matmul(X1, W1), b1)

costFunc = tf.reduce_mean(tf.square(Y_train - y_pred))  # Mean Squared Error
Y_mean = tf.reduce_mean(Y_train)
rsquareFunc = 1 - (tf.reduce_sum(tf.square(Y_train - y_pred)) / tf.reduce_sum(tf.square(Y_train - Y_mean)))
#rsquareFunc = tf.reduce_sum(tf.square(y_pred - Y_mean)) / tf.reduce_sum(tf.square(y_train - Y_mean))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
model1 = optimizer.minimize(costFunc)



config = tf.ConfigProto()
config.gpu_options.allow_growth = True
with tf.Session(config=config) as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(training_epochs):
        
        feedDict = feedDict = {X1: trainX1, Y_train: trainY}
        #sess.run(model1, feed_dict=feedDict)
        model1.run(feedDict)

        if step % display_step == 0:
            cost_step = costFunc.eval(feedDict)
            rsquare = rsquareFunc.eval(feedDict)
            msg0 = 'STEP: {:>3}, MSE: {:02.4f}, R2: {:02.4f}'.format(step, cost_step, rsquare)
            msg1 = 'Weights: {}, Bias: {}'.format(sess.run(W1).reshape((1,nDim1)), sess.run(b1))
            print(msg0)
            print(msg1)
            
            fig = plt.figure(figsize=(12, 8))
            #ax = fig.add_subplot(111, projection='3d')
            ax = Axes3D(fig, azim=-115, elev=15)
            Z1 = trainX1 @ sess.run(W1) + sess.run(b1)
            
            ax.scatter(trainX1.T[0], trainX1.T[1], trainY)
            ax.scatter(trainX1.T[0], trainX1.T[1], Z1.T[0], color='black')
            ax.plot(trainX1.T[0], trainX1.T[1], Z1.T[0], color='red', alpha=.4)
            plt.show()
            #print(trainX1 @ sess.run(W1) + sess.run(b1))
            #plt.plot(trainX1[0], trainX1[1], trainY, c='r', marker='o', label='STEP: {step}'.format(step=step))
            #plt.plot(trainX1, trainX1 @sess.run(W1) + sess.run(b1))
            #plt.show()


fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig, azim=-115, elev=15)

ax.scatter(trainX1.T[0], trainX1.T[1], trainY)
plt.show()

# %% `tf.placeholder, 3 columns

# Variables
X2 = tf.placeholder(tf.float32, [None, nDim2])
Y_train = tf.placeholder(tf.float32, [None, 1])

W2 = tf.Variable(tf.random_normal([nDim2, 1]), name='weight')
b2 = tf.Variable(tf.random_normal([1]), name='bias')


y_pred_2 = tf.add(tf.matmul(X2, W2), b2)

costFunc = tf.reduce_mean(tf.square(Y_train - y_pred_2))  # Mean Squared Error
Y_mean = tf.reduce_mean(Y_train)
rsquareFunc = 1 - (tf.reduce_sum(tf.square(Y_train - y_pred_2)) / tf.reduce_sum(tf.square(Y_train - Y_mean)))
#rsquareFunc = tf.reduce_sum(tf.square(y_pred - Y_mean)) / tf.reduce_sum(tf.square(y_train - Y_mean))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
model2 = optimizer.minimize(costFunc)


config = tf.ConfigProto()
config.gpu_options.allow_growth = True
with tf.Session(config=config) as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(training_epochs):
        
        feedDict = feedDict = {X2: trainX2, Y_train: trainY}
        #sess.run(model1, feed_dict=feedDict)
        model2.run(feedDict)

        if step % display_step == 0:
            cost_step = costFunc.eval(feedDict)
            rsquare = rsquareFunc.eval(feedDict)
            msg0 = 'STEP: {:>3}, MSE: {:02.4f}, R2: {:02.4f}'.format(step, cost_step, rsquare)
            msg1 = 'Weights: {}, Bias: {}'.format(sess.run(W2).reshape((1,nDim2)), sess.run(b2))
            print(msg0)
            print(msg1)

