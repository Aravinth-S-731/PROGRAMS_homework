from flask import Flask,render_template,request     #header declaration
import mysql.connector                              #header declaration

mydb = mysql.connector.connect(                     #MySQL Connection
  host = 'localhost',                               #host name
  user = "Aravinth_Sayur",                          #user
  password = "123456789",                           #password
  database = 'Student_Database'                     #database name
)
mycursor = mydb.cursor()                            #creating a cursor

app = Flask(__name__)                               #starting Flask
students = []                                       #empty list/array to store datas

"""---------- STORE DATA ----------"""
@app.route("/get_student")                          #to store data in MySQL
def store():
    return render_template("Stud_get.html")         #render_template

@app.route("/insert", methods=["POST"])             #upload using POST method
def insert_data():
    id = request.form.get("id")                     #get user inputs
    name = request.form.get("name")                 #get user inputs
    dept = request.form.get("dept")                 #get user inputs
    data = [id,name,dept]                           #to insert in MySQL
    statement = "INSERT INTO Student_Database(IDNum,Name,Department) VALUES (%s,%s,%s)"
    mycursor.execute(statement,data)                #Inserting in MySQL
    mydb.commit()                                   #Commiting
    return ''                                       #returns NULL

"""---------- DISPLAY DATA ----------"""
@app.route("/disp_student")                         #to display stored data
def display():
    return render_template("Stud_disp.html")        #render_template

@app.route("/display")                              #to get datas from MySQL
def display_data():
    mycursor.execute("SELECT * FROM student_database.student_database")
    myres = mycursor.fetchall()                     #getting values from DB
    for index in myres:                             #looping data's 
        students.append(index)                      #storing datas in an array
    return students                                 #returnig the datas

app.run(debug=True)                                 #Run the server