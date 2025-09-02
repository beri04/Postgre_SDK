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


# 📂 Project Structure
```bash

Postgre_SDK/
│── .github/
│   └── workflows/
│       └── test.yml         # GitHub Actions workflow
│
│── postgres_sdk/
│   ├── __init__.py          # Package initializer
│   ├── crud.py              # CRUD operations
│   ├── db.py                # Database connection handler
│
│── tests/
│   └── test_crud.py         # Unit tests with pytest
│
│── .env                     # Local environment variables (not committed)
│── .env.example             # Example environment file
│── requirements.txt         # Python dependencies
│── LICENSE                  # License file
│── README.md                # Project documentation
│── .gitignore               # Git ignore rules
```


# 🧪 Running Tests
Run all tests with: pytest


# 🤝 Contributing

Contributions are welcome! 🎉

If you’d like to improve this SDK:

- Fork the repository
- Create a new branch (git checkout -b feature-name)
- Commit your changes (git commit -m "Add new feature")
- Push to your branch (git push origin feature-name)
- Open a Pull Request
- Please make sure your code passes all tests (pytest) before submitting.


# 📜 License
This project is licensed under the MIT License.