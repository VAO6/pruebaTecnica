import json
import boto3
import uuid

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('pruebaTecnicaDB')
    id = str(uuid.uuid1())
    variable1 = event['variable1']
    fecha = event['fecha']
    hora = event['hora']
    tipo = event['tipo']
    nId = event['nId']
    response = table.put_item(
        Item= {"id": id, "tipo": tipo, "variables": {"variable1": variable1}, 
        "timestamp": {"fecha": fecha, "hora": hora}, "nId": nId},
    ) 
    return response
