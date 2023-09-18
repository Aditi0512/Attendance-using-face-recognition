from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
import cv2
from cv2 import BORDER_ISOLATED,BORDER_REFLECT,resize
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Help Desk",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45) 
        #student detail button
        img1=Image.open(r"E:\imagesproj\1.jpg")
        img1=img1.resize((1400,720),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=55,width=1400,height=720)

        dev_label=Label(f_lbl,text="Email:choudharyaditi947@gmail.com",font=("time new roman",20,"bold"),bg="white")
        dev_label.place(x=450,y=300)



if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()                   