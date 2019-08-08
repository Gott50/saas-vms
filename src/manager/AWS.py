import boto3
import os
from time import sleep

KEYNAME = 'saas-bot'
SECURITYGROUPS = ['saas-bot']
IMAGE_ID = os.environ.get('IMAGE_ID')


class AWS:
    def __init__(self, logger):
        self.logger = logger
        self.ec2 = boto3.resource('ec2', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                                  aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
        self.client = boto3.client('ec2', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                                   aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))

    def start(self):
        instance = self.ec2.create_instances(
            ImageId=IMAGE_ID, InstanceType='t2.micro',
            KeyName=KEYNAME, SecurityGroups=SECURITYGROUPS,
            MaxCount=1, MinCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                },
            ],
        )[0]
        self.logger.warning("for User %s start new Instance: %s" % (instance))

        return self.wait_for_instance(instance).public_ip_address

    def wait_for_instance(self, instance):
        while not instance.public_ip_address:
            sleep(10)
            self.logger.warning("wait for public_ip_address: %s" % instance)
            instance = self.ec2.Instance(instance.id)

        while instance.state['Name'] == 'pending':
            sleep(10)
            self.logger.warning("wait while pending %s" % instance)
            instance = self.ec2.Instance(instance.id)

        return instance

    def get_running_list(self):
        return list(filter(lambda i: (i.state['Name'] == 'running'), self.get_instances()))

    def get_instances(self):
        response = self.client.describe_instances(Filters=[
            {
                'Name': 'image-id',
                'Values': [
                    IMAGE_ID,
                ]
            },
        ], )
        ids = list(map(lambda i: i['Instances'][0]['InstanceId'], response['Reservations']))
        return list(map(lambda i: self.ec2.Instance(i), ids))