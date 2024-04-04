from pymongo import MongoClient
import certifi

certificado = certifi.where()

MONGO ='mongodb+srv://juliana:ucundinamarca@cluster0.kd118a2.mongodb.net/'


def Conexion():
    try:
        client =  MongoClient(MONGO, tlsCAFile=certificado)
        bd = client["bd_personas"]
        print("Conexion Exitosa")
    except ConnectionError:
       print("Error de Conexion")
    return bd

Conexion()