from classes.DbMongo import *

class Producto: 
    def __init__(self, nombre, unidades, tienda):
        self.nombre = nombre
        self.unidades = unidades
        self.tienda = tienda
        self.__collection = "productos"

    def save(self,db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id
    