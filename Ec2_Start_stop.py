#AWS Ec2 instance Automation using python boto3
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
#create_ec2_instance()  #call this function to create EC2 intances
#Describe Ec2 Instance details
def describe_ec2_instance():
    try:
        print("Describe Ec2 Instance...")
        ec2=boto3.client('ec2')
        response = ec2.describe_instances(InstanceIds=['i-035a2063aa16a1ab9'])
        print(response['Reservations'][0]['Instances'][0]['InstanceId'])
    except Exception as e:
        print(e)
#describe_ec2_instance()    # call this function to describe EC2 Instance values
#Stop Instance
def stop_ec2():
    try:
        print("Stopping Ec2 Instance...")
        ec2=boto3.client('ec2')
        response = ec2.stop_instances(InstanceIds=['i-035a2063aa16a1ab9'])
    except Exception as e:
        print(e)
#stop_ec2()         #Call this function to stop instance
#Terminate Ec2 Instance
def terminate_ec2():
    try:
        print("Terminating Ec2 intances..")
        ec2=boto3.client('ec2')
        response = ec2.terminate_instances(InstanceIds=['i-035a2063aa16a1ab9'])
    except Exception as e:
        print(e)
#terminate_ec2()            #Call this function to Terminate Ec2 Instance
# Start Ec2 Intance
def start_ec2():
    try:
        print("Start Ec2 Instance...")
        ec2=boto3.client('ec2')
        response = ec2.start_instances(InstanceIds=['i-035a2063aa16a1ab9'])
    except Exception as e:
        print(e)
#start_ec2()                #Call this function to Start Ec2 Instance
#reboot Ec2 Instance 
def reboot_ec2():
    try:
        print("Rebooting Ec2....")
        ec2=boto3.client('ec2')
        response=ec2.reboot_instances(InstanceIds=['i-035a2063aa16a1ab9'])
    except Exception as e:
        print(e)
#reboot_ec2()               #call this function to reboot Ec2 Instance