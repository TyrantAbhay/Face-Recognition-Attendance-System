from tkinter import *
from PIL import Image, ImageTk

class Face_Recongition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set the window to full screen based on screen width and height
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # TOP Header
        # Open the image file from the specified path
        try:
            top_img = Image.open(r"images\Tyrant.jpg") 
            top_img = top_img.resize((screen_width, int(screen_height / 6)), Image.LANCZOS)
            self.photoimage = ImageTk.PhotoImage(top_img)
        except FileNotFoundError:
            print("Header image file 'Tyrant.jpg' not found. Please check the path and file name.")
            return
        
        # Create a label widget to display the image
        f_label = Label(self.root, image=self.photoimage)
        f_label.place(x=0, y=0, width=screen_width, height=screen_height / 6)
        
        # BACKGROUND image
        top_image_height = int(screen_height / 6)  
        try:
            background_img = Image.open(r"images\background image.jpeg")
            background_img = background_img.resize((screen_width, screen_height - top_image_height), Image.LANCZOS)
            self.background_img = ImageTk.PhotoImage(background_img)
        except FileNotFoundError:
            print("Background image file 'background image.jpeg' not found. Please check the path and file name.")
            return
        
        # Create a label widget to display the background image
        bg_label = Label(self.root, image=self.background_img)
        bg_label.place(x=0, y=top_image_height, width=screen_width, height=screen_height - top_image_height)

        # Title Label
        title = Label(self.root, text="Face Recognition System", font=("Arial", 36, "bold"), bg="lightgray", fg="navy")
        title.place(x=0, y=top_image_height + 50, width=screen_width, height=60)
        
        # Creating Student Details Button
        try:
            std_details = Image.open(r"images\student_information.jpeg")
            std_details = std_details.resize((130, 130), Image.LANCZOS)  # Resized for better fit
            self.stdDetails = ImageTk.PhotoImage(std_details)
        except FileNotFoundError:
            print("Image file 'student_information.jpeg' not found. Please check the path and file name.")
            return
        
        # Create the image button for student details
        std_btn = Button(self.root, image=self.stdDetails, cursor="hand2", bd=0, bg="lightgray", activebackground="lightblue")
        std_btn.place(x=100, y=top_image_height + 120, width=130, height=130)

        # Create a text button below the image button for "Student Details"
        std_txt_btn = Button(self.root, text="Student Details", font=("Arial", 12, "bold"), bg="lightgray", fg="navy", cursor="hand2", bd=0, activebackground="lightblue")
        std_txt_btn.place(x=100, y=top_image_height + 250, width=130, height=30)  # Positioned below the image button

        # Add functionality to the Student Details button (optional)
        std_btn.config(command=self.show_student_details)

    def show_student_details(self):
        print("Student Details button clicked!")  # Placeholder for button action

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recongition_System(root)
    root.mainloop()
