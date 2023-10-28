import sqlite3


def get_total(ids, qtys):
    total = 0
    for i in range(len(ids)):
        data = get_products(ids[i])
        if data == []:
            return 0
        total += int(data[0][2]) * int(qtys[i])
    return total


def buy(ids, qty):
    with sqlite3.connect("database.sqlite") as conn:
        conn.row_factory = lambda c, r: dict(
            zip([col[0] for col in c.description], r))
        cursor = conn.cursor()
        for i in range(len(ids)):
            cursor.execute(
                "UPDATE products SET stock=stock-? WHERE id=?", (qty[i], ids[i]))
        conn.commit()


def get_products(id=None):
    try:
        with sqlite3.connect("database.sqlite") as conn:
            conn.row_factory = lambda c, r: dict(
                zip([col[0] for col in c.description], r))
            cursor = conn.cursor()
            if id:
                cursor.execute("SELECT * FROM products WHERE id=?", (id,))
            else:
                cursor.execute("SELECT * FROM products")
            results = cursor.fetchall()
            # results = [tuple(row) for row in results]
            return results
    except Exception as e:
        print(e)
        return []


def add_product(name, price, stock):
    with sqlite3.connect("database.sqlite") as conn:
        conn.row_factory = lambda c, r: dict(
            zip([col[0] for col in c.description], r))
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, stock) VALUES (?,?,?)", (name, price, stock))
        conn.commit()
        return cursor.lastrowid


def update_product(id, name, price, stock):
    with sqlite3.connect("database.sqlite") as conn:
        conn.row_factory = lambda c, r: dict(
            zip([col[0] for col in c.description], r))
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET name=?, price=?, stock=? WHERE id=?", (name, price, stock, id))
        conn.commit()
        return cursor.lastrowid


def delete_product(id):
    with sqlite3.connect("database.sqlite") as conn:
        conn.row_factory = lambda c, r: dict(
            zip([col[0] for col in c.description], r))
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=?", (id,))
        conn.commit()
        return cursor.lastrowid
