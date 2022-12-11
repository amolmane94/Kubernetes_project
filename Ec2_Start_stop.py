
import boto3

#create Ec2 instance
def create_ec2_instance():
    try:
        print("Creating Ec2 Instances::")
        ec2 = boto3.client('ec2')
        ec2.run_instances(
            ImageId="ami-0beaa649c482330f7",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="EC2PracticeOhioReg"
        )
    except Exception as e:
        print(e)
#create_ec2_instance()

def describe_ec2_instance():
    try:
        print("Describe Ec2 Instance...")
        ec2=boto3.client('ec2')
        response = ec2.describe_instances(InstanceIds=['i-035a2063aa16a1ab9'])
        print(response['Reservations'][0]['Instances'][0]['InstanceId'])
    except Exception as e:
        print(e)
#describe_ec2_instance()

def stop_ec2():
    try:
        print("Stopping Ec2 Instance...")
        ec2=boto3.client('ec2')
        response = ec2.stop_instances(InstanceIds=['i-035a2063aa16a1ab9'])
    except Exception as e:
        print(e)
#stop_ec2()
def terminate_ec2():
    try:
        print("Terminating Ec2 intances..")
        ec2=boto3.client('ec2')
        response = ec2.terminate_instances(InstanceIds=['i-0415a7c42b1259640'])
    except Exception as e:
        print(e)

#terminate_ec2()
def start_ec2():
    try:
        print("Start Ec2 Instance...")
        ec2=boto3.client('ec2')
        response = ec2.start_instances(InstanceIds=['i-035a2063aa16a1ab9'])
    except Exception as e:
        print(e)
#start_ec2()