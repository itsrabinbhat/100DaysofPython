import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw


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

        # store resized img
        global original_img
        original_img = img.copy()

        # display the img in label
        img_label.config(image=tk_img)
        img_label.image = tk_img


# Function to add watermark to image
def add_watermark():
    watermark_txt = text.get().strip()
    if original_img and watermark_txt:
        img = original_img.copy()
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default(36)

        # Get text size using textbbox
        bbox = draw.textbbox((0, 0), watermark_txt, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Position the text in the bottom-right corner
        width, height = img.size
        x = (width - text_width) / 2
        y = (height - text_height) / 2

        # Draw the text on the image
        draw.text((x, y), watermark_txt, font=font, fill=(255, 255, 255, 50))

        # Convert image to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(img)

        # Display the watermarked image in the label
        img_label.config(image=tk_image)
        img_label.image = tk_image

        # clear text entry
        text.delete(0, 'end')


# Create main app window
app = tk.Tk()
app.title("Image watermark")

# resizing the window
app.geometry('1000x800')

# create a label and text input field
text_label = tk.Label(app, text='Enter watermark text: ', font=16)
text_label.pack()
text = tk.Entry(app, width=40, font=18)
text.pack(pady=10)

# create add watermark btn
watermark_btn = tk.Button(app, text='Add watermark', command=add_watermark, font=16)
watermark_btn.pack()

# create a label to display image
img_label = tk.Label(app)
img_label.pack(pady=10)

# create a upload button
upload_btn = tk.Button(app, text='Upload Image', command=upload_img, font=16)
upload_btn.pack(pady=10)

app.mainloop()
