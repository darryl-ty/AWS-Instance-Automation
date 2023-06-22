import time
import schedule
import boto3


def aws_instance_shutdown():
    pass


def aws_instance_startup():
    pass


def job_scheduling():
    schedule.every().monday.at("09:00", "US/Eastern").do(aws_instance_startup())
    schedule.every().monday.at("17:00", "US/Eastern").do(aws_instance_shutdown())

    schedule.every().tuesday.at("09:00", "US/Eastern").do(aws_instance_startup())
    schedule.every().tuesday.at("17:00", "US/Eastern").do(aws_instance_shutdown())

    schedule.every().wednesday.at("09:00", "US/Eastern").do(aws_instance_startup())
    schedule.every().wednesday.at("17:00", "US/Eastern").do(aws_instance_shutdown())

    schedule.every().thursday.at("09:00", "US/Eastern").do(aws_instance_startup())
    schedule.every().thursday.at("17:00", "US/Eastern").do(aws_instance_shutdown())

    schedule.every().friday.at("09:00", "US/Eastern").do(aws_instance_startup())
    schedule.every().friday.at("17:00", "US/Eastern").do(aws_instance_shutdown())

    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    job_scheduling()


if __name__ == '__main__':
    main()
