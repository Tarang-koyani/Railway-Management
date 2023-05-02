import socket
import os
from reportlab.lib.units import mm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
from reportlab.pdfgen import canvas
from dotenv import load_dotenv


load_dotenv()
password = os.environ.get('MY_PASSWORD')


def send_email(to, subject, text, files):
    email_user = '21cek062@nirmauni.ac.in'
    email_password = password
    email_send = to

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = COMMASPACE.join(email_send)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment',
                        filename=file.split("/")[-1])
        msg.attach(part)

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(email_user, email_password)
    smtp_server.sendmail(email_user, email_send, msg.as_string())
    smtp_server.close()


def create_pdf_and_sendmail(name, email, phone, source, destination, date, train_class, my_price, my_train):

    c = canvas.Canvas("RailwayTicket.pdf")

    c.setFont('Helvetica', 12)

    c.roundRect(50, 750, 500, 80, 20, stroke=1, fill=0)
    c.drawCentredString(300, 790, "Railway Ticket")

    c.line(50, 720, 550, 720)

    c.line(250, 750, 250, 720)
    c.line(350, 750, 350, 720)

    c.drawString(70, 685, "Name:")
    c.drawString(70, 665, "Email:")
    c.drawString(70, 645, "Phone:")
    c.drawString(70, 625, "Your Booked Trains Name :")
    c.drawString(70, 605, "Source:")
    c.drawString(70, 585, "Destination:")
    c.drawString(70, 565, "Date:")
    c.drawString(70, 545, "Train Class:")
    c.drawString(70, 525, "Total amount :")

    # Draw the actual ticket information
    c.drawString(270, 685, name)
    c.drawString(270, 665, email)
    c.drawString(270, 645, phone)
    c.drawString(270, 625, my_train)
    c.drawString(270, 605, source)
    c.drawString(270, 585, destination)
    c.drawString(270, 565, str(date))
    c.drawString(270, 545, train_class)
    c.drawString(270, 525, my_price)

    # Add the railway logo to the ticket
    logo_path = "./static/images/train.png"
    c.drawImage(logo_path, 450, 680, width=70, height=70)

    # Draw the footer of the ticket
    # c.line(50, 560, 515, 560)
    c.drawCentredString(300, 480, "Thank you for choosing the railways!")
    c.drawCentredString(
        300, 460, "Please keep this ticket with you at all times.")
    c.drawCentredString(300, 440, "Have a safe and enjoyable journey!")

    c.save()
    send_email(to=email, subject='Your booked Railway Ticket',
               text='Your Booked Ticket', files=['RailwayTicket.pdf'])
