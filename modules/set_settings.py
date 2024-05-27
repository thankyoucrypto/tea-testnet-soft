import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
from database import save_private_key_to_db, is_private_key_account, save_address_to_db, save_refer_link_to_db
from functions import random_sleep

def set_settings(driver, login):
    try:
        if is_private_key_account(login):
            print(f'У аккаунта {login} уже есть private_key, пропускаем register_username!')
            return f'Уже есть private_key, пропускаем'
    except Exception as e:
        return f'Ошибка при проверке наличия private_key: {e}'

    try:
        print("Переходим в настройки")
        driver.get("https://app.tea.xyz/settings")
        print("Ожидание загрузки страницы настроек")
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'rc-slider')))
        random_sleep()
    except Exception as e:
        print(f"Ошибка при переходе в настройки или ожидании загрузки страницы: {e}")
        return f'Ошибка при переходе в настройки или ожидании загрузки страницы: {e}'

    try:
        print("Ожидание Copy Address")
        copy_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[1]/header[3]/div[2]/div[2]')))
        random_sleep()
        copy_button.click()
        time.sleep(1)
        copied_text = pyperclip.paste()
        print(f"Address: {copied_text}")
        save_address_to_db(login, copied_text)
    except Exception as e:
        return f'Ошибка при копировании адреса аккаунта: {e}'

    try:
        print("Ожидание реферальной ссылки")
        copy_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[3]/div[2]/span/div[1]')))
        random_sleep()
        copy_button.click()
        time.sleep(1)
        copied_text = pyperclip.paste()
        print(f"Ref link: {copied_text}")
        save_refer_link_to_db(login, copied_text)
    except Exception as e:
        return f'Ошибка при копировании реферальной ссылки: {e}'

    try:
        print("Находим slider_container")
        slider_container = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'rc-slider')))
        random_sleep()
        slider_container_width = slider_container.size['width']
        slider = slider_container.find_element(By.XPATH, './/div[@role="slider"]')
        slider_width = slider.size['width']
        actions = ActionChains(driver)
        offset_pixels = int(slider_container_width + slider_width / 2)
        print("Перемещаем ползунок")
        random_sleep()
        actions.click_and_hold(slider).move_by_offset(offset_pixels, 0).release().perform()
    except Exception as e:
        return f'Ошибка при перемещении ползунка: {e}'

    try:
        print("Ожидание результата")
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,
                                '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[2]/div[4]/div/div/button[1]/span')))
        random_sleep()
        print("Ожидание Copy to clipboard")
        copy_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[2]/div[4]/div/div/button[1]/span')))
        random_sleep()
        copy_button.click()
        time.sleep(1)
        copied_text = pyperclip.paste()
        print(f"Private key: {copied_text}")
        save_private_key_to_db (login, copied_text)
    except Exception as e:
        return f'Ошибка при копировании приватного ключа или ожидании результатов: {e}'

    try:
        print("Крутим вниз страницы")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except Exception as e:
        return(f"Произошла ошибка при прокрутке страницы вниз: {e}")

    try:
        print("Выбираем уровень знаний новичок")
        knowledge_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[5]/button/span')))
        random_sleep()
        knowledge_button.click()
    except Exception as e:
        return(f"Произошла ошибка при выборе уровня знаний: {e}")

    try:
        print("Кликаем подтвердить")
        confirm_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                     '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[5]/button/span')))
        random_sleep()
        confirm_button.click()
    except Exception as e:
        return(f"Произошла ошибка при подтверждении уровня знаний: {e}")

    try:
        print("Кликаем добавить почту")
        add_email_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[4]/button/span')))
        random_sleep()
        add_email_button.click()
    except Exception as e:
        return(f"Произошла ошибка при клике на кнопку добавления почты: {e}")

    try:
        print("Вводим почту")
        email_input = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,
                                                                                        '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[4]/div[2]/div/div/input')))
        random_sleep()
        email_input.send_keys(f'{login}')
    except Exception as e:
        return(f"Произошла ошибка при вводе почты: {e}")

    try:
        print("Кликаем сохранить")
        save_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                  '/html/body/div/div[2]/div[2]/div/section/main/div/section/div/article[4]/div[2]/button/span')))
        random_sleep()
        save_button.click()
        random_sleep()
    except Exception as e:
        return(f"Произошла ошибка при клике на кнопку сохранить: {e}")

    return 'Успешно'
