from tkinter import*
from pil import Image
from tkinter import ttk
from pil import Image,ImageTk
import pil.Image
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x800+0+0")
        self.root.title("face Recognition System")
        
        title_lb1=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=-2,width=1365,height=40)
        
        
        img3=pil.Image.open("D:\\project exhibition compet\\face\\b.jpg")
        img3=img3.resize((1330,660),pil.Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=35,width=1350,height=660)
        
        img_top=pil.Image.open("D:\\project exhibition compet\\face\\facet.png")
        img_top=img_top.resize((550,320),pil.Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(bg_img,image=self.photoimg_top)
        f_lb1.place(x=15,y=7,width=550,height=320)
        
        img_bottom=pil.Image.open("D:\\project exhibition compet\\face\\leftimg.jpg")
        img_bottom=img_bottom.resize((550,300),pil.Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(bg_img,image=self.photoimg_bottom)
        f_lb1.place(x=15,y=330,width=550,height=300)
        
        
        b1_1=Button(bg_img,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="red",fg="white")
        b1_1.place(x=610,y=570,width=600,height=70)


        
      
    # train
    def train_classifier(self):
        data_dir=("D:\\project exhibition compet\\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)    

        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")







if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()