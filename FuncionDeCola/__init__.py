import logging

import azure.functions as func
import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage, BinaryBase64DecodePolicy, BinaryBase64EncodePolicy


connect_str = "DefaultEndpointsProtocol=https;AccountName=colafun;AccountKey=9lrsrXglDMb2+9aY3V8uZzZbI36AXU1tVIc8QSpdmFRacuJeGJEZlU2IisrgZi2HNBzvbtuRc1x++AStbm3BaQ==;EndpointSuffix=core.windows.net"

queue_name = "colafunqueue"
def main(req: func.HttpRequest) -> func.HttpResponse:

    
    logging.info('Python HTTP trigger function processed a request.')
    queue_client = QueueClient.from_connection_string(connect_str, queue_name)
    queue_client.send_message(req)


    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
