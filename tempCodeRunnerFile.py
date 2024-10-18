        photo_btn_frame = Frame(student_info_frame, bg="#d9edf7")  # Added background color
        photo_btn_frame.place(x=0, y=200, width=l_frame_width - 20, height=100)

        # Width and height of photo btn frame
        wid = l_frame_width / 4
        hei = 100 / 2

        # Save Photo Button
        save_btn = Button(photo_btn_frame, width=wid, height=hei, text="Save Photo", bg="#28a745", fg="white", font=("Arial", 10, "bold"))
        save_btn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        # Update Button
        update_btn = Button(photo_btn_frame, width=wid, height=hei, text="Update", bg="#ffc107", fg="black", font=("Arial", 10, "bold"))
        update_btn.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Delete Button
        delete_btn = Button(photo_btn_frame, width=wid, height=hei, text="Delete", bg="#dc3545", fg="white", font=("Arial", 10, "bold"))
        delete_btn.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

        # Reset Button
        reset_btn = Button(photo_btn_frame, width=wid, height=hei, text="Reset", bg="#007bff", fg="white", font=("Arial", 10, "bold"))
        reset_btn.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

        # Take Photo Button
        take_photo_btn = Button(photo_btn_frame, width=wid, height=hei, text="Take Photo", bg="#5bc0de", fg="white", font=("Arial", 10, "bold"))
        take_photo_btn.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        # Update Photo Button
        update_photo_btn = Button(photo_btn_frame, width=wid, height=hei, text="Update Photo", bg="#6f42c1", fg="white", font=("Arial", 10, "bold"))
        update_photo_btn.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
