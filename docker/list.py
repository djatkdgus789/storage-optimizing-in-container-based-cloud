import docker

client = docker.from_env()
images = client.images.list()
print(images)
#for c in containers:
    #print(c.image)
