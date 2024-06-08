import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Function to open files and select image
def upload_img():
    # open files and get path for selected img
    img_path = filedialog.askopenfilename(filetypes=[('Image Files', "*.png;*.png;*.jpg;*.jpeg;*.bmp")])

    if img_path:
        # load img using pillow
        img = Image.open(img_path)

        # resize img
        max_size = (900, 700)
        img.thumbnail(max_size)  # thumbnail preserves the aspect ratio of image

        # convert image to tk compatible
        tk_img = ImageTk.PhotoImage(img)

        # display the img in label
        img_label.config(image=tk_img)
        img_label.image = tk_img


# Create main app window
app = tk.Tk()
app.title("Image watermark")

# resizing the window
app.geometry('1000x800')

# create a upload button
upload_btn = tk.Button(app, text='Upload Image', command=upload_img)
upload_btn.pack(pady=20)

# create a label to display image
img_label = tk.Label(app)
img_label.pack(pady=20)

app.mainloop()
