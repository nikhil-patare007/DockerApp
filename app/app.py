from typing import List, Dict
from flask import Flask ,render_template, request
#from flask_table import Table, Col
import mysql.connector 
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home() -> List[Dict]:
    if request.method == "POST":
         emp_id = request.form['id']
         ename = request.form['name']
         sal = request.form['sal']
         config = {
           'user': 'root',
           'password': 'root',
           'host': 'db',
           'port': '3306',
           'database': 'Data1'
            }
         
         connection = mysql.connector.connect(**config)
         cursor = connection.cursor()
         result=cursor.execute("INSERT INTO EmpData VALUES (%s,%s,%s)",(emp_id,ename,sal))
         
         cursor.close()
         connection.commit()
         connection.close()
         return "Entry Added....."
    return render_template('index.html',msg1 = "insert successfully")



#DELEATE
@app.route('/dele', methods=['GET', 'POST'])
def delet() -> List[Dict]:
    if request.method == "POST":
         demp_id = request.form['d_id']
         config = {
           'user': 'root',
           'password': 'root',
           'host': 'db',
           'port': '3306',
           'database': 'Data1'
            }
         connection = mysql.connector.connect(**config)
         cursor = connection.cursor()
         sql1 = "DELETE FROM EmpData WHERE id = %s"
         #result=cursor.execute("DELETE FROM EmpData WHERE id = (%s)",(demp_id))
         result=cursor.execute(sql1, (demp_id,))
         
         cursor.close()
         connection.commit()
         connection.close()
         return "Deleted Successfully"
    return render_template('show.html',msg2 = "deleted successfully")   



@app.route('/dis')  
def connection():
        con=mysql.connector.connect(host="db",user="root",password="root",port="3306",database="Data1")
        cursor=con.cursor()
        sql2 = "SELECT * FROM EmpData "
        result=cursor.execute(sql2)
        s = "<table style='border:1px solid red'>"  
        for row in cursor:  
            s = s + "<tr>"  
        for x in row:  
            s = s + "<td>" + str(x) + "</td>"  
        s = s + "</tr>"
        # cursor.close()
        con.commit()
        con.close()
        return "<html><body>"+s+"</body></html>"        
        
 

@app.route('/dis')  
def connectio():
        con=mysql.connector.connect(host="db",user="root",password="root",port="3306",database="Data1")
        cursor=con.cursor()
        sql2 = "SELECT * FROM EmpData "
        result=cursor.execute(sql2)
        s = "<table style='border:1px solid red'>"  
        for row in cursor:  
            s = s + "<tr>"  
        for x in row:  
            s = s + "<td>" + str(x) + "</td>"  
        s = s + "</tr>"
        # cursor.close()
        con.commit()
        con.close()
        return "<html><body>"+s+"</body></html>"     

# @app.route('/display')  
# def displaydata() -> List[Dict]:
#         config = {
#            'user': 'root',
#            'password': 'root',
#            'host': 'db',
#            'port': '3306',
#            'database': 'Data1'
#             }
#         connection = connector.connect(**config)
#         select_all_query = """SELECT * FROM EmpData"""
#         cursor = connection.cursor()
#         cursor.execute(select_all_query)
#         data = cursor.fetchall()
#         connection.close()
#         return data
#         data = EmpData.getList()
#         return render_template('display.html', rows=data)
    
# @app.route('/')  
# @app.route('/dis')  
# def show1():  
#     return "<html><body>"+s+"</body></html>"   


#UPDATE
@app.route('/update', methods=['GET', 'POST'])
def updat() -> List[Dict]:
    if request.method == "POST":
         uemp_id = request.form['id1']
         usal1 = request.form['sal1']
         config = {
           'user': 'root',
           'password': 'root',
           'host': 'db',
           'port': '3306',
           'database': 'Data1'
            }
         connection = mysql.connector.connect(**config)
         cursor = connection.cursor()
         data = (usal1, uemp_id)
         query2 = """ UPDATE EmpData SET sal = %s WHERE id = %s """
         
         result=cursor.execute(query2, data)
        
         cursor.close()
         connection.commit()
         connection.close()
         return "salary updated successfully........"
    return render_template('update.html',msg2 = "sal update successfully")





if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(debug=True)