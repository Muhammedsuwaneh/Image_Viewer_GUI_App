
from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("Image viewer")
root.iconbitmap('Gallery_icon-icons.com_76885.ico')
root.geometry("800x600")

frame1 = LabelFrame(root, padx=5, pady=5)
frame1.pack()
frame2 = LabelFrame(root, padx=5, pady=5)
frame2.pack()

# Design
img1 = ImageTk.PhotoImage(Image.open('images/img1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('images/img2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('images/img3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('images/img4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('images/img5.jpg'))
img6 = ImageTk.PhotoImage(Image.open('images/img6.jpg'))

image_list = [img1, img2, img3, img4, img5, img6]

label = Label(frame1, image=image_list[1], width=500, height=500)
label.grid(row=0, column=0, columnspan=3)

# App logic


def next(current):
    global label
    global next_btn
    global prev_btn

    label.grid_forget()
    label = Label(frame1, image=image_list[current-1], width=500, height=500)
    next_btn = Button(frame2, text=">>", command=lambda: next(current+1))
    prev_btn = Button(frame2, text="<<", command=lambda: previous(current-1))

    if current == 5:
          next_btn = Button(frame2, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    prev_btn.grid(row=1, column=0, padx=2, pady=2)
    next_btn.grid(row=1, column=2, padx=2, pady=2)


def previous(current):
    global label
    global next_btn
    global prev_btn

    label.grid_forget()
    label = Label(frame1, image=image_list[current-1], width=500, height=500)
    next_btn = Button(frame2, text=">>", command=lambda: next(current+1))
    prev_btn = Button(frame2, text="<<", command=lambda: previous(current-1))

    if current == 0:
        prev_btn = Button(frame2, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    prev_btn.grid(row=1, column=0, padx=2, pady=2)
    next_btn.grid(row=1, column=2, padx=2, pady=2)


prev_btn = Button(frame2, text="<<", command=previous)
exit_btn = Button(frame2, text="exit", command=root.quit)
next_btn = Button(frame2, text=">>", command=lambda: next(1))

prev_btn.grid(row=1, column=0, padx=2, pady=2)
exit_btn.grid(row=1, column=1, padx=2, pady=2)
next_btn.grid(row=1, column=2, padx=2, pady=2)

root.mainloop()
