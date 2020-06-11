spark-submit --packages com.amazonaws:aws-java-sdk:1.7.4,org.apache.hadoop:hadoop-aws:2.7.7 \
             --master spark://ec2-44-231-72-130.us-west-2.compute.amazonaws.com:7077 \
             --driver-memory 6G \
             --executor-memory 6G \
             --conf "spark.driver.maxResultSize=3G" \
             $PYTHONFILE