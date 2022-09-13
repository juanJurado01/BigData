#Juan Jurado
#importamos las librerias necesarias
import json
import boto3
import datetime

def lambda_handler1():
    #TODO implement
    # Se importa la funcion date time para sacar la fecha y poderla agregar al nombre del archivo txt
    now= datetime.datetime.now()
    #se llama la funcion strtime para convertir la funcion datetime a string 
    x = now.strftime('%d %m %Y')
    
    import urllib3
    #Realizamos el scraping de la pagina del banco de la republica 
    http= urllib3.PoolManager()

    url= 'https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario'

    resp= http.request('GET', url)
    print(resp.data.decode('utf-8'))
    #Se inicia a subir el archivo con la libreria boto3 al bucket con nombre dolarraw01 
    client= boto3.client("s3","us-east-1")
    s3= boto3.resource('s3')
    bucket = s3.Bucket('dolarraw12')

    client.put_object(Body=resp.data.decode('utf-8'), Bucket='dolarraw12', Key ='dolar '+ x + '.txt')

    return{
        'statusCode':200,
        'body': json.dumps('Hola Mundo')
    }
