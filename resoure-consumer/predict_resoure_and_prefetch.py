import requests
import json
import re
import time
import numpy as np
import tensorflow as tf

#variable 
current_cpu = 0
index = 0
i = 0
#data
index_data = [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,19.0,20.0,21.0,22.0,23.0,24.0,25.0,26.0,27.0,28.0,29.0,30.0]
cpu_data = [23239206.0,27297002.0,29957584.0,40042484.0,60113088.0,59487911.0,83481160.0,90052321.0,91185030.0,97138010.0,119667668.0,119746500.0,119345751.0,151194477.0,150143175.0,180756707.0,180153868.0,180123170.0,203999971.0,209154673.0,210121129.0,216793440.0,239968343.0,240745639.0,242904293.0,270728751.0,271993320.0,278647466.0,298509925.0,298780137.0]
for x in cpu_data:
    cpu_data[i] = x/10000000
    i=i+1

for t in range(0,100000000):
    pod_list = requests.get('http://localhost:8080/apis/metrics.k8s.io/v1beta1/pods').json().get('items')
    pods = dict()
    cpu_n = 0
    pod_n = 0
    for p in pod_list:
        pod = dict()
        container = p.get('containers')[0]

        if container.get('name') == 'resource-consumer':
            pod_n = pod_n + 1
            name = container.get('name')
            cpu = container.get('usage').get('cpu')
            cpu_n += int(re.findall('\d+', cpu)[0])

    if current_cpu != cpu_n:
        current_cpu = cpu_n
        index += 1
        index_data.append(index)
        cpu_data.append(cpu_n/10000000)
#print("({i},{c},{p})".format(i = index, c = cpu_n, p = pod_n))
		# W, b initialize
        W = tf.Variable(10.0)
        b = tf.Variable(10.0)

		# W, b update
        for i in range(100):
			# Gradient descent
            with tf.GradientTape() as tape:
                hypothesis = W * index_data + b
                cost = tf.reduce_mean(tf.square(hypothesis - cpu_data))
            learning_rate = 0.001
            W_grad, b_grad = tape.gradient(cost, [W, b])
            W.assign_sub(learning_rate * W_grad)
            b.assign_sub(learning_rate * b_grad)
			
        infer_cpu = W*(index+1) + b

        print("(index ={i},cpu_n ={c},pod ={p}-> predict: index ={i_p},cpu_n={c_p})".format(i = index, c = cpu_n/10000000,p = pod_n ,i_p = index+1, c_p = infer_cpu))

    time.sleep(1)
    


