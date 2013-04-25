import sqlite3, sys

conn = sqlite3.connect('f:/py/food.db')
curs = conn.cursor()

#query = 'select * from food where %s % sys.argv[1]
query = 'select * from food where kcal <= 100 and fiber >=10 order by sugar'
print query
curs.execute(query)
name = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print '%s: %s' % pair
    print
