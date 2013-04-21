#!c:\Python27\python.exe
import cgi, cgitb, sqlite3

conn = sqlite3.connect('usuario.db')
sql = 'DROP TABLE usuario'
c = conn.cursor()
c.execute(sql)