import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import date
from src.leerDato.vacio import vacio


def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('pruebaTecnicaDB')
    resp = {}    
    x = ""
    y = 1
    try:
        if event['tipo'] != x:
            response = table.scan(
                    FilterExpression=Attr('tipo').eq(event['tipo'])
                )
            if event['fechainicial'] != x and event['fechafinal'] != x:
                fechaInicial = date.fromisoformat(event['fechainicial'])
                fechaFinal = date.fromisoformat(event['fechafinal'])
                for item in response['Items']:
                    if date.fromisoformat(item['timestamp']['fecha']) > fechaInicial and date.fromisoformat(item['timestamp']['fecha']) < fechaFinal:
                        resp["medida"+str(y)] = item
                        y += 1
                    
            elif event['fechainicial'] == x and event['fechafinal'] == x:
                for item in response['Items']:
                    resp['medida'+str(y)] = item
                    y += 1
                    
            elif event['fechainicial'] != x and event['fechafinal'] == x:
                fechaInicial = date.fromisoformat(event['fechainicial'])
                for item in response['Items']:
                    if date.fromisoformat(item['timestamp']['fecha']) > fechaInicial:
                        resp["medida"+str(y)] = item
                        y += 1
                        
            elif event['fechainicial'] == x and event['fechafinal'] != x:
                fechaFinal = date.fromisoformat(event['fechafinal'])
                for item in response['Items']:
                    if date.fromisoformat(item['timestamp']['fecha']) < fechaFinal:
                        resp["medida"+str(y)] = item
                        y += 1
                        
        else: 
            response = table.scan()
            if event['fechainicial'] != x and event['fechafinal'] != x:
                fechaInicial = date.fromisoformat(event['fechainicial'])
                fechaFinal = date.fromisoformat(event['fechafinal'])
                for item in response['Items']:
                    if date.fromisoformat(item['timestamp']['fecha']) > fechaInicial and date.fromisoformat(item['timestamp']['fecha']) < fechaFinal:
                        resp["medida"+str(y)] = item
                        y += 1
                        
            elif event['fechainicial'] != x and event['fechafinal'] == x:
                fechaInicial = date.fromisoformat(event['fechainicial'])
                for item in response['Items']:
                    if date.fromisoformat(item['timestamp']['fecha']) > fechaInicial:
                        resp["medida"+str(y)] = item
                        y += 1
                        
            elif event['fechainicial'] == x and event['fechafinal'] != x:
                fechaFinal = date.fromisoformat(event['fechafinal'])
                for item in response['Items']:
                    if date.fromisoformat(item['timestamp']['fecha']) < fechaFinal:
                        resp["medida"+str(y)] = item
                        y += 1
              
    except ValueError:
        resp = {"Error de formato": "La fecha debe ser ingresada con el formato AAAA-MM-DD"}
    
    return vacio(resp)

