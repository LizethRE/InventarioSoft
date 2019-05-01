import mysql.connector
from mysql.connector import errorcode

class DBConn:
    def __init__(self, db_host='arquitecturabd.mysql.database.azure.com', db_user='estudiante@arquitecturabd', db_pass='estudiantepswd', db_name='inventario'):
        self.db_host= db_host
        self.db_user= db_user
        self.db_pass= db_pass
        self.db_name= db_name

    def connect(self):
        self.db= mysql.connector.connect(host=self.db_host, user=self.db_user,
                                        passwd=self.db_pass, db=self.db_name)

    def openCursor(self):
        self.cursor = self.db.cursor()

    def executeQuery(self, query, values=''):
        if values != '':
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

    def getData(self):
        self.rows = self.cursor.fetchall()

    def sendCommit(self, query):
        sql = query.lower()
        es_lectura = sql.count('select')
        if es_lectura < 1:
            self.db.commit()

    def closeCursor(self):
        self.cursor.close()

    def execute(self, query, values='', response=False):
        if (self.db_host and self.db_user and self.db_pass and self.db_name and
            query):
            try:
                self.connect()
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with the user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
            else:
                self.openCursor()
                self.executeQuery(query, values)
                self.sendCommit(query)
                if response:
                    self.getData()
                    self.closeCursor()
                    return self.rows
                else:
                    self.closeCursor()
                    return 'complete..'
