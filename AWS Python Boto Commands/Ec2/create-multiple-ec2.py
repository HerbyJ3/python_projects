import boto3
ec2_resource=boto3.resource('ec2')
response = ec2_resource.create_instances(ImageId='ami-03657b56516ab7912',
        InstanceType='t2.micro',
        MaxCount=3,
        MinCount=3)
print(response)