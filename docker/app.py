from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from requests import put, get, post

app = Flask(__name__)
api = Api(app)


@app.route('/api/nodes')
def node_usage():
    node_list = get('http://localhost:8080/apis/metrics.k8s.io/v1beta1/nodes').json().get('items')
    nodes = dict()
    for n in node_list:
        node = dict()
        node["cpu"] = n.get('usage').get('cpu')
        node["memory"] = n.get('usage').get('memory')
        nodes[n.get('metadata').get('name')] = node
    return nodes


@app.route('/api/images', methods=['GET'])
def image_list():
    node_name = request.args.get('node_name')
    if node_name == 'whale01':
        return get('http://10.128.0.9:3000/api/images').json()
    elif node_name == 'whale02':
        return get('http://10.128.0.10:3000/api/images').json()
    elif node_name == 'whale03':
        return get('http://10.128.0.14:3000/api/images').json()
    elif node_name == 'whale04':
        return get('http://10.128.0.17:3000/api/images').json()
    elif node_name == 'whale05':
        return get('http://10.128.0.18:3000/api/images').json()


@app.route('/api/pull', methods=['GET'])
def image_pull():
    node_name = request.args.get('node_name')

    if node_name == 'whale01':
        return post('http://10.128.0.9:3000/api/pull').json()
    elif node_name == 'whale02':
        return post('http://10.128.0.10:3000/api/pull').json()
    elif node_name == 'whale03':
        return post('http://10.128.0.14:3000/api/pull').json()
    elif node_name == 'whale04':
        return post('http://10.128.0.17:3000/api/pull').json()
    elif node_name == 'whale05':
        return post('http://10.128.0.18:3000/api/pull').json()



@app.route('/api/prune', methods=['GET'])
def prune_image():
    node_name = request.args.get('node_name')
    if node_name == 'whale01':
        return get('http://10.128.0.9:3000/api/prune').json()
    elif node_name == 'whale02':
        return get('http://10.128.0.10:3000/api/prune').json()
    elif node_name == 'whale03':
        return get('http://10.128.0.14:3000/api/prune').json()
    elif node_name == 'whale04':
        return get('http://10.128.0.17:3000/api/prune').json()
    elif node_name == 'whale05':
        return get('http://10.128.0.18:3000/api/prune').json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
