from tkinter import*
from PIL import Image
from tkinter import ttk
from ctypes.wintypes import RGB
from pil import Image
from PIL import Image,ImageTk
import PIL.Image
import pil.Image
from tkinter import messagebox
from registeradmin import Register_admin
from forgot import Forgot_pass
from main1 import Face_Recognition_System
import mysql.connector

class Login_admin:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x800+0+0")
        self.root.title("login")
        
        self.var_uname=StringVar()
        self.var_pass=StringVar()
        
        title_lb1=Label(self.root,text="Admin Login",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1365,height=45)
        Rsubject=StringVar()
        Rsender=StringVar()
        img3=pil.Image.open("D:\\project exhibition compet\\face\\he1.jpg")
        img3=img3.resize((1330,690),pil.Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1350,height=690)

      
        Left_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",12,"bold"))
        Left_frame.place(x=450,y=80,width=400,height=450)
        
        head_label=Label(Left_frame,text="Login",font=("times new roman",20,"bold"),bg="white")
        head_label.place(x=90,y=10,width=200,height=50)
        
        
        fullName_label=Label(Left_frame,text="Password ",font=("times new roman",14,"bold"),bg="white")
        fullName_label.place(x=40,y=180,width=200,height=50)
        fullName_entry=ttk.Entry(Left_frame,width=10,textvariable=self.var_pass,font=("times new roman",14,"bold"))
        fullName_entry.place(x=40,y=220,width=300,height=35)
        img4=pil.Image.open("D:\\project exhibition compet\\face\\icon\\pa.png")
        img4=img4.resize((30,25),pil.Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(Left_frame,image=self.photoimg4,bg="white")
        bg_img.place(x=45,y=190,width=30,height=25)
        
        email_label=Label(Left_frame,text="User Name ",font=("times new roman",16,"bold"),bg="white")
        email_label.place(x=40,y=80,width=200,height=50)

        email_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_uname,font=("times new roman",14,"bold"))
        email_entry.place(x=40,y=120,width=300,height=35)
        img5=pil.Image.open("D:\\project exhibition compet\\face\\icon\\user4.png")
        img5=img5.resize((30,25),pil.Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        bg_img=Label(Left_frame,image=self.photoimg5,bg="white")
        bg_img.place(x=45,y=90,width=30,height=25)
        
        
        
        
        b1_1=Button(Left_frame,text="Login",command=self.login,font=("times new roman",16,"bold"),bg="#038cfc",fg="white")
        b1_1.place(x=40,y=290,width=300,height=35)
        
        forgot=Button(Left_frame,text="Forgot Password",font=("times new roman",12,"bold"),command=self.forgot_detais,bg="white",fg="black",borderwidth=0)
        forgot.place(x=40,y=350,width=120,height=35)
        
        register_label=Button(Left_frame,text="Register",command=self.register_details,font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        register_label.place(x=260,y=350,width=80,height=35)

        
       
    def forgot_detais(self):
        self.new_window=Toplevel(self.root)
        self.app=Forgot_pass(self.new_window)    
        
    
            
    def register_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_admin(self.new_window)   
        
        
    def login(self):
        
        if self.var_uname.get()==" " or self.var_pass.get()==" ":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
            my_cursor=conn.cursor()
            sql="select * from adminregister where username='%s' and password='%s'" %(self.var_uname.get(), self.var_pass.get())
            my_cursor.execute(sql)
            if my_cursor.fetchone():
                messagebox.showinfo("Success","Login successfully",parent=self.root)
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
                
                
                
            else:
                messagebox.showerror("Error","Invalid username or password")
if __name__ == "__main__":
    root=Tk()
    obj=Login_admin(root)
    root.mainloop()