from flask import Flask, request
from main import fetch_users,emp_by_id,insertdata

app = Flask(__name__)

@app.route("/getemp",methods=["GET"])
def get_emp():
    data = fetch_users()
    return data
@app.route("/getempid/<int:employee_id>",methods=["GET"])
def get_empby_id(employee_id):
    data = emp_by_id(employee_id)
    return data
@app.route("/insert",methods=["POST"])
def insert_db():
    data = request.get_json()
    print(data)
    insertdata(data)
    return "Data inserted Successfully"

if __name__ =="__main__":
    app.run(debug=True)

