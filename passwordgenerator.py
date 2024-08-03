import random
import string
import tkinter as tk
from tkinter import messagebox, StringVar

class PasswordGenerator:

    def __init__(self, length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_digits = use_digits
        self.use_special = use_special

    def generate_password(self):
        character_pool = ''

        if self.use_uppercase:
            character_pool += string.ascii_uppercase
        if self.use_lowercase:
            character_pool += string.ascii_lowercase
        if self.use_digits:
            character_pool += string.digits
        if self.use_special:
            character_pool += string.punctuation

        if not character_pool:
            raise ValueError("At least one character type must be selected.")

        password = ''.join(random.choice(character_pool) for _ in range(self.length))
        return password

class PasswordGeneratorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Password Length:").pack(pady=10)

        self.length_var = StringVar(value="12")
        tk.Entry(self.root, textvariable=self.length_var).pack(pady=5)

        self.uppercase_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.uppercase_var).pack()

        self.lowercase_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Lowercase Letters", variable=self.lowercase_var).pack()

        self.digits_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var).pack()

        self.special_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Special Characters", variable=self.special_var).pack()

        tk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=20)

        self.result_var = StringVar()
        tk.Entry(self.root, textvariable=self.result_var, width=50).pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length < 6:
                raise ValueError("Password length must be at least 6.")

            generator = PasswordGenerator(
                length,
                self.uppercase_var.get(),
                self.lowercase_var.get(),
                self.digits_var.get(),
                self.special_var.get()
            )
            password = generator.generate_password()
            self.result_var.set(password)

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
