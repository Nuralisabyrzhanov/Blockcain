import sqlite3
import json
from main import bloks_dir

db = sqlite3.connect('blokchain.db')
cursor = db.cursor()
filename = 1
total = 3
file = filename =+ 1
data = json.load(open(f'./bloks/{file}'))

columns = ['creditor','money','borrower']
for i in columns:
    creditor = data['creditor']
    money = data['money']
    borrower = data ['borrower']
    cursor.execute(f'''INSERT INTO blokchain(creditor,money,borrower) values (?,?,?)''',[creditor,money,borrower])






# cursor.execute('''Create table blokchain
#                  (id PRIMARY KEY,
#                  creditor VARCHAR,
#                  money INTEGER,
#                  borrower VARCHAR)''')


cursor.commit()
cursor.close()

# def tiger()
