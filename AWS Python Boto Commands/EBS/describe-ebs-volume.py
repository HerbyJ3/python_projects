import boto3
ec2_client = boto3.client('ec2')
response = ec2_client.describe_snapshots(SnapshotIds=['snap-023e72ba4d5c137b9'])

print(response)