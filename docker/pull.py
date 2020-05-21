import docker

client = docker.from_env()
image = client.images.pull('gcr.io/kubernetes-e2e-test-images/resource-consumer:1.4')

print(image)

