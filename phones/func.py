import sqlite3


# Регистрация контакат
def registrationContact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите личный номер телефона: ')
    phone_job =  input('Введите рабочий номер телефона: ')
    email =  input('Введите электронную почту: ')

    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        
        values = [last_name, first_name, phone, phone_job, email]
        cursor.execute("INSERT INTO phone(last_name, first_name, phone, phone_job, email) VALUES(?, ?, ?, ?, ?)", values)
        db.commit()
        print('Вы зарегестрировали новый контакт!')
    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()

# Главное меню
def main_menu():
    main_menu = '''/nКоманды справочника:
    1 - поиск телефона по фамилии:
    2 - поиск почты по фамилии:
    3 - поиск фамилии по телефону:
    4 - редактирование контакта:
    5 - регистрация контакта:
    0 - выход
    '''
    print(main_menu)

# меню изменения
def menu_update():
    menu_update = '''/nКоманды справочника редактирование:
    1 - изменение телефона по id:
    2 - изменение email по id:
    3 - отчистка графы телефон:
    4 - отчистка графа email:
    5 - удаление по id:
    0 - назад
    '''
    print(menu_update)


# Изменение телефона по id
def update_numberPhones_by_id():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        id_phone = input('Введите и id: ')
        phone = input('Введите и номер телефона: ')
        
        update_phones = "UPDATE phone SET phone = ? where id = ? "
        data = (phone, id_phone)
        cursor.execute(update_phones, data)
        db.commit()
        print('Запись обновлена')
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()


# Изменение email по id
def update_email_by_id():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        id_phone = input('Введите и id: ')
        email = input('Введите и email: ')
        
        update_phones = "UPDATE phone SET email = ? where id = ? "
        data = (email, id_phone)
        cursor.execute(update_phones, data)
        db.commit()
        print('Запись обновлена')
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()        

# удаление по id
def delete_contact_by_id(id_phone):

    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        # id_phone = input('Введите и id: ')
        # phone = input('Введите и номер телефона: ')
        
        update_phones = "DELETE from phone where id = ? "
        # data = (id_phone)
        cursor.execute(update_phones, (id_phone))
        db.commit()
        print('Запись обновлена')
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()


# удаление графа телефон
def delete_numberPhones_by_id():

    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        id_phone = input('Введите id')
        # phone = input('Введите и номер телефона: ')
        
        update_phones = "UPDATE phone SET phone = NULL where id = ? "
        # data = (phone)
        cursor.execute(update_phones, id_phone)
        db.commit()
        print('Запись обновлена')
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()


# удаление email
def delete_email_by_id():


    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        id_phone = input('Введите id')
        # phone = input('Введите и номер телефона: ')
        
        update_phones = "UPDATE phone SET email = NULL where id = ? "
        # data = (phone)
        cursor.execute(update_phones, id_phone)
        db.commit()
        print('Запись обновлена')
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()



# поиск телефона по фамилии

def search_phone():
    

    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите фамилию для поиска: ')
        # phone = input('Введите и номер телефона: ')
        # text_search = ("SELECT phone FROM phone WHERE last_name = ?", (text, ))
        cursor.execute("SELECT last_name, first_name, phone FROM phone WHERE last_name = ?", (text, ))
        # data = (phone)
        # cursor.execute(text_search)
        db.commit()
        print(cursor.fetchall())
        # return

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()
    return

# поиск фамилии по телефону

def search_first_name():
    

    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите номер телефона для поиска: ')
        # phone = input('Введите и номер телефона: ')
        # text_search = ("SELECT phone FROM phone WHERE last_name = ?", (text, ))
        cursor.execute("SELECT last_name, first_name, phone FROM phone WHERE phone = ?", (text, ))
        # data = (phone)
        # cursor.execute(text_search)
        db.commit()
        print(cursor.fetchall())
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()
    return

# поиск почты по фамилии

def search_email():
    

    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите фамилию для поиска: ')
        # phone = input('Введите и номер телефона: ')
        # text_search = ("SELECT phone FROM phone WHERE last_name = ?", (text, ))
        cursor.execute("SELECT last_name, first_name, email FROM phone WHERE last_name = ?", (text, ))
        # data = (phone)
        # cursor.execute(text_search)
        db.commit()
        print(cursor.fetchall())
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()