# SDK for PostgreSQL
[![Run tests](https://github.com/beri04/Postgre_SDK/actions/workflows/test.yml/badge.svg)](https://github.com/beri04/Postgre_SDK/actions/workflows/test.yml)

A lightweight Python SDK to interact with PostgreSQL databases.

It provides simple methods to:
- Create tables
- Insert rows
- Update existing values
- Delete records


# ☑️ Installation

```bash 
git clone https://github.com/beri04/Postgre_SDK.git
cd Postgre_SDK
pip install -r requirements.txt

```python 
from postgres_sdk.crud import create_table, insert_row, update_row, delete_row

# Create a table
create_table()

# Insert a row
insert_row("students", {"name": "Saksham", "age": 20})

# Update a row
update_row("students", {"age": 21}, "name = 'Saksham'")

# Delete a row
delete_row("students", "name = 'Saksham'")
```

# 🧪 Running Tests
Run all tests with:
pytest


# 📜 License
This project is licensed under the MIT License.