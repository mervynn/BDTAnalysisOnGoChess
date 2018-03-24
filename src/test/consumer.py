from kafka import KafkaConsumer
consumer = KafkaConsumer('sampleTopic')
for msg in consumer:
	print (msg)
