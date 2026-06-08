# import libraries
import time
import customtkinter as cutk

# Configure font styles for consistent UI design
Title_font = ("Segoe UI", 30, "bold")
Msg_font = ("Segoe UI", 20)


def walking_reminder():
    # Initialize the pop-up window
    popup = cutk.CTk()
    popup.title("WALKING REMINDER")
    popup.resizable(False, False)
    
    # Define window dimensions and calculate center coordinates
    w, h = 500, 400
    popup.update_idletasks()

    x = int((popup.winfo_screenwidth() - w) / 2)
    y = int((popup.winfo_screenheight() - h) / 2)
    popup.geometry(f"{w}x{h}+{x}+{y}")

    popup.attributes("-topmost", True)
    cutk.set_appearance_mode("System")

    # UI elements: Main title, message, and the action button
    title_label = cutk.CTkLabel(popup, text="Break the loop! ♾️", font=Title_font)
    title_label.pack(pady=(30, 10))

    msg_label = cutk.CTkLabel(
        popup,
        text="You've been sitting for an hour ⏳ 💻 \n Time to walk for a few minutes 🚶",
        font=Msg_font,
    )
    msg_label.pack(pady=20)
    
    # Close the window when clicked
    cutk.CTkButton(
        popup,
        text="I am ready to break the loop",
        command=popup.destroy,
        font=("Segoe UI", 17, "bold"),
    ).pack(pady=50)

    popup.mainloop()

# Main loop to trigger the reminder every hour (3600 seconds)
while True:
    walking_reminder()
    time.sleep(3600)
