from classes import Categoria,  DbMongo, Tienda, Producto
from dotenv import load_dotenv


def main():
    client, db = DbMongo.getDB()
#
# Producto("nombre").save(db)
#  Producto("cantidad").save(db)
#   Producto("tienda_id").save(db)
#
Producto("carne", "15")

Tienda("superTech")

if __name__ == "__main__":
    load_dotenv()
    main()