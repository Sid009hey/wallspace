from PIL import Image
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.font import Font


# Create a Tkinter window
window = tk.Tk()
window.title("Wall-E")
window.geometry("720x400")
window.configure(bg="#242424")  # Set dark mode background color

# Path variables
path = "./wallpaper/"

# Wallpapers list and dictionary
wallpapers = []
wallpaper_dict = {}


def load_wallpapers():
    for file in os.listdir(path):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            wallpapers.append(file)
            wallpaper_dict[file] = os.path.splitext(file)[0]


def update_wallpapers_list():
    wallpapers_listbox.delete(0, tk.END)
    for wallpaper in wallpapers:
        wallpapers_listbox.insert(tk.END, wallpaper)


def select_wallpaper(event):
    selection = wallpapers_listbox.get(wallpapers_listbox.curselection())
    img = Image.open(os.path.join(path, selection))
    img.show()


def add_wallpaper():
    file_path = filedialog.askopenfilename(
                                           parent=window,
                                           initialdir=os.getcwd(),
                                           title="Select Wallpaper",
                                           )
    if file_path:
        try:
            file_name = os.path.basename(file_path)
            shutil.copy(file_path, path)
            wallpapers.append(file_name)
            wallpaper_dict[file_name] = os.path.splitext(file_name)[0]
            update_wallpapers_list()
            print("✅ File added")
        except FileNotFoundError:
            print("❌ No Such Path")
    else:
        print("❌ No File Selected")


# Load wallpapers and update the list
load_wallpapers()

# Wallpapers Listbox
wallpapers_frame = tk.Frame(window, bg="#242424")
wallpapers_frame.pack(pady=10)

wallpapers_listbox = tk.Listbox(wallpapers_frame, bg="#242424", fg="#FFFFFF", font=("Arial", 12), width=70, height=10,
                                highlightthickness=0, selectbackground="#1E88E5", selectforeground="#FFFFFF")
wallpapers_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
wallpapers_listbox.bind("<<ListboxSelect>>", select_wallpaper)

wallpapers_scrollbar = ttk.Scrollbar(wallpapers_frame)
wallpapers_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
wallpapers_listbox.config(yscrollcommand=wallpapers_scrollbar.set)
wallpapers_scrollbar.config(command=wallpapers_listbox.yview)

update_wallpapers_list()

# Add Wallpaper Button
add_button_font = Font(family="Arial", size=12, weight="bold")
add_button = tk.Button(window, text="Add Wallpaper", command=add_wallpaper, bg="#5E81AC", fg="#FFFFFF",
                       font=add_button_font, relief=tk.FLAT)
add_button.pack(pady=10)

#wall title stuff
walltitle_font = Font(family="Arial", size=40)
walltitle = tk.Label(window, text="Wall-E Wallpaper Engine", bg="#242424", fg="#FFFFFF",font=add_button_font, relief=tk.FLAT)

walltitle.pack(pady=40)

# Run the Tkinter event loop
window.mainloop()

