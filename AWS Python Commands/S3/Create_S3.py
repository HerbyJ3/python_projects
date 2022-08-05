import boto3
s3 =boto3.resource("s3")
bucket=s3.Bucket("totaltechnology32323") #set the bucket name here
response = bucket.create(
    ACL='public-read', #edit for different ACL policy
    CreateBucketConfiguration={
        'LocationConstraint':'us-west-1' #edit for different region
    },

)

print(response) # this will enable the action to create the bucket