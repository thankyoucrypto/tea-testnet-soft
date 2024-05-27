from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import generate_username, random_sleep
from database import save_username_to_db, is_username_account

def register_username(driver, login):
    # -------------------------- РЕГИСТРАЦИЯ USERNAME  -------------------------------------------

    try:
        if is_username_account(login):
            print(f'У аккаунта {login} уже есть username, пропускаем register_username!')
            return 'Уже есть, не выполняем'
    except Exception as e:
        return f'Ошибка при проверке наличия username: {e}'

    try:
        print("Вводим username")
        input_field = WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div/section/div[2]/article/div[4]/div/div/input'))
        )
        random_sleep()
    except Exception as e:
        return f'Ошибка при ожидании элемента ввода username: {e}'

    try:
        username = generate_username()
        print(f'Сгенерированный ник: {username}')
        input_field.send_keys(username)  # Вставка текста в поле для ввода
    except Exception as e:
        return f'Ошибка при генерации или вводе username: {e}'

    try:
        print("Кликаем complete registration")
        next_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div/section/div[2]/footer/button'))
        )
        random_sleep()
        next_button.click()
    except Exception as e:
        return f'Ошибка при нажатии кнопки завершения регистрации: {e}'

    try:
        save_username_to_db(login, username)
    except Exception as e:
        return f'Ошибка при сохранении username в базу данных: {e}'

    try:
        refresh_button = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[1]/div/div[1]/div/figure/div'))
        )
        random_sleep()
        print("Установка username успешно завершена")
    except Exception as e:
        return f'Ошибка завершения установки username: {e}'

    return 'OK'
    # -------------------------- КОНЕЦ РЕГИСТРАЦИИ USERNAME  -------------------------------------------
