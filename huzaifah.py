import tkinter as tk
root = tk.Tk()
from tkinter import messagebox
def login():
    email=admin.get()
    password= paas.get()
    if email== 'admin@gmail.com' and password == '123456':
        messagebox.showinfo('yayyy','login successful')
    else:
        messagebox.showerror('ohh!', 'worng ID or password')
    
root.geometry(("500x600"))
root.title("kiryana store") 
root.configure(background='lightgrey')

lable = tk.Label(root,bg='light grey', text=("Admin Login"), font=('times new roman', 30))
lable.pack(padx=(20), pady=(20))

label = tk.Label(root, bg='light grey', text=("Enter ID"), font=('arial', 15))
label.pack(padx=20, pady=15)

admin = tk.Entry(root,width=(30) ,font=('arial', 14))
admin.pack(ipady=3)

lab = tk.Label(root, bg='light grey', text=("Enter Password"), font=('arial', 15))
lab.pack(padx=20, pady=15)

paas = tk.Entry(root, width=(30), font=('arial', 14))
paas.pack(ipady=3)

button = tk.Button(root, text='Login!',width=(10),font=('arial', 15),command=login)
button.pack(pady=10)


root.mainloop()