import boto3
ec2_client = boto3.client('ec2')
ec2_client.create_volume(AvailabilityZone='us-east-1a',
      Encrypted=True,
      Size=12,
      SnashotId='snap-0937bebed9fe4564e',
      VolumeType='gp2')