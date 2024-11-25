import sqlite3
from db import queries
import aiosqlite

db = sqlite3.connect('db/store.sqlite3.db')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена!')
        cursor.execute(queries.CREATE_TABLE_product_details)
        cursor.execute(queries.CREATE_TABLE_collection_products)


async def sql_insert_store_to_product_details(productid, category, infoproduct):
    cursor.execute(
        queries.INSERT_product_details,
        (productid, category, infoproduct)
    )
    db.commit()

async def sql_insert_store_to_collection_products(productid, collection):
    cursor.execute(
        queries.INSERT_collection_products,
        (productid, collection)
    )
    db.commit()

def get_db_connection():
    conn = sqlite3.connect('C:/Users/nuris/html/HomeWORKS3moonth/db/store.sqlite3.db')
    conn.row_factory = sqlite3.Row
    return conn
def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
        SELECT * FROM collection_products
        INNER JOIN product_details sd ON collection_products.productid = sd.productid
        """).fetchall()
    conn.close()
    return products


def delete_product(product_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM STORE WHERE product_id = ?', (product_id,))
    conn.commit()
    conn.close()