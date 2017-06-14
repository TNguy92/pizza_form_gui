from tkinter import *
from tkinter import messagebox

def thankYou():
    messagebox.showinfo("Submitted Order:", "Thank you for ordering Thomas Pizza, Please come again!")

def nextBox2():

    root3 = Tk()
    root3.wm_title("Payment Information")
    Label(root3, text="------ Enter Information Below: ----------").grid(row=0)
    Label(root3, text = "Quantity:").grid(row = 1)
    Label(root3, text = "Coupon Code:").grid(row = 2)
    Label(root3, text = "Payment Method:").grid(row = 3)
    Label(root3, text = "Credit Card Number:").grid(row = 4)
    Label(root3, text = "Expiration Date: ").grid( row = 5)
    Label(root3, text = "Sub Total: (Sub Total Amount)").grid(row = 6)
    Label(root3, text = "Tax 5%: (Tax * Sub Total Amount)").grid(row = 7)
    Label(root3, text = "Total Amount: (Amount after the tax)").grid(row = 8)

    Button(root3, text = 'Submit Order', command = thankYou).grid(row = 9, column = 1, sticky = W, pady = 4)
    Button(root3, text = 'Cancel', command = root3.quit).grid(row = 9, column = 0, sticky = W, pady = 4)
    e1 = Entry(root3)
    e2 = Entry(root3)
    e3 = Entry(root3)
    e4 = Entry(root3)
    e5 = Entry(root3)

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    e5.grid(row=5, column=1)

    root3.mainloop()


def nextBox():
    root.destroy()
    root2 = Tk()
    root2.wm_title("Order Number: 777 ")
    v = IntVar()
    Label(root2, text="----------------------------------------------------------------------").grid(row=0)
    Label(root2, text = "Pizza Size:").grid(row = 1)
    Radiobutton(root2, text = "Small", variable = v, value = 1).grid(row = 1, column = 1)
    Radiobutton(root2, text = "Medium", variable = v, value = 2).grid(row = 1, column = 2)
    Radiobutton(root2, text = "Large", variable = v, value = 3).grid(row = 1, column = 3)
    Radiobutton(root2, text = "Super Large", variable = v, value = 4).grid(row = 1, column = 4)

    Label(root2, text = "----------------------------------------------------------------------").grid(row = 2)
    Label(root2, text = "Toppings (Add $0.50 Each):").grid(row = 3)
    Radiobutton(root2, text = "Pepperoni", variable = v, value = 5).grid(row = 3, column = 1)
    Radiobutton(root2, text = "Onions", variable = v, value = 6).grid(row = 3, column = 2)
    Radiobutton(root2, text = "Sausage", variable = v, value = 7).grid(row = 3, column = 3)
    Radiobutton(root2, text = "Anchovies", variable = v, value = 8).grid(row = 4, column = 1)
    Radiobutton(root2, text = "Olives", variable = v, value = 9).grid(row = 4, column = 2)
    Radiobutton(root2, text = "Pineapples", variable = v, value = 10).grid(row = 4, column = 3)

    Button(root2, text = 'Pizza Finish', command = nextBox2).grid(row = 6, column = 1, sticky = W, pady = 4)
    Button(root2, text = 'Cancel', command = root2.quit).grid(row = 6, column = 0, sticky = W, pady = 4)
    root2.mainloop()



root = Tk()
root.wm_title("Pizza Form - Thomas Nguyen")

Label(root, text = "Name:").grid(row = 0)
Label(root, text = "Address:").grid(row = 1)
Label(root, text = "City:").grid(row = 2)
Label(root, text = "Zip Code:").grid(row = 3)
Label(root, text = "State:").grid(row = 4)
Label(root, text = "Phone Number:").grid(row = 5)

entry0= Entry(root)
entry1= Entry(root)
entry2= Entry(root)
entry3= Entry(root)
entry4= Entry(root)
entry5= Entry(root)

entry0.grid(row = 0, column = 1)
entry1.grid(row = 1, column = 1)
entry2.grid(row = 2, column = 1)
entry3.grid(row = 3, column = 1)
entry4.grid(row = 4, column = 1)
entry5.grid(row = 5, column = 1)

Label(root, text = "-------------- Thank You! ------------").grid(row = 8)
Button(root, text = 'Order Pizza Time!', command = nextBox).grid(row = 6, column = 1, sticky = W, pady = 4)
Button(root, text = 'Cancel', command = root.quit).grid(row = 6, column = 0, sticky = W, pady = 4)

root.mainloop()

