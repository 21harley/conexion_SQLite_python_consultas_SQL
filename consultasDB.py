import sqlite3
import json
import time
from sqlite3 import Error

#crear la conexion
def sql_connection():
    try:
        con = sqlite3.connect('SQLite/test.sqlite3')
        return con
    except Error:
        print(Error)
        
#codigo consulta 1 tabla
def sql_consulta1(con):
    print("consulta 1 nombre y edad de cada empleado que trabaja en los departamentos de Software y Hardware")
    cursorObj = con.cursor()
    cursorObj.execute("""
     SELECT id_empleado from trabajo_en where id_dpto=(
        SELECT id from departamento WHERE nombre="Software" or  nombre="Hardware"
     );
    """)
    resp=cursorObj.fetchall()
    for item in resp:
        curso1=con.cursor()
        curso1.execute("SELECT nombre,edad from empleado WHERE id="+str(item[0])+";")
        resp1=curso1.fetchall()
        print(resp1)
    con.commit()
    
#codigo consulta 2 tabla
def sql_consulta2(con):
    print("consulta 2 nombre de jefe de departamento con presupuesto mas elevado")
    cursorObj = con.cursor()
    cursorObj.execute("""
     SELECT id_jefe FROM departamento ORDER BY presupuesto DESC;
    """)
    resp=cursorObj.fetchall()
    global numero
    numero=0
    while (numero<3):
        curso1=con.cursor()
        curso1.execute("SELECT nombre from empleado WHERE id="+str(resp[numero][0])+";")
        resp1=curso1.fetchone()
        print(resp1)
        numero+=1  
    con.commit()

#codigo consulta 3 tabla
def sql_consulta3(con):
    print("consulta 3 empleado con sueldo superior al presupuesto del departamento")
    cursorObj = con.cursor()
    cursorObj.execute("""
     SELECT id,nombre,presupuesto from departamento;
    """)
    resp=cursorObj.fetchall()
    con.commit()

    for item in resp:
        curso1=con.cursor()
        curso1.execute("SELECT id_empleado from trabajo_en where id_dpto="+str(item[0])+";")
        resp1=curso1.fetchall()
        con.commit()
        
        for item1 in resp1:
            curso2=con.cursor()
            curso2.execute("SELECT nombre,sueldo from empleado where id="+str(item1[0])+";")
            resp2=curso2.fetchone()
            if(resp2[1]>item[2]):
                print(item[1])
                print(resp2[0])
            con.commit()
            
#codigo consulta 4 tabla
def sql_consulta4(con):
    print("consulta 4 departamento con 20 o mas empleados a tiempo completo")
    cursorObj = con.cursor()
    cursorObj.execute("""
     SELECT id,nombre,presupuesto from departamento;
    """)
    resp=cursorObj.fetchall()
    con.commit()

    for item in resp:
        curso1=con.cursor()
        curso1.execute("SELECT id_empleado from trabajo_en where id_dpto="+str(item[0])+";")
        resp1=curso1.fetchall()
        con.commit()
        if(len(resp1)>=20):
            print(item[1],len(resp1))
            
#creo conexión, llamo funciones de consulta      
con = sql_connection()
resul=sql_consulta1(con);
resul=sql_consulta2(con);
resul=sql_consulta3(con);
resul=sql_consulta4(con);

#cierro connect
con.close
