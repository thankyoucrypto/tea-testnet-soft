from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from database import save_statistic_to_db
from functions import random_sleep
from selenium.common.exceptions import TimeoutException


def get_statistic(driver, login):
    # -------------------------- ПОЛУЧИТЬ СТАТИСТИКУ АККАУНТА  -------------------------------------------

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            print("Переходим на сайт https://app.tea.xyz/.. для получения статистики")
            driver.get("https://app.tea.xyz/")
            WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[1]/div/div[1]/div/figure/div'))
            )
            random_sleep()
            break  # Если успешно загрузили элемент, выходим из цикла
        except TimeoutException:
            attempts += 1
            if attempts < max_attempts:
                print("Не удалось найти элемент. Перезагрузка страницы...")
                driver.refresh()
            else:
                return "Сайт не открывается. Достигнуто максимальное количество попыток перезагрузки."
        except Exception as e:
            return f"Ошибка при переходе на сайт для получения статистики: {e}"

    try:
        print("Кликаем обновить данные")
        refresh_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[1]/div/div[1]/div/figure/div'))
        )
        refresh_button.click()
        random_sleep()
    except Exception as e:
        return(f"Ошибка при клике на кнопку обновления данных: {e}")

    try:
        print("Получаем значения Init и Rewards")
        elements = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.XPATH,
                                                 "//*[contains(@class, 'text-3xl') and contains(@class, 'font-semibold') and contains(@class, 'font-mona') and contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'gap-2') and contains(@class, 'overflow-hidden')]"))
        )
        random_sleep()

        if len(elements) < 3:
            print("Найдено недостаточно элементов с поинтами на экране!")
            for element in elements:
                print(f'Значение: {element.text}')
            balance = '?'
            staking = '?'
            rewards = '?'
        else:
            balance = elements[0].find_element(By.TAG_NAME, "span").text
            staking = elements[1].find_element(By.TAG_NAME, "span").text
            rewards = elements[2].find_element(By.TAG_NAME, "span").text
            print(f"Balance: {balance}")
            print(f"Staking: {staking}")
            print(f"Rewards: {rewards}")
        random_sleep()
    except Exception as e:
        return(f"Ошибка при получении значений Init и Rewards: {e}")

    try:
        print(f'Получаем количество Points')
        points = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[@class="text-5xl font-semibold text-headline leading-normal font-mona "]/span'))
        ).text
        random_sleep()

        print(f"Total Earned Points: {points}")
        save_statistic_to_db(login, balance, staking, rewards, points)
    except Exception as e:
        return(f"Ошибка при получении количества Points: {e}")

    try:
        refresh_button = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/main/div/div[1]/div/div[1]/div/figure/div'))
        )
        print("Получение статистики успешно завершено")
        return f'Успешно'
    except Exception as e:
        return (f"Ошибка завершения статистики: {e}")

    # -------------------------- КОНЕЦ СТАТИСТИКИ АККАУНТА  -------------------------------------------
