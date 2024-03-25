import logging

import azure.functions as func
import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage, BinaryBase64DecodePolicy, BinaryBase64EncodePolicy



queue_name = "colaDeReservas"
def main(req: func.HttpRequest) -> func.HttpResponse:

    
    logging.info('Python HTTP trigger function processed a request.')
    try:
        queue_client = QueueClient.from_connection_string(connect_str, queue_name)
        queue_client.send_message(req)

    except Exception as e:
        logging.info("errrorr")

        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
