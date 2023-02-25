from classes.DbMongo import *
from classes.Producto import *
class Tienda:
    def __init__(self, nombre, categoria, id=""):
        self.nombre = nombre
        self.categoria = categoria
        self.__id =id
        self.__collection = "tienda"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id


    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def get_one(db, id):
        collection = db["tienda"]
        filterToUse = { '_id' : id }
        result = collection.find_one(filterToUse)

        return Tienda(result["nombre"], result["_id"])
    
     @staticmethod
    def get_list(db):
        collection = db["tienda"]
        tipos = collection.find()

        list_tienda = []
        for e in tipos:
            temp_tipo = Tienda(
                e["nombre"]
                , e["_id"] 
            )

            list_tienda.append(temp_tipo)
        return list_tienda
    
    @staticmethod
    def get_dict(db):
        collection = db["tienda"]
        tipos = collection.find()

        dict_tienda = {}
        for e in tipos:
            dict_tienda[e["nombre"]] = e["_id"] 

        return dict_tienda
    
    @staticmethod
    def delete_all(db):
        lista_e = Tienda.get_list(db)
        for e in lista_e:
            e.delete(db)