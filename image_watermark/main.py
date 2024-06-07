import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Function to open files and select image
def upload_img():
    # open files and get path for selected img
    img_path = filedialog.askopenfile(filetypes=[('Image Files', "*.png;*.png;*.jpg;*.jpeg;*.bmp")])

    if img_path:
        # load img using pillow
        img = Image.open(img_path)


# Create main app window
app = tk.Tk()
app.title("image watermark")



