from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk,ImageDraw
from student import Student
from train import Training_system
import os
from cv2 import BORDER_ISOLATED,resize
from time import strftime,time
from datetime import datetime
from pytz import timezone
from attendance import Attendance
from face_recognition import Face_Recognition
from developer import Developer
from help import Help
class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("face recognition system")
        
        img=Image.open(r"E:\imagesproj\facerecognition_1.jpg")
        img=img.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)

        img1=Image.open(r"E:\imagesproj\face_3.JPEG")
        img1=img1.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=130)
 
        img2=Image.open(r"E:\imagesproj\face_2.JPEG")
        img2=img2.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=130)

        img3=Image.open(r"E:\imagesproj\back.JPEG")
        img3=img3.resize((1400,790),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1400,height=790)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("time new roman",15,"bold"),bg="white",fg="red")     
        lbl.place(x=8,y=0,width=120,height=50)
        time()
        
        #student detail button
        img4=Image.open(r"E:\imagesproj\face_7.JPEG")
        img4=img4.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)

        b2=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("time new roman",10,"bold"),bg="white",fg="black")
        b2.place(x=200,y=250,width=150,height=40)
        #detect face button
        img5=Image.open(r"E:\imagesproj\face.jpg")
        img5=img5.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=100,width=150,height=150)

        b2=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("time new roman",10,"bold"),bg="white",fg="black")
        b2.place(x=450,y=250,width=150,height=40)

        #Attendance button
        img6=Image.open(r"E:\imagesproj\att.JPEG")
        img6=img6.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=100,width=150,height=150)

        b2=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("time new roman",10,"bold"),bg="white",fg="black")
        b2.place(x=700,y=250,width=150,height=40)
        # Help Button
        img7=Image.open(r"E:\imagesproj\help.JPEG")
        img7=img7.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=950,y=100,width=150,height=150)

        b2=Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_data,font=("time new roman",10,"bold"),bg="white",fg="black")
        b2.place(x=950,y=250,width=150,height=40)
       
       #Train button
        img8=Image.open(r"E:\imagesproj\train.JPEG")
        img8=img8.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=320,width=150,height=150)

        b2=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("time new roman",10,"bold"),bg="white",fg="black")
        b2.place(x=200,y=470,width=150,height=40)

        #Photos button
        img9=Image.open(r"E:\imagesproj\photos.jpg")
        img9=img9.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=320,width=150,height=150)

        b2=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("time new roman",10,"bold"),bg="white",fg="black")
        b2.place(x=450,y=470,width=150,height=40)
       
       #Developer button
        img10=Image.open(r"E:\imagesproj\developer.JPEG")
        img10=img10.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=320,width=150,height=150)

        b2=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("time new roman",10,"bold"),bg="white",fg="black")
        b2.place(x=700,y=470,width=150,height=40)

        #Exit button
        img11=Image.open(r"E:\imagesproj\exit.JPEG")
        img11=img11.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b1.place(x=950,y=320,width=150,height=150)

        b2=Button(bg_img,text="EXIT",cursor="hand2",command=self.iexit,font=("time new roman",10,"bold"),bg="white",fg="black")
        b2.place(x=950,y=470,width=150,height=40)




    def open_img(self):
        os.startfile("data")  

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("face recognition","Are you sure you want to exit",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return          
 
 ## ===================Function button

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window) 
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Training_system(self.new_window) 
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)  
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)         
       

if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()        