import logging
import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(bucket, object_name, file_name=None):
    """Download a file from an S3 bucket

    :param bucket: Bucket to download from
    :param object_name: S3 object name.
    :param file_name: Downloaded file name. If not specified then object_name is used
    :return: True if file was downloaded, else False
    """

    # If S3 file_name was not specified, use object_name
    if file_name is None:
        file_name = object_name

    # Download the file
    s3_client = boto3.client('s3')
    try:
        s3_client.download_file(bucket, object_name, file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


upload_file("random_small.txt", "natthanonsdsact3")
upload_file("random_large.txt", "natthanonsdsact3")
