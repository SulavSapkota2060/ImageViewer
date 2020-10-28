from tkinter import *
from PIL import ImageTk, Image

root = Tk()

my_image = ImageTk.PhotoImage(Image.open("images/1.jpg"))
index = 1
my_label = Label(image=my_image)
my_label.grid(row=0, column=0, columnspan=3)

root.title("Simple Image Viewer")
root.iconbitmap("icon.ico")


def nextImage():
    global index
    global nextBtn
    global before
    index += 1
    if index == 6:
        nextBtn = Button(text=">", command=nextImage, width=10, state=DISABLED).grid(row=1, column=2)
    if index > 1:
        before = Button(text="<", command=prev_image, width=10).grid(row=1, column=0)
    global my_label
    global my_image
    my_label.grid_forget()
    a = "Images/{0}.jpg".format(index)
    my_image = ImageTk.PhotoImage(Image.open(a))
    my_label = Label(image=my_image)
    my_label.grid(row=0, column=0, columnspan=3)
    Label(text=index).grid(row=2)


def prev_image():
    global my_label
    global my_image
    global before
    global nextBtn
    global index
    index -= 1
    if index == 1:
        before = Button(text="<", command=prev_image, width=10, state=DISABLED).grid(row=1, column=0)
    if index < 6:
        nextBtn = Button(text=">", command=nextImage, width=10).grid(row=1, column=2)
    my_label.grid_forget()
    a = "Images/{0}.jpg".format(index)
    my_image = ImageTk.PhotoImage(Image.open(a))
    my_label = Label(image=my_image)
    my_label.grid(row=0, column=0, columnspan=3)
    Label(text=index).grid(row=2)


before = Button(text="<", command=prev_image, width=10, state=DISABLED).grid(row=1, column=0)
Button(text="Close", command=quit, width=10).grid(row=1, column=1)
nextBtn = Button(text=">", command=nextImage, width=10).grid(row=1, column=2)

root.mainloop()
