import MySQLdb

# Modo padrão e simples de se conectar a um banco de dados
db = MySQLdb.connect(user="root", passwd="BDpa$$wd*", db="jc_clientes", host="localhost", port=3306)

#Criando um cursor para manipular dados do banco de dados
cursor = db.cursor()

#.execute envia comandos para o banco de dados
cursor.execute("SELECT * FROM cliente")

print(cursor.fetchall()) #imprime todos os dados da consulta anterior que está no cursor

print("Conexão realizada com sucesso")
db.close()

# -----------------------------------------------------------------------------------------
