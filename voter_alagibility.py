from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()

# function

def checkage():
    age=age_input.get()
    if age>str(18):
        messagebox.showinfo("eligible for voting")
    else:
        messagebox.showerror("not eligible for voting")




# gui interface
root.geometry('350x500')
root.configure(background='#FF0000')
root.title('Voter eligibility')
root.iconbitmap('letter-v_9590176.ico')
# gui image
img=Image.open('gettyimages-1252066448-612x612.jpg')
resized_img=img.resize((550,750))
img=ImageTk.PhotoImage(Image.open('gettyimages-1252066448-612x612.jpg'))

label_img=Label(root,image=img)
label_img.pack(pady=(10,10))  


#age label

age_label=Label(root,text='Enter the Age of Voter:',bg='#FFFFFF')
age_label.pack()
age_label.config(font=('',20))


# age input
age_input=Entry(root,width=19)
age_input.pack(pady=(10,10),ipady=5)
age_input.config(font=('',20))

#check button
check_btn=Button(root,text='Check',command=checkage)
check_btn.pack(pady=(50,10),ipady=(20),ipadx=(20))
check_btn.config(font=('',30))
root.mainloop()

