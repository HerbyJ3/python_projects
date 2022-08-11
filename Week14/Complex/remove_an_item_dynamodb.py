import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('My_Favorite_Movies')
    remove = table.delete_item(
        Key={
            'year': '1999',
            'title': 'The Matrix'
        }
    )
    return remove
