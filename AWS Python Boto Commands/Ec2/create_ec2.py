import boto3
ec2_resource = boto3.resource("ec2")
response = ec2_resource.create_instances(ImageId='string', #mandatory parameters
                InstanceType = 't2.micro', #mandatory parameters
                MaxCount = 1,   #mandatory parameters
                MinCount = 1)   #mandatory parameters