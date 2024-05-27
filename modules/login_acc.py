from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import config
from functions import random_sleep, change_ip

def login(driver, login, password, reserv_mail):
    max_attempts = 5  # Максимальное количество попыток открыть сайт со сменой ip
    for attempt in range(max_attempts):
        try:
            print(f"Попытка {attempt + 1}: Переходим на сайт https://app.tea.xyz/sign-up?r=coinlist...")
            driver.get("https://app.tea.xyz/sign-up?r=coinlist")

            # Разворачиваем окно браузера на весь экран
            if not config.BROWSER_VISIBLE:
                screen_width, screen_height = pyautogui.size()
                driver.set_window_size(screen_width, screen_height)
            else:
                driver.maximize_window()

            # Ожидание загрузки страницы
            WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div/section/div/figure/div[1]/section/div[1]/button[1]'))
            )
            random_sleep()
            break  # Если успешно, выходим из цикла

        except Exception as e:
            if "net::ERR_TUNNEL_CONNECTION_FAILED" in str(e):
                print(f"Ошибка при обработке аккаунта {login}: {e}")
                print(f'Меняем IP...')
                change_ip(config.CHANGE_IP_LINKS)
            else:
                print(f'Ошибка открытия сайта: {e}')
                return f'Ошибка открытия сайта: {e}'

    try:
        print("Нажимаем на почту гугл...")
        login_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div/section/div/figure/div[1]/section/div[1]/button[1]'))
        )
        random_sleep()
        login_button.click()
        print("Нажали на почту гугл")
    except Exception as e:
        return f'Ошибка при нажатии на почту гугл: {e}'

    try:
        print("Ждем новое окно")
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
        random_sleep()
        print("Переключаемся на новое окно")
        driver.switch_to.window(driver.window_handles[-1])
    except Exception as e:
        return f'Ошибка при переключении на новое окно: {e}'

    try:
        print("Вводим логин")
        login_input = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'))
        )
        random_sleep()
        login_input.send_keys(login)
    except Exception as e:
        return f'Ошибка при вводе логина: {e}'

    try:
        print("Кликаем далее")
        next_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span'))
        )
        random_sleep()
        next_button.click()
    except Exception as e:
        return f'Ошибка при нажатии кнопки далее после ввода логина: {e}'




    try:
        print("Вводим пароль")
        password_input = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'))
        )
        random_sleep()
        password_input.send_keys(password)
    except Exception as e:
        return f'Ошибка при вводе пароля: {e}'

    try:
        print("Кликаем далее")
        next_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span'))
        )
        random_sleep()
        next_button.click()
    except Exception as e:
        return f'Ошибка при нажатии кнопки далее после ввода пароля: {e}'

    try:
        print("Ожидание элемента для подтверждения")
        element = WebDriverWait(driver, 20).until(
            EC.any_of(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span')),
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/section/div/div/div/ul/li[3]/div/div[2]'))
            )
        )
        random_sleep()

        if element.tag_name == 'span':
            print("Кликаем continue")
            confirm_button = element
            confirm_button.click()
            random_sleep()
        else:
            print("Кликаем подтвердить резервную почту")
            confirm_button = element
            confirm_button.click()
            random_sleep()

            password_input = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]'))
            )
            random_sleep()

            print("Вводим резервный адрес почты")
            password_input.send_keys(reserv_mail)
            random_sleep()

            print("Кликаем далее")
            confirm_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button'))
            )
            random_sleep()
            confirm_button.click()


            print("Кликаем continue")
            confirm_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div[2]/div/div/button'))
            )
            random_sleep()
            confirm_button.click()
    except Exception as e:
        return f"Ошибка при подтверждении: {e}"

    try:
        print("Ожидание проверки блокировки аккаунта")
        WebDriverWait(driver, 20).until(
            EC.any_of(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/div')) or
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/h1')) # под вопросом
            )
        )
        return 'BAN'
    except Exception:
        print('Аккаунт не вылетел')

    try:
        print("Возвращаемся на изначальное окно")
        driver.switch_to.window(driver.window_handles[0])
        random_sleep()
    except Exception as e:
        return f'Ошибка при переключении на исходное окно: {e}'

    try:
        print("Ожидание для проверки результата")
        WebDriverWait(driver, 120).until(
            lambda d: EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/div[2]/div[2]/div/section/div[2]/article/div[4]/div/div/input'))(d) or
                      EC.visibility_of_element_located((By.XPATH,
                                                        '//div[@class="text-5xl font-semibold text-headline leading-normal font-mona "]/span'))(
                          d) or
                      EC.visibility_of_element_located((By.XPATH,
                                                        '/html/body/div/div[2]/div[2]/div/section/header/div[1]/div/span'))(
                          d) or
                      EC.visibility_of_element_located((By.XPATH,
                                                        '//div[contains(@class, "flex justify-between mt-3")]//span'))(
                          d) or
                      EC.visibility_of_element_located((By.XPATH,
                                                        '/html/body/div/div[2]/div[2]/div/section/main/div/div[1]/div/div[1]/div/figure/div'))(
                          d)
        )
        print("Логин успешно завершен")

    except Exception as e:
        return f"Ошибка завершения логина: {e}"

    return 'Успешно'

