# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fwYA53hEowMOT1DWCeCGU7lQ7LE7w4R9
"""

#09-08-2023
#Jamith Bolaños Vidal
#Script para conectarse a base de datos MySQL obtener los datos e insertar y actualizar datos
#Prueba DA Jikkisoft.
#!pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

def connect():
    """Establece la conexión con la base de datos y retorna el objeto conexión"""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',        # DB_HOST
            port=3306,               # DB_PORT
            database='academic_db',  # DB_DATABASE
            user='root',             # DB_USERNAME
            password='Ak4d3Mi1C0.'              # DB_PASSWORD
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def fetch_data(connection):
    """Recupera y muestra datos de una tabla"""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cursos")
        records = cursor.fetchall()
        print("Datos recuperados:")
        for row in records:
            print(row)
    except Error as e:
        print(f"Error al recuperar datos: {e}")
    finally:
        if cursor:
            cursor.close()

def insert_data(connection, data):
    """Inserta un nuevo registro en la tabla"""
    try:
        cursor = connection.cursor()
        query = "INSERT INTO cursos (nombre_curso, grupo) VALUES (%s, %s)"
        cursor.execute(query, data)
        connection.commit()
        print("Datos insertados correctamente")
    except Error as e:
        print(f"Error al insertar datos: {e}")
        connection.rollback()
    finally:
        if cursor:
            cursor.close()

def update_data(connection, data):
    """Actualiza un registro existente en la tabla"""
    try:
        cursor = connection.cursor()
        query = "UPDATE cursos SET nombre_curso = %s WHERE nombre_curso = %s"
        cursor.execute(query, data)
        connection.commit()
        print("Datos actualizados correctamente")
    except Error as e:
        print(f"Error al actualizar datos: {e}")
        connection.rollback()
    finally:
        if cursor:
            cursor.close()

def main():
    connection = connect()
    if connection:
        # Recuperar datos
        fetch_data(connection)

        # Insertar nuevos datos
        data_to_insert = ('Primero', 'C')
        insert_data(connection, data_to_insert)

        # Actualizar datos existentes
        data_to_update = ('1', 'Primero')
        update_data(connection, data_to_update)

        # Cerrar la conexión
        connection.close()
        print("Conexión cerrada")

if __name__ == "__main__":
    main()