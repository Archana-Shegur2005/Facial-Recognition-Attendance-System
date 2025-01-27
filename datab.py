from tkinter import*
from pil import Image
from tkinter import ttk
from pil import Image,ImageTk
import pil.Image
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
my_cursor=conn.cursor()

my_cursor.execute("select password from adminregister where username='Archana@123'")
c=my_cursor.fetchone()
print(c)

'''my_cursor.execute("select distinct(year) as year from combo where dept='CSE'")
my_list2=my_cursor.fetchall()

print(my_list2)'''