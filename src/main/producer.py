import sgf
import os  
import json
import glob
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

#all kgs files
#for fn in os.listdir('.'):
#     if os.path.isfile(fn):
#        print (fn)
directory = "/home/cloudera/workspace/GogoGo/input/kgs-19-2018-02-new/"
files = glob.glob(directory + "*.sgf")

for file in files:
	with open(file) as f:
		collection = sgf.parse(f.read())
	producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
	msgpack = ""
	for gameTree in collection:
	    cnt = 0
	    for node in gameTree:
	        for key, values in sorted(node.properties.items()):
	            for value in values:
	                msgpack = msgpack + str(cnt) + "----" + key + "----" + value + "===="
	        cnt += 1
	msgpack = msgpack.rstrip("====")
	print(file)
	print(msgpack[:200])
	producer.send('sampleTopic', msgpack).get(timeout = 60)
	time.sleep(5)