from tkinter import*
from PIL import Image
from tkinter import ttk
from ctypes.wintypes import RGB
from pil import Image
from PIL import Image,ImageTk
import PIL.Image
import pil.Image
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector

class Register_admin:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x800+0+0")
        self.root.title("Register")
        
        #==========variables=======
        self.var_uname=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()


        title_lb1=Label(self.root,text="Admin Registration",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1365,height=45)
        Rsubject=StringVar()
        Rsender=StringVar()
        img3=pil.Image.open("D:\\project exhibition compet\\face\\he1.jpg")
        img3=img3.resize((1330,690),pil.Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1350,height=690)

      
        Left_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",12,"bold"))
        Left_frame.place(x=450,y=50,width=400,height=550)
        
        head_label=Label(Left_frame,text="Registration Details",font=("times new roman",15,"bold"),bg="white")
        head_label.place(x=90,y=10,width=200,height=50)
        
        
        fullName_label=Label(Left_frame,text="Username ",font=("times new roman",12,"bold"),bg="white")
        fullName_label.place(x=40,y=160,width=200,height=50)
        self.var_sub=StringVar()
        fullName_entry=ttk.Entry(Left_frame,width=10,textvariable=self.var_uname,font=("times new roman",14,"bold"))
        fullName_entry.place(x=40,y=200,width=300,height=30)
        img4=pil.Image.open("D:\\project exhibition compet\\face\\icon\\pa.png")
        img4=img4.resize((30,25),pil.Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(Left_frame,image=self.photoimg4,bg="white")
        bg_img.place(x=45,y=170,width=30,height=25)
        
        pass_label=Label(Left_frame,text="Password ",font=("times new roman",12,"bold"),bg="white")
        pass_label.place(x=40,y=240,width=200,height=50)
        self.var_sub=StringVar()
        passName_entry=ttk.Entry(Left_frame,width=10,textvariable=self.var_pass,font=("times new roman",14,"bold"))
        passName_entry.place(x=40,y=280,width=300,height=30)
        img6=pil.Image.open("D:\\project exhibition compet\\face\\icon\\pa.png")
        img6=img6.resize((30,25),pil.Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        bg_img=Label(Left_frame,image=self.photoimg6,bg="white")
        bg_img.place(x=45,y=250,width=30,height=25)
        
        email_label=Label(Left_frame,text="Email Id ",font=("times new roman",12,"bold"),bg="white")
        email_label.place(x=40,y=80,width=200,height=50)

        self.var_mail=StringVar()
        email_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.place(x=40,y=120,width=300,height=30)
        img5=pil.Image.open("D:\\project exhibition compet\\face\\icon\\user4.png")
        img5=img5.resize((30,25),pil.Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        bg_img=Label(Left_frame,image=self.photoimg5,bg="white")
        bg_img.place(x=45,y=90,width=30,height=25)
        
        security_Q=Label(Left_frame,text="Select Security Questions",font=("times new roman",12,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=330)

        self.combo_security_Q=ttk.Combobox(Left_frame,font=("times new roman",12,"bold"),textvariable=self.var_securityQ,state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Best Friend Name","Your pet Name")
        self.combo_security_Q.place(x=50,y=360,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(Left_frame,text="Security Answer",font=("times new roman",12,"bold"),bg="white",fg="black")
        security_A.place(x=50,y=410)

        self.txt_security=ttk.Entry(Left_frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=50,y=440,width=250)
    
        
        b1_1=Button(Left_frame,text="Register",command=self.register_data,font=("times new roman",16,"bold"),bg="#038cfc",fg="white")
        b1_1.place(x=40,y=490,width=300,height=35)
        
        
        
    def register_data(self):
        if self.var_uname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
            
            my_cursor=conn.cursor()
            Query=("select * from adminregister where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(Query,value)
            
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exits,please try another email")
                
            else:
                    my_cursor.execute("insert into adminregister values(%s,%s,%s,%s,%s)",(
                                                                                                self.var_uname.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_securityQ.get(),
                                                                                                self.var_securityA.get(),
                                                                                                self.var_pass.get()
                                                                                    
                                                                                          ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register successfully",parent=self.root) 
               
            self.root.destroy()
       
       
 
        
if __name__ == "__main__":
    root=Tk()
    obj=Register_admin(root)
    root.mainloop()