import io
import requests
from PIL import Image
from azure.storage.blob import BlobClient
import os

ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT")
ACCOUNT_KEY = os.getenv("AZURE_STORAGE_KEY")
CONTAINER = os.getenv("AZURE_CONTAINER")

def enqueue_image_job(blob_url):
    # In production use Azure Queue Storage / RabbitMQ / SQS.
    # Here we run sync for demo.
    process_image(blob_url)

def process_image(blob_url):
    print("Downloading original:", blob_url)
    resp = requests.get(blob_url)
    img = Image.open(io.BytesIO(resp.content))

    sizes = [512, 256, 64]

    for size in sizes:
        resized = img.copy()
        resized.thumbnail((size, size))

        buf = io.BytesIO()
        resized.save(buf, format="JPEG", quality=80)
        buf.seek(0)

        variant_name = blob_url.replace("original/", f"{size}/")

        upload_to_blob(variant_name, buf)

    print("Processing complete!")


def upload_to_blob(url, file_stream):
    # Convert URL → blob name
    blob_name = url.split(f"{CONTAINER}/")[1]

    blob_client = BlobClient(
        f"https://{ACCOUNT_NAME}.blob.core.windows.net",
        container_name=CONTAINER,
        blob_name=blob_name,
        credential=ACCOUNT_KEY
    )

    blob_client.upload_blob(file_stream, overwrite=True)
