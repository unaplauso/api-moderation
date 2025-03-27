from enum import Enum
from os import getenv


class S3Bucket(Enum):
    PUBLIC = 'unaplauso-public'

def get_bucket_host(bucket: S3Bucket):
    if bucket == S3Bucket.PUBLIC:
        return getenv('S3_PUBLIC_URL')
