import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import random_sleep


def make_donat(driver):
    # -------------------------- ДОНАТ ВАЛИДАТОРУ  -------------------------------------------
    try:
        print(f"Переходим в стейкинг для доната")
        driver.get("https://app.tea.xyz/oss-staking")
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/div/div[2]/div[2]/div/section/main/div/div[4]/div/section/div[2]/div/div/div[1]/table/tbody/tr[1]/td[5]/div/button[2]'))
        )
        random_sleep()
    except Exception as e:
        return(f"Произошла ошибка при переходе в стейкинг для доната: {e}")

    try:
        num_validator = random.randint(1, 10)
        print(f"Кликаем на детали {num_validator} валидатора")
        path_validator = f'/html/body/div/div[2]/div[2]/div/section/main/div/div[4]/div/section/div[2]/div/div/div[1]/table/tbody/tr[{num_validator}]/td[5]/div/button[2]'
        validator_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, path_validator))
        )
        random_sleep()
        validator_button.click()
    except Exception as e:
        return(f"Произошла ошибка при клике на детали валидатора: {e}")

    try:
        print(f"Крутим вниз страницы")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        random_sleep()

        print(f"Кликаем на make donat")
        path_donat = f'/html/body/div/div[2]/div[2]/div/section/main/div/section/article/div[3]/div/div/button'
        path_donat2 = '/html/body/div/div[2]/div[2]/div/section/main/div/section/article/div[4]/div/div/button'
        xpath_queries = [path_donat, path_donat2]
        donat_button = WebDriverWait(driver, 60).until(
            lambda driver: next(
                (driver.find_element(By.XPATH, xpath) for xpath in xpath_queries if
                 driver.find_elements(By.XPATH, xpath)),
                None)
        )
        random_sleep()

        donat_button.click()
    except Exception as e:
        return(f"Произошла ошибка при клике на кнопку make donat: {e}")

    try:
        num = random.randint(5, 15)
        print(f"Кидаем донат от 5 до 15 tea: {num} TEA")
        donat_input = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/input'))
        )
        random_sleep()
        donat_input.send_keys(str(num))
    except Exception as e:
        return(f"Произошла ошибка при вводе значения доната: {e}")

    try:
        print(f"Кликаем на confirm")
        path_confirm = f'/html/body/div[2]/div/div/div/div[2]/div[3]/button[2]'
        confirm_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, path_confirm))
        )
        random_sleep()
        confirm_button.click()
    except Exception as e:
        return(f"Произошла ошибка при клике на кнопку confirm: {e}")

    try:
        print(f"Ждем завершения доната (максимум 2 мин)..")
        got_it_button = WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/button'))
        )
    except Exception as e:
        return(f"Произошла ошибка при ожидании завершения доната: {e}")

    try:
        print("Задержка 10 секунд")
        time.sleep(10)
        return f'Успешно'
    except Exception as e:
        print(f"Произошла ошибка при задержке: {e}")

    # -------------------------- КОНЕЦ ДОНАТА ВАЛИДАТОРУ  -------------------------------------------
