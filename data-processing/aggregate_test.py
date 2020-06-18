from __future__ import print_function
import os
import sys
from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("CreatePackage")\
        .getOrCreate()

    projects = "s3a://insight-de-data/projects.csv"
    project_lines = spark.read.text(projects).rdd.map(lambda r: r[0])\
                                                 .map(lambda line: line.split(','))\
                                                 .map(lambda x:((x[0],x[20]),(x[1].strip().lower(),x[2],x[7],x[16])))\
                                                 .sortByKey()  # Agrregate the statements for test
                                                 .collect()

    project_path = os.path.join("project_test.csv")
    count = 0
    with open(project_path, "w", encoding="utf-8") as testFile:
        testFile.write('id,platform,name,homepage_url,language,repository_id\n')
        for l in project_lines:
            v = list(l)
            # data cleaning for the repository_id columns(handle missing or unqualified values)
            if v[0][1] == None or v[0][1]==0 or v[0][1].strip()=="0" or not v[0][1].strip().isdigit():
                v[0][1] = "null"
            if count == 0:
                count = 1
            else:
                testFile.write('%s,%s,%s,%s,%s,%s\n' % (v[0][0], v[1][0],v[1][1], v[1][2],v[1][3], v[0][1]))
    spark.stop()