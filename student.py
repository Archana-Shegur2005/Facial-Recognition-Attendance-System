from ctypes.wintypes import RGB
from tkinter import*
from pil import Image
from tkinter import ttk
from pil import Image,ImageTk
import pil.Image
from tkinter import messagebox
import os
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x800+0+0")
        self.root.title("student registration")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()
        

        img3=pil.Image.open("D:\\project exhibition compet\\face\\back.jfif")
        img3=img3.resize((1330,690),pil.Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1350,height=690)

        title_lb1=Label(self.root,text="Student Registration Management",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1330,height=50)
        
        
        Left_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=30,y=55,width=650,height=500)


        Currrent_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course information",font=("times new roman",10,"bold"))
        Currrent_course_frame.place(x=5,y=5,width=630,height=120)

        
        dept_label=Label(Currrent_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo=ttk.Combobox(Currrent_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly",width=20)
        dept_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        Course_label=Label(Currrent_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)

        Course_combo=ttk.Combobox(Currrent_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly",width=20)
        Course_combo["values"]=("Select Course","FE","SE","TE","BE")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        year_label=Label(Currrent_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Currrent_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        semester_label=Label(Currrent_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(Currrent_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","semester-1","semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",8,"bold"))
        class_student_frame.place(x=5,y=150,width=630,height=400)


        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",8,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",8,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",8,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",8,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",8,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),state="readonly",width=15)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",10,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",8,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",8,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly",width=15)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",8,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",8,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        email_label=Label(class_student_frame,text="Email:",font=("times new roman",8,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",8,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",8,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",8,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        address_label=Label(class_student_frame,text="Address:",font=("times new roman",8,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",8,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        teacher_label=Label(class_student_frame,text="Subject Name:",font=("times new roman",8,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",8,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)



        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)



        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=630,height=30)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",11,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=280,width=635,height=33)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",11,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",11,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        Right_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=690,y=55,width=640,height=500)


        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",10,"bold"))
        search_frame.place(x=5,y=50,width=630,height=60)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",10,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phono_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=110,width=630,height=355)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("Dep","course","Year","Semester","Student_id","Name","Division","Roll","Gender","Dob","Email","Phone","Address","Teacher","PhotoSample"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("course",text="Couse")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student_id",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll",text="Division")
        self.student_table.heading("Gender",text="Roll no")
        self.student_table.heading("Division",text="Gender")
        self.student_table.heading("Dob",text="Date Of Birth")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("PhotoSample",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student_id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("PhotoSample",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


      

    def add_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
        try:
           conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
           my_cursor=conn.cursor()
           my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                    
                                                                                                         ))
           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("Success","Student details added successfully",parent=self.root)
        except Exception as es:
           messagebox.showerror("Error",f"Due to :{str(es)} ",parent=self.root)


    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()

      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("",END,values=i)
        conn.commit()
      conn.close()


    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]

      self.var_dep.set(data[0])
      self.var_course.set(data[1])
      self.var_year.set(data[2])
      self.var_semester.set(data[3])
      self.var_std_id.set(data[4])
      self.var_std_name.set(data[5])
      self.var_div.set(data[6])
      self.var_roll.set(data[7])
      self.var_gender.set(data[8])
      self.var_dob.set(data[9])
      self.var_email.set(data[10])
      self.var_phone.set(data[11])
      self.var_address.set(data[12])
      self.var_teacher.set(data[13])
      self.var_radio1.set(data[14])


    def update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
        try:
          Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
          if Update>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get()            
                                                                                                                                                                                                        ))
          else:
            if not Update:
              return
          messagebox.showinfo("Success","Student details Successfully update completed",parent=self.root)
          conn.commit()
          self.fetch_data()
          conn.close()
        except Exception as es:
          messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)


    def delete_data(self):
      if self.var_std_id.get()=="":
        messagebox.showerror("Error","Student id must be required",parent=self.root)
      else:
        try:
          delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
          if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
            my_cursor=conn.cursor()
            sql="delete from student where Student_id=%s"
            val=(self.var_std_id.get(),)
            my_cursor.execute(sql,val)
          else:
            if not delete:
              return
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Delete","Successfully delete student details..!",parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)


    def reset_data(self):
      self.var_dep.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester")
      self.var_std_id.set("")
      self.var_std_name.set("")
      self.var_div.set("Select Division")
      self.var_roll.set("")
      self.var_gender.set("Male")
      self.var_dob.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_address.set("")
      self.var_teacher.set("")
      self.var_radio1.set("")



    def generate_dataset(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
          messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
        try:
          conn=mysql.connector.connect(host="localhost",username="root",password="NPA#29kgrw9",database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from student")
          myresult=my_cursor.fetchall()
          id=0
          for x in myresult:
              id+=1
          my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get()==id+1
                                                                                                                                                                                                                     
                                                                                                                                                                                                        ))

          conn.commit()
          self.fetch_data()
          self.reset_data()
          conn.close()


          face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
          
          
          def face_cropped(img):
            #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(img,1.3,5)

            for (x,y,w,h) in faces:
              face_cropped=img[y:y+h,x:x+w]
              return face_cropped
            
          cap=cv2.VideoCapture(0)
          img_id=0
          while True:
              ret,my_frame=cap.read()
              if face_cropped(my_frame) is not None:
                  img_id+=1
                  face=cv2.resize(face_cropped(my_frame),(500,500))
                  #face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                  file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                  cv2.imwrite(file_name_path,face)
                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                  cv2.imshow("Cropped Face",face)

              if cv2.waitKey(1)==13 or int(img_id)==100:
                 break
          cap.release()
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Generating data set completed !")
        except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  






if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()