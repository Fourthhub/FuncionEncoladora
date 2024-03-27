import logging

import azure.functions as func
import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage, BinaryBase64DecodePolicy, BinaryBase64EncodePolicy


connect_str = "DefaultEndpointsProtocol=https;AccountName=facturaciononcola;AccountKey=ipAS4lsYSlLmk1vhy5L//l2zoXSV2Fui5f0rc3b5ikPzY7SHJvu1w66Rb2h4vZODIxZcddyZnBg3+AStslU+3w==;EndpointSuffix=core.windows.net"
queue_name = "colita"
def main(req: func.HttpRequest) -> func.HttpResponse:

    
    logging.info('Python HTTP trigger function processed a request.')
    queue_client = QueueClient.from_connection_string(connect_str, queue_name)
    queue_client.send_message(req.get_json())


    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
