import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Least_Favorite_Movies')

response = table.delete()
print(response)
print("Table status:", table.table_status)