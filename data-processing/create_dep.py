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

    deps = "s3a://insight-de-data/dependencies.csv"
    rdd = spark.read.text(deps).rdd.map(lambda r: r[0])\
                                   .map(lambda line: line.split(','))\
                                   .map(lambda x:(x[0],x[3],x[4],x[6],x[7],x[8],x[9],x[10],x[11]))
    header = rdd.first()
    dep_lines=rdd.filter(lambda x: x!=header).filter(lambda x:(int(x[1])<=10000 and(x[8]=='' or int(x[8])<=10000))).collect()

    dep_path = os.path.join("deps_out.csv")
    with open(dep_path, "w", encoding="utf-8") as testFile2:
        for v in dep_lines:
            testFile2.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (v[0], v[1],v[2], v[3],v[4], v[5],v[6],v[7],v[8]))
    spark.stop()