from flask import Flask, request
import sqlite3
app=Flask(__name__)
@app.get('/')
def hi():
    return "good night"
@app.post('/h')
def hi1():
    con = sqlite3.Connection("C:/Users/trc/bhala/sample/Scripts/day.db")
    cur=con.cursor()
    data = request.get_json()
    cur.execute("create table if not exists student(name varchar(255),Rollno varchar(255),mark int)")
    for i in range(2):
        Name=data[i]["Name"]
        Rollno=data[i]["Rollno"]
        Mark=data[i]["Mark"]
        student=(Name,Rollno,Mark)
        cur.execute("insert into student values(?,?,?)",student)
    con.commit()
    con.close()
    print(data)
    return "data collected"
@app.patch('/pat/<inputmark>')
def patchmethod(inputmark):
    data = request.get_json()
    users = data
    if inputmark in users.values():
        users["Mark"] = 99
        res = "Data updated"
        return res
    print(f"The data after creation is {users}")
    res = "Data created"
@app.delete("/delete/<rollno>")

def deletes(rollno):
    
    delete(rollno);
    return("deleted");
def delete(rollno):
    con = sqlite3.Connection("C:/Users/trc/bhala/sample/Scripts/day.db") 
    query = f'delete from student where rollno = "{rollno}"';
    cur = con.cursor();
    cur.execute(query)
    con.commit()
  
app.run(debug=True)