import boto3
client = boto3.client("ec2")
x = client.describe_vpcs()
no_of_vpcs = x["Vpcs"]
#len(no_of_vpcs) Displays the amount
for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    