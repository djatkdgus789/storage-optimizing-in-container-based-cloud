import docker

client = docker.from_env()
image = client.images.pull('djatkdgus789/hello:latest')

print(image)

