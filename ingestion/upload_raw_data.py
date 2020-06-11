import boto3
  
def upload(bucket_name):
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key='dependencies.csv', Body='dependencies.csv')
    print('Uploaded...to s3 ', ' ', 'dependencies.csv')
    s3.put_object(Bucket=bucket_name, Key='projects.csv', Body='projects.csv')
    print('Uploaded...to s3 ', ' ', 'projects.csv')
    s3.put_object(Bucket=bucket_name, Key='repositories.csv', Body='repositories.csv')
    print('Uploaded...to s3 ', ' ', 'repositories.csv')
    s3.put_object(Bucket=bucket_name, Key='tags.csv', Body='tags.csv')
    print('Uploaded...to s3 ', ' ', 'tags.csv')

upload('insight-de-data')