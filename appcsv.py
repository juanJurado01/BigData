#Juan Jurado
#importamos las librerias necesarias
import json
import boto3
import datetime
import csv 

def lambda_handler2():
    #TODO implement
    # Se importa la funcion date time para sacar la fecha y poderla agregar al nombre del archivo txt
    now2= datetime.datetime.now()
    #se llama la funcion strtime para convertir la funcion datetime a string 
    x2 = now2.strftime('%d %m %Y')
    
    s3 = boto3.resource('s3')
    s3.Bucket('dolarraw12').download_file('dolar '+ x2 + '.txt', '/tmp/dolar.txt')
    
    #with open('dolar '+ x2 + '.txt','r',encoding = "utf-8") as a:
    #    for line in a:
    #        print(line)
    
    
    client= boto3.client("s3","us-east-1")
    s3= boto3.resource('s3')
    bucket = s3.Bucket('dolarprocessed12')

    client.put_object(Body='dolarraw12', Bucket='dolarprocessed12', Key ='dolar_processed_ '+ x2 + '.csv')

    return{
        'statusCode':200,
        'body': json.dumps('Hello from Lambda!')
    }
