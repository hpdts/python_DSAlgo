from fastapi import FastAPI
from pydantic import BaseModel
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from image_worker import enqueue_image_job

load_dotenv()

app = FastAPI()

ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT")
ACCOUNT_KEY = os.getenv("AZURE_STORAGE_KEY")
CONTAINER = os.getenv("AZURE_CONTAINER")

blob_service = BlobServiceClient(
    f"https://{ACCOUNT_NAME}.blob.core.windows.net",
    credential=ACCOUNT_KEY
)

class FilenameRequest(BaseModel):
    filename: str

@app.post("/api/get-upload-url")
def get_upload_url(req: FilenameRequest):
    blob_name = f"original/{req.filename}"

    sas_token = generate_blob_sas(
        ACCOUNT_NAME,
        CONTAINER,
        blob_name,
        account_key=ACCOUNT_KEY,
        permission=BlobSasPermissions(write=True, create=True),
        expiry=datetime.utcnow() + timedelta(minutes=10)
    )

    sas_url = (
        f"https://{ACCOUNT_NAME}.blob.core.windows.net/"
        f"{CONTAINER}/{blob_name}?{sas_token}"
    )

    blob_url = f"https://{ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER}/{blob_name}"

    return {"sasUrl": sas_url, "blobUrl": blob_url}


class ProcessRequest(BaseModel):
    blobUrl: str

@app.post("/api/process-uploaded-image")
def begin_processing(req: ProcessRequest):
    # push message to worker queue (simplified)
    enqueue_image_job(req.blobUrl)
    return {"status": "queued"}
