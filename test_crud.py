import pytest
from postgres_sdk.crud import create_table, insert_row, read_table, update, delete

TABLE = "users"

def test_setup_table():
    # Ensure users table exists before running CRUD tests
    result = create_table()
    assert "ready" in result

def test_insert():
    result = insert_row(TABLE, {"name": "Saksham Ji", "age": 20})
    assert "Inserted" in result

def test_read():
    rows = read_table(TABLE, {"name": "Saksham Ji"})
    assert isinstance(rows, list)
    assert any("Saksham Ji" in row for row in rows)

def test_update():
    result = update(TABLE, {"age": 22}, {"name": "Saksham Ji"})
    assert "updated" in result
    rows = read_table(TABLE, {"name": "Saksham Ji"})
    assert rows[0][2] == 22  # assuming (id, name, age)

def test_delete():
    result = delete(TABLE, {"name": "Saksham Ji"})
    assert "deleted" in result
    rows = read_table(TABLE, {"name": "Saksham Ji"})
    assert rows == []
