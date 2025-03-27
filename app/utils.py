
from io import BytesIO

import requests
from PIL import Image

from app.s3_bucket import S3Bucket, get_bucket_host


def build_file_url(uuid: str, bucket = S3Bucket.PUBLIC):
    return get_bucket_host(bucket) + '/' + uuid

def url_to_image(image_url: str) -> Image.Image: 
    response = requests.get(image_url, timeout=5)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))
