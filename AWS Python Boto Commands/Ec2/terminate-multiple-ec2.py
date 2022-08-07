import boto3
ec2_client=boto3.client('ec2')
response = ec2_client.describe_instances()

#print(len(response['Reservations'])) #Reservations refer to how many times the amount of instances has been initiated and not how many intances
data = response['Reservations']
li=[]
for instances in data:
    instance=instances['Instances']
    for ids in instance:
        instance_id = ids['InstanceId']
        li.append(instance_id)
prin(ec2_client.terminate_instances(InstanceIds=li))
