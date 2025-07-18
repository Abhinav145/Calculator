from tkinter import *
from PIL import ImageTk,Image
import os

root=Tk()
def rotate_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter=counter+1




counter=1

files=os.listdir('wallpapers')
img_array=[]
for file in files:
    img=Image.open(os.path.join('wallpapers',file))
    resized_img=img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))


img_label=Label(root,image=img_array[0])
img_label.pack(pady=(15,10))


create_btn=Button(root,text='Next',command=rotate_image)
create_btn.pack(pady=(40,10),ipadx=40,ipady=30)
create_btn.config(font=('',20))


root.geometry('350x500')
root.configure(background='black')
root.title('wallpaper Changer')

root.mainloop()