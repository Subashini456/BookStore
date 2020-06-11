from tkinter import *
from backend import Database

database = Database("book.db")

def get_index_row(event):
    try:
        global selected_index
        index = list1.curselection()[0]
        selected_index = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_index[1])
        e2.delete(0,END)
        e2.insert(END,selected_index[2])
        e3.delete(0,END)
        e3.insert(END,selected_index[3])
        e4.delete(0,END)
        e4.insert(END,selected_index[4])
    except IndexError:
        pass
    

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(),Author_text.get(),Year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert_data(title_text.get(),Author_text.get(),Year_text.get(),isbn_text.get())    
    list1.delete(0,END)  
    list1.insert(END,(title_text.get(),Author_text.get(),Year_text.get(),isbn_text.get()))

def delete_command():
    database.delete_item(selected_index[0])  

def update_command():
    database.update_data(selected_index[0],title_text.get(),Author_text.get(),Year_text.get(),isbn_text.get())   
    

window = Tk()

window.wm_title("BookStore")

#lable
l1 = Label(window,text = "Title")
l1.grid(row = 0,column = 0)

l1 = Label(window,text = "Author")
l1.grid(row = 0,column = 2)

l1 = Label(window,text = "Year")
l1.grid(row = 1,column = 0)

l1 = Label(window,text = "ISBN")
l1.grid(row = 1,column = 2)

#entry
title_text = StringVar()
e1 = Entry(window,textvariable = title_text)
e1.grid(row = 0,column = 1)

Author_text = StringVar()
e2 = Entry(window,textvariable = Author_text)
e2.grid(row = 0,column = 3)

Year_text = StringVar()
e3 = Entry(window,textvariable = Year_text)
e3.grid(row = 1,column = 1)

isbn_text = StringVar()
e4 = Entry(window,textvariable = isbn_text)
e4.grid(row = 1,column = 3)

#listView
list1 = Listbox(window,height = 6,width = 35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

#letting each other known .....list and scrollbar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>',get_index_row)

#button
b1 = Button(window,text="ViewAll",width=13,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search Entry",width=13,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add Entry",width=13,command = add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update",width=13,command = update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",width=13,command = delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=13,command = window.destroy)
b6.grid(row=7,column=3)


window.mainloop()