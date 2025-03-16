
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_PATH = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.close()
connection.close()
