from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()

def handle_login():
    email=email_input.get()
    password=pass_input.get()
    if email=='ab1236127@gmail.com' and password=='9882596645':
        messagebox.showinfo('Login successful')
    else:
        messagebox.showerror('Login unsuccessful')

root.title("Gmail login")
root.iconbitmap('5415922.ico')
root.minsize(400,400)
root.maxsize(1000,1000)
root.geometry('350x500')
root.configure(background='#FFFFFF')
img=Image.open('5415922.ico')
resized_img=img.resize((300,450))
img=ImageTk.PhotoImage(Image.open('5415922.ico'))

label_img=Label(root,image=img)
label_img.pack(pady=(10,10))  


label_text=Label(root,text='Gmail',bg='#FFFFFF')
label_text.pack()
label_text.config(font=("Helvetica",30))



email_label=Label(root,text='Enter Email:',bg='#FFFFFF')
email_label.pack(pady=(20,5))
email_label.config(font=(20))

email_input=Entry(root,width=50)
email_input.pack(ipady=5)


pass_label=Label(root,text='Password:',bg='#FFFFFF')
pass_label.pack(pady=(20,5))
pass_label.config(font=(20))

pass_input=Entry(root,width=50)
pass_input.pack(ipady=5)


login_btn=Button(root,text='Login Here',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,5))


root.mainloop()
