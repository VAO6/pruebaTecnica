import json

def vacio(resp):
        if resp:
            return resp
        else:
            return {"message": 'No hubo coincidencias en la busqueda'}

            