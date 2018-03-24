#connect to virtual machine
ssh cloudera@192.168.56.101

#update source code from macbook to centOS
rm -rf /home/cloudera/workspace/GogoGo && scp -r Mingwei@192.168.56.1:/Users/hemingwei/Documents/MUM/BDT/GogoGo /home/cloudera/workspace/GogoGo

#start kafka server
bash /home/cloudera/workspace/GogoGo/tools/kafka_2.12-1.0.1/bin/kafka-server-start.sh /home/cloudera/workspace/GogoGo/tools/kafka_2.12-1.0.1/config/server.properties

#create a topic named sampleTopic
bash /home/cloudera/workspace/GogoGo/tools/kafka_2.12-1.0.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sampleTopic

#launch consumer
spark-submit --conf spark.ui.port=40440 /home/cloudera/workspace/GogoGo/src/main/consumer.py localhost:9092 sampleTopic

#launch producer
spark-submit /home/cloudera/workspace/GogoGo/src/main/producer.py


