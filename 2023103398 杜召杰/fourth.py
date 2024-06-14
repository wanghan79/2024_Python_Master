import tkinter as tk
from tkinter import messagebox
import random
import csv
import ast

def count_info_generation(func):
    def wrapper(*args, **kwargs):
        wrapper.count += kwargs.get('quantity', 0)
        result = func(*args, **kwargs)
        print(f"第 {wrapper.count} 次调用 {func.__name__}，生成了 {len(result)} 条用户信息。")
        return result
    wrapper.count = 0
    return wrapper

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

    @count_info_generation
    def generate_user_infos(self, occupation, quantity):
        user_infos = [
            {
                "姓名": self.random_name(),
                "年龄": random.randint(18, 65),
                "邮箱": self.random_email(),
                "职业": occupation,
                **self.generate_random_structure(),
                **self.extra_kwargs
            }
            for _ in range(quantity)
        ]
        return user_infos

    def random_name(self):
        first_names = ["张", "李", "王", "刘"]
        last_names = ["三", "四", "五", "六"]
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

    def generate_random_structure(self):
        structure = {}
        for _ in range(random.randint(1, 5)):  # 随机生成1到5个属性
            key = f"属性{random.randint(1, 100)}"
            value = f"值{random.randint(1, 100)}"
            structure[key] = value
        return structure

class UserInfoGeneratorGUI:
    def __init__(self, generator):
        self.generator = generator
        self.root = tk.Tk()
        self.root.title("用户信息生成器")
        self.root.geometry("400x200")  # 设置窗口大小

        self.instruction_label = tk.Label(self.root, text="请输入职业和数量（字典、列表、元组或集合）：")
        self.input_text = tk.Text(self.root, height=5, width=50)  # 创建一个文本框供用户输入
        self.generate_button = tk.Button(self.root, text="生成用户信息", command=self.generate_users)
        self.save_button = tk.Button(self.root, text="保存用户信息", command=self.save_users)  # 新增的保存按钮

        self.instruction_label.pack()
        self.input_text.pack()
        self.generate_button.pack()
        self.save_button.pack()  # 将新的保存按钮添加到界面上

    def generate_users(self):
        user_input = self.input_text.get("1.0", tk.END)  # 从文本框获取输入
        try:
            user_requirements = ast.literal_eval(user_input)
            self.user_infos = self.generator.generate_info(user_requirements)
            messagebox.showinfo("成功", f"成功生成了用户信息。")
        except ValueError as e:
            messagebox.showerror("错误", f"输入错误: {e}")

    def save_users(self):
        try:
            self.generator.save_to_csv(self.user_infos)
            messagebox.showinfo("成功", f"成功保存了用户信息。")
        except Exception as e:
            messagebox.showerror("错误", f"保存错误: {e}")

    def run(self):
        self.root.mainloop()

class Application:
    def __init__(self):
        extra_data = {
            "国籍": "中国",
            "城市": "北京"
        }
        self.generator = UserInfoGenerator(**extra_data)
        self.gui = UserInfoGeneratorGUI(self.generator)

    def run(self):
        self.gui.run()

if __name__ == "__main__":
    app = Application()
    app.run()
