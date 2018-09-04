import sqlite3


class DBHandler:
    def __init__(self, filepath):
        self.conn = sqlite3.connect(filepath)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE bookSalesRights
                     (filename text, recordReference integer, salesRightsType integer, territory text)''')


    def create_row(self, filename, recordReference, salesRightsType, territory):
        self.cursor.execute("insert into bookSalesRights (filename, recordReference, salesRightsType, territory) values (?, ?, ?, ?)",
                    (filename, recordReference, salesRightsType, territory))


    def commit_changes(self):
        self.conn.commit()


    def close_connection(self):
        self.conn.close()
