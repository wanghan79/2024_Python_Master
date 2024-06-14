import tkinter as tk
from tkinter import messagebox
import random
import csv
import ast

def count_info_generation(func)
    def wrapper(args, kwargs)
        wrapper.count += kwargs.get('quantity', 0)
        result = func(args, kwargs)
        print(fCall {wrapper.count} times to {func.__name__}, generated {len(result)} user information records.)
        return result
    wrapper.count = 0
    return wrapper

class UserInfoGenerator
    def __init__(self, kwargs)
        self.extra_kwargs = kwargs

    def generate_info(self, user_requirements)
        user_infos = []
        if isinstance(user_requirements, dict)
            for occupation, quantity in user_requirements.items()
                user_infos.extend(self.generate_user_infos(occupation, quantity))
        elif isinstance(user_requirements, (list, tuple, set))
            for requirement in user_requirements
                if isinstance(requirement, dict)
                    for occupation, quantity in requirement.items()
                        user_infos.extend(self.generate_user_infos(occupation, quantity))
                elif isinstance(requirement, (list, tuple, set)) and len(requirement) == 2
                    occupation, quantity = requirement
                    user_infos.extend(self.generate_user_infos(occupation, quantity))
        return user_infos

    @count_info_generation
    def generate_user_infos(self, occupation, quantity)
        user_infos = [
            {
                Name self.random_name(),
                Age random.randint(18, 65),
                Email self.random_email(),
                Occupation occupation,
                self.generate_random_structure(),
                self.extra_kwargs
            }
            for _ in range(quantity)
        ]
        return user_infos

    def random_name(self)
        first_names = [张, 李, 王, 刘]
        last_names = [三, 四, 五, 六]
        return random.choice(first_names) + random.choice(last_names)

    def random_email(self)
        domains = [@example.com, @mail.com, @test.com]
        return fuser{random.randint(1000, 9999)}{random.choice(domains)}

    def save_to_csv(self, user_infos)
        try
            with open(user_info.csv, a, newline=, encoding='utf-8-sig') as csvfile
                writer = csv.DictWriter(csvfile, fieldnames=user_infos[0].keys())
                if csvfile.tell() == 0
                    writer.writeheader()
                writer.writerows(user_infos)
        except Exception as e
            messagebox.showerror(Save Error, fError occurred while saving user information {e})

    def generate_random_structure(self)
        structure = {}
        for _ in range(random.randint(1, 5))  # Generate 1 to 5 random attributes
            key = fAttribute{random.randint(1, 100)}
            value = fValue{random.randint(1, 100)}
            structure[key] = value
        return structure

class UserInfoGeneratorGUI
    def __init__(self, generator)
        self.generator = generator
        self.root = tk.Tk()
        self.root.title(User Information Generator)
        self.root.geometry(400x200)  # Set window size

        self.instruction_label = tk.Label(self.root, text=Enter occupation and quantity (dictionary, list, tuple, or set))
        self.input_text = tk.Text(self.root, height=5, width=50)  # Create a text box for user input
        self.generate_button = tk.Button(self.root, text=Generate User Information, command=self.generate_users)
        self.save_button = tk.Button(self.root, text=Save User Information, command=self.save_users)  # New save button

        self.instruction_label.pack()
        self.input_text.pack()
        self.generate_button.pack()
        self.save_button.pack()  # Add the new save button to the interface

    def generate_users(self)
        input_data = self.input_text.get(1.0, tk.END)
        try
            user_requirements = ast.literal_eval(input_data.strip())
            user_infos = self.generator.generate_info(user_requirements)
            messagebox.showinfo(Generation Complete, fSuccessfully generated {len(user_infos)} user information records.)
            self.input_text.delete(1.0, tk.END)  # Clear input box
        except Exception as e
            messagebox.showerror(Error, fInput data format error {e})

    def save_users(self)
        user_infos = self.generator.generate_info([])  # Save an empty list to trigger saving to CSV
        if user_infos
            self.generator.save_to_csv(user_infos)
            messagebox.showinfo(Save Complete, User information has been saved to user_info.csv.)

if __name__ == __main__
    generator = UserInfoGenerator()
    app = UserInfoGeneratorGUI(generator)
    app.root.mainloop()
