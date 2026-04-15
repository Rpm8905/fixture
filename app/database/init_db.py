import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def inicializar_base_de_datos():
    # Primero conecta sin especificar la base de datos
    conexion  = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = conexion.cursor()

    # Lee y ejecuta el archivo SQL
    with open("app/database/init_db.sql") as archivo_sql:
        contenido_sql = archivo_sql.read()

    for sentencia in contenido_sql.split(";"):
        sentencia_limpia = sentencia.strip()
        if sentencia_limpia:
            cursor.execute(sentencia_limpia)
            conexion.commit()

    cursor.close()
    conexion.close()
    print("Base de datos inicializada correctamente")

if __name__ == "__main__":
    inicializar_base_de_datos()