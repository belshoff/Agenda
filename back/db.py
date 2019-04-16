import sqlite3

with sqlite3.connect('storage.db') as conn:
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Produtos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL 
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Compras (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            produto_id INTEGER,
            FOREIGN KEY (produto_id) REFERENCES Produtos(id)
        );
        """
    )

class Produto(object):
    def getAll(self):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    SELECT * FROM Produtos;
                """
            )
            return [
                {
                    "id": items[0],
                    "name": items[1],
                    "price": items[2]
                } for items in cursor.fetchall()
            ]

    def insert(self, *args):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Produtos (name, price) VALUES (?, ?)
                """, (*args, )
            )

    def getById(self, id):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    SELECT * FROM Produtos WHERE id = ? ;
                """, (id, )
            )
            return [
                {
                    "id": items[0],
                    "name": items[1],
                    "price": items[2]
                } for items in cursor.fetchall()
            ][0]

    def update(self, id, *args):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Produtos
                SET name = ?, price = ?
                WHERE id = ?;
                """, (*args, id)
            )

    def delete(self, id):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                DELETE FROM Produtos WHERE id = ?
                """, (id, )
            )

class Compra(object):
    def __init__(self):
        self.produto = Produto()

    def getAll(self):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    SELECT * FROM Compras;
                """
            )
            return [
                {
                    "id": items[0],
                    "date": items[1],
                    "produto": self.produto.getById(items[2])
                } for items in cursor.fetchall()
            ]

    def insert(self, *args):
        self.produto.insert(args[1]['name'], args[1]['price'])
        produto = self.produto.getAll()[-1]
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Compras (date, produto_id) VALUES (?, ?)
                """, (args[0], produto['id'])
            )

    def getById(self, id):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    SELECT * FROM Compras WHERE id = ? ;
                """, (id, )
            )
            return [
                {
                    "id": items[0],
                    "date": items[1],
                    "produto": self.produto.getById(items[2])
                } for items in cursor.fetchall()
            ][0]

    def getByDate(self, date):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                    SELECT * FROM Compras WHERE date = ? ;
                """, (date, )
            )
            return [
                {
                    "id": items[0],
                    "date": items[1],
                    "produto": self.produto.getById(items[2])
                } for items in cursor.fetchall()
            ]

    def update(self, id, *args):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Compras
                SET date = ?, produto_id = ?
                WHERE id = ?;
                """, (*args, id)
            )

    def delete(self, id):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                DELETE FROM Compras WHERE id = ?
                """, (id, )
            )