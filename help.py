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


class Help:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x800+0+0")
        self.root.title("Contact")

        title_lb1=Label(self.root,text="Contact Us",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1365,height=45)
        Rsubject=StringVar()
        Rsender=StringVar()
        img3=pil.Image.open("D:\\project exhibition compet\\face\\he1.jpg")
        img3=img3.resize((1330,690),pil.Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1350,height=690)

      
        Left_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",12,"bold"))
        Left_frame.place(x=650,y=80,width=600,height=500)
        
        head_label=Label(Left_frame,text="Send Message ",font=("times new roman",20,"bold"),bg="white")
        head_label.place(x=20,y=20,width=200,height=50)
        
        
        fullName_label=Label(Left_frame,text="Full Name :",font=("times new roman",16,"bold"),bg="white")
        fullName_label.place(x=0,y=190,width=200,height=50)
        self.var_sub=StringVar()
        fullName_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_sub,font=("times new roman",14,"bold"))
        fullName_entry.place(x=155,y=195,width=400,height=35)
       
        email_label=Label(Left_frame,text="Email ID :",font=("times new roman",16,"bold"),bg="white")
        email_label.place(x=0,y=120,width=200,height=50)

        self.var_mail=StringVar()
        email_entry=ttk.Entry(Left_frame,width=20,textvariable=self.var_mail,font=("times new roman",14,"bold"))
        email_entry.place(x=155,y=125,width=400,height=35)
        
        message_label=Label(Left_frame,text="Enter Query :",font=("times new roman",16,"bold"),bg="white")
        message_label.place(x=0,y=270,width=200,height=50)
        self.var_msg=StringVar()
        message_entry=Text(Left_frame,width=50,font=("times new roman",14,"bold"))
        message_entry.place(x=155,y=275,width=400,height=100)
        
        def sendemail():
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()

            server.login('archanashegur29@gmail.com','xiqo cwzx upxk aysp')
            mess=f"subject: {self.var_sub.get()}\n\n{message_entry.get(1.0,'end')}"
            sendermail=self.var_mail.get()
            server.sendmail('archanashegur29@gmail.com',sendermail,mess)
        
        
        
        right_frame=LabelFrame(bg_img,bd=2,bg="",relief=RIDGE,text="",font=("times new roman",12,"bold"))
        right_frame.place(x=30,y=130,width=450,height=400)
       
        
        ema_label=Label(right_frame,text="Email ID ",font=("times new roman",16,"bold"),bg="#0b2150",fg="#03e7fc")
        ema_label.place(x=177,y=160,width=100,height=25)
        emai_label=Label(right_frame,text="archanashegur29@gmail.com ",font=("times new roman",16,"bold"),bg="#0b2150",fg="white")
        emai_label.place(x=184,y=190,width=250,height=25)
        img4=pil.Image.open("D:\\project exhibition compet\\face\\icon\\email3.png")
        img4=img4.resize((120,70),pil.Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(right_frame,image=self.photoimg4,bg="#0b2150")
        bg_img.place(x=67,y=150,width=120,height=70)
        
        
        phone_label=Label(right_frame,text="Phone Number ",font=("times new roman",16,"bold"),bg="#0b2150",fg="#03e7fc")
        phone_label.place(x=150,y=300,width=220,height=25)
        pho_label=Label(right_frame,text="7620734520",font=("times new roman",16,"bold"),bg="#0b2150",fg="white")
        pho_label.place(x=120,y=330,width=250,height=25)
        img6=pil.Image.open("D:\\project exhibition compet\\face\\icon\\add1.png")
        img6=img6.resize((140,80),pil.Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        bg_img=Label(right_frame,image=self.photoimg6,bg="#0b2150")
        bg_img.place(x=53,y=280,width=140,height=80)
        
        add_label=Label(right_frame,text="Address ",font=("times new roman",16,"bold"),bg="#0b2150",fg="#03e7fc")
        add_label.place(x=175,y=10,width=100,height=25)
        addr_label=Label(right_frame,text="997/3, Nilam nagar,",font=("times new roman",12,"bold"),bg="#0b2150",fg="white")
        addr_label.place(x=100,y=40,width=300,height=25)
        addr1_label=Label(right_frame,text=" MIDC, Solapur ",font=("times new roman",12,"bold"),bg="#0b2150",fg="white")
        addr1_label.place(x=90,y=70,width=300,height=25)
        img5=pil.Image.open("D:\\project exhibition compet\\face\\icon\\loca1.png")
        img5=img5.resize((90,80),pil.Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        bg_img=Label(right_frame,image=self.photoimg5,bg="#0b2150")
        bg_img.place(x=85,y=15,width=90,height=80)
        
        
        b1_1=Button(Left_frame,text="Send",font=("times new roman",16,"bold"),command=sendemail,bg="#038cfc",fg="white")
        b1_1.place(x=230,y=430,width=180,height=45)
       
    
            
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()