from PyQt5 import QtSql

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('data.sqlite')

if not db.open():
    print('Error')

query = QtSql.QSqlQuery()
query.exec_('create table userdata (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL);')
query.exec_('insert into userdata (username, password) values ("User", "12345");')

query.exec_('select * from userdata where id=1')
query.first()
print(query.value('username'), query.value('password'))