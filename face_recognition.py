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


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x800+0+0")
        self.root.title("Attendance")
        
        self.var_dep=StringVar()
        self.var_sel=StringVar()
        
        title_lb1=Label(self.root,text="Face Recognition Attendance",font=("times new roman",25,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=-2,width=1365,height=40)
        
        
        img3=pil.Image.open("D:\\project exhibition compet\\face\\bg.jpg")
        img3=img3.resize((1330,690),pil.Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=40,width=1350,height=690)
        
        img_bottom=pil.Image.open("D:\\project exhibition compet\\face\\studentface.jpg")
        img_bottom=img_bottom.resize((650,650),pil.Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(bg_img,image=self.photoimg_bottom)
        f_lb1.place(x=10,y=0,width=600,height=650)
        
        Left_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",12,"bold"))
        Left_frame.place(x=650,y=130,width=650,height=400)
        
        head_label=Label(Left_frame,text="Take Attendance  ",font=("times new roman",20,"bold"),bg="white")
        head_label.place(x=200,y=20,width=300,height=50)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
        my_cursor=conn.cursor()
        my_list=[]     
        my_list2=[]   
        my_cursor.execute("select distinct(dept) as dept from combo")
        my_list=my_cursor.fetchall()
        
        my_cursor.execute("select distinct(year) as year from combo where dept='CSE'")
        my_list2=my_cursor.fetchall()
        
        
        
        set=StringVar()
        
        sub_label=Label(Left_frame,text="Select Department : ",font=("times new roman",15,"bold"),bg="white")
        sub_label.place(x=50,y=110,width=200,height=50)

        sub_combo=ttk.Combobox(Left_frame,font=("times new roman",12,"bold"),values=my_list,textvariable=self.var_sel,state="readonly",width=20)
        sub_combo.place(x=250,y=120,width=230,height=30)
        
        
        year_label=Label(Left_frame,text="Select Year : ",font=("times new roman",15,"bold"),bg="white")
        year_label.place(x=50,y=170,width=200,height=50)

        year_combo=ttk.Combobox(Left_frame,values=my_list2,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo.place(x=250,y=180,width=230,height=30)
        
        
        dept_label=Label(Left_frame,text="Select Subject : ",font=("times new roman",15,"bold"),bg="white")
        dept_label.place(x=50,y=230,width=200,height=50)

        dept_combo=ttk.Combobox(Left_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dept_combo["values"]=("Select Subject","Python","Java","Data Structure","Ruby")
        dept_combo.current(0)
        dept_combo.place(x=250,y=240,width=230,height=30)
        
        

        b1_1=Button(Left_frame,text="Take Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=230,y=300,width=180,height=40)
    
    
    def mark_attendance(self,i,r,n,d):
        with open("napls.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select course from student where Student_id="+str(i))
                c=my_cursor.fetchone()
                c="+".join(c)
                my_cursor.execute("select Division from student where Student_id="+str(i))
                di=my_cursor.fetchone()
                di="+".join(di)
                st=self.var_dep.get();
                f.writelines(f"\n{d},{c},{di},{st},{i},{n},{r},{d1},{dtString},Present")
                    
                    
               
        
        
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unkown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,y]
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.3,5,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome To face Recognition",img)
            
            k=cv2.waitKey(1)
            if k==ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()  

    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()        