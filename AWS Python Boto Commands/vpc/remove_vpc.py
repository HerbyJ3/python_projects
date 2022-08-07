import boto3
client = boto3.client("ec2")
response = client.delete_vpc(
    VpvId = 'vpc0fb438cbd8e4kf8f'
)
print(response)