import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('archanashegur29@gmail.com','xiqo cwzx upxk aysp')

server.sendmail('archanashegur29@gmail.com','archanashegur29105@gmail.com','hi this is python')