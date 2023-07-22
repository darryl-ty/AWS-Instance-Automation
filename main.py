import pytz
import time
import schedule
import boto3

region = 'INSERT_REGION'
instances = ['INSERT_INSTANCES']
ec2 = boto3.client('ec2', region_name=region)


def aws_instance_shutdown():
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))


def aws_instance_startup():
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))


def job_scheduling():
    schedule.every().monday.at("09:00", "US/Eastern").do(aws_instance_startup)
    schedule.every().monday.at("17:00", "US/Eastern").do(aws_instance_shutdown)

    schedule.every().tuesday.at("09:00", "US/Eastern").do(aws_instance_startup)
    schedule.every().tuesday.at("17:00", "US/Eastern").do(aws_instance_shutdown)

    schedule.every().wednesday.at("09:00", "US/Eastern").do(aws_instance_startup)
    schedule.every().wednesday.at("17:00", "US/Eastern").do(aws_instance_shutdown)

    schedule.every().thursday.at("09:00", "US/Eastern").do(aws_instance_startup)
    schedule.every().thursday.at("17:00", "US/Eastern").do(aws_instance_shutdown)

    schedule.every().friday.at("09:00", "US/Eastern").do(aws_instance_startup)
    schedule.every().friday.at("17:00", "US/Eastern").do(aws_instance_shutdown)

    while True:
        schedule.run_pending()
        time.sleep(1)


def lambda_handler(event, context):
    job_scheduling()


