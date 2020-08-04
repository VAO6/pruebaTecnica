import random
import datetime
import uuid
import json
import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
    
    tipos = ["televisor", "nevera", "aire"]
    valores = [x for x in range(100)]
    min5 = datetime.timezone(datetime.timedelta(hours=-5))
    d = str(datetime.datetime.now(min5))
    fechacompleta = d[:-13]
    fecha, hora = fechacompleta.split(" ")
    nId = "".join((fecha.split("-")))[2:] + "".join((hora.split(":")))
    
    d = {"variable1": str(random.choice(valores)), "tipo": random.choice(tipos), 
        "fecha": fecha, "hora": hora, "nId": nId}
    data = json.dumps(d)
    response = client.invoke(
        FunctionName='agregarDatoServerless',
        InvocationType = 'RequestResponse',
        Payload = data
        )
    print(data)
    responseJson = json.load(response['Payload'])
    print('\n')
    print(responseJson)
    print('\n')

