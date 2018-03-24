from __future__ import print_function

import sys
import sgf

from pyspark import SparkContext
from pyspark.sql import Row, DataFrame, SQLContext, HiveContext
from pyspark.sql.types import *
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

# def getSparkSessionInstance():
#     if ('sparkSessionSingletonInstance' not in globals()):
#         globals()['sparkSessionSingletonInstance'] = SparkSession \
#         .builder \
#         .appName("Python Spark SQL Hive integration example") \
#         .config("hive.metastore.uris", "thrift://127.0.0.1:9083") \
#         .enableHiveSupport() \
#         .getOrCreate()
#     return globals()['sparkSessionSingletonInstance']
hc = None
def sendRecord(kafkaRDD):
    if kafkaRDD.isEmpty():
        return kafkaRDD
    a = kafkaRDD.foreach(lambda l: print(l[1]))
    # print(tup.offsetRanges())
    # print("*************" + str(len(tup)))
    # arr = tup[1].split(" ")
    # print(tuple(arr))
    # sc = SparkContext.getOrCreate()
    # sqlc = SQLContext(sc)
    # schemaString = "First Second Third Fourth Fifth"
    # fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
    # schema = StructType(fields)
    print(hc.tableNames())
    if "record_20" not in hc.sql("show tables").collect():
        hc.sql("create table if not exists record_20(a string, b string, c string, d string, e string)")
        # hc.createExternalTable("record_20", "/", "parquet", schema)
        # df.write.saveAsTable("record_20", mode = "overwrite")
    #hc.sql("insert into table record_20 values (1, 2, 3, 4, 5)")
    #hc.sql("insert into record_20 select * from (select 1, 2, 3, 4, 5) t")
    # data = [(1, 2, 3, 4, 5),(1, 2, 3, 4, 5)]
    # data2 = [("a", "b", "c", "d", "e"),("a", "b", "c", "d", "e")]
    # df = hc.createDataFrame(data, schema)
    # df.write.mode("overwrite").saveAsTable("record_20")
    # hc.createDataFrame(data2, schema).write.mode("overwrite").saveAsTable("record_20")
    hc.sql("insert into record_20 select * from (select 1, 3, 5, 7, 9) t")
    hc.sql("insert into record_20 select * from (select 'z', '1', 'ee', '2', 3.33) t")
    # df.write.mode("append").saveAsTable("record_20")
    # df.persist()
    #df.show()
    #.sqlc.setConf("spark.sql.hive.thriftServer.singleSession", "true")
    # data = sqlc.sql("select "+ str(arr[0]) + "," + str(arr[1]) +"," + str(arr[2]))
    #df.write.mode("overwrite").saveAsTable("record_20")
    res = hc.sql("select * from record_20")
    res.show()
    # sqlc.stop()
    # sc.stop()

if __name__ == "__main__":
    print("start.....")
    if len(sys.argv) != 3:
        print("Usage: direct_kafka_wordcount.py <broker_list> <topic>", file=sys.stderr)
        sys.exit(-1)
    sc = SparkContext.getOrCreate()
    # sqlc = HiveContext(sc)
    # sqlc.setConf("spark.sql.hive.thriftServer.singleSession", "true")
    #sqlContext = SQLContext(sc)
    sc.setLogLevel("WARN")
    #every two seconds
    ssc = StreamingContext(sc, 2)
    hc = HiveContext(sc)
    hc.setConf("hive.metastore.uris", "thrift://localhost:9083");
    hc.refreshTable("record_20")
    brokers, topic = sys.argv[1:]
    #spark.sql("create table if not exists record(id string, key string, value string)")
    kafkaDStream = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
    #kafkaDStream.saveAsTextFiles("rawdata.txt")
    #kafkaDStream.saveAsTextFiles("rawdata", "txt")
    #lines = sc.textFile("rawdata.txt")
    #kafkaDStream.foreachRDD(lambda kafkaRDD: kafkaRDD.foreach(sendRecord))
    asdf = kafkaDStream.transform(sendRecord)
    asdf.pprint()
    #lines = kafkaDStream.map(lambda x: x[1])
    #parts = lines.flatMap(lambda l: l.split(" "))
    #record = parts.map(lambda p: (p[0], p[1]))
    #record.pprint()
    #schemaString = "id key value"
    #fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
    #print(fields)
    #schema = StructType(fields)
    #print(fields)
    # Apply the schema to the RDD.
    # schemaRecord = sqlContext.createDataFrame(record, schema)
    # schemaRecord.registerTempTable("record")
    # SQL can be run over DataFrames that have been registered as a table.
    # results = sqlContext.sql("select id, key, value from record")
    #for oneData in results.collect():
        #print(oneData)
    # results.show()

    #res.createOrReplaceTempView("mytempTable") 
    # sqlc.sql("create table if not exists mytable as select * from mytempTable");
    #kafkaDStream.write.mode("append").saveAsTable("record")
    #sqlc.sql("select * from record").show()
    ssc.start()
    ssc.awaitTermination()
    # ssc.stop()
    # sc.stop()
    print("end.....")


    # rowRdd = rdd.map(lambda p: Row(movie_id=long(p[0]), budget=long(p[1]), popularity=float(p[2]), release_year=p[3], release_month=p[4], revenue=long(p[5]), title=p[6], voting_score=float(p[7]), voting_count=float(p[8])))
    #   sgfDF = spark.createDataFrame(rowRdd)
    #   newSgfDF = sgfDF[~sgfDF.movie_id.isin(existedMovieIdList)]
    #   newSgfDF.write.mode("append").saveAsTable("default.movie")