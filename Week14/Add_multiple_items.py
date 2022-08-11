import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('My_Favorite_Movies')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'year': '1997',
            'title': 'The Fifth Element'
            }
    )
    batch.put_item(
        Item={
            'year': '2006',
            'title': '300'
            }
    )
    batch.put_item(
        Item={
            'year': '2010',
            'title': 'Tron: Legacy'
            }
    )
    batch.put_item(
        Item={
            'year': '1999',
            'title': 'The Matrix'
            }
    )
    batch.put_item(
        Item={
            'year': '2014',
            'title': 'John Wick'
            }
    )
    batch.put_item(
        Item={
            'year': '1997',
            'title': 'Starship Troopers'
            }
    )
    batch.put_item(
        Item={
            'year': '1988',
            'title': 'Action Jackson'
            }
    )
    batch.put_item(
        Item={
            'year': '2008',
            'title': 'The Incredible Hulk'
            }
    )
    batch.put_item(
        Item={
            'year': '1985',
            'title': 'The Last Dragon'
            }
    )
    batch.put_item(
        Item={
            'year': '2005',
            'title': 'Constantine'
            }
    )
