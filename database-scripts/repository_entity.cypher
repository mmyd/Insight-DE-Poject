LOAD CSV WITH HEADERS FROM 'https://insight-de-data.s3.us-west-2.amazonaws.com/repository_cleaned.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3IYXZGSCUBBZD45X%2F20200610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200610T232946Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=f2be33e5f0985452402543a2548642beef3f3f6a70ce6d00a84df5ff0c69fa8d' AS line
CREATE (:Repository {id:line.id, url:line.url,issue_count:toInt(line.issues),watcher_count:toInt(line.watchers)})