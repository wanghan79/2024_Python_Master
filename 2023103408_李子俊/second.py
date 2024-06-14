import tkinter as tk
from tkinter import messagebox
import random
import csv
import ast

class UserInfoGenerator:
    def __init__(self, **kwargs):
        self.extra_kwargs = kwargs

    def generate_info(self, user_requirements):
        user_infos = []
        if isinstance(user_requirements, dict):
            for occupation, quantity in user_requirements.items():
                user_infos.extend(self.generate_user_infos(occupation, quantity))
        elif isinstance(user_requirements, (list, tuple, set)):
            for requirement in user_requirements:
                if isinstance(requirement, dict):
                    for occupation, quantity in requirement.items():
                        user_infos.extend(self.generate_user_infos(occupation, quantity))
                elif isinstance(requirement, (list, tuple, set)) and len(requirement) == 2:
                    occupation, quantity = requirement
                    user_infos.extend(self.generate_user_infos(occupation, quantity))
        self.save_to_csv(user_infos)
        return user_infos

    def generate_user_infos(self, occupation, quantity):
        return [
            {
                "Name": self.random_name(),
                "Age": random.randint(18, 65),
                "Email": self.random_email(),
                "Occupation": occupation,
                **self.extra_kwargs
            }
            for _ in range(quantity)
        ]

    def random_name(self):
        first_names = ["Zhang", "Li", "Wang", "Liu"]
        last_names = ["San", "Si", "Wu", "Liu"]
        return random.choice(first_names) + random.choice(last_names)

    def random_email(self):
        domains = ["@example.com", "@mail.com", "@test.com"]
        return f"user{random.randint(1000, 9999)}{random.choice(domains)}"

    def save_to_csv(self, user_infos):
        with open("user_info.csv", "a", newline="", encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=user_infos[0].keys())
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerows(user_infos)

class UserInfoGeneratorGUI:
    def __init__(self, generator):
        self.generator = generator
        self.root = tk.Tk()
        self.root.title("User Information Generator")
        self.root.geometry("400x200")  # Set window size

        self.instruction_label = tk.Label(self.root, text="Enter occupation and quantity (dictionary, list, tuple, or set):")
        self.input_text = tk.Text(self.root, height=5, width=50)  # Create a text box for user input
        self.generate_button = tk.Button(self.root, text="Generate User Information", command=self.generate_users)
        self.save_button = tk.Button(self.root, text="Save User Information", command=self.save_users)  # New save button

        self.instruction_label.pack()
        self.input_text.pack()
        self.generate_button.pack()
        self.save_button.pack()  # Add the new save button to the interface

    def generate_users(self):
        user_input = self.input_text.get("1.0", tk.END)  # Get input from text box
        try:
            user_requirements = ast.literal_eval(user_input)
            self.user_infos = self.generator.generate_info(user_requirements)
            messagebox.showinfo("Success", "Successfully generated user information.")
        except ValueError as e:
            messagebox.showerror("Error", f"Input error: {e}")

    def save_users(self):
        try:
            self.generator.save_to_csv(self.user_infos)
            messagebox.showinfo("Success", "Successfully saved user information.")
        except Exception as e:
            messagebox.showerror("Error", f"Save error: {e}")

    def run(self):
        self.root.mainloop()

class Application:
    def __init__(self):
        extra_data = {
            "Nationality": "China",
            "City": "Beijing"
        }
        self.generator = UserInfoGenerator(**extra_data)
        self.gui = UserInfoGeneratorGUI(self.generator)

    def run(self):
        self.gui.run()

if __name__ == "__main__":
    app = Application()
    app.run()
