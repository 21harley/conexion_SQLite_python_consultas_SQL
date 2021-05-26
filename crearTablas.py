import sqlite3
import json
from sqlite3 import Error

#crear la conexion
def sql_connection():
    try:
        con = sqlite3.connect('SQLite/test.sqlite3')
        return con
    except Error:
        print(Error)

#codigo crear tabla
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS empleado( id integer primary key, nombre VARCHAR(50), edad INTEGER, sueldo FLOAT)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS departamento( id integer primary key,nombre VARCHAR(50), presupuesto FLOAT,id_jefe INTEGER,  foreign key(id_jefe) references empleado(id))")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS trabajo_en( id_empleado INTEGER,id_dpto INTEGER,porcentaje_tiempo INTEGER,foreign key(id_empleado) references empleado(id),foreign key(id_dpto) references departamento(id))")
    con.commit()   

#codigo agregar tabla
def sql_insert(con,dato1,dato2,dato3,dato4,tipo):
    cursorObj = con.cursor()
    if(tipo==1):
        cursorObj.execute("INSERT INTO empleado (id,nombre,edad,sueldo) VALUES( ?,?,?,?)",(dato1,dato2,dato3,dato4))
    if(tipo==2):
        cursorObj.execute("INSERT INTO departamento (id,nombre,presupuesto,id_jefe) VALUES( ?,?,?,?)",(dato1,dato2,dato3,dato4))
    if(tipo==3):
        cursorObj.execute("INSERT INTO trabajo_en (id_empleado,id_dpto,porcentaje_tiempo) VALUES( ?,?,?)",(dato1,dato2,dato3))
    con.commit()

#creao tabla
con = sql_connection()
sql_table(con)

#cargo datos
f = open("empleados.txt", "r")
while(True):
    linea = f.readline()
    palabras=linea.split(",")
    listaE=[]
    for palabra in palabras:
        listaE.append(palabra)
    if(listaE[0]!=''):
       sql_insert(con,int(float(listaE[0])),listaE[1],int(float(listaE[2])),float(listaE[3]),1)    
    if not linea:
        break
f.close()

f = open("trabaja_en.txt", "r")
while(True):
    linea = f.readline()
    palabras=linea.split(",")
    listaT=[]
    for palabra in palabras:
        listaT.append(palabra)
    if(listaT[0]!=''):
        sql_insert(con,int(float(listaT[0])),int(float(listaT[1])),int(float(listaT[2])),0,3)    
    if not linea:
        break
f.close()

f = open("departamento.txt", "r")
while(True):
    linea = f.readline()
    palabras=linea.split(",")
    listaD=[]
    for palabra in palabras:
        listaD.append(palabra)
    if(listaD[0]!=''):
        sql_insert(con,int(float(listaD[0])),listaD[1],float(listaD[2]),int(float(listaD[3])),2)    
    if not linea:
        break
f.close()
#cierro connect
con.close
