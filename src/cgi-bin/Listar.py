#!c:\Python27\python.exe
import cgi, cgitb, sqlite3
form = cgi.FieldStorage()
nome = str(form.getvalue('nome'))
email = str(form.getvalue('email'))
telefone = str(form.getvalue('telefone'))

conn = sqlite3.connect('usuario.db')
sql = 'CREATE TABLE IF NOT EXISTS usuario (nm_usuario varchar(50) not null, ds_email varchar(50), ds_telefone vachar (50) )'
c = conn.cursor()
c.execute(sql)
sql = 'INSERT INTO usuario values (\''+nome+'\', \''+email+'\', \''+telefone+'\')'
c.execute(sql)
with conn:
    sql = 'SELECT * FROM usuario'
    c.execute(sql)

    rows = c.fetchall()

    print 'Content-Type: text/html'
    print
    ##for row in rows:
      ##  print row
        
    aux = '<table><tr><td>Id:</td><td>Nome:</td><td>Email:</td><td>Telefone:</td></tr>' 
    count = 0 
    for row in rows:
        count = count + 1
        if count % 2 == 0:
            aux = aux + '<tr>'
        else:
            aux = aux + '<tr style=\'background: #FFC;\'>'      
        aux = aux + '<td>'+str(count)+'</td>'
        aux = aux + '<td>'+row[0]+'</td>'
        aux = aux + '<td>'+row[1]+'</td>'
        aux = aux + '<td>'+row[2]+'</td></tr>'
    aux = aux + '</table>'
    arq = open('./index.html')
    open
    doc = arq.read()
    arq.close()
    print doc.replace('<!-- test -->', aux)
    