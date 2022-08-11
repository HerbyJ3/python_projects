import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('My_Favorite_Movies')

response = table.get_item(
    Key={
        'year': '1985',
        'title': 'The Last Dragon'
    }
)
item = response['Item']
print(item)