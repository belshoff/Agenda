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
                    "produtoId": items[2]
                } for items in cursor.fetchall()
            ]

    def insert(self, *args):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Compras (date, produto_id) VALUES (?, ?)
                """, (*args, )
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
                    "produtoId": items[2]
                } for items in cursor.fetchall()
            ][0]

    def update(self, id, *args):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Compras
                SET date = ?, produtoId = ?
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