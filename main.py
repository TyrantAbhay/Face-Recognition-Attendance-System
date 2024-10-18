from tkinter import *
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set the window to full screen based on screen width and height
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Define the button size
        button_width = 130
        button_height = 130
        
        # Calculate remaining width for spacing
        total_button_width = 3 * button_width  # Total width occupied by 3 buttons
        remaining_space = screen_width - total_button_width  # Remaining space
        
        # Calculate gap (z/4) between buttons
        gap = remaining_space / 4

        # Adjust vertical spacing
        top_image_height = int(screen_height / 8)
        button_row_y_position = top_image_height + 100

        # TOP Header
        try:
            top_img = Image.open(r"images\Tyrant.jpg") 
            top_img = top_img.resize((screen_width, int(screen_height / 8)), Image.LANCZOS)  # Reduced height
            self.photoimage = ImageTk.PhotoImage(top_img)
        except FileNotFoundError:
            print("Header image file 'Tyrant.jpg' not found. Please check the path and file name.")
            return

        # Create a label widget to display the image
        f_label = Label(self.root, image=self.photoimage)
        f_label.place(x=0, y=0, width=screen_width, height=screen_height / 8)

        # BACKGROUND image
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
        title.place(x=0, y=top_image_height, width=screen_width, height=60)

        # -------------------- ROW 1 (Top 3 Buttons) -------------------- #
        self.create_button("images/student_information.jpeg", "Student Details", gap, button_row_y_position, button_width, button_height)
        self.create_button("images/Face Detection.jpg", "Face Detector", 2 * gap + button_width, button_row_y_position, button_width, button_height)
        self.create_button("images/attendance.png", "Attendance", 3 * gap + 2 * button_width, button_row_y_position, button_width, button_height)

        # -------------------- ROW 2 (Bottom 3 Buttons) -------------------- #
        second_row_y_position = button_row_y_position + button_height + 60  # Adjust for second row
        
        self.create_button("images/train_data.png", "Train Data", gap, second_row_y_position, button_width, button_height)
        self.create_button("images/images.png", "Photos", 2 * gap + button_width, second_row_y_position, button_width, button_height)
        self.create_button("images/exit.png", "Exit", 3 * gap + 2 * button_width, second_row_y_position, button_width, button_height)

    def create_button(self, image_path, button_text, x_position, y_position, width, height):
        """Creates an image button with text label."""
        try:
            img = Image.open(image_path)
            img = img.resize((width, height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
        except FileNotFoundError:
            print(f"Image file '{image_path}' not found. Please check the path and file name.")
            return
        
        # Create image button
        img_button = Button(self.root, image=photo, cursor="hand2", bd=0, bg="lightgray", activebackground="lightblue")
        img_button.place(x=x_position, y=y_position, width=width, height=height)
        img_button.image = photo  # Keep a reference to avoid garbage collection
        
        # Create text label below the image button
        txt_button = Button(self.root, text=button_text, font=("Arial", 12, "bold"), bg="lightgray", fg="navy", cursor="hand2", bd=0, activebackground="lightblue")
        txt_button.place(x=x_position, y=y_position + height + 5, width=width, height=30)












if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()