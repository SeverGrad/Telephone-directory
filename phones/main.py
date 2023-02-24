import sqlite3
import func

with sqlite3.connect("phones.db") as db:
    cursor = db.cursor()


        

func.main_menu()

num = int(input('Введите номер команды: '))



while True:
    if num == 1:
        func.search_phone()
        while num == 1:
            func.main_menu()
            num = int(input('Введите номер команды: '))
    elif num == 2:
        func.search_email()
        while num == 2:
            func.main_menu()
            num = int(input('Введите номер команды: '))
    elif num == 3:
        func.search_first_name()
        while num == 3:
            func.main_menu()
            num = int(input('Введите номер команды: '))
    elif num == 4:
        func.menu_update()
        num = int(input('Введите номер команды: '))
        if num == 1:
            func.update_numberPhones_by_id() 
            while num == 1:
                func.menu_update()
                num = int(input('Введите номер команды: '))
        elif num == 2:
            func.update_email_by_id()
            while num == 2:
                func.menu_update()
                num = int(input('Введите номер команды: '))
        elif num == 3:
            func.delete_numberPhones_by_id()
            while num == 3:
                func.menu_update()
                num = int(input('Введите номер команды: '))
        elif num == 4:
            func.delete_email_by_id()
            while num == 4:
                func.menu_update()
                num = int(input('Введите номер команды: '))
        elif num == 5:
            id_phone = input('Введите id для удаления: ')
            func.delete_contact_by_id(id_phone)
            while num == 5:
                func.menu_update()
                num = int(input('Введите номер команды: '))
        elif num == 0:
            func.main_menu()
            num = int(input('Введите номер команды: '))
    elif num == 5:
        func.registrationContact()
        while num == 5:
            func.main_menu()
            num = int(input('Введите номер команды: '))
    elif num == 0:
        break

