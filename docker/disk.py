import shutil
import csv
import os
import time
from requests import get


index = 0


master = './master_storage.csv'
if os.path.isfile(master):
	os.remove(master)

whale01 = './whale01_storage.csv'
if os.path.isfile(whale01):
	os.remove(whale01)

whale02 = './whale02_storage.csv'
if os.path.isfile(whale02):
	os.remove(whale02)

whale03 = './whale03_storage.csv'
if os.path.isfile(whale03):
	os.remove(whale03)

whale04 = './whale04_storage.csv'
if os.path.isfile(whale04):
	os.remove(whale04)

whale05 = './whale05_storage.csv'
if os.path.isfile(whale05):
	os.remove(whale05)


def write_csv(index, total, used, free, node):
	with open(node, 'a') as outfile:
		writer = csv.writer(outfile)
		data = list()
		data.append(index)
		data.append(total)
		data.append(used)
		data.append(free)
		writer.writerow(data)

for t in range(0,3600):
	total, used, free = shutil.disk_usage("/")
	write_csv(index, total, used, free, master)

	data = list()
	data.append(get('http://10.128.0.9:3001/api/disk').json())	
	data.append(get('http://10.128.0.10:3001/api/disk').json())	
	data.append(get('http://10.128.0.14:3001/api/disk').json())	
	data.append(get('http://10.128.0.17:3001/api/disk').json())	
	data.append(get('http://10.128.0.18:3001/api/disk').json())	
	
	write_csv(index, data[0]["total"], data[0]["used"], data[0]["free"], whale01)
	write_csv(index, data[1]["total"], data[1]["used"], data[1]["free"], whale02)
	write_csv(index, data[2]["total"], data[2]["used"], data[2]["free"], whale03)
	write_csv(index, data[3]["total"], data[3]["used"], data[3]["free"], whale04)
	write_csv(index, data[4]["total"], data[4]["used"], data[4]["free"], whale05)


	index += 1

	time.sleep(1)
