from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
import cv2
from cv2 import BORDER_ISOLATED,BORDER_REFLECT,resize
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("Face Recognition System")
        
        #===========variable=========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        
        
        
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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1350,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1250,height=600) 

        ##left label frame

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=600,height=420)

       # img_left=Image.open(r"E:\imagesproj\student2.jpg")
        #img_left=img_left.resize((350,120),Image.Resampling.LANCZOS)
        #self.photoimg_left=ImageTk.PhotoImage(img1)

        #f_lbl=Label(Left_frame,image=self.photoimg_left)
        #f_lbl.place(x=5,y=0,width=590,height=100) 
        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=10,width=585,height=120)
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("time new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",10,"bold"),state="read only")
        dep_combo["values"]=("Select Department","IT","CIVIL","BIOLOGY","MECHANICAL","COMPUTER","ELECTRONIC","ELECTRICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course

        course_label=Label(current_course_frame,text="Course",font=("time new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)


        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("time new roman",10,"bold"),state="read only")
        course_combo["values"]=("Select Course","BTECH","MSC","BSC","BCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        
        year_label=Label(current_course_frame,text="Year",font=("time new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)


        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",10,"bold"),state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        
        semester_label=Label(current_course_frame,text="Semester",font=("time new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)


        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("time new roman",10,"bold"),state="read only")
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # class student information

        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("time new roman",12,"bold"))
        class_student_frame.place(x=5,y=150,width=585,height=230)

        #student id
        studentid_label=Label(class_student_frame,text="Student Id",font=("time new roman",10,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=10,font=("time new roman",10,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
       
        #student name
        
        studentname_label=Label(class_student_frame,text="Student Name",font=("time new roman",10,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=10,font=("time new roman",10,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #roll no

        rollno_label=Label(class_student_frame,text="Roll No",font=("time new roman",10,"bold"),bg="white")
        rollno_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=10,font=("time new roman",10,"bold"))
        rollno_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #gender
        
        gender_label=Label(class_student_frame,text="Gender",font=("time new roman",10,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

       ## gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=10,font=("time new roman",10,"bold"))
       ## gender_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("time new roman",10,"bold"),state="read only")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #dob
        
        dob_label=Label(class_student_frame,text="DOB",font=("time new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=10,font=("time new roman",10,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #phone no

        phone_label=Label(class_student_frame,text="Phone No",font=("time new roman",10,"bold"),bg="white")
        phone_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=10,font=("time new roman",10,"bold"))
        phone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         #email
        
        email_label=Label(class_student_frame,text="Email",font=("time new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=10,font=("time new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #address

        address_label=Label(class_student_frame,text="Address",font=("time new roman",10,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=10,font=("time new roman",10,"bold"))
        address_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="YES")
        radiobtn1.grid(row=4,column=0)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio2,text="No Photo Sample",value="NO")
        radiobtn2.grid(row=4,column=1)
         
         
        #button frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=160,width=570,height=23)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=26,font=("time new roman",6,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        
        update_btn=Button(btn_frame,text="Upadte",command=self.update_data,width=26,font=("time new roman",6,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
 
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=27,font=("time new roman",6,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=27,font=("time new roman",6,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        
        btn1_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn1_frame.place(x=5,y=185,width=570,height=20)
        take_photo_btn=Button(btn1_frame,text="Take photo sample",command=self.generate_dataset,width=55,font=("time new roman",6,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn1_frame,text="Update photo sample",width=55,font=("time new roman",6,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


         ##right label frame

        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=650,y=10,width=500,height=420)
        
        ## search system----------

        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        search_frame.place(x=5,y=10,width=489,height=70)

        search_label=Label(search_frame,text="Search By:",font=("time new roman",10,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("time new roman",10,"bold"),state="read only")
        search_combo["values"]=("Select","Roll_No","PhoneNo")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        

        search_entry=ttk.Entry(search_frame,width=13,font=("time new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=13,sticky=W)

        search_btn=Button(search_frame,text="Search",width=6,font=("time new roman",8,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=1)
        
        showall_btn=Button(search_frame,text="Show All",width=6,font=("time new roman",8,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)


        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=90,width=489,height=290)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("department","course","year","semester","id","name","rollno","gender","dob","email","phoneno","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("rollno",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phoneno",text="PhoneNo")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phoneno",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        #==============func declaration


    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="aadi",database="facerecogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_radio1.get()

                                                                                                        ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    


####============Fetch Data ===================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="aadi",database="facerecogniser")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

##============get cursor=============
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
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])
        self.var_radio1.set(data[12])

## update function


    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="aadi",database="facerecogniser")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_Id=%s",(
                                                                                                                                                                                         self.var_dep.get(),
                                                                                                                                                                                         self.var_course.get(),
                                                                                                                                                                                         self.var_year.get(),
                                                                                                                                                                                         self.var_semester.get(),
                                                                                                                                                                                         self.var_std_name.get(),
                                                                                                                                                                                         self.var_roll.get(),
                                                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                                                         self.var_dob.get(),
                                                                                                                                                                                         
                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                         self.var_phone.get(),
                                                                                                                                                                                         self.var_address.get(),
                                                                                                                                                                                         self.var_radio1.get(),
                                                                                                                                                                                         self.var_std_id.get(),
                                                              ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)    
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

      ## delete func

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","Do you want to delete this  student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="aadi",database="facerecogniser")
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
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

## reset func
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

#===========Generate data set or Take photo samples ============

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="aadi",database="facerecogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1

                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_Id=%s",(
                                                                                                                                                                                         self.var_dep.get(),
                                                                                                                                                                                         self.var_course.get(),
                                                                                                                                                                                         self.var_year.get(),
                                                                                                                                                                                         self.var_semester.get(),
                                                                                                                                                                                         self.var_std_name.get(),
                                                                                                                                                                                         self.var_roll.get(),
                                                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                                                         self.var_dob.get(),
                                                                                                                                                                                         
                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                         self.var_phone.get(),
                                                                                                                                                                                         self.var_address.get(),
                                                                                                                                                                                         self.var_radio1.get(),
                                                                                                                                                                                         self.var_std_id.get()==id+1
                                                              ))    

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


#===============Load predefinede data on face frontal from opencv
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    #cv2.imshow("preview", my_frame)
                    face=cv2.resize(face_cropped(my_frame),(350,350))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dat sets completed")




            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


        
               
            


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()           