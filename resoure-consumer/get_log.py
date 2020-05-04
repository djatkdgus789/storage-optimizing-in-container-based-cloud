import requests
import json
import re
import time

for t in range(0,100000):
    pod_list = requests.get('http://localhost:8080/apis/metrics.k8s.io/v1beta1/pods').json().get('items')
    pods = dict()
    n_apache = 0
    sum_apache = 0
    for p in pod_list:
        pod = dict()
        # print(p.get('metadata').get('name'))
        # print(p.get('metadata').get('usage'))
        container = p.get('containers')[0]
        # print(container.get('name'))
        if container.get('name') == 'resource-consumer':
            name = container.get('name')
            cpu = container.get('usage').get('cpu')
            cpu_n = int(re.findall('\d+', cpu)[0])
            # print(cpu_n)
            n_apache += 1
            sum_apache += cpu_n
    print("pod : "+ str(n_apache))
    print("cpu_n : "+ str(sum_apache))
    time.sleep(0.1)


