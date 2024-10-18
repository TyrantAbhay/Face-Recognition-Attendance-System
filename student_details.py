from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import re

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Data Entry")
        
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set the window to full screen based on screen width and height
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # TOP Header
        try:
            top_img = Image.open(r"images\Tyrant.jpg") 
            top_img = top_img.resize((screen_width, int(screen_height / 8)), Image.LANCZOS)  # Reduced height
            self.photoimage = ImageTk.PhotoImage(top_img)
        except FileNotFoundError:
            print("Header image file 'Tyrant.jpg' not found. Please check the path and file name.")
            return
        
        # Create a label widget to display the top header image
        f_label = Label(self.root, image=self.photoimage)
        f_label.place(x=0, y=0, width=screen_width, height=screen_height / 8)

        # BACKGROUND image
        try:
            background_img = Image.open(r"images\student details\student_details_background.jpeg")
            background_img = background_img.resize((screen_width, int(screen_height - (screen_height / 8))), Image.LANCZOS)
            self.background_img = ImageTk.PhotoImage(background_img)
        except FileNotFoundError:
            print("Background image file 'student_details_background.jpeg' not found. Please check the path and file name.")
            return
        
        # Create a label widget to display the background image
        bg_label = Label(self.root, image=self.background_img)
        bg_label.place(x=0, y=screen_height / 8, width=screen_width, height=screen_height - (screen_height / 8))

        # Title Label
        title = Label(self.root, text="Student Details", font=("Arial", 36, "bold"), bg="#4a90e2", fg="white")
        title.place(x=0, y=(screen_height / 8), width=screen_width, height=60)
        
        # Creating frame for data entry
        self.mainframe = Frame(bg_label, bd=2, bg="#eaeaea")  # Light gray background for main frame
        self.mainframe.place(x=5, y=65, width=screen_width - 15, height=screen_height - 141 - (screen_height / 8))
        
        # Left frame for data entry
        l_frame_width = (screen_width - 15) / 2 - 10  # Width for left frame
        self.l_frame = LabelFrame(self.mainframe, bd=2, text="Student Details", bg="#d9edf7", font=("Arial", 14, "bold"), fg="#31708f")
        self.l_frame.place(x=6, y=5, width=l_frame_width, height=screen_height - 141 - (screen_height / 8)-15)

        # Add a header image for the left frame
        try:
            header_img = Image.open(r"images\student details\student_details_background.jpeg")
            header_img = header_img.resize((int(l_frame_width - 10), 80), Image.LANCZOS)  # Adjust header image width
            self.header_photo = ImageTk.PhotoImage(header_img)  # Store image as an instance attribute
        except FileNotFoundError:
            print("Header image file 'student_details_background.jpeg' not found. Please check the path and file name.")
            return
        
        # Create a label widget to display the header image in the left frame
        header_label = Label(self.l_frame, image=self.header_photo, bg="#d9edf7")  # Set background color to match left frame
        header_label.place(x=0, y=0, width=l_frame_width, height=80)
        
        self.subjects_dict = {
            "AIML": ["Machine Learning", "Deep Learning", "Data Science"],
            "CV": ["Image Processing", "Computer Vision", "Pattern Recognition"],
            "EC": ["Digital Electronics", "Signal Processing", "Communication Systems"],
            "ME": ["Thermodynamics", "Fluid Mechanics", "Machine Design"],
            "EEE": ["Circuit Theory", "Control Systems", "Power Electronics"],
            "CSE": ["Data Structures", "Algorithms", "Software Engineering"],
            "ISE": ["Web Technologies", "Database Management", "Mobile App Development"]
        }

        # Current Course Frame
        current_course_frame = LabelFrame(self.l_frame, bd=2, text="Current Course", bg="#d9edf7", font=("Arial", 12, "bold"), fg="#31708f")
        current_course_frame.place(x=6, y=85, width=l_frame_width - 12, height=90)  
        
        # Department Label and ComboBox
        dept_label = Label(current_course_frame, text="Department:", bg="#d9edf7", font=("Arial", 9))
        dept_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        self.dept_combo = ttk.Combobox(current_course_frame, width=15, state="readonly")
        self.dept_combo["values"] = ("Select Department", "AIML", "CV", "EC", "ME", "EEE", "CSE", "ISE")
        self.dept_combo.current(0)
        self.dept_combo.grid(row=0, column=1, padx=5, pady=5)
        self.dept_combo.bind("<<ComboboxSelected>>", self.update_subjects)

        # Subject Label and ComboBox
        subject_label = Label(current_course_frame, text="Subject:", bg="#d9edf7", font=("Arial", 9))
        subject_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        
        self.subject_combo = ttk.Combobox(current_course_frame, width=15, state="readonly")
        self.subject_combo["values"] = ("Select Subject",)  
        self.subject_combo.current(0)
        self.subject_combo.grid(row=0, column=3, padx=5, pady=5)

        # Year Label and ComboBox
        year_label = Label(current_course_frame, text="Year:", bg="#d9edf7", font=("Arial", 9))
        year_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
        self.year_combo = ttk.Combobox(current_course_frame, width=15, state="readonly")
        self.year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        self.year_combo.current(0)
        self.year_combo.grid(row=1, column=1, padx=5, pady=5)

        # Semester Label and ComboBox
        sem_label = Label(current_course_frame, text="Semester:", bg="#d9edf7", font=("Arial", 9))
        sem_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        
        self.sem_combo = ttk.Combobox(current_course_frame, width=15, state="readonly")
        self.sem_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        self.sem_combo.current(0)
        self.sem_combo.grid(row=1, column=3, padx=5, pady=5)

        # Student Information Frame (2 Rows and 3 Columns)
        student_info_frame = LabelFrame(self.l_frame, bd=2, text="Student Information", bg="#d9edf7", font=("Arial", 12, "bold"), fg="#31708f")
        student_info_frame.place(x=6, y=175, width=l_frame_width - 12, height=270)

        # Name
        name_label = Label(student_info_frame, text="Name:", bg="#d9edf7", font=("Arial", 9))
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.name_input = ttk.Entry(student_info_frame)
        self.name_input.grid(row=0, column=1, padx=5, pady=5)

        # Roll Number
        roll_label = Label(student_info_frame, text="USN:", bg="#d9edf7", font=("Arial", 9))
        roll_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.roll_input = ttk.Entry(student_info_frame)
        self.roll_input.grid(row=0, column=3, padx=5, pady=5)

        # Division
        division_label = Label(student_info_frame, text="Division:", bg="#d9edf7", font=("Arial", 9))
        division_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.division_input = ttk.Entry(student_info_frame)
        self.division_input.grid(row=1, column=1, padx=5, pady=5)

        # Advisor
        advisor_label = Label(student_info_frame, text="Faculty Advisor:", bg="#d9edf7", font=("Arial", 9))
        advisor_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        self.advisor_input = ttk.Entry(student_info_frame)
        self.advisor_input.grid(row=1, column=3, padx=5, pady=5)

        # Email
        email_label = Label(student_info_frame, text="Email:", bg="#d9edf7", font=("Arial", 9))
        email_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.email_input = ttk.Entry(student_info_frame)
        self.email_input.grid(row=2, column=1, padx=5, pady=5)

        # Phone Number
        phone_label = Label(student_info_frame, text="Phone No:", bg="#d9edf7", font=("Arial", 9))
        phone_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        self.phone_input = ttk.Entry(student_info_frame)
        self.phone_input.grid(row=2, column=3, padx=5, pady=5)

        # Gender
        gender_label = Label(student_info_frame, text="Gender:", bg="#d9edf7", font=("Arial", 9))
        gender_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.gender_var = StringVar()
        male_radio = ttk.Radiobutton(student_info_frame, text="Male", variable=self.gender_var, value="Male")
        male_radio.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        female_radio = ttk.Radiobutton(student_info_frame, text="Female", variable=self.gender_var, value="Female")
        female_radio.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        
        
        
        
        
        
        # Radio Buttons 
        style = ttk.Style()

        # Configure custom style for Radiobuttons
        style.configure("Custom.TRadiobutton", background="#d9edf7", foreground="#31708f", font=("Arial", 9))

        # Radio Buttons with custom style
        take_radiobtn = ttk.Radiobutton(student_info_frame, text="Take Photo Sample", value="yes", style="Custom.TRadiobutton")
        take_radiobtn.grid(row=4, column=0, padx=5, pady=5)

        not_take_radiobtn = ttk.Radiobutton(student_info_frame, text="No Photo Sample", value="no", style="Custom.TRadiobutton")
        not_take_radiobtn.grid(row=4, column=1, padx=5, pady=5)

        # Photo Buttons frame
        # Radio Buttons 
        take_radiobtn = ttk.Radiobutton(student_info_frame, text="Take Photo Sample", value="yes")
        take_radiobtn.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        not_take_radiobtn = ttk.Radiobutton(student_info_frame, text="No Photo Sample", value="no")
        not_take_radiobtn.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Photo Buttons frame
        photo_btn_frame = Frame(student_info_frame, bg="#d9edf7")  # Added background color
        photo_btn_frame.place(x=0, y=170, width=l_frame_width - 20, height=40)

        # Width and height of photo btn frame
        wid = 17

        # Save Photo Button
        save_btn = Button(photo_btn_frame, width=wid, text="Save Photo", bg="#28a745", fg="white", font=("Arial", 10, "bold"))
        save_btn.grid(row=0, column=0, padx=5, pady=5)

        # Update Button
        update_btn = Button(photo_btn_frame, width=wid, text="Update", bg="#ffc107", fg="black", font=("Arial", 10, "bold"))
        update_btn.grid(row=0, column=1, padx=5, pady=5)

        # Delete Button
        delete_btn = Button(photo_btn_frame, width=wid, text="Delete", bg="#dc3545", fg="white", font=("Arial", 10, "bold"))
        delete_btn.grid(row=0, column=2, padx=5, pady=5)

        # Reset Button
        reset_btn = Button(photo_btn_frame, width=wid, text="Reset", bg="#007bff", fg="white", font=("Arial", 10, "bold"))
        reset_btn.grid(row=0, column=3, padx=5, pady=5)
        
        
        
        
        photo_btn_frame1 = Frame(student_info_frame, bg="#d9edf7")  # Added background color
        photo_btn_frame1.place(x=0, y=210, width=l_frame_width - 20, height=35)

        # Take Photo Button
        take_photo_btn = Button(photo_btn_frame1, width= 35, text="Take Photo", bg="#5bc0de", fg="white", font=("Arial", 10, "bold"))
        take_photo_btn.grid(row=1, column=0, padx=5, pady=5)

        # Update Photo Button
        update_photo_btn = Button(photo_btn_frame1, width=35, text="Update Photo", bg="#6f42c1", fg="white", font=("Arial", 10, "bold"))
        update_photo_btn.grid(row=1, column=1, padx=5, pady=5)


        # Buttons Frame
        self.button_frame = Frame(self.mainframe, bg="#eaeaea")
        self.button_frame.place(x=6, y=485, width=l_frame_width - 12, height=50)

        self.submit_button = Button(self.button_frame, text="Submit", command=self.validate_and_submit)
        self.submit_button.pack(side=LEFT, padx=5, pady=5)

        self.clear_button = Button(self.button_frame, text="Clear", command=self.clear_fields)
        self.clear_button.pack(side=RIGHT, padx=5, pady=5)

        self.status_label = Label(self.mainframe, text="", bg="#eaeaea", fg="red")
        self.status_label.place(x=6, y=530, width=l_frame_width - 12)  # Space for feedback messages
        
        
        
        
        #-----------------------------------------------Right Frame----------------------------------------------------
        # Right frame for additional information
        self.r_frame = LabelFrame(self.mainframe, bd=2, text="Additional Information", bg="#d9edf7", font=("Arial", 14, "bold"), fg="#31708f")
        self.r_frame.place(x=l_frame_width + 16, y=5, width=l_frame_width, height=screen_height - 141 - (screen_height / 8) - 15)

        # Add a header image for the right frame
        try:
            right_header_img = Image.open(r"images\student details\student_details_background.jpeg")
            right_header_img = right_header_img.resize((int(l_frame_width - 10), 80), Image.LANCZOS)  # Adjust header image width
            self.right_header_photo = ImageTk.PhotoImage(right_header_img)  # Store image as an instance attribute
        except FileNotFoundError:
            print("Header image file 'student_details_background.jpeg' not found. Please check the path and file name.")
            return

        # Create a label widget to display the header image in the right frame
        r_header_label = Label(self.r_frame, image=self.right_header_photo, bg="#d9edf7")  # Set background color to match the right frame
        r_header_label.place(x=0, y=0, width=l_frame_width, height=80)

        #====================================Search System============================================
        search_frame = LabelFrame(self.r_frame, bd=2, text="Search System", bg="#d9edf7", font=("Arial", 12, "bold"), fg="#31708f")
        search_frame.place(x=6, y=85, width=l_frame_width - 12, height=65)

        search_label = Label(search_frame, text="Search by:", bg="#d9edf7", font=("Arial", 9))
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Search by combobox
        self.search_combo = ttk.Combobox(search_frame, width=15, state="readonly")
        self.search_combo["values"] = ("Select", "USN", "Phone no")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=5, pady=5)

        # Search input
        search_input = ttk.Entry(search_frame)
        search_input.grid(row=0, column=2, padx=5, pady=5)

        # Search button
        search_btn = Button(search_frame, width=12, text="Search", bg="#007bff", fg="white", font=("Arial", 10, "bold"), cursor="hand2")
        search_btn.grid(row=0, column=3, padx=5, pady=5)

        # Show all button
        show_all_btn = Button(search_frame, width=12, text="Show all", bg="#007bff", fg="white", font=("Arial", 10, "bold"), cursor="hand2")
        show_all_btn.grid(row=0, column=4, padx=5, pady=5)

        #=============================Table Frame=================================================================
        table_frame = Frame(self.r_frame, bd=2, bg="#d9edf7", relief=RIDGE)
        table_frame.place(x=6, y=150, width=l_frame_width - 12, height=250)
        
        
        scroll_x = ttk.Scrollbar(table_frame,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient = VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("USN", "Name", "Department", "Subject", "Phone no"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("USN", text = "USN")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Subject", text="Subject")
        self.student_table.heading("Phone no", text="Phone No")
        
        self.student_table["show"] = "headings"
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.column("USN", width=100)
        self.student_table.column("Name", width=150)
        self.student_table.column("Department", width=150)
        self.student_table.column("Subject", width=150)
        self.student_table.column("Phone no", width=120)
        
        













    def update_subjects(self, event):
        selected_department = self.dept_combo.get()
        if selected_department in self.subjects_dict:
            self.subject_combo["values"] = ["Select Subject"] + self.subjects_dict[selected_department]
            self.subject_combo.current(0)  # Reset subject selection
        else:
            self.subject_combo["values"] = ["Select Subject"]
            self.subject_combo.current(0)

    def validate_email(self, email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def validate_phone(self, phone):
        regex = r'^\d{10}$'  # Simple regex for 10-digit phone number
        return re.match(regex, phone) is not None

    def validate_and_submit(self):
        email = self.email_input.get()
        phone = self.phone_input.get()
        
        if not self.validate_email(email):
            self.status_label.config(text="Invalid email format")
            return
        
        if not self.validate_phone(phone):
            self.status_label.config(text="Invalid phone number format")
            return
        
        # Save data logic (e.g., write to a file or database)
        # For demonstration, you can just print the inputs
        print(f"Name: {self.name_input.get()}, Roll: {self.roll_input.get()}, Email: {email}, Phone: {phone}")
        self.status_label.config(text="Data submitted successfully.", fg="green")
        self.clear_fields()  # Clear fields after submission

    def clear_fields(self):
        self.name_input.delete(0, END)
        self.roll_input.delete(0, END)
        self.division_input.delete(0, END)
        self.advisor_input.delete(0, END)
        self.email_input.delete(0, END)
        self.phone_input.delete(0, END)
        self.gender_var.set("")  # Clear gender selection
        self.dept_combo.current(0)  # Reset department selection
        self.subject_combo["values"] = ["Select Subject"]
        self.subject_combo.current(0)  # Reset subject selection
        self.year_combo.current(0)  # Reset year selection
        self.sem_combo.current(0)  # Reset semester selection
        self.status_label.config(text="")  # Clear status label

if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()