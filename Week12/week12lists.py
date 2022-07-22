awsservices = []
awsservices += ['S3', 'Lambda', 'EC2', 'CloudFormation', 'DynamoDB', 'CodeDeploy', 'Cloud9']
print(awsservices)
print("The length of this list is ", len(awsservices))
del awsservices[1:4:2]
print(awsservices)
print("The new length of this list is now ", len(awsservices))