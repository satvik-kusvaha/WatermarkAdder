from tkinter import *
from tkinter import filedialog
from PIL import Image

image = None

def image_uploader():
    global image
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)


def watermark_uploader():
    global image
    if image is None:
        print("please paste image")
        return

    file_path = filedialog.askopenfilename()
    if file_path:
        watermark = Image.open(file_path).convert("RGBA")  # Ensure transparency
        image = image.convert("RGBA")  # Ensure base image is also RGBA

        image.paste(watermark, (0, 0), watermark)
        image.show()


window = Tk()
window.title("Add Watermark")

upload_image = Button(text="Upload image", command=image_uploader)
upload_image.grid(column=0, row=0)

add_watermark = Button(text="Add Watermark", command=watermark_uploader)
add_watermark.grid(column=1, row=1)





window.mainloop()