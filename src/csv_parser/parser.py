import sqlite3
import csv
import os


def parse(file_path):
    with open('.testfiles/test.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

def db_inject(schema, data=""):
    with sqlite3.connect('data.db') as con:
        cursor = con.cursor()
        columns_with_types = [f"{col_name} {constraints}" for col_name, constraints in schema.items()]
        attributes = ', '.join(columns_with_types)
        cursor.execute(f'CREATE TABLE message({attributes})')
        placeholders = ', '.join(['?'] * len(schema))
        cursor.execute(f'INSERT INTO message VALUES ({placeholders})', data)
        print('injection successful')
        print('table contents:')
        statement = '''SELECT * FROM message'''
        cursor.execute(statement)
        output = cursor.fetchall()
        for i in output:
            print(i)
    con.close()

if os.path.exists('data.db'):
    os.remove('data.db')

table_schema = {
    'id': 'INTEGER PRIMARY KEY',  
    'date': 'DATETIME NOT NULL',      
    'message': 'TEXT NOT NULL'             
}

row_to_insert = (1, '2026-01-01', 'első üzenet')


db_inject(table_schema, row_to_insert)
