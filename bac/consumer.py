from __future__ import print_function

import sys
import sgf

from pyspark import SparkContext#, HiveContext
from pyspark.sql import SQLContext, Row, DataFrame #,SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

def getSparkSessionInstance():
    if ('sparkSessionSingletonInstance' not in globals()):
        globals()['sparkSessionSingletonInstance'] = SparkSession \
        .builder \
        .appName("Python Spark SQL Hive integration example") \
        .config("hive.metastore.uris", "thrift://127.0.0.1:9083") \
        .enableHiveSupport() \
        .getOrCreate()
    return globals()['sparkSessionSingletonInstance']

if __name__ == "__main__":
    # spark = getSparkSessionInstance()
    print("start.....")
    if len(sys.argv) != 3:
        print("Usage: direct_kafka_wordcount.py <broker_list> <topic>", file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext.getOrCreate()
    #sqlc = HiveContext(sc)
    sqlContext = SQLContext(sc)
    sc.setLogLevel("WARN")
    #every two seconds
    ssc = StreamingContext(sc, 2)

    brokers, topic = sys.argv[1:]
    #sqlc.sql("create table if not exists record(id string, key string, value string)")
    #spark.sql("create table if not exists record(id string, key string, value string)")
    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
    lines = kvs.map(lambda x: x[1])
    rowRdd = lines.filter(lambda line: "-" in line and line[0:line.index("-")] != "0")\
    	.flatMap(lambda line: line.split(" "))\
        .map(lambda p: Row(id=p[0], key=p[1], value=p[2]))

    sgfDF = sqlContext.createDataFrame(rowRdd)
    sgfDF.registerTempTable("record")
    sgfDF.write.parquet("record.parquet")
    parquetFile = sqlContext.read.parquet("people.parquet")
    parquetFile.registerTempTable("parquetFile");
    datasToShow = sqlContext.sql("SELECT id, key, value FROM parquetFile")
    for oneData in datasToShow.collect():
        print(oneData)

    #res.createOrReplaceTempView("mytempTable") 
    # sqlc.sql("create table if not exists mytable as select * from mytempTable");
    #kvs.write.mode("append").saveAsTable("record")
    #sqlc.sql("select * from record").show()
    print("end....pprint")
    ssc.start()
    ssc.awaitTermination()
    print("end.....")


    # rowRdd = rdd.map(lambda p: Row(movie_id=long(p[0]), budget=long(p[1]), popularity=float(p[2]), release_year=p[3], release_month=p[4], revenue=long(p[5]), title=p[6], voting_score=float(p[7]), voting_count=float(p[8])))
    #   sgfDF = spark.createDataFrame(rowRdd)
    #   newSgfDF = sgfDF[~sgfDF.movie_id.isin(existedMovieIdList)]
    #   newSgfDF.write.mode("append").saveAsTable("default.movie")