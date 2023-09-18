from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
import cv2
from cv2 import BORDER_ISOLATED,BORDER_REFLECT,resize
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45) 
        #student detail button
        img1=Image.open(r"E:\imagesproj\developer.JPEG")
        img1=img1.resize((1400,720),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=55,width=1400,height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=500,height=500) 
        
        img2=Image.open(r"E:\imagesproj\face_7.JPEG")
        img2=img2.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,text="Hello my name,Aditi",font=("time new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am currently pursuing BTech",font=("time new roman",10,"bold"),bg="white")
        dev_label.place(x=0,y=40)





if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()                   