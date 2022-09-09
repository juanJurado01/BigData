#importamos las librerias necesarias
import csv
import boto3
import pandas as pd
#Jyuan Jurado
#Creacion de la funcion que hace la conversion del archivo txt a cvs
def lambda_handler2(event, context):
    s3 = boto3.resource('s3') #utilizamos boto3 para poder mandarle informacion al bucket
    out = open('dolar-timestamp.csv', 'w', newline='') #abrimos el archvo csv y con w lo escribimos
    csv_writer = csv.writer(out, dialect='excel') #escribimos sobre el archivo csv
    f = open("https://dolarraw01.s3.amazonaws.com/dolar-timestamp.txt", "r")
    #Se crean las columnas del cvs
    websites = pd.read_csv("dolar-timestamp.txt", header=None)
    websites.columns = ['Fecha Hora', 'Valor'] #Asignamos el valor o nombre a cada columna
    websites.to_csv('dolar-timestamp.csv',index=None)
    for line in f.readlines():
        line = line.replace(',', '\ t')  # Reemplaza la coma de cada línea con un espacio
        list = line.split()  # Convierta la cadena en una lista, para que pueda escribir csv
    csv_writer.writerow(list)
    data = open('dolar-timestamp.csv', 'rb')
    s3.Bucket('ddolarprocessed11').put_object(Key='dolar-timestamp.txt', Body=data)