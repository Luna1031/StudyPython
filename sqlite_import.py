from sys import argv
import csv
import sqlite3

conn = sqlite3.connect('sample.db')
c = conn.cursor()

if len(argv) < 2: # 아규먼트 에러
    print("Error")
    exit(1)
else: # 정상실행
    csvfile = argv[1]
    print(csvfile)
    c.execute('CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY AUTOINCREMENT, \
        name TEXT, birth DATE, gender CHAR)')
    student = csv.reader(open(csvfile, 'r'), delimiter = ',', quotechar = '"')

    for row in student:
        print('{}'.format(row)) # print('%s' % (row))  
        c.execute('INSERT INTO student (name, birth, gender) VALUES (?, ?, ?)', \
            (row[0], row[1], row[2]))

    conn.commit()
    conn.close()
    exit(0)