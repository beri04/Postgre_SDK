from .db import Database


def create_table():
    db = Database()
    query = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT
    );
    """
    db.execute_query(query)
    db.close()
    return "Users table ready"


def insert_row(table,data):
    db = Database()
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["%s"] * len(data))
    values = tuple(data.values())


    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    db.execute_query(query,values)
    db.close()
    return f"Inserted in {table}"


def read_table(table,conditions = None):
    db = Database()

    query = f"SELECT * FROM {table}"
    values = None


    if conditions:
        condition_str = " AND ".join([f"{col}=%s" for col in conditions.keys()])
        values = tuple(conditions.values())
        query += f" WHERE {condition_str}"


    result = db.execute_query(query,values)
    db.close()
    return result   

def update(table, data, conditions):
    db = Database()
    set_str = ", ".join([f"{col}=%s" for col in data.keys()])
    values = tuple(data.values())

    conditions_str = " AND ".join([f"{col}=%s" for col in conditions.keys()])
    condition_values = tuple(conditions.values())

    query = f"UPDATE {table} SET {set_str} WHERE {conditions_str};"
    db.execute_query(query, values + condition_values)
    db.close()
    return f"Record updated in {table}"


def delete(table,conditions):
    db = Database()

    conditions_str = " AND ".join([f"{col}=%s" for col in conditions.keys()])
    conditions_values = tuple(conditions.values())

    query = f"DELETE FROM {table} where {conditions_str};"

    db.execute_query(query,conditions_values)
    db.close()
    return f"Record deleted from {table}"