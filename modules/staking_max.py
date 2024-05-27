import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import random_sleep


def staking_max(driver):
    try:
        # Переход в стейкинг
        print(f"Переходим в стейкинг")
        driver.get("https://app.tea.xyz/oss-staking")

    except Exception as e:
        return(f"Произошла ошибка при переходе в стейкинг: {e}")

    try:
        # Ожидание загрузки страницы настроек
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "flex justify-between mt-3")]//span'))
        )
        random_sleep()

    except Exception as e:
        return(f"Произошла ошибка при ожидании загрузки страницы настроек: {e}")

    try:
        # Выбор случайного валидатора
        num_validator = random.randint(1, 10)
        print(f"Кликаем на стейкинг в {num_validator} валидатора")
        path_validator = f'/html/body/div/div[2]/div[2]/div/section/main/div/div[4]/div/section/div[2]/div/div/div[1]/table/tbody/tr[{num_validator}]/td[5]/div/button[1]'
        validator_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, path_validator))
        )
        random_sleep()
        validator_button.click()

    except Exception as e:
        return(f"Произошла ошибка при выборе валидатора: {e}")

    try:
        # Получение значения из Available Balance
        available_balance_element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "flex justify-between mt-3")]//span'))
        )
        random_sleep()
        available_balance = available_balance_element.text.split()[0]  # Извлечение числового значения, например, '127'
        available_balance = float(available_balance.replace(',', ''))  # Преобразование в число после удаления запятых
        print(f"Доступный балланс: {available_balance}")

    except Exception as e:
        return(f"Произошла ошибка при получении доступного баланса: {e}")

    try:
        # Расчет значения для num_staking (от 70% до 90% от available_balance) целое число
        num_staking = round(available_balance * random.uniform(0.7, 0.9))
        print(f"Заносим в стейкинг от 70% до 90%: {num_staking}")

    except Exception as e:
        return(f"Произошла ошибка при расчете значения для стейкинга: {e}")

    try:
        # Вставка значения в нужное поле
        staking_input = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/div/div[2]/div[2]/div/section/main/div/div[3]/aside/div/div/div/div/div[3]/div[2]/div/input'))
        )
        random_sleep()
        staking_input.send_keys(str(num_staking))

    except Exception as e:
        return(f"Произошла ошибка при вставке значения в поле стейкинга: {e}")

    try:
        # Нажатие кнопки 'stake tea'
        stake_tea_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[3]/aside/div/button'))
        )
        random_sleep()
        stake_tea_button.click()

    except Exception as e:
        return(f"Произошла ошибка при нажатии на кнопку 'stake tea': {e}")

    try:
        # Установка галочек
        checkbox1 = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[3]/aside/div/div/div[1]/input'))
        )
        random_sleep()
        checkbox1.click()

        checkbox2 = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[3]/aside/div/div/div[2]/input'))
        )
        random_sleep()
        checkbox2.click()

    except Exception as e:
        return(f"Произошла ошибка при установке галочек: {e}")

    try:
        # Нажатие кнопки 'confirm'
        confirm_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[3]/aside/div/div/button'))
        )
        random_sleep()
        confirm_button.click()

    except Exception as e:
        return(f"Произошла ошибка при нажатии на кнопку 'confirm': {e}")

    try:
        # Ожидание кнопки 'got it' и нажатие на нее
        print(f"Ждем завершения стейкинга (максимум 2 мин)..")
        got_it_button = WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[3]/aside/div/button'))
        )
        random_sleep()
        print(f"Нажатие кнопки 'got it'")
        got_it_button.click()

    except Exception as e:
        return(f"Произошла ошибка при нажатии на кнопку 'got it': {e}")

    # Ожидание для проверки результата
    print("Задержка 10 секунд")
    time.sleep(10)

    return f'Успешно'

    # -------------------------- КОНЕЦ ЗАНОСА В СТЕЙКИНГ  -------------------------------------------
