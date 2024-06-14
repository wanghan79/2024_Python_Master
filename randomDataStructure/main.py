import tkinter as tk
from tkinter import ttk
import ast
import json
from data_generator import TreeNode

class DataGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Generator and Stats Calculator")
        self.input_data_entry = ttk.Entry(self, width=40)
        self.count_entry = ttk.Entry(self)
        self.generate_button = ttk.Button(self, text="Generate and Save", command=self.generate_and_save_data)
        self.status_label = ttk.Label(self, text="")
        self.stats_label = ttk.Label(self, text="")

        self.input_data_label = ttk.Label(self, text="Input Data:")
        self.count_label = ttk.Label(self, text="Count:")

        self.input_data_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.input_data_entry.grid(row=0, column=1, padx=5, pady=5)
        self.count_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.count_entry.grid(row=1, column=1, padx=5, pady=5)
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.status_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.stats_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def generate_and_save_data(self):
        try:
            input_data = ast.literal_eval(self.input_data_entry.get())
            n = int(self.count_entry.get())
            if n <= 0:
                raise ValueError("Count must be a positive integer.")
            root_node = TreeNode("root", None)
            root_node = root_node.parse_data(input_data)
            generated_data = root_node.generate_random_data(n)
            with open('generated_data.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(generated_data, jsonfile, ensure_ascii=False, indent=4)
            stats = root_node.calculate_stats(generated_data)
            self.status_label.config(text="Data generated and stats calculated.")
            self.stats_label.config(text=f"Integer Stats: Total={stats['int']['total']}, Average={stats['int']['average']}\n"
                                            f"Float Stats: Total={stats['float']['total']}, Average={stats['float']['average']}")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    app = DataGeneratorApp()
    app.mainloop()


'''
输入样例：
{
  "姓名": "张三",
  "年龄": 30,
  "地址": {
    "城市": "北京",
    "区": "朝阳区",
    "邮编": "100000"
  },
  "联系方式": [
    {
      "类型": "手机",
      "号码": "13800138000"
    },
    {
      "类型": "邮箱",
      "号码": "zhangsan@example.com"
    }
  ],
  "兴趣爱好": ["旅游", "阅读", "音乐"],
  "在校状态": True
}''' 