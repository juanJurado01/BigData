#importamos las librerias necesarias
import json
import boto3
import datetime
from app import lambda_handler1
from appcsv import lambda_handler2

#llamamos las dos funciones para que se ejecuten al mismo tiempo
def lambda_handler(event, contex):
    lambda_handler1()
    lambda_handler2()
