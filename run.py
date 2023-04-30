from flask import Flask, Response, redirect, render_template, url_for, request, session, flash, jsonify
import mysql.connector
from chat import get_response
from booking import *
import random
import time
from message import *
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
app_login = os.environ.get('SECRET_KEY')

app = Flask(__name__)
app.secret_key = app_login
dbr = mysql.connector.connect(host='localhost',
                              user='root',
                              database='temp',
                              password='Admin123,'
                              )

cr = dbr.cursor()
s = """select source,destination from trains; """
# val = ()
cr.execute(s)
xyz = list(cr.fetchall())
from_destination = []
to_destination = []
for i in range(len(xyz)):
    from_destination.append(xyz[i][0])
    to_destination.append(xyz[i][1])
from_destination = [*set(from_destination)]
to_destination = [*set(to_destination)]


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        if 'user' in session:
            # username = session['user']
            return render_template('index.html', data1=from_destination, data2=to_destination)
        return render_template("login.html")
    else:
        source = request.form.get('source')
        destination = request.form.get('destination')
        try:
            s = """select prn,name,arrival,price from trains t where t.source=%s and t.destination=%s"""
            val = (source, destination,)
            cr.execute(s, val)
            my_data = cr.fetchall()
            all_pnr = []
            all_train_names = []
            all_train_times = []
            my_price = []
            for i in range(len(my_data)):
                all_pnr.append(my_data[i][0])
                all_train_names.append(my_data[i][1])
                all_train_times.append(my_data[i][2])
                my_price.append(my_data[i][3])
            return render_template('available_train.html', all_pnr=all_pnr, all_train_names=all_train_names, all_train_times=all_train_times, my_source=source, my_destination=destination, my_price=my_price)
        except mysql.connector.Error:
            return render_template('Error.html')
        # print(source)


@app.route("/bookTicket", methods=['GET', 'POST'])
def bookTicket():
    if request.method == 'GET':
        if 'user' not in session:
            # username = session['user']
            return render_template('login.html')
        s1 = """select source ,destination from trains; """
        cr.execute(s1)
        xyz = list(cr.fetchall())
        from_destination = []
        to_destination = []
        for i in range(len(xyz)):
            from_destination.append(xyz[i][0])
            to_destination.append(xyz[i][1])
        from_destination = [*set(from_destination)]
        to_destination = [*set(to_destination)]

        my_source = request.args.get('id1')
        my_destination = request.args.get('id2')
        my_price = request.args.get('id3')

        # print(session['user'])
        customer_name = session['user']
        # select name,email,phone from registers r where r.name = "%s";
        try:
            s2 = """select name,email,phone from registers r where r.name = %s"""
            val = (customer_name,)
            cr.execute(s2, val)
            # customers_detail = []
            customers_detail = cr.fetchall()

            return render_template('bookTicket.html',  data1=from_destination, data2=to_destination, my_class=my_class, customers_detail=customers_detail, my_source=my_source, my_destination=my_destination, my_price=my_price)
        except mysql.connector.Error:
            my_msg = "Datbase Error"
            return render_template('Error.html', msg=my_msg)
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        from_dest = request.form.get('from')
        to_dest = request.form.get('to')
        my_date = request.form.get('inputdate')
        journey_class = request.form.get('class')
        my_price = request.form.get('my_price')

        try:
            s = 'INSERT INTO ALL_BOOKING(NAME,EMAIL,PHONE,FROM_DEST,TO_DEST,DATE,CLASS) VALUES(%s,%s,%s,%s,%s,%s,%s);'
            val = (name, email, phone, from_dest,
                   to_dest, my_date, journey_class)
            cr.execute(s, val)
            dbr.commit()
            data = list(val)
            data.append(my_price)
            print(data)

            create_pdf_and_sendmail(
                name, email, phone, from_dest, to_dest, my_date, journey_class)
            # time.sleep(5)
            return render_template('invoice.html', data=data)

        except mysql.connector.Error:
            # print(mysql.connector.Error)
            return render_template('Error.html')


@app.route("/available_train", methods=['GET', 'POST'])
def available_train():
    if request.method == 'GET':
        # s = """select prn,name,arrival from trains t where t.source="%s" and t.destination="Ahmedabad""""
        return render_template('available_train.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirm-password')
        phone = request.form.get('phone')
        address = request.form.get('address')

        s1 = """select name from registers where name=%s"""
        val = (name,)
        cr.execute(s1, val)
        xyz = cr.fetchall()
        if (xyz):
            msg = "user already exists. Please Login"
            return redirect(url_for('Error', msg=msg))

        if (confirmpassword == password):
            try:
                s2 = 'INSERT INTO REGISTERS(NAME,EMAIL,PHONE,ADDRESS,PASSWORD) VALUES(%s,%s,%s,%s,%s);'
                val = (name, email, phone, address, password,)
                cr.execute(s2, val)
                dbr.commit()
                return render_template('RegisterSuccess.html')
            except mysql.connector.Error:
                # print(mysql.connector.Error)
                print(mysql.connector.Error)
                return render_template('Error.html')
        return render_template('Error.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form.get('loginUsername')
        email = request.form.get('loginEmailId')
        password = request.form.get('loginPwd')

        try:
            s = """select * from registers r where r.name=%s and r.password=%s and r.email=%s"""
            val = (name, password, email,)
            cr.execute(s, val)
            xyz = cr.fetchall()

            if (not xyz):
                my_msg = "User is not Found"
                return render_template('Error.html', msg=my_msg)
        except mysql.connector.Error:
            my_msg = "Datbase Error"
            return render_template('error.html', msg=my_msg)
        session['user'] = name

    return render_template('index.html', data1=from_destination, data2=to_destination)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('login.html')


@app.route("/myBooking")
def myBooking():
    try:
        s = """select * from all_booking where name=%s"""
        val = (session['user'],)
        cr.execute(s, val)
        my_data = list(cr.fetchall())
        my_data_list = [list(x) for x in my_data]
        # print(my_data_list)
        return render_template('myBooking.html', data=my_data_list)
    except:
        return render_template('error.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('cname')
        email = request.form.get('cemail')
        massage = request.form.get('cmessage')
        try:
            s = 'INSERT INTO CONTACT(user_name,email,massage) VALUES(%s,%s,%s);'
            val = (name, email, massage)
            cr.execute(s, val)
            dbr.commit()
        except mysql.connector.Error:
            return render_template('Error.html')
    return render_template('contact.html')


@app.route("/Error")
def Error():
    print("hello world")
    flash('User exist please login!')
    return render_template('login.html')


@app.route("/base", methods=["GET", "POST"])
def index_get():
    return render_template("chatbot.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")

    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/cancel_booking', methods=['GET'])
def cancel_booking():
    customer_id = request.args.get('id')
    # delete from all_booking where customer_id =70;
    print(customer_id)
    s1 = """delete from all_booking where customer_id =%s"""
    val = (customer_id,)
    cr.execute(s1, val)
    dbr.commit()

    s2 = """select * from all_booking where name=%s"""
    val = (session['user'],)
    cr.execute(s2, val)
    my_data = list(cr.fetchall())
    my_data_list = [list(x) for x in my_data]
    return render_template('myBooking.html', data=my_data_list)


app.run(debug=True)
