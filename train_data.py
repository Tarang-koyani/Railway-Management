import mysql.connector

dbr = mysql.connector.connect(host='localhost',
                              user='root',
                              database='temp',
                              password='Admin123,'
                              )
cr = dbr.cursor()
# s='create table trains(prn numeric(8) primary key, name varchar(200), source varchar(20), destination varchar(20), arrival TIME);'
# cr.execute(s)
# cr.execute('CREATE TABLE registers(name varchar(10) primary key,email varchar(50), phone varchar(13), address varchar(200), password varchar(10));')
# cr.execute('CREATE TABLE contact(user_name varchar(10) primary key,email varchar(50), massage varchar(10));')
# user_name, email, massage
# create table all_booking
#    (
#    customer_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
#    name varchar(20),
#    date DATE,
#    phone varchar(10),
#    email varchar(40),from_dest varchar(50),to_dest varchar(50),class varchar(20));
s = "insert into trains values(92144129,'Rajdhani Express','Delhi','Ahmedabad','06:30:00','500');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(97645753,'Vande Bharat','Delhi','Mumbai','16:30:00','250');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(37534585,'Jammu Tavi Express','Delhi','Jammu','04:15:00','850');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(47241559,'Shatabdi Express','Delhi','Bhopal','19:30:00','850');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(92144785,'Shatabdi Express','Delhi','Pune','04:30:00','450');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(93461646,'Tejas Express','Delhi','Bangalore','07:30:00','399');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(36875768,'Vande Bharat Express','Delhi','Kolkata','11:30:00','450');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(65418831,'Delhi Express','Delhi','Kanyakumari','13:30:00','699');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(95118791,'Intercity Express','Delhi','Jamnagar','17:30:00','450');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(95118491,'Intercity Express','Ahmedabad','Jamnagar','17:30:00','450');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(47245359,'Shatabdi Express','New Delhi','Bhopal','19:30:00','950');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(37531885,'Jammu Tavi Express','Ahmedabad','Jammu','04:15:00','850');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(92144753,'Shatabdi Express','Ahmedabad','Pune','04:30:00','450');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(92145631,'Karnavati Express','Mumbai','Ahmedabad','23:30:00','450');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(65418491,'Karnavati Express','Ahmedabad','Mumbai','05:30:00','650');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(94456231,'Sampark Kranti Express','New Delhi','Pune','15:30:00','550');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(65418231,'Vivek Express','Dibrugarh','Kanyakumari','13:30:00','599');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(92145000,'Rajdhani Express','Jaipur','Ahmedabad','06:30:00','500');"
cr.execute(s)
dbr.commit()

s = "insert into trains values(97645001,'Vande Bharat','Jaipur','Mumbai','16:30:00','250');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(37535002,'Jammu Tavi Express','Jaipur','Jammu','04:15:00','850');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(47245003,'Shatabdi Express','Jaipur','Bhopal','19:30:00','850');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(92145004,'Shatabdi Express','Jaipur','Pune','04:30:00','450');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(93465005,'Tejas Express','Jaipur','Bangalore','07:30:00','399');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(36875006,'Vande Bharat Express','Jaipur','Kolkata','11:30:00','450');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(65415007,'Delhi Express','Jaipur','Kanyakumari','13:30:00','699');"
cr.execute(s)
dbr.commit()


s = "insert into trains values(95115008,'Intercity Express','Jaipur','Jamnagar','17:30:00','450');"
cr.execute(s)
dbr.commit()
