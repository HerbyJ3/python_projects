import boto3
client = boto3.client("ec2")
response = client.create_vpc(CidrBlock='10.0.0.0/16') # CidrBlock is required
print(response)
