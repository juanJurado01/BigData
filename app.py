#importamos las librerias necesarias
import json
import urllib3
import boto3
#Juan Jurado
#Creacion de la funcion que hace el scraping de la pagina del banco de la republica
#y lo guarda en un archivo txt llamado dolar-timestamp.txt

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    http = urllib3.PoolManager()
    #Declaramos la ruta de la pagina donde traeremos los archivos
    url = 'https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario'

    resp = http.request('GET', url)
    archivo = open("dolar-timestamp.txt", "w") #con el metodo open le damos el archivo que queremos abrir y con la w lo escribimos
    archivo.write(print(resp.data.decode('utf -8')))

    archivo.close() #funcion para cerrar el archivo modificado
    #se usa boto3 para subir el archivo a el bucket
    data = open('dolar-timestamp.txt', 'rb')
    s3.Bucket('dolarraw01').put_object(Key='dolar-timestamp.txt', Body=data)