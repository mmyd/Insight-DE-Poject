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

    projs = "s3a://insight-de-data/packages_out.csv"
    proj_rdd = spark.read.text(projs).rdd.map(lambda r: r[0])\
                                   .map(lambda line: line.split(','))\
                                   .map(lambda x:(x[3],x[0]))
    header1 = proj_rdd.first()
    proj_lines=proj_rdd.filter(lambda x: x!=header1)

    repos = "s3a://insight-de-data/repositories.csv"
    repo_rdd = spark.read.text(repos).rdd.map(lambda r: r[0])\
                                   .map(lambda line: line.split(','))\
                                   .filter(lambda x: len(x)>20)\
                                   .map(lambda x:(x[0],(x[8],x[17],x[19])))

    header2 = repo_rdd.first()
    repo_lines=repo_rdd.filter(lambda x: x!=header2)

    lines = repo_lines.join(proj_lines).collect()

    dep_path = os.path.join("repos_out.csv")
    with open(dep_path, "w", encoding="utf-8") as testFile2:
        testFile2.write("id,url,issues,watchers\n")
        for v in lines:
            testFile2.write('%s,%s,%s,%s\n' % (v[0], v[1][0][0],v[1][0][1],v[1][0][2]))
    spark.stop()
