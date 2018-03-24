ssh cloudera@192.168.56.101

#python2.7 /usr/local/bin/pip2.7 -V

#sudo yum install python-pip
#pip install kafka-python
#sudo python2.7 /usr/local/bin/pip2.7 install kafka-python
#pip install pyspark
#pip install sgf
#sudo python2.7 /usr/local/bin/pip2.7 install pyspark

#synch file propoal 1, (stable way)
rm -rf /home/cloudera/workspace/GogoGo && scp -r Mingwei@192.168.56.1:/Users/hemingwei/Documents/MUM/BDT/GogoGo /home/cloudera/workspace/GogoGo
#synch file propoal 2, (is better, no operation each time) 
# cd /opt/VBoxGuestAdditions-*/init
# sudo ./vboxadd setup
# sudo mount -t vboxsf GogoGo ~/workspace/GogoGo

#lsof -i :8030
#nmap -p 8000 127.0.0.1
#jps
#vim ~/spark/conf/spark-env.sh
#sudo vim /etc/hosts
#ls | wc -l
#netstat -anp | grep <port>

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

#Not need, coz start-hbase.sh already started zoopkeeper with specified 2181 port
#bash /home/cloudera/workspace/GogoGo/tools/kafka_2.12-1.0.1/bin/zookeeper-server-start.sh /home/cloudera/workspace/GogoGo/tools/kafka_2.12-1.0.1/config/zookeeper.properties

# rm metastore_db/*.lck
hive --service metastore 

#start kafka server
bash /home/cloudera/workspace/GogoGo/tools/kafka_2.12-1.0.1/bin/kafka-server-start.sh /home/cloudera/workspace/GogoGo/tools/kafka_2.12-1.0.1/config/server.properties

#create a topic named sampleTopic
bash /home/cloudera/workspace/GogoGo/tools/kafka_2.12-1.0.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sampleTopic


#Test for kafka broadcasting
#spark-submit /home/cloudera/workspace/GogoGo/src/main/test/consumer.py
#spark-submit /home/cloudera/workspace/GogoGo/src/main/test/producer.py

spark-submit --conf spark.ui.port=40440 /home/cloudera/workspace/GogoGo/src/main/consumer.py localhost:9092 sampleTopic
spark-submit /home/cloudera/workspace/GogoGo/src/main/producer.py


