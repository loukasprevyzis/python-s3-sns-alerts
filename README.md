# loukas-python-s3-alert

#### A Python script that uses the AWS SDK to check that every file within an S3 bucket has been updated within the past 24 hours. The bucket is expected to contain between 20 and 30 files. After checking, the script should notify us (either by email, Slack message or similar) of any files which have not been updated.

- This script has been run and tested on macOS.
- Python version used for this exercise is Python 3.10.8 -> check you have the correct Python.version running `python3 --version` in your virtual environment.
- Using AWS as the cloud provider & the Amazon SNS service for the messaging process.  
- Please check the requirements.txt file for the dependencies that need to be installed 
- A virtual env has been created to run the script -> ``python3 -m venv <<name of venv>>``
- Install ``pip``
- Will need to upgrade pip if needed in the venv -> ``pip install --upgrade pip``

### boto3

**Boto3** is a Python library that allows you to easily integrate with Amazon Web Services (AWS) services.
Therefore, it needs to be installed in the virtual environment, in order for the import in the Python code to function without any errors. 

Choosing to use ``boto3`` was due to this project requiring interaction with AWS and this tool makes it simpler and more convenient. 

To install run ``pip install boto3`` or ``pip3 install boto3`` or ``python -m pip install boto3``, depending on your venv Python setup. 

### pytz module
- ***Pytz*** is a Python module that provides timezone database and timezone localization functionality. It was used in this script to convert the timings of the alers in UTC timezone to the local timezone of the user. 

### Datetime & timedelta imports 

The ``datetime`` class provides a way to represent dates and times in Python. It allows you to work with dates and times as objects, and provides methods for performing common operations such as formatting dates, converting between time zones, and performing arithmetic with dates and times.

The ``timedelta`` class is used to represent a duration of time. It allows you to perform arithmetic with time values, such as adding or subtracting a certain number of days, hours, minutes, or seconds from a given datetime object.

##### Specify your AWS Credentials

Please note that considering the Security of hard coded AWS credentials, is not standard practice and these should be encrypted if added hard coded in the script like the following: 

``aws_access_key_id = '<key-id-to-be-added-here>'``
``aws_secret_access_key = '<secret-access-key-to-be-added-here'``

Alternatively, for the AWS credentials to function properly, instead of having a credentials file in a ``~/.aws/credentials`` directory, the AWS keys are validated when running the following in your terminal within the virtual environment:

- AWS CLI will need to be installed in the virtual environment 

``pip install --upgrade awscli``

- If AWS CLI is already installed in the venv you are working in, they can also be upgraded if needed:

``pip install --upgrade awscli``

- Once AWS CLI is installed run ``aws configure`` to validate your AWS Credentials. 


For the purporse of this exercise, a separate IAM user has been created in the AWS Console and S3 IAM policies have been attached to that user. 

### IAM Access

Polices attached can be found in the ``deployment-screenshots`` folder, which include 

- The IAM user 
- The Policies attached to the user

### S3 Bucket Creation 

For testing purposes, an S3 Bucket was created on the AWS Console (Screenshot can be found in ``s3-bucket-screenshots`` folder of this repository).

Multiple **.jpg** objects have been uploaded to test the script (see ``deployment-screenshots`` folder, in this repository for the deployment example).

### S3 Bucket & SNS

Please note that the S3 Bucket and the SNS topic need to be within the same AWS Region
