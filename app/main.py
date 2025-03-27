# SPDX-License-Identifier: Elastic-2.0
# Copyright (C) 2025 Un Aplauso

from os import getenv

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse

from app.predictors.opennsfw2 import opennsfw2_predict_image
from app.s3_bucket import S3Bucket
from app.utils import build_file_url, url_to_image

load_dotenv()
IS_PRODUCTION = getenv('ENV') == 'production'

app = FastAPI(docs_url=(None if IS_PRODUCTION else '/api/moderation/docs'))

@app.middleware('http')
async def app_key_middleware(request: Request, call_next):
    if IS_PRODUCTION and request.headers.get('x-api-key') != getenv('MODERATION_API_KEY'):
        return JSONResponse(status_code=403, content=None)
    return await call_next(request)

api_router = APIRouter(prefix='/api/moderation')

@api_router.get('/health') 
async def health(): return True

@api_router.get('/image-review/{bucket}/{uuid}') 
async def image_review(bucket: S3Bucket, uuid: str):
    print
    url = build_file_url(uuid, bucket)
    image = url_to_image(url)
    return opennsfw2_predict_image(image)

app.include_router(api_router)
