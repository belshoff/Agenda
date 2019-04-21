import sqlite3

with sqlite3.connect('storage.db') as conn:
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Produtos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL,
            compra_id INTEGER,
            FOREIGN KEY (compra_id) REFERENCES Compras(id)
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Compras (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL
        );
        """
    )

class Produto(object):
    def getAll(self):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Produtos;")
            return [
                {
                    "id": items[0],
                    "name": items[1],
                    "price": items[2],
                    "compra_id": items[3]
                } for items in cursor.fetchall()
            ]

    def getByCompra(self, compraId):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            print(f"SELECT * FROM Produtos WHERE compra_id = {compraId}")
            cursor.execute(f"SELECT * FROM Produtos WHERE compra_id = {compraId}")
            return [
                {
                    "id": items[0],
                    "name": items[1],
                    "price": items[2],
                } for items in cursor.fetchall()
            ]

    def insert(self, *args):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            print(f"INSERT INTO Produtos (name, price, compra_id) VALUES ('{args[0]}', {args[1]}, {args[2]})")
            cursor.execute(f"INSERT INTO Produtos (name, price, compra_id) VALUES ('{args[0]}', {args[1]}, {args[2]})")

    def getById(self, id):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Produtos WHERE id = {id} ;")
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
            cursor.execute(f"UPDATE Produtos SET name = {args[0]}, price = {args[1]}, compra_id = {args[2]} WHERE id = {id};")

    def delete(self, id):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM Produtos WHERE id = {id}")

class Compra(object):
    def __init__(self):
        self.produto = Produto()

    def getAll(self):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            print("SELECT * FROM Compras;")
            cursor.execute("SELECT * FROM Compras;")
            return [
                {
                    "id": items[0],
                    "date": items[1],
                    "produtos": self.produto.getByCompra(items[0])
                } for items in cursor.fetchall()
            ]

    def insert(self, *args):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            print(f"INSERT INTO Compras (date) VALUES ('{args[0]}')")
            cursor.execute(f"INSERT INTO Compras (date) VALUES ('{args[0]}')")
        c = self.getAll()[-1]
        ps = list(args[1])
        for p in ps:
            self.produto.insert(str(p["name"]), p["price"], c["id"])
        # return self.getById(c.id)

    def getById(self, id):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Compras WHERE id = {id} ;")
            return [
                {
                    "id": items[0],
                    "date": items[1],
                    "produtos": self.produto.getByCompra(id)
                } for items in cursor.fetchall()
            ][0]

    def getByDate(self, date):
        with sqlite3.connect('storage.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM Compras WHERE date = '{date}' ;")
            return [
                {
                    "id": items[0],
                    "date": items[1],
                    "produtos": self.produto.getByCompra(items[0])
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