import MySQLdb

db = MySQLdb.connect(host = '210.119.12.52', \
                     user = 'test_usr', \
                     passwd = 'mysql_p@ssw0rd', \
                     db = 'shopdb', \
                     charset = 'utf8')
cur = db.cursor()
cur.execute('select * from producttbl')

while True:
    product = cur.fetchone()
    if not product:
        break
    
    print(product)

cur.close()
db.close()