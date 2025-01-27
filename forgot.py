from tkinter import*
from PIL import Image
from tkinter import ttk
from ctypes.wintypes import RGB
from pil import Image
from PIL import Image,ImageTk
import PIL.Image
import pil.Image
from tkinter import messagebox
import mysql.connector

class Forgot_pass:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x800+0+0")
        self.root.title("face Recognition System")

        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_uname=StringVar()
        self.var_conpass=StringVar()

        title_lb1=Label(self.root,text="Admin Details",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1365,height=45)
        Rsubject=StringVar()
        Rsender=StringVar()
        img3=pil.Image.open("D:\\project exhibition compet\\face\\he1.jpg")
        img3=img3.resize((1330,690),pil.Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1350,height=690)

        global Left_frame
      
        Left_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",12,"bold"))
        Left_frame.place(x=450,y=50,width=400,height=550)
        
        head_label=Label(Left_frame,text="Forgot Password",font=("times new roman",12,"bold"),bg="white")
        head_label.place(x=90,y=5,width=200,height=50)
        
        email_label=Label(Left_frame,text="User Name ",font=("times new roman",12,"bold"),bg="white")
        email_label.place(x=40,y=67,width=200,height=50)

        email_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_uname,font=("times new roman",12,"bold"))
        email_entry.place(x=50,y=110,width=280,height=25)
        img5=pil.Image.open("D:\\project exhibition compet\\face\\icon\\user4.png")
        img5=img5.resize((30,25),pil.Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        bg_img=Label(Left_frame,image=self.photoimg5,bg="white")
        bg_img.place(x=45,y=80,width=30,height=25)
        
        security_Q=Label(Left_frame,text="Select Security Questions",font=("times new roman",12,"bold"),bg="white",fg="black")
        security_Q.place(x=0,y=160,width=280)

        self.combo_security_Q=ttk.Combobox(Left_frame,font=("times new roman",12,"bold"),textvariable=self.var_securityq,state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Best Friend Name","Your pet Name")
        self.combo_security_Q.place(x=50,y=190,width=280)
        self.combo_security_Q.current(0)
        
        security_A=Label(Left_frame,text="Security Answer",font=("times new roman",12,"bold"),bg="white",fg="black")
        security_A.place(x=50,y=240)

        self.txt_security=ttk.Entry(Left_frame,textvariable=self.var_securitya,font=("times new roman",12))
        self.txt_security.place(x=50,y=270,width=280,height=25)
        
        
        global b1_1
        b1_1=Button(Left_frame,text="Verify",command=self.forgot_p,font=("times new roman",16,"bold"),bg="#038cfc",fg="white")
        b1_1.place(x=50,y=310,width=280,height=35)
        
        
        
    def forgot_p(self):
        
        if self.var_securitya.get()=="" or self.var_uname.get()=="" or self.var_securityq.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
            my_cursor=conn.cursor()
            sql="select * from adminregister where username='%s' and securityQ='%s' and securityA='%s'" %(self.var_uname.get(),self.var_securityq.get(), self.var_securitya.get())
            my_cursor.execute(sql)
            if my_cursor.fetchone():
                messagebox.showinfo("Success","Varified successfully",parent=self.root)
                b1_1=Button(Left_frame,text="Verify",command=self.forgot_p,font=("times new roman",16,"bold"),bg="#038cfc",fg="white")
                b1_1.place(x=50,y=310,width=280,height=35)
        
                b1_1=Button(Left_frame,text="Change Password",command=self.con_pass,font=("times new roman",16,"bold"),bg="green",fg="white")
                b1_1.place(x=50,y=460,width=280,height=35)
                
                
                pass_label=Label(Left_frame,text="Enter New Passowrd",font=("times new roman",15,"bold"),bg="white",fg="black")
                pass_label.place(x=50,y=370)
                self.txt_security=ttk.Entry(Left_frame,textvariable=self.var_conpass,font=("times new roman",12))
                self.txt_security.place(x=50,y=415,width=280,height=30)
                
            else:
                messagebox.showerror("Error","Invalid ")    
       
    def con_pass(self):
        
        if self.var_conpass.get()==" " :
            messagebox.showerror("Error","All fields are required")
            
        else:
            try:
                Update=messagebox.askyesno("Update","Are you sure you want to change password",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="update adminregister set password='%s' where username='%s'" %(self.var_uname.get(),self.var_conpass.get())
                    
                    my_cursor.execute(sql)
                    my_cursor.fetchall()
                    conn.commit()
                    messagebox.showinfo("Success","Password change Successfully",parent=self.root)
                    self.root.destroy()
                else:
                    if not Update:
                        messagebox.showinfo("Error","not change completed",parent=self.root)
                
                conn.commit()
                conn.close()
            except Exception as es:
                 messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)    
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Forgot_pass(root)
    root.mainloop()