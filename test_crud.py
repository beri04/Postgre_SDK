import pytest
import psycopg2

from postgres_sdk.crud import create_table, insert_row, read_table, update, delete

TABLE = "users"


class DummyCursor:
    def __init__(self):
        self.data = {}
        self.last_result = []
        self.auto_id = 1
        self.description = []

    def execute(self, query, params=None):
        query = query.lower()
        if query.startswith("insert"):
            self.data[self.auto_id] = params
            self.auto_id += 1

        elif query.startswith("select"):
            results = []
            for row_id, row_data in self.data.items():
                if all(row_data.get(k) == v for k, v in params.items()):
                    results.append((row_id, row_data))
            self.last_result = results

        elif query.startswith("update"):
            age, name = params 

            for row_id, row_data in self.data.items():
                if row_data.get("name") == name:
                    row_data["age"] = age

        elif query.startswith("delete"):
            to_delete = []
            for row_id, row_data in self.data.items():
                if all(row_data.get(k) == v for k, v in params.items()):
                    to_delete.append(row_id)
            for row_id in to_delete:
                del self.data[row_id]

    def fetchone(self):
        if self.last_result:
            return self.last_result[0]
        return ()

    def close(self):
        pass
    
    def fetchall(self):
        return self.last_result if self.last_result else [] 

class DummyConnection:
    def cursor(self):
        return DummyCursor()
    def commit(self):
        pass
    def close(self):
        pass
    

        

def test_setup_table(monkeypatch):
    monkeypatch.setattr(psycopg2,'connect',lambda *args, **kwargs:DummyConnection())
    result = create_table()
    assert "ready" in result

def test_insert(monkeypatch):
    monkeypatch.setattr(psycopg2,'connect',lambda *args,**kwargs:DummyConnection())
    result = insert_row(TABLE, {"name": "Saksham Ji", "age": 20})
    assert "Inserted" in result

# def test_read(monkeypatch):
#     monkeypatch.setattr(psycopg2,'connect',lambda *args,**kwargs:DummyConnection())
#     rows = read_table(TABLE, {"name": "Saksham Ji"})
#     assert isinstance(rows, list)
#     assert any(row_data.get("name") == "Saksham Ji" for _, row_data in rows)

# def test_update(monkeypatch):
#     monkeypatch.setattr(psycopg2,'connect',lambda *args,**kwargs:DummyConnection())
#     result = update(TABLE, {"age": 22}, {"name": "Saksham Ji"})
#     assert "updated" in result
#     rows = read_table(TABLE, {"name": "Saksham Ji"})
#     assert rows[0][1]["age"] == 22

# def test_delete(monkeypatch):
#     monkeypatch.setattr(psycopg2,'connect',lambda *args,**kwargs:DummyConnection())
#     result = delete(TABLE, {"name": "Saksham Ji"})
#     assert "deleted" in result
#     rows = read_table(TABLE, {"name": "Saksham Ji"})
#     assert rows == None