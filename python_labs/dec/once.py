import sqlite3
import functools

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called: 
            # func.called = () # Сравнить работу once в случае 
            # сохранения внутри func и внутри inner        
            func(*args, **kwargs)
            inner.called = True
            print('called is changed')
    return func 
    inner.called = False 
    return inner

@once
def connect_to_db(path_to_db):
    connection = None
    if (path_to_db):
        try:
            connection = sqlite3.connect(
                'file:' + path_to_db + '?mode=rw', uri=True)
            # connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}

    return connection


def wrapper():
    # он должен в себе содержать:
    # ввод с клавиатуры или получения из другого источника
    # логина и пароля
    print("Введите логин: ")
    log = input()
    print("Введите пароль: ")
    pwd = input()
    # получение из БД пользователя с тем логином, который был введен
    # сверка пароля введенного пользователем с паролем, хранящемся в БД
    usersString = str(users)
    user = usersString.find("('"+log+"', '"+pwd+"', ")
    if user != -1:
        pz = private_zone_area()
    # если успех и аутентификация прошла успешно, показываем
    else:
        print("пользователя с таким паролем - нет")
    # private_zone_area
    # если нет, то показать надпись пользователю о том, пользователя с таким паролем - нет
    pass


def private_zone_area():
    print("private_zone_area")

    return "private_zone_area"


def get_users_from_table(conn, table):
    sql_query = "SELECT * FROM " + str(table)
    cursor = conn.cursor()
    res = cursor.execute(sql_query)
    users_lst = res.fetchall()

    print(users_lst)

    return users_lst


conn_dict = connect_to_db('example.db')
conn, cur = conn_dict["conn"], conn_dict["cursor"]

# 2 вариант
try:
    sql_query = '''CREATE TABLE users
             (login text, pass text, role int)'''
    cur.execute(sql_query)
except sqlite3.OperationalError as e:
    e_str = str(e)

    if ("already exists" in e_str):
        print(f' NOTICE: {e}. CONTINUE ')

        sql_query = '''INSERT INTO users VALUES (?, ?, ?)'''

        users_lst = [('root', '123', 0), ('admin', '789', 1), ('user', 'qwe',
                                                               2)]
        try:
            cur.executemany(sql_query, users_lst)
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error with adding users to db. {e}')

users = get_users_from_table(conn, 'users')

#print(users)
wrapper()
conn.close()
cur, conn = None, None
