import sqlite3
from fake_useragent import UserAgent


# СОЗДАНИЕ БАЗЫ ДАННЫХ: №, LOGIN, PASS, USERNAME, PRIVATE_KEY, POINTS, STATUS
def create_database():
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
                 (id INTEGER PRIMARY KEY,
                  login TEXT,
                  pass TEXT,
                  reserv_mail TEXT,
                  username TEXT,
                  private_key TEXT,
                  balance TEXT,
                  staking TEXT,
                  rewards TEXT,
                  points TEXT,
                  status TEXT,
                  user_agent TEXT,
                  address TEXT,
                  refer_link TEXT
                  )''')
    conn.commit()
    conn.close()


def get_account_info_from_db(login):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()

    # Извлечение информации из БД по логину
    c.execute("SELECT * FROM accounts WHERE login=?", (login,))
    account_info = c.fetchone()

    conn.close()

    if account_info:
        # Формирование сообщения с информацией об аккаунте
        message = f"Информация об аккаунте:\n\nЛогин: {account_info[1][:3]}{'*' * (len(account_info[1]) - 3)}\nПароль: {account_info[2][:3]}{'*' * (len(account_info[2]) - 3)}\nUsername: {account_info[4][:3]}{'*' * (len(account_info[4]) - 3)}\nПриватный ключ: {account_info[5][:3]}{'*' * (len(account_info[4]) - 3)}\n\nBalance: {account_info[6]}\nStaking: {account_info[7]}\nUnclaimed revards: {account_info[8]}\nPoints: {account_info[9]}"
        return message
    else:
        return "Аккаунт с таким логином не найден в базе данных."


# ФУНКЦИЯ СОХРАНЕНИЯ ПОЧТЫ В БД LOGIN:PASS
def save_email_to_db(login, password, reserv_mail):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()

    # Проверяем, существует ли уже такой логин в базе данных
    c.execute('SELECT * FROM accounts WHERE login = ?', (login,))
    existing_account = c.fetchone()

    if existing_account:
        print(f"Логин {login} уже существует в базе данных, не добавляем.")
    else:
        # Сохраняем новый аккаунт в базе данных
        c.execute('INSERT INTO accounts (login, pass, reserv_mail) VALUES (?, ?, ?)', (login, password, reserv_mail))
        conn.commit()
        print(f"Аккаунт {login} успешно сохранен в базе данных.")

    conn.close()


# ФУНКЦИЯ ПОЛУЧЕНИЯ USERAGENT В БД LOGIN
def get_user_agent_db(login):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()

    try:
        # Проверяем, существует ли уже такой логин в базе данных
        c.execute('SELECT user_agent FROM accounts WHERE login = ?', (login,))
        existing_account = c.fetchone()

        if existing_account and existing_account[0]:
            print(f"Useragent для {login} уже существует в базе данных")
            return existing_account[0]
        else:
            # Генерируем новый user_agent и сохраняем его
            user_agent = UserAgent().random
            c.execute('UPDATE accounts SET user_agent = ? WHERE login = ?', (user_agent, login))
            conn.commit()
            print(f"Useragent для {login} успешно сохранен в базе данных.")
            return user_agent
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
        return None
    finally:
        conn.close()


# ФУНКЦИЯ СОХРАНЕНИЯ USERNAME В БД
def save_statistic_to_db(login, balance, staking, rewards, points):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('UPDATE accounts SET balance= ?, staking= ?, rewards= ?, points= ? WHERE login = ?', (balance, staking, rewards, points , login))
    conn.commit()
    conn.close()


# ФУНКЦИЯ СОХРАНЕНИЯ STATUS В БД
def save_status_to_db(login,status):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('UPDATE accounts SET status= ? WHERE login = ?', (status, login))
    conn.commit()
    conn.close()

# ФУНКЦИЯ ПРОВЕРКИ STATUSА В БАНЕ
def is_account_in_ban_db(login):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('SELECT status FROM accounts WHERE login = ?', (login,))
    status = c.fetchone()  # Получаем значение статуса

    if status and status[0] == 'BAN':  # Проверяем, что статус есть и он равен 'BAN'
        conn.close()  # Закрываем соединение с базой данных
        return True
    else:
        conn.close()  # Закрываем соединение с базой данных
        return False

# ФУНКЦИЯ ПРОВЕРКИ НАЛИЧИЯ ПОИНТОВ ДЛЯ КЛЕЙМА В БД
def is_points_in_acc_bd(login):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('SELECT rewards FROM accounts WHERE login = ?', (login,))
    rewards = c.fetchone()  # Получаем значение rewards

    if rewards and rewards[0] is not None and rewards[0] != 0:  # Проверяем, что rewards не является None и не равно 0
        conn.close()  # Закрываем соединение с базой данных
        return True
    else:
        conn.close()  # Закрываем соединение с базой данных
        return False


# ФУНКЦИЯ СОХРАНЕНИЯ private_key В БД
def save_private_key_to_db(login, private_key):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('UPDATE accounts SET private_key = ? WHERE login = ?', (private_key, login))
    conn.commit()
    conn.close()


# ФУНКЦИЯ СОХРАНЕНИЯ address В БД
def save_address_to_db(login, address):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('UPDATE accounts SET address = ? WHERE login = ?', (address, login))
    conn.commit()
    conn.close()


# ФУНКЦИЯ СОХРАНЕНИЯ refer link В БД
def save_refer_link_to_db(login, refer_link):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('UPDATE accounts SET refer_link = ? WHERE login = ?', (refer_link, login))
    conn.commit()
    conn.close()


# ФУНКЦИЯ СОХРАНЕНИЯ private_key В БД
def save_username_to_db(login, username):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('UPDATE accounts SET username = ? WHERE login = ?', (username, login))
    conn.commit()
    conn.close()


# ФУНКЦИЯ ПОЛУЧЕНИЯ АККАУНТОВ
def get_all_accounts():
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('SELECT login, pass, reserv_mail FROM accounts ')
    accounts = c.fetchall()
    conn.close()
    return accounts

# ФУНКЦИЯ ПОЛУЧЕНИЯ АККАУНТОВ
def get_accounts_from_file(logins):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    # Создаем плейсхолдеры для логинов
    placeholders = ','.join(['?'] * len(logins))
    # Используем плейсхолдеры в запросе
    query = f'SELECT login, pass, reserv_mail FROM accounts WHERE login IN ({placeholders})'
    c.execute(query, logins)
    accounts = c.fetchall()
    conn.close()
    return accounts


# ФУНКЦИЯ ПОЛУЧЕНИЯ ЕСТЬ ЛИ USERNAME У АККАУНТА ПО ЛОГИНУ
def is_username_account(login):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('SELECT username FROM accounts WHERE login = ?', (login,))
    account = c.fetchone()
    conn.close()

    if account and account[0]:  # Проверяем, есть ли результат и не является ли он NULL
        return True
    else:
        return False


# ФУНКЦИЯ ПОЛУЧЕНИЯ ЕСТЬ ЛИ PRIVATE KEY У АККАУНТА ПО ЛОГИНУ
def is_private_key_account(login):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('SELECT private_key FROM accounts WHERE login = ?', (login,))
    account = c.fetchone()
    conn.close()

    if account and account[0]:  # Проверяем, есть ли результат и не является ли он NULL
        return True
    else:
        return False


# ФУНКЦИЯ ОБНОВЛЕНИЯ АККАУНТА
def update_account_status(login, status):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute('UPDATE accounts SET status = ? WHERE login = ?', (status, login))
    conn.commit()
    conn.close()
