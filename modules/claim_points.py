import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import random_sleep
from database import is_points_in_acc_bd


def claim_points(driver,login):
    # -------------------------- КЛЕЙМИМ НАГРАДЫ ЗА СТЕЙКИНГ  -------------------------------------------

    try:
        if (is_points_in_acc_bd(login) == False):
            print(f'У аккаунта {login} нет доступных поинтов для клейма, пропускаем модуль!')
            return 'Нет доступных наград, пропускаем'
    except Exception as e:
        return(f"Произошла ошибка при проверке наличия поинтов в аккаунте: {e}")

    try:
        driver.get("https://app.tea.xyz/")
        refresh_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[1]/div/div[3]/div/figure/div'))
        )
        random_sleep()
        print('Обновляем доступные награды за стейкинг')
        refresh_button.click()
    except Exception as e:
        return(f"Произошла ошибка при обновлении доступных наград за стейкинг: {e}")

    try:
        claim_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[1]/div/div[3]/button'))
        )
        random_sleep()
        print(f"Кликаем claim rewards")
        claim_button.click()
    except Exception as e:
        return(f"Произошла ошибка при нажатии кнопки claim rewards: {e}")

    try:
        claim_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/button'))
        )
        random_sleep()
        print(f"Кликаем claim rewards")
        claim_button.click()
    except Exception as e:
        return(f"Произошла ошибка при нажатии кнопки claim rewards: {e}")

    try:
        confirm_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div/div/button'))
        )
        random_sleep()
        print(f"Кликаем confirm")
        confirm_button.click()
    except Exception as e:
        return(f"Произошла ошибка при нажатии кнопки confirm: {e}")

    try:

        # Нажимаем done


        try:
            print("Нажимаем done (ждем максимум 180 секунд")
            next_button = WebDriverWait(driver, 180).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div/button'))
            )
            random_sleep()
            next_button.click()
        except Exception as e:
            return f'Ошибка при нажатии кнопки завершения регистрации: {e}'

        print("Задержка 20 секунд")
        time.sleep(20)
        return f'Успешно'
    except Exception as e:
        return (f"Произошла ошибка при задержке: {e}")

    # -------------------------- КОНЕЦ КЛЕЙМА НАГРАД ЗА СТЕЙКИНГ  -------------------------------------------
