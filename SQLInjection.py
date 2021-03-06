#Exemplo de aplicação Python simples que mostra um dos possíveis ataques de SQL Injection.
#A aplicação estabeleceu conexão com um BD que continha uma tabela chamada "clientes", onde existia um dado de um cliente. A tupla do cliente foi indevidamente alterada, através do injeção de código.
#O exemplo é específico para meu banco de dados, que tem uma tabela "clientes"(idcliente, nome, idade) e tem um cliente com idcliente = 13 e como nome e idade diferentes dos setados na veriável nome(linha 15).

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
