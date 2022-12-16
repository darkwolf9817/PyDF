from tkinter import *
from tkinter.filedialog import askopenfilename
from sys import platform
from PIL import Image, ImageTk
from pdf2image import convert_from_path

if platform == "win32" or platform == "cygwin":
    poppler_path = r"\Poppler\Windows\poppler-22.12.0\Library\bin"

# Create the Tk container
root = Tk()

# Create the frame for the PDF Viewer
pdf_frame = Frame(root).pack(fill=BOTH, expand=1)

# Add Scrollbar to the frame
scroll_y = Scrollbar(pdf_frame, orient=VERTICAL)

# Add text widget for inserting images
pdf = Text(pdf_frame, yscrollcommand=scroll_y.set, bg="lightgrey")

# Set the scrollbar to the right side
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=pdf.yview)

# Pack the text widget
pdf.pack(fill=BOTH, expand=1)

# convert the PDF to a list of images
path = askopenfilename(initialdir='C:/')
if platform == "Linux" or platform == "Darwin":
    pages = convert_from_path(path, size=(800, 900))
else:
    pages = convert_from_path(path, size=(800, 900), poppler_path=poppler_path)

# Empty list for storing images
photos = []

# Store converted images in a list
for i in range(len(pages)):
    photos.append(ImageTk.PhotoImage(pages[i]))

# Adding all the images to the text widget
for photo in photos:
    pdf.image_create(END, image=photo)
    
    # Separate pages
    pdf.insert(END, '\n\n')

mainloop()