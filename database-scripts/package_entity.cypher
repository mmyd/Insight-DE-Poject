LOAD CSV WITH HEADERS FROM 'https://insight-de-data.s3.us-west-2.amazonaws.com/package_cleaned.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3IYXZGSCUBBZD45X%2F20200610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200610T205645Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=b98d4fd5e34bc4847b1eac7f4a24433d00cb6f7d695c0d60101479c21067a955' AS line
CREATE (:Package {id:line.id, name: line.name, url:line.homepage_url})