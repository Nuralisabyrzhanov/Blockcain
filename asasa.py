import sqlite3
import json
from main import bloks_dir

#DATABASE

db = sqlite3.connect('blockchain.db')

cursor = db.cursor()

# cursor.execute('''Create table blockchain
#         (id PRIMARY KEY,
#         creditor VARCHAR,
#         money INTEGER,
#         borrower VARCHAR
#                 )''')


# JSON

filename = 1
total = 3
data = json.load(open('./bloks/3'))
if data :
    total =+ 1

columns = ['creditor','money','borrower']
for i in columns :
    creditor = data['creditor']
    money = data['money']
    borrower = data['borrower']
    # cursor.execute(f'''INSERT INTO blockchain (creditor,money,borrower) values(?,?,?)''',[creditor,creditor,borrower])
    db.commit()

# cursor.execute('''SELECT * FROM blockchain''')
record = cursor.fetchall()
print(record)
db.commit()
db.close()
import sqlite3
import json
from main import bloks_dir

#DATABASE

db = sqlite3.connect('blockchain.db')

cursor = db.cursor()
#
# cursor.execute('''Create table blockchain
#         (id PRIMARY KEY,
#         creditor VARCHAR,
#         money INTEGER,
#         borrower VARCHAR
#                 )''')


# JSON

filename = 1
total = 3
data = json.load(open('./bloks/2'))
if data :
    total =+ 1

columns = ['creditor','money','borrower']
for i in columns :
    creditor = data['creditor']
    money = data['money']
    borrower = data['borrower']
    # cursor.execute(f'''INSERT INTO blockchain (creditor,money,borrower) values(?,?,?)''',[creditor,creditor,borrower])
    db.commit()

cursor.execute('''SELECT * FROM blockchain''')
record = cursor.fetchall()
print(record)
db.commit()
db.close()
import sqlite3
import json
from main import bloks_dir

#DATABASE

db = sqlite3.connect('blockchain.db')

cursor = db.cursor()

# cursor.execute('''Create table blockchain
#         (id PRIMARY KEY,
#         creditor VARCHAR,
#         money INTEGER,
#         borrower VARCHAR
#                 )''')


# JSON

filename = 1
total = 3
data = json.load(open('./bloks/2'))
if data :
    total =+ 1

columns = ['creditor','money','borrower']
for i in columns :
    creditor = data['creditor']
    money = data['money']
    borrower = data['borrower']
    cursor.execute(f'''INSERT INTO blockchain (creditor,money,borrower) values(?,?,?)''',[creditor,creditor,borrower])
    db.commit()

# cursor.execute('''SELECT * FROM blockchain''')
record = cursor.fetchall()
print(record)
db.commit()
db.close()