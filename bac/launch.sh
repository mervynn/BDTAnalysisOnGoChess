ssh cloudera@192.168.56.101

#python2.7 /usr/local/bin/pip2.7 -V

#sudo yum install python-pip
#pip install kafka-python
#sudo python2.7 /usr/local/bin/pip2.7 install kafka-python
#pip install pyspark
#sudo python2.7 /usr/local/bin/pip2.7 install pyspark

scp -r Mingwei@192.168.56.1:/Users/hemingwei/Documents/MUM/BDT/GogoGo ~/workspace/Go

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

#Not need, coz start-hbase.sh already started zoopkeeper with specified 2181 port
#bash ~/workspace/GogoGo/kafka_2.12-1.0.1/bin/zookeeper-server-start.sh ~/workspace/GogoGo/kafka_2.12-1.0.1/config/zookeeper.properties

#start kafka server
bash ~/workspace/GogoGo/kafka_2.12-1.0.1/bin/kafka-server-start.sh ~/workspace/GogoGo/kafka_2.12-1.0.1/config/server.properties

#start kafka one app on kafka with a topic name sampleTopic
bash ~/workspace/GogoGo/kafka_2.12-1.0.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sampleTopic

#Test for kafka broadcasting
#spark-submit ~/workspace/GogoGo/consumer.py
#spark-submit ~/workspace/GogoGo/producer.py

#spark-submit --jars ~/workspace/GogoGo/ksslib/shc-core-1.1.1-2.1-s_2.11.jar,~/workspace/GogoGo/ksslib/spark-core_2.11-2.3.0.jar,~/workspace/GogoGo/ksslib/hbase-client-1.4.2.jar,~/workspace/GogoGo/ksslib/hbase-common-1.4.2.jar,~/workspace/GogoGo/ksslib/hbase-protocol-1.4.2.jar,~/workspace/GogoGo/ksslib/hbase-hadoop2-compat-1.4.2.jar,~/workspace/GogoGo/ksslib/hbase-hadoop-compat-1.4.2.jar,~/workspace/GogoGo/ksslib/hbase-metrics-api-1.4.2.jar,~/workspace/GogoGo/ksslib/hbase-metrics-1.4.2.jar ~/workspace/GogoGo/sparkSqlAccessHBase.py

spark-submit ~/workspace/GogoGo/testsparksql.py

spark-submit --jars ~/workspace/GogoGo/ksslib/spark-streaming-kafka-0-8_2.11-2.3.0.jar,~/workspace/GogoGo/ksslib/kafka_2.11-0.8.2.1.jar,~/workspace/GogoGo/ksslib/scala-library-2.10.0-M3.jar,~/workspace/GogoGo/ksslib/metrics-core-2.2.0.jar ~/workspace/GogoGo/streamingFromKafka.py localhost:9092 sampleTopic



