from flask import Flask,render_template,request,session,redirect,url_for,make_response
from mysql.connector import connect 

con=connect(host='sql6.freemysqlhosting.net',
            port=3306,
            database='sql6705242',
            user='sql6705242',
            password='p8UGc4D67p')
app=Flask(__name__)
app.secret_key= '2b449a7d94480a7a0ec53c7329ed'
session={}
@app.route("/home")
@app.route("/")
def hello():
    return render_template("form.html")

@app.route("/fillform",methods=["GET","POST"])
def myform():
    if request.method=="POST":
        num1=request.form["num1"]
        num2=request.form["num2"]
        cursor=con.cursor()
        cursor.execute("insert into arth(num1,num2) values(%s,%s)",(num1,num2))
        con.commit()
        return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True)
