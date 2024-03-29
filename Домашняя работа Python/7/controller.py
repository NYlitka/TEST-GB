import model
import view
from tkinter import *
from tkinter import ttk

elements = {}

def add_contact():
    view.set_new_contact()

def add_to_listbox(contact):
    elements['contacts list'].insert(END, contact)

def delete_contact():
    elements['contacts list'].delete(elements[ 'contacts list'].curselection()[0])

def get_elements():
    return elements

def start ():
    root = Tk()
    frm = ttk. Frame (root, padding=30)
    frm.grid()

    Label(frm, text= 'Телефонный справочник'). grid(row=0, column=0)
    
    Label(frm, text= 'Введите имя'). grid(row=1, column=0)
    name_ent= Entry(frm)
    name_ent.grid(row=1,column=1)
    elements['name']=name_ent

    Label(frm, text= 'Введите фамилию'). grid(row=2, column=0)
    surname_ent= Entry(frm)
    surname_ent.grid(row=2,column=1)
    elements['surname']=surname_ent

    Label(frm, text= 'Введите номер телефона'). grid(row=3, column=0)
    phone_number_ent= Entry(frm)
    phone_number_ent.grid(row=3,column=1)
    elements['phone']=phone_number_ent

    add_contact_btn = Button(frm, text= 'Добавить контакт', command = add_contact). grid(row=4, column=0)
    delete_contact_btn = Button(frm, text= 'Удалить контакт', command = delete_contact). grid(row=6, column=1)

    all_contacts = Listbox(frm)
    all_contacts = Listbox(frm).grid(row=6,column=0)
    elements['all contacts']=all_contacts

    root.mainloop()



start ()