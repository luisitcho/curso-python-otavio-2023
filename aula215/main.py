import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_PATH = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Fazendo DELETE sem WHERE
cursor.execute(  # Apagando os registros da tabela
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(  # Reseta o contador de IDs
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela se não existir
cursor.execute(
    f'''CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight TEXT
    )'''
)
connection.commit()

# ✅ AJUSTE: use apenas um par de placeholders (?, ?) no SQL
sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'

# ✅ AJUSTE: forneça uma lista de tuplas para o executemany
data = [("Luisitchou", 74), ("Peppa", 1200), ("Toddy", 10)]

# ✅ AJUSTE: agora está correto com executemany
cursor.executemany(sql, data)
connection.commit()

cursor.close()
connection.close()
