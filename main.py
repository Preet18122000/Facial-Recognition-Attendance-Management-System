from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Top left
        img = Image.open("img\BestFacialRecognition.jpg")
        img = img.resize((510, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=130)

        # Top Middle
        img1 = Image.open("img\\facialrecognition.png")
        img1 = img1.resize((510, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=0, width=510, height=130)

        # Top Right
        img2 = Image.open("img\\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img2 = img2.resize((510, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=0, width=510, height=130)

        # Background Image
        img3 = Image.open("img\dev.jpg")
        img3 = img3.resize((1530, 660), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=660)

        # Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION STUDENT ATTENDANCE SYSTEM", font=("time new roman", 35, "bold"), bg="white", fg="navyblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student Button
        img4 = Image.open("img\student.jpg")
        img4 = img4.resize((220, 180), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=180)
        b1_txt = Button(bg_img, text="Student Details", cursor="hand2", font=("time new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_txt.place(x=200, y=280, width=220, height=40)

        # Face Detection
        img5 = Image.open("img\\face_detector1.jpg")
        img5 = img5.resize((220, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=180)
        b2_txt = Button(bg_img, text="Face Recognition", cursor="hand2", font=("time new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_txt.place(x=500, y=280, width=220, height=40)

        # Attendance Button
        img6 = Image.open("img\smart-attendance.jpg")
        img6 = img6.resize((220, 180), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=180)
        b3_txt = Button(bg_img, text="Attendance", cursor="hand2", font=("time new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_txt.place(x=800, y=280, width=220, height=40)

        # Help Desk
        img7 = Image.open("img\help.jpg")
        img7 = img7.resize((220, 180), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=180)
        b4_txt = Button(bg_img, text="Help Desk", cursor="hand2", font=("time new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_txt.place(x=1100, y=280, width=220, height=40)

        # Train Data
        img8 = Image.open("img\di.jpg")
        img8 = img8.resize((220, 180), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b5.place(x=200, y=370, width=220, height=180)
        b5_txt = Button(bg_img, text="Train Data", cursor="hand2", font=("time new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        b5_txt.place(x=200, y=550, width=220, height=40)

        # Photos
        img9 = Image.open("img\poto.jpg")
        img9 = img9.resize((220, 180), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b6.place(x=500, y=370, width=220, height=180)
        b6_txt = Button(bg_img, text="Photos", cursor="hand2", font=("time new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        b6_txt.place(x=500, y=550, width=220, height=40)

        # Developer
        img10 = Image.open("img\\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img10 = img10.resize((220, 180), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=370, width=220, height=180)
        b7_txt = Button(bg_img, text="Developer", cursor="hand2", font=("time new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        b7_txt.place(x=800, y=550, width=220, height=40)

        # Exit
        img11 = Image.open("img\exit.jpg")
        img11 = img11.resize((220, 180), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=370, width=220, height=180)
        b8_txt = Button(bg_img, text="Exit", cursor="hand2", font=("time new roman", 15, "bold"),
                        bg="darkblue", fg="white")
        b8_txt.place(x=1100, y=550, width=220, height=40)


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()