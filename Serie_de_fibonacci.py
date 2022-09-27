import sqlite3
import pandas as pd

file="register_requests.db"

connection = sqlite3.connect(file)
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS register (Numero integer PRIMARY KEY, Serie text NOT NULL)')
connection.commit()
connection.close()

def serie_fibonacci(limite:int=None):
    if limite<0:
        return ("Ingrese numeros positivos")
    serie=[0,1]
    for i in range(0,limite):
        new_element=sum(serie[-2:])
        serie.append(new_element)
    
    records(limite,serie[1:])

    return(serie[1:])

def records(num:int=None,serie:list=None,save:bool=True):

    connection = sqlite3.connect(file)
    cursor = connection.cursor()
    if save:
        query=f'INSERT INTO register VALUES ("{num}","{serie}")'
    else:
        query=f'DELETE From register Where Numero = {num}'

    print(query)

    cursor.execute(query)
    connection.commit()
    connection.close()
    
    return None
