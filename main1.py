from tkinter import*
from pil import Image
from tkinter import ttk
from pil import Image,ImageTk
import pil.Image
import tkinter
from student import Student
from train import Train
from face_recognition import Face_Recognition
from Attendance import Attendance
from help import Help
from time import strftime
from datetime import datetime
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Dashboard")
        

        img3=pil.Image.open("D:\\project exhibition compet\\face\\bg.jpg")
        img3=img3.resize((1330,690),pil.Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1350,height=690)

        title_lb1=Label(self.root,text="Face Recognition Attendance System ",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1330,height=50)
        

        b1_1=Button(title_lb1,text="Logout",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="red",fg="black")
        b1_1.place(x=1200,y=0,width=100,height=40)
        
        

        def time():
         string = strftime("%H:%M:%S %p")
         lb1.config(text=string)
         lb1.after(1000,time)

        lb1=Label(title_lb1,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lb1.place(x=50,y=0,width=110,height=50)
        time()
        
        
        
        img4=pil.Image.open("D:\\project exhibition compet\\face\\regstration.JPG")
        img4=img4.resize((250,250),pil.Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2",background="darkblue",border="2")
        b1.place(x=180,y=50,width=250,height=250,bordermode="outside")

        b1_1=Button(bg_img,text="Student Management",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=180,y=260,width=250,height=40)


        img5=pil.Image.open("D:\\project exhibition compet\\face\\face1.png")
        img5=img5.resize((250,250),pil.Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data,border="2",background="darkblue")
        b1.place(x=520,y=50,width=250,height=250,bordermode="outside")

        b1_1=Button(bg_img,text="Take Attendance",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=520,y=260,width=250,height=40)


        img6=pil.Image.open("D:\\project exhibition compet\\face\\attendance.jfif")
        img6=img6.resize((250,250),pil.Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data,border="2",background="darkblue")
        b1.place(x=850,y=50,width=250,height=250,bordermode="outside")

        b1_1=Button(bg_img,text="Attendance Management",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=850,y=260,width=250,height=40)


        img8=pil.Image.open("D:\\project exhibition compet\\face\\tra.png")
        img8=img8.resize((250,250),pil.Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data,background="darkblue",border="2")
        b1.place(x=180,y=360,width=250,height=250,bordermode="outside")

        b1_1=Button(bg_img,text="Train Photos",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=180,y=580,width=250,height=40)


        img9=pil.Image.open("D:\\project exhibition compet\\face\\\\ph1.png")
        img9=img9.resize((250,250),pil.Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img,background="darkblue",border="2")
        b1.place(x=520,y=360,width=250,height=250,bordermode="outside")

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=520,y=580,width=250,height=40)


        img7=pil.Image.open("D:\\project exhibition compet\\face\\\\ph1.png")
        img7=img7.resize((250,250),pil.Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.help_data,background="darkblue",border="2")
        b1.place(x=850,y=360,width=250,height=250,bordermode="outside")

        b1_1=Button(bg_img,text="Contact",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=850,y=580,width=250,height=40)


    def open_img(self):
        os.startfile("D:\\project exhibition compet\\data")
    
    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
       if self.iExit >0:
          self.root.destroy()
       else:
          return 






    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
     
    def attendance_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Attendance(self.new_window)
       
       
    def help_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Help(self.new_window)
   





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()