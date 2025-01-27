from tkinter import*
from tkinter import ttk
from pil import Image
from PIL import Image,ImageTk
from tkinter import messagebox
from pil import Image,ImageTk
import pil.Image
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x800+0+0")
        self.root.title("face recognition System")

        #============= variables===================
        
        self.var_atten_dep=StringVar()
        self.var_year=StringVar()
        self.var_div=StringVar()
        self.var_sub=StringVar()
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        

        img3=pil.Image.open("D:\\project exhibition compet\\face\\back.jfif")
        img3=img3.resize((1330,690),pil.Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1350,height=690)

        title_lb1=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1330,height=50)
        

         
        Left_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=30,y=55,width=650,height=500)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=20,width=630,height=450)
        
        
        Currrent_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",15,"bold"))
        Currrent_course_frame.place(x=5,y=5,width=630,height=150)

        # Department
        dept_label=Label(Currrent_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=10,pady=30,sticky=W)

        dept_combo=ttk.Combobox(Currrent_course_frame,textvariable=self.var_atten_dep,font=("times new roman",10,"bold"),state="readonly",width=20)
        dept_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


         # year
        Course_label=Label(Currrent_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=25,sticky=W)

        Course_combo=ttk.Combobox(Currrent_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        Course_combo["values"]=("Select Course","FE","SE","TE","BE")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=0,pady=10,sticky=W)


        
        class_div_label=Label(Currrent_course_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        div_combo=ttk.Combobox(Currrent_course_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),state="readonly",width=15)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
      
        
        subject_label=Label(Currrent_course_frame,text="Subject Name:",font=("times new roman",12,"bold"),bg="white")
        subject_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        subject_entry=ttk.Entry(Currrent_course_frame,width=20,textvariable=self.var_sub,font=("times new roman",10,"bold"))
        subject_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",13,"bold"))
        class_student_frame.place(x=5,y=160,width=630,height=400)

  
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        
        dateLabel=Label(class_student_frame,text="Date:",bg="white",font="comicsansansns 12 bold")
        dateLabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        atten_date=ttk.Entry(class_student_frame,width=20,textvariable=self.var_atten_date,font="comicsansansns 12 bold")
        atten_date.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        

        timeLabel=Label(class_student_frame,text="Time:",bg="white",font="comicsansansns 12 bold")
        timeLabel.grid(row=2,column=0,padx=10,pady=5)

        atten_time=ttk.Entry(class_student_frame,width=18,textvariable=self.var_atten_time,font="comicsansansns 12 bold")
        atten_time.grid(row=2,column=1,padx=10,pady=8)
        
        
        
        attendanceLabel=Label(class_student_frame,text="Attendance Status",bg="white",font="comicsansansns 11 bold")
        attendanceLabel.grid(row=2,column=2,pady=15)


        self.atten_status=ttk.Combobox(class_student_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansansns 11 bold",state="comicsansansns 11 bold")
        self.atten_status["values"]=("status","Present","Absent")
        self.atten_status.grid(row=2,column=3,pady=8)
        self.atten_status.current(0)

       
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=267,width=630,height=40)

        save_btn=Button(btn_frame,text="Import cvs",command=self.importCsv,width=16,font=("times new roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export cvs",command=self.exportCsv,width=16,font=("times new roman",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",11,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",11,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
       
        Right_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=690,y=55,width=640,height=500)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=620,height=425)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("department","year","division","subject","id","name","roll","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("year",text="Year")
        self.AttendanceReportTable.heading("division",text="Division")
        self.AttendanceReportTable.heading("subject",text="Subject")
        self.AttendanceReportTable.heading("id",text="Id")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("department",width=100) 
        self.AttendanceReportTable.column("year",width=100)
        self.AttendanceReportTable.column("division",width=100)
        self.AttendanceReportTable.column("subject",width=100)
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll",width=100)        
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+"Successfully")
        except Exception as es:
           messagebox.showerror("Error",f"Due to :{str(es)} ",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_dep.set(rows[0])
        self.var_year.set(rows[1])
        self.var_div.set(rows[2])
        self.var_sub.set(rows[3])
        self.var_atten_id.set(rows[4])
        self.var_atten_name.set(rows[5])
        self.var_atten_roll.set(rows[6])
        self.var_atten_date.set(rows[7])
        self.var_atten_time.set(rows[8])
        self.var_atten_attendance.set(rows[9])

    def reset_data(self):
        self.var_atten_dep.set("")
        self.var_year.set("")
        self.var_div.set("")
        self.var_sub.set("")
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_attendance.set("")
        


if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()

    




