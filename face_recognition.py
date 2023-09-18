###--Useful libraries
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
import cv2
from cv2 import BORDER_ISOLATED,BORDER_REFLECT,resize
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os
from datetime import datetime
from time import strftime
class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("face recognition system")
        
        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45)
        #-------background-------------
        img_top=Image.open(r"E:\imagesproj\face_4.jpg")
        img_top=img_top.resize((600,700),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=600,height=650)

        img_bottom=Image.open(r"E:\imagesproj\face_3.jpeg")
        img_bottom=img_bottom.resize((700,700),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f1_lbl=Label(self.root,image=self.photoimg_bottom)
        f1_lbl.place(x=600,y=55,width=600,height=650)
 
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=350,y=450,width=200,height=40)

    #======attendance func==========================

    def mark_attendance(self,i,r,n):
        with open("aditi.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (r not in name_list)):
                now =datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{dtString},{d1},Present")








     
     #----------------face function--------------------   
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
             gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
             features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
             coord=[]
             for (x,y,w,h) in features:
                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                 id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                 confidence=int((100*(1-predict/300)))
                 
                 conn=mysql.connector.connect(host="localhost",username="root",password="aadi",database="facerecogniser")
                 my_cursor=conn.cursor()

                 my_cursor.execute("select Name from student where Student_Id="+str(id))
                 n=my_cursor.fetchone()
                 n="+".join(n)

                 my_cursor.execute("select Roll from student where Student_Id="+str(id))
                 r=my_cursor.fetchone()
                 r="+".join(r)

                 my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                 i=my_cursor.fetchone()
                 i="+".join(i)

                 if confidence>77:
                     cv2.putText(img,f"Id:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                     cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                     cv2.putText(img,f"Name:{n}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                     self.mark_attendance(i,r,n)
                 else:
                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                     cv2.putText(img,"Unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 coord=[x,y,w,h] 
             return coord
        def recognize(img,clf,faceCascade):  
            coord =draw_boundary(img,faceCascade,1.1,10,(255,255,255),"face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("lbph_classifier.xml")

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
    
    # Check if the frame was read successfully
            if not ret:
               continue
    
            img = recognize(img, clf, faceCascade)
            cv2.imshow("welcome to face recognition", img)
    
            if cv2.waitKey(1) == 13:
               break

        # Release the video capture and destroy all OpenCV windows
        video_cap.release()
        cv2.destroyAllWindows()







                 
                     
                     
                      





        
if __name__ == "__main__":
    root=Tk()
    object=Face_Recognition(root)
    root.mainloop() 