from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student_Details:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img = Image.open("img\girl.jpeg")
        img = img.resize((510, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=130)

        # Top Middle
        img1 = Image.open("img\\university.jpg")
        img1 = img1.resize((510, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=0, width=510, height=130)

        # Top Right
        img2 = Image.open("img\clg.jpg")
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
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("time new roman", 35, "bold"), bg="white", fg="navyblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Frame
        mainframe = Frame(bg_img, bd=2)
        mainframe.place(x=0, y=45, width=1530, height=615)

        # Left Label Frame
        left_label_frame = LabelFrame(mainframe, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_label_frame.place(x=10, y=5, width=740, height=600)

        # Frame Img
        img4 = Image.open("img\img1.jpeg")
        img4 = img4.resize((725, 130), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        left_frame_img = Label(left_label_frame, image=self.photoimg4)
        left_frame_img.place(x=5, y=0, width=725, height=130)

        # Label Frame Details
        current_course = LabelFrame(left_label_frame, bd=2, relief=RIDGE, text="Current Course",
                                      font=("times new roman", 12, "bold"))
        current_course.place(x=5, y=135, width=725, height=115)

        # Current Course Label
        # Departmet
        dep_label = Label(current_course, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(current_course, font=("times new roman", 12, "bold"), width=25, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "Information Technology", "Electronics and Telecommunication", "Chemical", "Artificial Intelligence & Data Science")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_course, font=("times new roman", 12, "bold"), width=25, state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course, font=("times new roman", 12, "bold"), width=25, state="readonly")
        year_combo["values"] = ("Select Year", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course, text="Semester", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(current_course, font=("times new roman", 12, "bold"), width=25, state="readonly")
        semester_combo["values"] = ("Select Semester", "Semester I", "Semester II")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student Details Frame
        student_label_frame = LabelFrame(left_label_frame, bd=2, relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"))
        student_label_frame.place(x=5, y=250, width=725, height=320)

        # Student ID
        std_id_label = Label(student_label_frame, text="Student ID:", font=("times new roman", 12, "bold"))
        std_id_label.grid(row=0, column=0, padx=5, sticky=W)
        std_id_entry = ttk.Entry(student_label_frame, width=25, font=("times new roman", 12, "bold"))
        std_id_entry.grid(row=0, column=1, pady=5, sticky=W)

        # Student Name
        std_name_label = Label(student_label_frame, text="Student Name:", font=("times new roman", 12, "bold"))
        std_name_label.grid(row=0, column=2, pady=5, sticky=W)
        std_name_entry = ttk.Entry(student_label_frame, width=25, font=("times new roman", 12, "bold"))
        std_name_entry.grid(row=0, column=3, pady=5, sticky=W)

        # Student Division
        std_div_label = Label(student_label_frame, text="Student Division:", font=("times new roman", 12, "bold"))
        std_div_label.grid(row=1, column=0, pady=5, sticky=W)
        div_combo = ttk.Combobox(student_label_frame, font=("times new roman", 12, "bold"), width=23, state="readonly")
        div_combo["values"] = ("Select Divison", "A", "B")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, pady=5, sticky=W)

        #Student Roll Number
        std_roll_label = Label(student_label_frame, text="Roll Number:", font=("times new roman", 12, "bold"))
        std_roll_label.grid(row=1, column=2, pady=5, sticky=W)
        std_roll_entry = ttk.Entry(student_label_frame, width=25, font=("times new roman", 12, "bold"))
        std_roll_entry.grid(row=1, column=3, pady=5, sticky=W)

        # Student Gender
        std_gender_label = Label(student_label_frame, text="Gender:", font=("times new roman", 12, "bold"))
        std_gender_label.grid(row=2, column=0, pady=5, sticky=W)
        gender_combo = ttk.Combobox(student_label_frame, font=("times new roman", 12, "bold"), width=23, state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Transgender")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=5, sticky=W)

        # DOB
        dob_label = Label(student_label_frame, text="DOB:", font=("times new roman", 12, "bold"))
        dob_label.grid(row=2, column=2, pady=5, sticky=W)
        dob_entry = ttk.Entry(student_label_frame, width=25, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, pady=5, sticky=W)

        # EMail
        email_label = Label(student_label_frame, text="Email:", font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, pady=5, sticky=W)
        email_entry = ttk.Entry(student_label_frame, width=25, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, pady=5, sticky=W)

        # number
        num_label = Label(student_label_frame, text="Phone Number:", font=("times new roman", 12, "bold"))
        num_label.grid(row=3, column=2, pady=5, sticky=W)
        num_entry = ttk.Entry(student_label_frame, width=25, font=("times new roman", 12, "bold"))
        num_entry.grid(row=3, column=3, pady=5, sticky=W)

        # Adress
        address_label = Label(student_label_frame, text="Address:", font=("times new roman", 12, "bold"))
        address_label.grid(row=4, column=0, pady=5, sticky=W)
        address_entry = ttk.Entry(student_label_frame, width=25, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, pady=5, sticky=W)

        # Teacher
        teacher_label = Label(student_label_frame, text="Teacher:", font=("times new roman", 12, "bold"))
        teacher_label.grid(row=4, column=2, pady=5, sticky=W)
        teacher_entry = ttk.Entry(student_label_frame, width=25, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, pady=5, sticky=W)

        # Radio Button
        sample_radio1 = ttk.Radiobutton(student_label_frame, text="Take Photo Sample", value="Yes")
        sample_radio1.grid(row=5, column=0, pady=5,padx=10, sticky=W)
        sample_radio1 = ttk.Radiobutton(student_label_frame, text="Take Photo Sample", value="No")
        sample_radio1.grid(row=5, column=1, pady=5,padx=10, sticky=W)

        # Buttons
        btn_frame = Frame(student_label_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=5, y=205, width=710, height=85)

        save_btn = Button(btn_frame, text="Save", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=19)
        reset_btn.grid(row=0, column=3)

        poto_frame = Frame(btn_frame, bd=2, relief=RIDGE)
        poto_frame.place(x=0, y=34, width=705, height=34)

        take_photo_btn = Button(poto_frame, text="Take Photo Sample", font=("times new roman", 12, "bold"), bg="blue", fg="white",
                           width=39)
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(poto_frame, text="Update Photo Sample", font=("times new roman", 12, "bold"), bg="blue",
                                fg="white",
                                width=39)
        update_photo_btn.grid(row=1, column=1)


        # Right Label Frame
        right_label_frame = LabelFrame(mainframe, bd=2, relief=RIDGE, text="Student Details",
                                      font=("times new roman", 12, "bold"))
        right_label_frame.place(x=770, y=5, width=740, height=600)

        img5 = Image.open("img\images.jpg")
        img5 = img5.resize((725, 130), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        right_frame_img = Label(right_label_frame, image=self.photoimg5)
        right_frame_img.place(x=5, y=0, width=725, height=130)

        # ---- Search System -------
        search_frame = LabelFrame(right_label_frame, bd=2, relief=RIDGE, text="Search System ",
                                         font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=725, height=90)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 14, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Roll Number", "Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=12)
        search_btn.grid(row=0, column=3, padx=2, pady=5)

        show_all_btn = Button(search_frame, text="Show All", font=("times new roman", 12, "bold"), bg="blue", fg="white",
                            width=12)
        show_all_btn.grid(row=0, column=4, padx=2, pady=5)

        # Table Frame
        table_frame = LabelFrame(right_label_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=230, width=725, height=340)

        # Scroll bar
        scrollx = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=('dep', 'course', 'year', 'sem', 'id', 'name', 'div', 'roll', 'gender', 'dob', 'email', 'phone', 'address', 'teacher', 'photo'), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll Number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Residential Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)


        self.student_table.pack(fill=BOTH, expand=1)






if __name__ == '__main__':
    root = Tk()
    obj = Student_Details(root)
    root.mainloop()