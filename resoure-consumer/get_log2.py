import requests
import json
import re
import time
import csv
import os

#variable
current_cpu = 0
index = 0


#write index cpu_n to file
def write_csv(index, cpu):
    with open('output.csv', 'a') as outfile:
        writer = csv.writer(outfile)
        data = list()
        data.append(index)
        data.append(cpu)
        writer.writerow(data)


#remove file if exist
file = './output.csv'
if os.path.isfile(file):
    os.remove(file)


for t in range(0,100000):
    pod_list = requests.get('http://localhost:8080/apis/metrics.k8s.io/v1beta1/pods').json().get('items')
    pods = dict()
    cpu_n = 0
    for p in pod_list:
        pod = dict()
        container = p.get('containers')[0]

        if container.get('name') == 'resource-consumer':
            name = container.get('name')
            cpu = container.get('usage').get('cpu')
            cpu_n += int(re.findall('\d+', cpu)[0])

    if current_cpu != cpu_n:
        print("({i},{c})".format(i = index, c = cpu_n))
        current_cpu = cpu_n
        write_csv(index, cpu_n)
        index += 1

    time.sleep(0.1)

