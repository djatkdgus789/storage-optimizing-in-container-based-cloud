from flask import Flask, request
import shutil

app = Flask(__name__)


@app.route('/api/disk', methods=['GET'])
def disk_usage():
	total, used, free = shutil.disk_usage("/")
	data = dict()
	data["total"] = total
	data["used"] = used
	data["free"] = free	

	return data

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3001)
