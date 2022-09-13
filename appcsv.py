#Juan Jurado
#importamos las librerias necesarias
import json
import boto3
import datetime
import csv 
import pandas as pd

def lambda_handler2():
    #TODO implement
    #Utilizamos la funcion datatime para agregarle al nombre del archivo la fecha de hoy
    now2= datetime.datetime.now()
    #con la funcion strftime convertimos el dato de la fecha en un string 
    x2 = now2.strftime('%d %m %Y')
    
    s3 = boto3.resource('s3')
    #Con download_file descargamos el archivo txt que se encuentra en el s3
    s3.Bucket('dolarraw12').download_file('dolar '+ x2 + '.txt', '/tmp/dolar.txt')
    
    websites = pd.read_csv('dolar '+ x2 + '.txt',header = None) #leemos el archivo txt
    websites.columns = ['FechaHora', 'Valor'] #Agregamos lo nombres de las columnas al csv
    websites.to_csv('dolar_processed_ '+ x2 + '.csv', index = None) #generamos el archivo de texto como un archivo de tipo csv
    
    #Mediante la libreria boto3 le agregamos el bucket con la variable s3
    client= boto3.client("s3","us-east-1")
    s3= boto3.resource('s3')
    bucket = s3.Bucket('dolarprocessed12')

    client.put_object(Body='dolar '+ x2 + '.txt', Bucket='dolarprocessed12', Key ='dolar_processed_ '+ x2 + '.csv')

    #mensaje de retorno para validar que el codigo se ejecuto de manera satisfactoria
    return{
        'statusCode':200,
        'body': json.dumps('Hola mundo!')
    }
