import mysql.connector

# o computador em que o banco de dados está rodando
# se estiver no mesmo computador que o sistema está rodando,
# pode ser # localhost ou 127.0.0.1
# A Porta padrão é 3306, mas verifique para ter certeza 
# se o seu sistema não está rodando em outra porta.
hostname = "127.0.0.1"
port = "3306"

# as credenciais de acesso do
# SGBD que o sistema vai utilizar
# você pode criar um usuário e senha
# só pra isso ou, no caso, usar o
# usuário raiz do SGBD
user = "root"
password =""

# o nome do esquema de banco de dados
# que o sistema estará utilizando
# aqui você deve preencher o nome
# que você deu ao seu banco de dados.
banco = "MeuBancoDeDadosFeliz"

def connect():
    conexao = mysql.connector.connect(host=hostname,
    port=port,
    user=user,
    password=password,
    database=banco)
    return conexao

# use essa função quando for executar um comando
# no banco de dados que precise alterar os dados
# lá dentro.
def executeCommand(command:str):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()
    connection.close()

# use essa função quando for executar uma consulta,
# ou seja, um comando que retorna dados do banco.
def executeQuery(query:str) -> list:
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result