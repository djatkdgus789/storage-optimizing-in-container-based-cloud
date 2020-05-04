import requests
import json
'''
r = requests.get('http://localhost:3000/api/nodes')

print(r.text)

r = requests.get('http://localhost:3000/api/images?node_name=whale01').json()
print(r)

print(type(r))

r = r.values()
print(range(len(r)))
for imagelist in r:
    for image in imagelist:
        print(image)
'''
pod_list = requests.get('http://localhost:8080/apis/metrics.k8s.io/v1beta1/pods').json().get('items')
pods = dict()
for p in pod_list:
    pod = dict()
    # pod["cpu"]
    #print(p.get('metadata').get('name'))
    #print(p.get('metadata').get('usage'))
    # pod["memory"]
    container = p.get('containers')[0]
    #print(p.get('containers')[0])
    print(container.get('name'))
    print(container.get('usage'))
    #print(type(p.get('containers')[0]))
    # pods[n.get('metadata').get('name')] = pod
    # pod_list[0].get('metadata').get('name')
