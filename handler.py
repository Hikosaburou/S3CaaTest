import boto3
import json
import os
import logging
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from botocore.awsrequest import AWSRequest
from botocore.auth import SigV4Auth
from botocore.endpoint import BotocoreHTTPSession
from botocore.credentials import Credentials

def runner(event, context):
    s3 = boto3.resource('s3')

    bucketname = os.environ['BUCKET_NAME']
    keyname = os.environ['KEY_NAME']

    obj = s3.Object(bucketname, keyname)
    response = obj.get()
    body = response['Body'].read().decode('utf-8')

    print(body)
