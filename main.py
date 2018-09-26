import MySQLdb

# Modo padrão e simples de se conectar a um banco de dados
db = MySQLdb.connect(user="root", passwd="BDpa$$wd*", db="jc_clientes", host="localhost", port=3306, autocommit=False)
# se o autocommit ficar como False, as alterações, inserções e etc não são feitas no banco real

#Criando um cursor para manipular dados do banco de dados
cursor = db.cursor()

#.execute envia comandos para o banco de dados
#cursor.execute("SELECT * FROM cliente")
# fetchall faz que o cursor percorra todos os dados da consulta
#print(cursor.fetchall()) # imprime todos os dados da consulta anterior que está no cursor

#cursor.execute("SELECT * FROM cliente WHERE idcliente=1")
# fetchone faz que o cursor percorra apenas o primeiro registro encontrado
#print(cursor.fetchone()) # imprime o primeiro registro encontrado pelo cursor

#cursor.execute("SELECT * FROM cliente")
# fetchmany traz a quantidade de registros que queremos retornar
#print(cursor.fetchmany(1)) # entre parenteses, passar a quantidade de registros à ser apresentado

# Nesse bloco será inserido dois cliente no BD se ocorrer algo certo, caso algo de errado será feito um rollback.
try:
    db.begin()
    # Inserindo novos registros no BD
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Maria', 25)")
    cursor.execute("INSERT INTO cliente (nomes, idade) VALUES ('José', 25)")
    db.commit() # commita modificações para o banco
except:
    db.rollback() # se algo der errado, desfaz as modificações
    print("Algo deu errado!")

cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())

# lastrowid é responsável por capturar o ultimo id do registro inserido no bando de dados
#print(cursor.lastrowid)

# atualiza registro no banco de dados
#cursor.execute("UPDATE cliente SET nome='Ana' WHERE idcliente=2")

# remove um registro do banco
#cursor.execute("DELETE FROM cliente WHERE idcliente=2")

#cursor.execute("SELECT * FROM cliente")
#print(cursor.fetchall())

print("Conexão realizada com sucesso")
db.close()

# -----------------------------------------------------------------------------------------
