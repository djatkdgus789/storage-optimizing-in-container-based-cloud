from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import docker
import json

app = Flask(__name__)
api = Api(app)


@app.route('/api/images', methods=['GET'])
def image_list():
    client = docker.from_env()
    images = client.images.list()
    image_json = dict()
    temp = list()
    for i in images:
        temp.append(i.tags)
    image_json['images'] = temp
    return image_json


@app.route('/api/pull', methods=['POST'])
def pull_image():
    client = docker.from_env()
    image = client.images.pull('gcr.io/kubernetes-e2e-test-images/resource-consumer:1.4')
    return dict()


@app.route('/api/prune', methods=['GET'])
def prune_image():
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    return client.prune_images(filters={'dangling': False})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
