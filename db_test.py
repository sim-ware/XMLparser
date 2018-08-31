import sqlite3


conn = sqlite3.connect('perlego.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE bookSalesRights
             (filename text, recordReference real, salesRightsType real, territory text)''')

a = {'recordReference': '9785555555556',
     'territory': 'GB IE DE FR DK US CA',
     'salesRightsType': '01',
     'fileName': '2.xml'}

c.execute("insert into bookSalesRights (filename, recordReference, salesRightsType, territory) values (?, ?, ?, ?)",
            (a['fileName'], a['recordReference'], a['salesRightsType'], a['territory']))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


# View info in DB
conn = sqlite3.connect('perlego.db')
cur = conn.cursor()
cur.execute("SELECT * FROM bookSalesRights")

rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
