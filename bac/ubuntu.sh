ssh mingweihe@192.168.56.102

#spark 2.3.0 hadoop 2.7.5 hbase 1.4.2

sudo apt-get install python-pip
pip install kafka-python
pip install pyspark

sudo apt-get install sshfs
sshfs Mingwei@192.168.56.1:/Users/hemingwei/Documents/MUM/BDT/Project /media/sf_Project/

#ls /media/sf_Project/
#lsof -i :8030
#nmap -p 8000 127.0.0.1
#jps
#vim ~/spark/conf/spark-env.sh
#sudo vim /etc/hosts

start-dfs.sh
start-yarn.sh

#if got exception when input list, restart it.
start-hbase.sh
#hadoop fs -ls /hbase
hbase shell
#spark
start-master.sh
#spark-shell 192.168.56.102:4040/jobs/
#spark-shell

#Not need, coz start-hbase.sh already started zoopkeeper with specified 2222 port
#bash /media/sf_Project/kafka_2.12-1.0.1/bin/zookeeper-server-start.sh /media/sf_Project/kafka_2.12-1.0.1/config/zookeeper.properties

bash /media/sf_Project/kafka_2.12-1.0.1/bin/kafka-server-start.sh /media/sf_Project/kafka_2.12-1.0.1/config/server.properties

bash /media/sf_Project/kafka_2.12-1.0.1/bin/kafka-topics.sh --create --zookeeper localhost:2222 --replication-factor 1 --partitions 1 --topic sampleTopic
#Test for kafka
#python /media/sf_Project/consumer.py
#python /media/sf_Project/producer.py

spark-submit --jars /media/sf_Project/ksslib/shc-core-1.1.1-2.1-s_2.11.jar,/media/sf_Project/ksslib/spark-core_2.11-2.3.0.jar,/media/sf_Project/ksslib/hbase-client-1.4.2.jar,/media/sf_Project/ksslib/hbase-common-1.4.2.jar,/media/sf_Project/ksslib/hbase-protocol-1.4.2.jar,/media/sf_Project/ksslib/hbase-hadoop2-compat-1.4.2.jar,/media/sf_Project/ksslib/hbase-hadoop-compat-1.4.2.jar,/media/sf_Project/ksslib/hbase-metrics-api-1.4.2.jar,/media/sf_Project/ksslib/hbase-metrics-1.4.2.jar /media/sf_Project/sparkSqlAccessHBase.py

spark-submit --jars /media/sf_Project/ksslib/shc-core-1.1.1-2.1-s_2.11.jar,$(echo /usr/local/HBase/lib/*.jar | tr ' ' ',') /media/sf_Project/sparkSqlAccessHBase.py

spark-submit --jars /media/sf_Project/ksslib/spark-streaming-kafka-0-8_2.11-2.3.0.jar,/media/sf_Project/ksslib/kafka_2.11-0.8.2.1.jar,/media/sf_Project/ksslib/scala-library-2.10.0-M3.jar,/media/sf_Project/ksslib/metrics-core-2.2.0.jar /media/sf_Project/streamingFromKafka.py localhost:9092 sampleTopic

