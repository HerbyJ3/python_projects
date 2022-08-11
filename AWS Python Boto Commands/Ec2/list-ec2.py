from importlib.util import resolve_name
import boto3
ec2_client=boto3.client("ec2")
response = ec2_client.describe_instances()

#print(response.keys())
#print(response['Reservations'][0])
x = response['Reservations'][0]
data_instannce = x['Instances']
for i in range (len(data_instannce)):
    print(f"Instances id is {data_instannce[i] ['InstanceId']}")