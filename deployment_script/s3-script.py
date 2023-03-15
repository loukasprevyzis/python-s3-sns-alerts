import boto3
import pytz
from datetime import datetime, timedelta

# Specify the name of the S3 bucket 
bucket_name = '<name-of-the-bucket-here>'

# Specify your AWS credentials before running the script
aws_access_key_id = '<credential-to-be-added-here>'
aws_secret_access_key = '<credential-to-be-added-here>'

#Specify the email address to receive the notification
email_address = 'loucaspre@hotmail.com'

sns = boto3.client('sns', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='eu-central-1')

# Specifying SNS topic ARN that has been created on the Console
sns_topic_arn = '<sns-arn-to-be-added-here>'

# This has been commented out as the SNS subscription was deployed manually on the console, 
# but it can be used to validate an email address subscription.

# Confirm the subscription to the SNS topic for the email address
####subscription = sns.subscribe(
    ###TopicArn=sns_topic_arn,
    ##Protocol='email',
    #Endpoint=email_address
#)

# Create a new S3 client
s3 = boto3.client('s3', 
                  aws_access_key_id=aws_access_key_id, 
                  aws_secret_access_key=aws_secret_access_key)

# Connect to the S3 service using the default session
s3 = boto3.resource('s3')

# Get a reference to the S3 bucket
bucket = s3.Bucket(bucket_name)

# Get a list of all objects in the bucket
objects = s3.Bucket(bucket_name).objects.filter()

# Get the current time in UTC timezone
utc = pytz.UTC
now = datetime.now(utc)

# Loop to iterate over all the files in the bucket
for obj in bucket.objects.all():
    # Get the time the file was last modified
    mod_time = obj.last_modified
    obj_key = obj.key


    # Calculate the time difference between now and the last modified time
    time_diff = now - mod_time

 # Send a notification indicating that the file was not updated within the past 24 hours
    message = f"File {obj_key} was not updated within the past 24 hours"
    subject = "File not updated"
    response = sns.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject=subject
    )

    # Print the result of the SNS notification
    print(f"Email notification sent for {obj_key}")
