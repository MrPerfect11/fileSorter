import os
import shutil
import tkinter as tk
from tkinter import filedialog

EXCLUDED_EXTENSIONS = {".txt", ".jpg", ".png", ".pdf", ".doc", ".docx", ".zip", ".rar"}

def is_valid_folder_name(folder_name):
    _, extension = os.path.splitext(folder_name)
    return extension.lower() not in EXCLUDED_EXTENSIONS

def is_same_extension_and_name(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if not files:
        return False

    base_name, extension = os.path.splitext(files[0])
    extension = extension.lower()

    return all(file.startswith(base_name) and file.endswith(extension) for file in files)

def organize_folder(folder_path, organize_subfolders):
    items = os.listdir(folder_path)

    if organize_subfolders and is_valid_folder_name(os.path.basename(folder_path)) and is_same_extension_and_name(folder_path):
        # Exclude the subfolder if it has the same extension and name for all files
        return

    for item in items:
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)
            extension = extension.lower()

            extension_folder = os.path.join(folder_path, extension[1:])
            os.makedirs(extension_folder, exist_ok=True)

            new_path = os.path.join(extension_folder, item)

            counter = 1
            while os.path.exists(new_path):
                base, ext = os.path.splitext(item)
                new_path = os.path.join(extension_folder, f"{base}_{counter}{ext}")
                counter += 1

            shutil.move(item_path, new_path)

    if organize_subfolders:
        for item in items:
            item_path = os.path.join(folder_path, item)

            if os.path.isdir(item_path) and is_valid_folder_name(item):
                subfolder_path = os.path.join(folder_path, item)
                organize_folder(subfolder_path, organize_subfolders)

def organize_files():
    warning_label.config(text="Sorting will happen each time the button is clicked.", fg="orange")
    target_folder = filedialog.askdirectory(title="Select Target Folder")
    if target_folder:
        organize_subfolders = organize_subfolders_var.get()
        organize_folder(target_folder, organize_subfolders)
        feedback_label.config(text="Organization completed!", fg="green")

# GUI setup
app = tk.Tk()
app.title("File Sorter")

# Styling
app.geometry("400x250")
app.configure(bg="#f0f0f0")

# Warning label
warning_label = tk.Label(app, text="Sorting will happen each time the button is clicked.", font=("Helvetica", 10), fg="orange", bg="#f0f0f0")
warning_label.pack()

# Create and configure the button
sort_button = tk.Button(
    app,
    text="Sort Files",
    command=organize_files,
    font=("Helvetica", 14),
    bg="#4CAF50",  # Green color
    fg="white",
    padx=10,
    pady=10,
)
sort_button.pack(pady=10)

# Checkbox for organizing subfolders
organize_subfolders_var = tk.BooleanVar()
organize_subfolders_check = tk.Checkbutton(
    app,
    text="Organize Subfolders",
    variable=organize_subfolders_var,
    font=("Helvetica", 12),
    bg="#f0f0f0",
)
organize_subfolders_check.pack()

# Create a label for user feedback
feedback_label = tk.Label(app, text="", font=("Helvetica", 12), fg="red", bg="#f0f0f0")
feedback_label.pack()

# Run the Tkinter main loop
app.mainloop()
