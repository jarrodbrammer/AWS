import boto3
import os
import sys
import inspect

## Import Modules from parent Directory
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

## Import AWS Modules
from moto import mock_s3
from s3code import S3Handler



#Mock AWS Infrastructure and perform actions
# You can enter you main.py for actions here.
@mock_s3
def test_my_model_save():
    s3_client = boto3.client("s3")
    s3_client.create_bucket(Bucket="my_bucket")
    s3_handler= S3Handler()
    s3_handler.upload_s3_file()

