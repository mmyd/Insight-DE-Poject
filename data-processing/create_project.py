from __future__ import print_function
import os
import sys
from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("CreateProject")\
        .getOrCreate()

    projects = "s3a://insight-de-data/projects.csv"
    project_lines = spark.read.text(projects).rdd.map(lambda r: r[0])\
                                                 .map(lambda line: line.split(','))\
                                                 .map(lambda x:(x[0],x[1].strip().lower(),x[2],x[7],x[16],x[20]))\
                                                 .collect()

    project_path = os.path.join("project_cleaned.csv")
    count = 0
    with open(project_path, "w", encoding="utf-8") as testFile:
        testFile.write('id,platform,name,homepage_url,language,repository_id\n')
        for l in project_lines:
            v = list(l)
            if v[4]== None or v[4]==0 or v[4].strip()=="0" or len(v[4].strip())>15:
                v[4] = "null"
            if v[5] == None or v[5]==0 or v[5].strip()=="0" or not v[5].strip().isdigit():
                v[5] = "null"
            if count == 0:
                count = 1
            else:
                testFile.write('%s,%s,%s,%s,%s,%s\n' % (v[0], v[1],v[2], v[3],v[4], v[5]))
    spark.stop()