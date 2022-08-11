import boto3
from boto3.dynamodb.conditions import Key, Attr

def handler_name(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('My_Favorite_Movies')
    response = table.query(
    KeyConditionExpression=Key('year').eq('1985')
    )
    items = response['Items']
    
    return items