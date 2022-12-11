#Creating VPC subnet and security gruops
import boto3
from botocore.exceptions import ClientError

class CreateEc2Instance(object):
    def __init__(self,ec2_client):
        self.ec2_client=ec2_client
    def grep_vpc_subnet_id(self):
        vpc_id=""
        response= self.ec2_client.describe_vpcs()
        #print(response)
        for vpc in response['Vpcs']:
            if vpc["Tags"][0]["Value"].__contains__("Default"):
                vpc_id=vpc['VpcId']
                break
        print("The Default VpC:",vpc_id)   
        response=self.ec2_client.describe_subnets(Filters=[{"Name":"vpc_id","Values":[vpc_id]}])
        print(response)      
# lest start Execution
try:
    ec2=boto3.client('ec2')
    call_obj=CreateEc2Instance(ec2)
    call_obj.grep_vpc_subnet_id()
except ClientError as e:
    print(e)