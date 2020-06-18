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

    projects = "s3a://insight-de-data/projects.csv"
    project_lines = spark.read.text(projects).rdd.map(lambda r: r[0])\
                                                 .map(lambda line: line.split(','))\
                                                 .map(lambda x:x[1].strip().lower())\
                                                 .distinct().collect()

    platform_path = os.path.join("platform_cleaned.csv")
    with open(platform_path, "w", encoding="utf-8") as testFile:
        testFile.write('plaform\n')
        for v in project_lines:
            testFile.write('%s\n' % (v))
    spark.stop()