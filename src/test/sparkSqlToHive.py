from pyspark import SparkContext, HiveContext

sc = SparkContext(appName = "test")
sqlc = HiveContext(sc)

sqlc.sql("create table if not exists asdf1(id string, name string)")
#sqlc.sql("insert into asdf select * from (select stack(3, 1.1, 'A', 1.2, 'b', 1.3, 'C')) t")
#sqlc.sql("insert into asdf select * from (select 2, 3.14) t")
data = sqlc.sql("select 1, 'AA'")
for i in range(5):
    data.write.mode("append").saveAsTable("asdf1")
res = sqlc.sql("select * from asdf")
res.show()
