import tkinter as tk
root = tk.Tk()
from tkinter import messagebox

def items():
        
    rice="Rice: price: 50, stock: 10,"
    wheat=" Wheat: price: 40, stock: 10,"
    flour= " Flour: price: 30, stock: 10,"
    oil= " Oil: price: 100, stock: 10,"
    daal=" Daal: price: 60, stock: 10,"
    soap=" Soap: price: 20, stock: 10,"
    surf= "Surf: price: 25, stock: 10"
    
    import tkinter as tk
    root = tk.Tk()
    root.geometry("350x450")
    root.title('items')
    head=tk.Label(root,text=("Grocery Items"),font=("times new roman",30))
    head.pack(pady=(15))
    
    head=tk.Label(root,text=(rice),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root,text=(wheat),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root,text=(flour),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root,text=(oil),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root,text=(daal),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root,text=(soap),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root,text=(surf),font=("arial",15))
    head.pack(pady=(10), anchor='w')

def add_items():
    import tkinter as tk
    root = tk.Tk()
    root.geometry('400x350')
    entry = tk.Entry(root, width=30)
    entry.pack(side=tk.LEFT, padx=5)

    button = tk.Button(root, text="Add Task")
    button.pack(side=tk.LEFT)

    button = tk.Button(root, text="Delete Task")
    button.pack(side=tk.BOTTOM,pady=5)



def second():
   
    
    import tkinter as tk
    root = tk.Tk()
    root.geometry("700x600")
    root.title("Kiryana Store")
    
    head=tk.Label(root,text=("User menu"),font=("times new roman",30))
    head.pack(pady=(15))
    
    button4= tk.Button(root,text="Show Items",width=15,height=2,font=('arial',15),bg='grey',command=items)
    button4.pack(padx= 10, pady=10, anchor='w')
    
    button4= tk.Button(root,text="Add Items",width=15,height=2,font=('arial',15),bg='grey',command=add_items)
    button4.pack(padx= 10, pady=10, anchor='w')
    
    button5= tk.Button(root,text="Remove Item",width=15,height=2,font=('arial',15),bg='grey')
    button5.pack(padx= 10, pady=10, anchor='w')
    
    button6= tk.Button(root,text="View Cart",width=15,height=2,font=('arial',15),bg='grey')
    button6.pack(padx= 10, pady=10, anchor='w')
    
    button7= tk.Button(root,text="Check Out",width=15,height=2,font=('arial',15),bg='grey')
    button7.pack(padx= 10, pady=10, anchor='w')


def admin_login():
    
    import tkinter as tk
    root = tk.Tk()
    
    def login():
        email=admin.get()
        password= paas.get()
        if email== 'admin@gmail.com' and password == '123456':
            import tkinter as tk
            root = tk.Tk()
            root.geometry('500x600')
            root.title('kiryana store')
            
            head=tk.Label(root,text=("Welcome Admin"),font=("times new roman",30))
            head.pack(pady=(15))
            
            button4= tk.Button(root,text="Show Items",width=15,height=2,font=('arial',15),bg='grey',command=items)
            button4.pack(padx= 10, pady=10, anchor='w')
    
            button4= tk.Button(root,text="Change Stock",width=15,height=2,font=('arial',15),bg='grey')
            button4.pack(padx= 10, pady=10, anchor='w')
    
            button5= tk.Button(root,text="Add Item",width=15,height=2,font=('arial',15),bg='grey')
            button5.pack(padx= 10, pady=10, anchor='w')
            
            root.mainloop()
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
    

root.geometry("600x400")
root.title('kiryana store')

label2=tk.Label(root, text=("____Welcome To Kiryana store!____"), font=('times new roman',30 ))
label2.pack(pady=(15))

label3=tk.Label(root, text=("Continue as:-"), font=('arial',20))
label3.pack(pady=(40))

button2=tk.Button(root, bg="grey", text=("Admin"),width=(12), height='2',font=("arial", 19),command=admin_login)
button2.pack(pady=15)

button3=tk.Button(root, bg="grey",text=("User"),width=(12), height='2',font=("arial", 19),command=second)
button3.pack(pady=15)
    
    
root.mainloop()