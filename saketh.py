
import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        # Set up GUI elements
        self.root.configure(bg="lavender")
        
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=10)
        
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()
        
        # Change button colors to medium sea green
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg="medium sea green", fg="white")
        self.generate_button.pack(pady=10)
        
        self.progress_bar = ttk.Progressbar(root, orient="horizontal", mode="indeterminate")
        self.progress_bar.pack(pady=10)
        
        self.password_label = tk.Label(root, text="")
        self.password_label.pack(pady=10)
        
        self.accept_button = tk.Button(root, text="Accept Password", command=self.accept_password, bg="medium sea green", fg="white")
        self.accept_button.pack()
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset, bg="medium sea green", fg="white")
        self.reset_button.pack()

        self.generated_password = ""

    def generate_password(self):
        self.progress_bar.start()
        self.root.update_idletasks()
        
        length = int(self.length_entry.get())
        
        characters = string.ascii_letters + string.digits + string.punctuation
        
        if characters:
            self.generated_password = ''.join(random.choice(characters) for _ in range(length))
            self.progress_bar.stop()
            self.password_label.config(text=f"Generated Password: {self.generated_password}")
        else:
            self.generated_password = ""
            self.progress_bar.stop()
            self.password_label.config(text="Error generating password.")

    def accept_password(self):
        if self.generated_password:
            self.password_label.config(text=f"Accepted Password: {self.generated_password}")
        else:
            self.password_label.config(text="No password generated yet.")

    def reset(self):
        self.generated_password = ""
        self.length_entry.delete(0, tk.END)
        self.password_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
