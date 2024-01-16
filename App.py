import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="LoUrD@12345",database="Books")
cursor = con.cursor()
from flask import Flask,redirect,render_template,request,url_for,session
import random
import datetime
webApp = Flask(__name__)
webApp.secret_key = "123"


# application request handler + Search Algorithm logic

@webApp.route("/app/<userdata>",methods=["GET","POST"])
def application(userdata):
    if request.method == "POST":
        title = ["The Hunger Games","Harry Potter and the Order of the Phoenix","To Kill a Mockingbird","Pride and Prejudice","Twilight","The Book Thief","Animal Farm","The Chronicles of Narnia","The Lord of the Rings","Gone with the Wind","The Fault in Our Stars","The Hitchhikers Guide to the Galaxy","The Giving Tree","Wuthering Heights","The Da Vinci Code","Memoirs of a Geisha","The Picture of Dorian Gray","Alice in Wonderland","Jane Eyre","Fahrenheit 451"]
        author = ["Suzanne Collins","JK Rowling","Harper Lee","Jane Austen","Stephenie Meyer","Markus Zusak","George Orwell","C.S. Lewis","J.R.R. Tolkien","Margaret Mitchell","John Green","Douglas Adams","Shel Silverstein","Emily BrontÃ","Dan Brown","Arthur Golden","Oscar Wilde","Lewis Carrol","Charlotte BrontÃ","Ray Bradbury"]
        genre = ["Fantasy","Classic","Historical Fiction","Romance","Science Fiction","Thriller"]
        data = eval(userdata)
        formData = request.form.get("hint")
        if formData in title:
            query = "select * from books where title = %s"
            value = (formData,)
            cursor.execute(query,value)
            x = cursor.fetchall()
            return render_template("App.html",user = data,bookdata = x)    
        elif formData in author:
            query = "select * from books where author = %s"
            value = (formData,)
            cursor.execute(query,value)
            x = cursor.fetchall()
            return render_template("App.html",user = data,bookdata = x)    
            
        elif formData in genre:
            query = "select * from books where genre = %s"
            value = (formData,)
            cursor.execute(query,value)
            x = cursor.fetchall()
            return render_template("App.html",user = data,bookdata = x)
        
        else:
            return "Please enter some value Go Back"
    if request.method == "GET":    
        data = eval(userdata)
        query = "select * from books where genre = %s"
        value = (data["preference"],)
        cursor.execute(query,value)
        result = cursor.fetchall()        
        return render_template("App.html",user = data,bookdata = result)

# signup request handler

@webApp.route("/signup")
def signup():
    return render_template("signup.html")

# login request handler

@webApp.route("/login")
def login():
    return render_template("login.html")

# logic handler for storing signup user data

@webApp.route("/signUpDataStore",methods=["POST","GET"])
def signUpDataStore():
    if request.method == "POST":
        user = request.form.get("user")
        password = str(request.form.get("password"))
        preference = request.form.get("preference")
        cursor.execute("select username,passwd from users")
        if (user,password) in cursor.fetchall():
            session["username"] = user
            query = "select preference from users where username = %s"
            values = (session["username"],)
            cursor.execute(query,values)
            for i in cursor.fetchall():
                userprefernce = i[0]
            return redirect(url_for("application",userdata = {"username":session["username"],"preference":userprefernce}))
        else:
            userid = random.randint(1,1000)
            query = "insert into users values(%s,%s,%s,%s)"
            values = (userid,user,password,preference)
            try:
                cursor.execute(query,values)
                con.commit()
            except:
                con.rollback()
            print(cursor.rowcount,"record inserted")
            
            return "You have successfully signed up <a href='http://localhost:8000/login'>click here to login </a>"

# logic handler for checking during user login

@webApp.route("/loginCheck",methods=["GET","POST"])
def loginCheck():
    if request.method == "GET":
        user = request.args.get("user")
        password = str(request.args.get("password"))
        if user == "admin" and password == "admin":
            session["username"] = user
            return redirect(url_for("admin"))
        cursor.execute("select username,passwd from users")
        session["username"] = user
        if (user,password) in cursor.fetchall():
            query = "select preference from users where username = %s"
            values = [session["username"]]
            cursor.execute(query,values)
            for i in cursor.fetchall():
                userprefernce = i[0]
            return redirect(url_for("application",userdata={"username":session["username"],"preference":userprefernce}))
        else:
            session.pop("username",None)
            return "Incorrect username or password <a href='http://localhost:8000/login'>try again</a>"

# Logout request handler
        
@webApp.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("login"))

# request handler for user page

@webApp.route("/user/<userdata>")
def user(userdata):
    data = eval(userdata)
    return render_template("user.html",user=data)

# request handler for Placing Order Confirmation page

@webApp.route("/placeOrder/<bookdata>")
def placeOrder(bookdata):
    bookdata = eval(bookdata)
    return render_template("placeOrder.html",i = bookdata)

# request handler for confirming Order (Storing order details in a database table)
@webApp.route("/confirmOrder/<orderdata>")
def confirmOrder(orderdata):
    orderdata = eval(orderdata)
    ordertime = datetime.datetime.now()
    query = "insert into orders values(%s,%s,%s)"
    values = (session["username"],orderdata[0],ordertime)
    try:
        cursor.execute(query,values)
        con.commit()
    except:
        con.rollback()
    return "<h1>Your Order is placed successfully</h1><a href='http://localhost:8000/logout'>click here</a>"

# request handler for admin page

@webApp.route("/admin")
def admin():
    cursor.execute("select * from orders")
    customerData = cursor.fetchall()
    return render_template("Admin.html",data = customerData)

# request handler for deleting records in orders table

@webApp.route("/delete/<datatodelete>")
def delete(datatodelete):
    datatodelete = eval(datatodelete)
    query = "delete from orders where customername = %s and bookname = %s"
    value = datatodelete
    try:
        cursor.execute(query,value)
        con.commit()
    except:
        con.rollback()
    return "<h1>Data has been deleted Successfully <a href='http://localhost:8000/admin'>click here</a></h1>"

if __name__ == "__main__":
    webApp.run(host="localhost",port=8000,debug=True)
