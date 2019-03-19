#!/usr/bin/python
# -*- coding: utf-8 -*-

#pip install mysqlclient
import MySQLdb

host = "localhost"
user = "usuario"
password = "123456"
db = "base"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

#Dict
c = con.cursor(MySQLdb.cursors.DictCursor)
#Tuble
#c = con.cursor()


def select(fields, tables, where=None):

    global c

    query = "SELECT " + fields + " FROM " + tables
    if (where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()


#print(select("nome, cpf", "tabela", "id = 1"))
#result = select("nome, cpf", "tabela")
#Imprimir como dict
#print(result[0]["cpf"])

def insert(value, table, fields=None):

    global c, con

    #INSET INTO <table> (fields) VALUES (), (), ()
    query = "INSERT INTO " + table

    if (fields):
        query = query + " (" + fields + ") "

    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    #print(query)
    c.execute(query)
    con.commit()



#values = ["DEFAULT,'Nome completo','Nascimento', 'Endereco', 'Cidade', 'Estado', 'CPF'",
#          "DEFAULT,'Nome completo','Nascimento', 'Endereco', 'Cidade', 'Estado', 'CPF'"]
#insert(values, "tabela")
#select("*", "tabela")


def update(sets, table, where=None):

    #UPDATE table SET field = value, field = value WHERE field = value
    global c, con

    query = "UPDATE " + table

    query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])


    if (where):
        query = query + " WHERE " + where

    #print(query)
    c.execute(query)
    con.commit()

#print(select("*", "tabela", "id = 8"))
#update({"nome": "Nome completo", "cidade": "Curitiba"}, "tabela", "id = 8")

def delete(table, where):

    #DELETE FROM table WHERE where
    global c, con

    query = "DELETE FROM " + table + " WHERE " + where
    c.execute(query)
    con.commit()

#print(select("*", "tabela", "id = 8"))
#print(delete("tabela", "id = 8"))
#print(select("*", "tabela", "id = 8"))

