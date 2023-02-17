import controller



def set_new_contact():
    elements = controller.get_elements()
    name = elements['name'].get()
    surname = elements['surname'].get()
    phone_number = elements['phone'].get()
    contact = f'{name} {surname}: {phone_number}'
    controller.add_to_listbox(contact)