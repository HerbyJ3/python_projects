import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('My_Favorite_Movies')
    response = table.get_item(
        Key={
            'year': '2005',
            'title': 'Constantine'
        }
        )
    item = response['Item']
    return item