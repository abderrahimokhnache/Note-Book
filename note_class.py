import sqlite3

class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect("data/Notes.db")
		self._db.row_factory = sqlite3.Row
		self._db.execute("create table if not exists Notes(ID integer primary key autoincrement,title text ,Note text , time date)")
		self._db.commit()
	def Add(self,title , Note , time):
		self._db.execute('insert into Notes(title , Note , time) values(?,?,?)'
		 , (title , Note , time))
		self._db.commit()
		return "Request is Submited"
	def Listrequest(self):
		cursor = self._db.execute('Select * from Notes')
		return cursor
	def DeleteRecord(self,ID):
		self._db.execute('delete from Notes where ID ={}'.format(ID))
		self._db.commit()
		return'Record is deleted'
	def Listrequest2(self ,ID):
		cursor2 = self._db.execute('Select * from Notes where ID = {}'.format(ID))
		return cursor2