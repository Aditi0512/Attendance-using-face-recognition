from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
import cv2
from cv2 import BORDER_ISOLATED,BORDER_REFLECT,resize
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os
import csv
from tkinter import filedialog
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("Face Recognition System")

        #===========variable=========
        self.var_atten_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_atten=StringVar()

        #-------background-------------
        img=Image.open(r"E:\imagesproj\student.JPEG")
        img=img.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)

        img1=Image.open(r"E:\imagesproj\student2.jpg")
        img1=img1.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=130)
 
        img2=Image.open(r"E:\imagesproj\student3.jpg")
        img2=img2.resize((450,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=130)

        img3=Image.open(r"E:\imagesproj\back.JPEG")
        img3=img3.resize((1400,790),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1400,height=790)

        title_lbl=Label(bg_img,text="ATTENDANCE",font=("time new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1250,height=600) 

        ##left label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text=" Student Attendance Detail",font=("time new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=600,height=420)
        
         ##right label frame

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=650,y=10,width=500,height=420)
        

        #student id
        attendanceid_label=Label(Left_frame,text="Attendance Id",font=("time new roman",10,"bold"),bg="white")
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceid_entry=ttk.Entry(Left_frame,width=10,textvariable=self.var_atten_id,font=("time new roman",10,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student rollno
        roll_label=Label(Left_frame,text="Roll No.",font=("time new roman",10,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(Left_frame,width=10,textvariable=self.var_roll,font=("time new roman",10,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


       #student name
        name_label=Label(Left_frame,text="Student name",font=("time new roman",10,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(Left_frame,width=10,textvariable=self.var_name,font=("time new roman",10,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

       #time
        time_label=Label(Left_frame,text="Time",font=("time new roman",10,"bold"),bg="white")
        time_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(Left_frame,width=10,textvariable=self.var_time,font=("time new roman",10,"bold"))
        time_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #date
        date_label=Label(Left_frame,text="Date",font=("time new roman",10,"bold"),bg="white")
        date_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(Left_frame,width=10,textvariable=self.var_date,font=("time new roman",10,"bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

   #attendance
        #student id
        attendanceid_label=Label(Left_frame,text="Attendance Status",font=("time new roman",10,"bold"),bg="white")
        attendanceid_label.grid(row=2,column=2,padx=10)
        self.attendance_combo=ttk.Combobox(Left_frame,textvariable=self.var_atten,font=("time new roman",10,"bold"),state="read only")
        self.attendance_combo["values"]=("Status","Present","Absent")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)


        #button frame

        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=360,width=570,height=23)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv,width=26,font=("time new roman",6,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        
        update_btn=Button(btn_frame,text="Export csv",width=26,command=self.exportcsv,font=("time new roman",6,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
 
        delete_btn=Button(btn_frame,text="Update",width=27,font=("time new roman",6,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=27,font=("time new roman",6,"bold"),command=self.reset_data,bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

 #right label frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=11,width=489,height=370)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("id","roll","name","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("id",text="Attendance Id")
        

        self.student_table.heading("roll",text="Roll No.")
        
        self.student_table.heading("name",text="Name")
        
        self.student_table.heading("time",text="Time")
        
        self.student_table.heading("date",text="Date")
        
        self.student_table.heading("attendance",text="Attendance ")
        
        self.student_table["show"]="headings"
        self.student_table.column("id",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("time",width=100)
        self.student_table.column("date",width=100)
        self.student_table.column("attendance",width=100)
        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)

    #=================fetch data=========
    def fetchdata(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data export","your data is exported"+os.path.basename(fln)+"successful")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0]) 
        self.var_roll.set(rows[1]) 
        self.var_name.set(rows[2])
        self.var_time.set(rows[3])  
        self.var_date.set(rows[4])  
        self.var_atten.set(rows[5])    
  
  
    def reset_data(self):
        self.var_atten_id.set("") 
        self.var_roll.set("") 
        self.var_name.set("")
        self.var_time.set("")  
        self.var_date.set("")  
        self.var_atten.set("") 














if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()                   