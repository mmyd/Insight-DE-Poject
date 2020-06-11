from __future__ import print_function
import os
import sys
from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
   
    spark = SparkSession\
        .builder\
        .appName("CreateEntity")\
        .getOrCreate()

    tags = "s3a://insight-de-data/tags.csv"
    tag_lines = spark.read.text(tags).rdd.map(lambda r: r[0])\
                                         .map(lambda line: line.split(','))
    tag_header = tag_lines.first()
    lines = tag_lines.filter(lambda x: x!=tag_header)\
            .filter(lambda x:int(x[3])>=30000000)\
                     .map(lambda x:(x[3],[x[4]])).reduceByKey(lambda x,y:x+y).collect()

    #tag_header = tag_lines.first()
    #tags_lines = tag_lines.filter(lambda x: x!=tag_header)
    tag_path = os.path.join("tags_out2.csv")
    with open(tag_path, "w", encoding="utf-8") as testFile:
        testFile.write('repository_id,tag_name\n')
        for v in lines:
            testFile.write('%s,%s\n' % (v[0],v[1]))
    print("tags2 finished!!")
    spark.stop()