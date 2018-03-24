ssh mingweihe@192.168.56.102

#python2.7 /usr/local/bin/pip2.7 -V

#sudo yum install python-pip
#pip install kafka-python
#sudo python2.7 /usr/local/bin/pip2.7 install kafka-python
#pip install pyspark
#pip install sgf
#sudo python2.7 /usr/local/bin/pip2.7 install pyspark

#sudo apt-get install sshfs
sshfs Mingwei@192.168.56.1:/Users/hemingwei/Documents/MUM/BDT/GogoGo /media/sf_Project/

#lsof -i :8030
#nmap -p 8000 127.0.0.1
#jps
#vim ~/spark/conf/spark-env.sh
#sudo vim /etc/hosts
#ls | wc -l
#netstat -lnap | grep <port>

#start-dfs.sh
#start-yarn.sh

#if got exception when input list, restart it.
#start-hbase.sh
#hadoop fs -ls /hbase
#hbase shell
#spark
#start-master.sh
#192.168.56.101:4040/jobs/
#spark-shell

bash /media/sf_Project/tools/kafka_2.12-1.0.1/bin/zookeeper-server-start.sh /media/sf_Project/tools/kafka_2.12-1.0.1/config/zookeeper.properties

hive service --metastore

#start kafka server
bash /media/sf_Project/tools/kafka_2.12-1.0.1/bin/kafka-server-start.sh /media/sf_Project/tools/kafka_2.12-1.0.1/config/server.properties

#start kafka one app on kafka with a topic name sampleTopic
bash /media/sf_Project/tools/kafka_2.12-1.0.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sampleTopic


#Test for kafka broadcasting
#spark-submit /media/sf_Project/src/main/test/consumer.py
#spark-submit /media/sf_Project/src/main/test/producer.py

spark-submit /media/sf_Project/src/main/consumer.py localhost:9092 sampleTopic
spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8:2.3.0 /media/sf_Project/src/main/consumer.py localhost:9092 sampleTopic
spark-submit /media/sf_Project/src/main/producer.py



