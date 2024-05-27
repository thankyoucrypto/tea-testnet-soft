import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import random_sleep


def staking_borrow(driver):
    # -------------------------- ЗАБИРАЕМ СО СТЕЙКИНГА  -------------------------------------------

    try:
        print(f"Переходим в стейкинг для вывода 25%")
        driver.get("https://app.tea.xyz/oss-staking")
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/div/div[2]/div[2]/div/section/main/div/div[4]/div/section/div[2]/header/div/button[2]'))
        )
        random_sleep()
    except Exception as e:
        return(f"Произошла ошибка при переходе в стейкинг для вывода 25%: {e}")

    try:
        print(f"Нажатие кнопки 'stake by me'")
        stake_by_me_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div/div[2]/div[2]/div/section/main/div/div[4]/div/section/div[2]/header/div/button[2]'))
        )
        random_sleep()
        stake_by_me_button.click()
    except Exception as e:
        return(f"Произошла ошибка при нажатии кнопки 'stake by me': {e}")

    try:
        print(f"Нажатие кнопки 'unstake'")
        unstake_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="root"]/div[2]/div[2]/div/section/main/div/div[4]/div/section/div[2]/div/div/div[1]/table/tbody/tr[1]/td[5]/div/button[2]'))
        )
        random_sleep()
        unstake_button.click()
    except Exception as e:
        return(f"Произошла ошибка при нажатии кнопки 'unstake': {e}")

    try:
        print(f"Нажатие кнопки '25 %'")
        percent_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div[1]'))
        )
        random_sleep()
        percent_button.click()
    except Exception as e:
        return(f"Произошла ошибка при нажатии кнопки '25 %': {e}")

    try:
        print(f"Нажатие кнопки 'unstake'")
        unstake_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/button'))
        )
        random_sleep()
        unstake_button.click()
    except Exception as e:
        return(f"Произошла ошибка при нажатии кнопки 'unstake': {e}")

    try:
        print(f"Нажатие кнопки 'confirm unstaking'")
        confirm_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div/button'))
        )
        random_sleep()
        confirm_button.click()
    except Exception as e:
        return(f"Произошла ошибка при нажатии кнопки 'confirm unstaking': {e}")

    try:
        print(f"Ждем завершения un-стейкинга (максимум 2 мин)..")
        got_it_button = WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div/button'))
        )
        random_sleep()
    except Exception as e:
        return(f"Произошла ошибка при ожидании завершения un-стейкинга: {e}")

    try:
        print(f"Нажатие кнопки 'done'")
        got_it_button.click()
    except Exception as e:
        return(f"Произошла ошибка при нажатии кнопки 'done': {e}")

    try:
        print("Задержка 10 секунд")
        time.sleep(10)
        return f'Успешно'
    except Exception as e:
        return(f"Произошла ошибка при задержке: {e}")

    # -------------------------- КОНЕЦ ЗАБОРА СО СТЕЙКИНГА  -------------------------------------------
