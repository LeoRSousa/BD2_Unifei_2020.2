import psycopg2 #Documetação: https://www.psycopg.org/docs/usage.html

conexao = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = '1234',
    dbname = 'SQLInjectionExample',
    port = 5432
)
cur = conexao.cursor() #Cria um cursor, para as ações
nome = "'Joao' , idade = 80"
cur.execute(f"UPDATE clientes SET nome={nome} WHERE idcliente=13")
conexao.commit() #Realiza as alterações
conexao.close() #Fecha conexão