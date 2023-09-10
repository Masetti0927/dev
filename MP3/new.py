import os
import tkinter as tk
from tkinter import filedialog

def rename_mp3_files(folder_path):
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        result_label.config(text="指定的文件夹路径无效")
        return

    mp3_files = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]

    for index, mp3_file in enumerate(mp3_files, start=1):
        new_name = f"aac_{index}_{mp3_file}"
        old_path = os.path.join(folder_path, mp3_file)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        result_label.config(text=f"重命名：{mp3_file} -> {new_name}")

def browse_file():
    file_selected = filedialog.askopenfilename()
    folder_path = os.path.dirname(file_selected)
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

def start_rename():
    folder_path = folder_path_entry.get()
    rename_mp3_files(folder_path)

# 创建主窗口
root = tk.Tk()
root.title("MP3文件重命名工具")

# 创建GUI组件
folder_path_label = tk.Label(root, text="选择文件夹路径:")
folder_path_entry = tk.Entry(root, width=50)
browse_button = tk.Button(root, text="浏览文件", command=browse_file)
start_button = tk.Button(root, text="开始", command=start_rename)
result_label = tk.Label(root, text="")

# 布局GUI组件
folder_path_label.grid(row=0, column=0, padx=10, pady=10)
folder_path_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button.grid(row=0, column=2, padx=10, pady=10)
start_button.grid(row=1, columnspan=3, padx=10, pady=10)
result_label.grid(row=2, columnspan=3, padx=10, pady=10)

# 启动主循环
root.mainloop()
