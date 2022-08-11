import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('My_Favorite_Movies')

response = table.scan()
items = response['Items']
for movies in items:
    print(movies['title'])