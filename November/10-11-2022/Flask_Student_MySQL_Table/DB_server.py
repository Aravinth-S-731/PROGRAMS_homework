from flask import Flask,render_template,request
import mysql.connector

mydb = mysql.connector.connect(
  host = 'localhost',
  user = "Aravinth_Sayur",
  password = "123456789",
  database = 'Student_Database'
)
mycursor = mydb.cursor()

app = Flask(__name__)

"""---------- STORE DATA ----------"""
@app.route("/studentForm")
def store():
    return render_template("Stud_get.html")

@app.route("/insert", methods=["POST"])
def insert_data():
    id = request.form.get("id")
    name = request.form.get("name")
    dept = request.form.get("dept")
    data = [id,name,dept]
    statement = "INSERT INTO Student_Database(IDNum,Name,Department) VALUES (%s,%s,%s)"
    mycursor.execute(statement,data)
    mydb.commit()
    return ''
"""---------- DISPLAY DATA ----------"""
@app.route("/studentView")
def display():
    return render_template("Stud_disp.html")

@app.route("/display")
def display_data():
    students = []
    mycursor.execute("SELECT * FROM student_database.student_database")
    myres = mycursor.fetchall()
    for index in myres:
        students.append(index)
    return students

app.run(debug=True)