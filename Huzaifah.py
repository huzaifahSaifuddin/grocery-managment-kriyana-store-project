import tkinter as tk
root = tk.Tk()
from tkinter import messagebox
cart=[]
quantit=[]

stock_wheat=10
stock_rice=10
stock_flour=10
stock_oil=10
stock_daal=10
stock_surf=10
stock_soap=10

stock={
    "Rice": 10,
    "wheat": 10, 
    "flour": 10,
    "oil": 10,
    "daal": 10,
    "soap": 10,
    "surf": 10,
}

price={
    "Rice": 50.0,
    "wheat": 40.0, 
    "flour": 30.0,
    "oil": 100.0,
    "daal": 60.0,
    "soap": 20.0,
    "surf": 25.0,
}   


def items():
        
    rice= f"  Rice:    price: 50,    stock: {stock_rice} ,"
    wheat=f"  Wheat:   price: 40,    stock: {stock_wheat},"
    flour=f"  Flour:   price: 30,    stock: {stock_flour},"
    oil=  f"  Oil:     price: 100,   stock: {stock_oil},"
    daal= f"  Daal:    price: 60,    stock: {stock_daal},"
    soap= f"  Soap:    price: 20,    stock: {stock_soap},"
    surf= f"  Surf:    price: 25,    stock: {stock_surf}"
    
    import tkinter as tk
    root1 = tk.Tk()
    root1.geometry("350x450")
    root1.title('items')
    head=tk.Label(root1,text=("Grocery Items"),font=("times new roman",30))
    head.pack(pady=(15))
    
    head=tk.Label(root1,text=(rice),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root1,text=(wheat),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root1,text=(flour),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root1,text=(oil),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root1,text=(daal),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root1,text=(soap),font=("arial",15))
    head.pack(pady=(10), anchor='w')
    
    head=tk.Label(root1,text=(surf),font=("arial",15))
    head.pack(pady=(10), anchor='w')


def veiw_cart():
    import tkinter as tk
    root6 = tk.Tk()
    root6.geometry('400x400')
    head=tk.Label(root6,text=('Your Cart'),font=("times new roman",25))
    head.pack(pady=(8))
    for i in range(len(cart)):
        head=tk.Label(root6,text=(f'Item: {cart[i]}    |    Quantity: {quantit[i]}'),font=("arial",20))
        head.pack(pady=(10), anchor='w')


def add_items():
    def add():
        item= entry1.get()
        quantity=entry2.get()
        try:
            qunt =int(quantity)
        except ValueError:
            messagebox.showerror('error','please enter a valid quantity')

        if item == "rice" or item == "wheat"or item == "flour"or item == "oil"or item == "daal"or item == "soap" or item == "surf":
            if qunt >=0 and qunt <= 10:
                messagebox.showinfo("sucessful","item added to your cart")                       
                cart.append(item)
                quantit.append(qunt)                    
            else:
                messagebox.showerror("error","not enough stock of this item")   
        else: 
            messagebox.showerror("error","this item is not avalible")
        root5.destroy()
    
    import tkinter as tk
    root5 = tk.Tk()
    root5.geometry('400x400')
    
    head=tk.Label(root5,text=('Add Items'),font=("times new roman",25))
    head.pack(pady=(8))
    
    head=tk.Label(root5,text=('Enter the name of item you want'),font=("arial",15))
    head.pack(pady=(3),anchor='w')
    
    entry1 = tk.Entry(root5, width=50,font='arial, 15' )
    entry1.pack(padx=5,ipady='3',pady='10')
    
    head=tk.Label(root5,text=('Enter the quantity of your item'),font=("arial",15))
    head.pack(pady=(3),anchor='w')
    
    entry2 = tk.Entry(root5, width=50,font='arial, 15' )
    entry2.pack(padx=5,ipady='3',pady='10')
    
    button = tk.Button(root5, text="Add",width='15',height='2',font=('arial',14),bg='grey',command=add)
    button.pack(pady='10')


def remove_item():
    def remove():
        item= entry1.get()
        quantity=entry2.get()
        try:
            qunt =int(quantity)
        except ValueError:
            messagebox.showerror('error','please enter a valid quantity')

        if item in cart:
            index = cart.index(item)
            if quantit[index] >= qunt:
                quantit[index] -= qunt
                stock[item] += qunt

                if quantit[index]==0:
                    cart.pop(index)
                messagebox.showinfo('successful','item removed from your cart')
            else:
                messagebox.showerror('error', 'not enough quantity of this titem to remove')
        else:
            messagebox.showerror('error','this item is not available in your cart')
        root7.destroy()
    
    
    import tkinter as tk
    root7 = tk.Tk()
    root7.geometry('400x400')
    
    head=tk.Label(root7,text=('Remove Items'),font=("times new roman",25))
    head.pack(pady=(8))
    
    head=tk.Label(root7,text=('Enter the name of item you want to remove'),font=("arial",15))
    head.pack(pady=(3),anchor='w')
    
    entry1 = tk.Entry(root7, width=50,font='arial, 15' )
    entry1.pack(padx=5,ipady='3',pady='10')
    
    head=tk.Label(root7,text=('Enter the quantity of your item to be removed'),font=("arial",15))
    head.pack(pady=(3),anchor='w')
    
    entry2 = tk.Entry(root7, width=50,font='arial, 15' )
    entry2.pack(padx=5,ipady='3',pady='10')
    
    button = tk.Button(root7, text="Remove",width='15',height='2',font=('arial',14),bg='grey',command=remove)
    button.pack(pady='10')


