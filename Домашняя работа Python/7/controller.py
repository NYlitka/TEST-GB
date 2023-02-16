import model
import view
from tkinter import *
from tkinter import ttk

def add_contact():
    view.set_new_contact()



def start ():
    root = Tk()
    frm = ttk. Frame (root, padding=30)
    frm.grid()

    Label(frm, text= 'Телефонный справочник'). grid(row=0, column=0)
    
    Label(frm, text= 'Введите имя'). grid(row=1, column=0)
    name_ent= Entry(frm).grid(row=1,column=1)
    Label(frm, text= 'Введите фамилию'). grid(row=2, column=0)
    surname_ent= Entry(frm).grid(row=2,column=1)
    Label(frm, text= 'Введите номер телефона'). grid(row=3, column=0)
    phone_number_ent= Entry(frm).grid(row=3,column=1)

    add_contact_btn = Button(frm, text= 'Добавить контакт', command=add_contact). grid(row=4, column=0)
    delete_contact_btn = Button(frm, text= 'Удалить контакт'). grid(row=6, column=1)

    all_contacts = Listbox(frm).grid(row=6,column=0)
    root.mainloop()



start ()