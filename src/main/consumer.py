from __future__ import print_function

import sys
import sgf

from pyspark import SparkContext
from pyspark.sql import HiveContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


def format(value):
    if value is None:
        return ",''"
    else:
        return ",'" + str(value) + "'"

hc = None
def sendRecord(kafkaRDD):
    if kafkaRDD.isEmpty():
        return kafkaRDD

    msg = kafkaRDD.collect()[0][1].rstrip("\"").lstrip("\"").split("====")
    if "game" not in hc.sql("show tables").collect():
        sqlstate = "create table if not exists game (ID int, FF string, SZ string, PW string, WR string, " \
            + "PB string, BR string, DT string, PC string, KM string, RE string, RU string, OT string, CA string, " \
            + "ST string, AP string, TM string, HA string"
        for i in range(9):
            sqlstate += ", AB" + str(i + 1) + " string"
        for i in range(361):
            sqlstate += ", STEP" + str(i + 1) + " string"
        sqlstate += ")"
        hc.sql(sqlstate)
    cntAB = 1
    dic = {}
    for i in msg:
        key, val = "", ""
        arr = i.split("----")
        if arr[0] == "0":
            if arr[1] == "AB":
                key = "AB" + str(cntAB)
                cntAB += 1
            else:   
                key = arr[1]
            val = arr[2]
        else:
            key = "STEP" + str(arr[0])
            val = arr[1] + "->" + arr[2]
        dic[key] = val

    #check data exists or not
    checkSql = "select 1 from game where PW='" + dic.get("PW", "") + "' and PB='" + dic.get("PB", "") + "' and DT='" + dic.get("DT", "")\
        + "' and STEP3='" + dic.get("STEP3", "") + "' and STEP6='" + dic.get("STEP6", "") + "' and STEP9='" + dic.get("STEP9", "")\
        + "' and STEP10='" + dic.get("STEP10", "") + "' and STEP15='" + dic.get("STEP15", "") + "' and STEP17='" + dic.get("STEP17", "")\
        + "' and STEP20='" + dic.get("STEP20", "") + "' and STEP24='" + dic.get("STEP24", "") + "' and STEP25='" + dic.get("STEP25", "") + "'"
    exiNum = hc.sql(checkSql).count()
    if exiNum >= 1:
        print("Data already exists in our database, please import a new game record.")
        return kafkaRDD
    maxId = hc.sql("select max(ID) from game").first()[0]
    maxIdPlusOne = 0
    if maxId is not None:
        maxIdPlusOne = maxId + 1
    insertSql = "insert into game select * from (select '" + str(maxIdPlusOne) + "'" + format(dic.get("FF")) + format(dic.get("SZ")) + format(dic.get("PW"))\
        + format(dic.get("WR")) + format(dic.get("PB")) + format(dic.get("BR"))+ format(dic.get("DT")) + format(dic.get("PC")) + format(dic.get("KM"))\
        + format(dic.get("RE")) + format(dic.get("RU")) + format(dic.get("OT")) + format(dic.get("CA")) + format(dic.get("ST")) + format(dic.get("AP"))\
        + format(dic.get("TM")) + format(dic.get("HA"))
    for i in range(9):
        insertSql += format(dic.get("AB" + str(i + 1)))
    for i in range(361):
        insertSql += format(dic.get("STEP" + str(i + 1)))
    insertSql += ") t"
    hc.sql(insertSql)

if __name__ == "__main__":
    print("start.....")
    if len(sys.argv) != 3:
        print("Usage: direct_kafka_wordcount.py <broker_list> <topic>", file=sys.stderr)
        sys.exit(-1)
    sc = SparkContext.getOrCreate()
    sc.setLogLevel("WARN")
    #every two seconds
    ssc = StreamingContext(sc, 2)
    hc = HiveContext(sc)
    hc.setConf("hive.metastore.uris", "thrift://localhost:9083");
    hc.refreshTable("record_20")
    brokers, topic = sys.argv[1:]
    kafkaDStream = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
    asdf = kafkaDStream.transform(sendRecord)
    asdf.pprint()
    #statistic 1
    #statistic 2
    #statistic 3
    # res = hc.sql("select * from game")
    ssc.start()
    ssc.awaitTermination()
    print("end.....")