def check_out():
    if not cart:
        messagebox.showinfo('checkout', 'your cart is empty....') 
        return
    
    def check():
        messagebox.showinfo('purchased','Thanks for Shopping :)')
        cart.clear()
        quantit.clear()
        root8.destroy()
    import tkinter as tk
    root8= tk.Tk()
    head=tk.Label(root8,text=("Check Out"),font=("times new roman",30))
    head.pack(pady=(15))
    total_cost = 0
    for i in range(len(cart)):
        item = cart[i]
        cost= price[item]  * quantit[i]
        total_cost+=cost 
        
        head=tk.Label(root8,text=(f'item: {item}   |   quantity: {quantit[i]}   |   Prices;  ${price[item]:.2f}   |   Total: ${cost:.2f}'),font=("arial",15))
        head.pack(pady=(10), anchor='w')
        
        head=tk.Label(root8,text=(f'Total amount: ${total_cost:.2f}'),font=("arial",15))
        head.pack(pady=(3),anchor='w')
    
    button4= tk.Button(root8,text="Check Out!!",width=15,height=2,font=('arial',15),bg='grey',command=check)
    button4.pack(padx= 10, pady=10)


def second():
    root.destroy()
    
    import tkinter as tk
    root2 = tk.Tk()
    root2.geometry("700x600")
    root2.title("Kiryana Store")
    
    head=tk.Label(root2,text=("User menu"),font=("times new roman",30))
    head.pack(pady=(15))
    
    button4= tk.Button(root2,text="Show Items",width=15,height=2,font=('arial',15),bg='grey',command=items)
    button4.pack(padx= 10, pady=10, anchor='w')
    
    button4= tk.Button(root2,text="Add Items",width=15,height=2,font=('arial',15),bg='grey',command=add_items)
    button4.pack(padx= 10, pady=10, anchor='w')
    
    button5= tk.Button(root2,text="Remove Item",width=15,height=2,font=('arial',15),bg='grey',command=remove_item)
    button5.pack(padx= 10, pady=10, anchor='w')
    
    button6= tk.Button(root2,text="View Cart",width=15,height=2,font=('arial',15),bg='grey',command=veiw_cart)
    button6.pack(padx= 10, pady=10, anchor='w')
    
    button7= tk.Button(root2,text="Check Out",width=15,height=2,font=('arial',15),bg='grey',command=check_out)
    button7.pack(padx= 10, pady=10, anchor='w')


def admin_login():
    root.destroy()
    import tkinter as tk
    root3 = tk.Tk()
    
    def login():
        email=admin.get()
        password= paas.get()
        if email== 'admin@gmail.com' and password == '123456':
            root3.destroy()
            import tkinter as tk
            root4 = tk.Tk()
            root4.geometry('500x600')
            root4.title('kiryana store')
            
            head=tk.Label(root4,text=("Welcome Admin"),font=("times new roman",30))
            head.pack(pady=(15))
            
            button4= tk.Button(root4,text="Show Items",width=15,height=2,font=('arial',15),bg='grey',command=items)
            button4.pack(padx= 10, pady=10, anchor='w')
    
            button4= tk.Button(root4,text="Change Stock",width=15,height=2,font=('arial',15),bg='grey')
            button4.pack(padx= 10, pady=10, anchor='w')
    
            button5= tk.Button(root4,text="Add Item",width=15,height=2,font=('arial',15),bg='grey')
            button5.pack(padx= 10, pady=10, anchor='w')
            
        else:
            messagebox.showerror('ohh!', 'worng ID or password')
    
    root3.geometry(("500x600"))
    root3.title("kiryana store") 
    root3.configure(background='lightgrey')

    lable = tk.Label(root3,bg='light grey', text=("Admin Login"), font=('times new roman', 30))
    lable.pack(padx=(20), pady=(20))

    label = tk.Label(root3, bg='light grey', text=("Enter ID"), font=('arial', 15))
    label.pack(padx=20, pady=15)

    admin = tk.Entry(root3,width=(30) ,font=('arial', 14))
    admin.pack(ipady=3)

    lab = tk.Label(root3, bg='light grey', text=("Enter Password"), font=('arial', 15))
    lab.pack(padx=20, pady=15)

    paas = tk.Entry(root3, width=(30), font=('arial', 14))
    paas.pack(ipady=3)

    button = tk.Button(root3, text='Login!',width=(10),font=('arial', 15),command=login)
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