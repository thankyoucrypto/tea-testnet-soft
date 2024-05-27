import random
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import config
import database
import functions
from urllib.parse import urlparse
from modules import claim_points, get_statistic, login_acc, make_donat, register_username, set_settings, staking_min, staking_max, staking_borrow
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver


# ЗАПУСК ОСНОВНОГО МАРШРУТА
def main():
    # 1. Считываем mails.txt (login:pass)
    with open('mails.txt', 'r') as file:
        mails = file.readlines()

    # 2. Создаем БД если ее нет
    database.create_database()

    logins = []

    # 3. Записываем в БД новые аккаунты
    for mail in mails:
        login, password, reserv_mail = mail.strip().split(':')
        database.save_email_to_db(login, password, reserv_mail)
        logins.append(login)

    # 4. Берем из БД аккаунты
    if (config.FETCH_ALL_ACCOUNTS):
        accounts = database.get_all_accounts()
        print(f'FETCH_ALL_ACCOUNTS = {config.FETCH_ALL_ACCOUNTS}, запускаем все аккаунты из БД')
    else:
        accounts = database.get_accounts_from_file(logins)
        print(f'FETCH_ALL_ACCOUNTS = {config.FETCH_ALL_ACCOUNTS}, запускаем только аккаунты из mails.txt')

    print(f'[{len(accounts)}] Accounts запущено: {accounts}')

    # Перемешиваем аккаунты если shuffle = True
    if config.SHUFFLE_ACCOUNTS:
        random.shuffle(accounts)

    # Для каждого аккаунта из БД
    for login, password, reserv_mail in accounts:

        print(f'Запускаем аакаунт {login}')

        # Проверяем не в бане ли почта и нужно ли восстанавливать
        if (database.is_account_in_ban_db(login)) and (config.TRY_TO_RECOVER_BAN == False):
            print(f'Аккаунт {login} в бане в БД, пропускаем')
            if (config.TELEGRAM_NOTIFICATIONS):
                functions.send_telegram_message(config.BOT_TOKEN, config.CHAT_ID,
                                            f'❌ Аккаунт {login} в бане в БД, пропускаем')
            continue



        # 5. Меняем ip у мобильной прокси, создаем fake_useragent
        print(f'Меняем IP..')
        if not functions.change_ip(config.CHANGE_IP_LINKS):
            print(f"Не удалось сменить IP для {login}")

        # Форматирование прокси
        proxy_parts = urlparse(config.MOBILE_PROXY)
        proxy_host = proxy_parts.hostname
        proxy_port = proxy_parts.port
        proxy_username = proxy_parts.username
        proxy_password = proxy_parts.password

        # Настройка Chrome с использованием прокси и рандомного юзерагента
        options = Options()
        user_agent = database.get_user_agent_db(login)
        options.add_argument(f"user-agent={user_agent}")

        # Отключаем webrdiver-mode:
        options.add_argument('--disable-blink-features=AutomationControlled')

        if (config.BROWSER_VISIBLE == False):

            # Настройки для headless режима
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")  # Необязательно, помогает избежать некоторых проблем с рендерингом в Windows

            # Эти опции могут быть полезны в контейнеризированных или ограниченных окружениях
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        # Прокси с авторизацией и без привязки к своему ip
        proxy_options = {
            'proxy': {
                # протокол:
                'http': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}',
                'https': f'https://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}',
            }
        }
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=options,
                                  seleniumwire_options=proxy_options
                                  )

        progon_info = ''

        # После общих настроек приступаем к прогону
        try:



            if (config.LOGIN):
                is_ban = login_acc.login(driver, login, password, reserv_mail)
                progon_info += f'LOGIN: {is_ban}\n'

                if (is_ban == 'BAN'):
                    print(f'Аккаунт {login} в бане, пропускаем')
                    if (config.TELEGRAM_NOTIFICATIONS):
                        functions.send_telegram_message(config.BOT_TOKEN, config.CHAT_ID,
                                                    f'❌ Аккаунт {login} в бане, пропускаем')
                    database.save_status_to_db (login, 'BAN')
                    continue

                if (is_ban != 'Успешно'):
                    print('Логин не прошел успешно, пропускаем аккаунт')
                    continue

                else:
                    print(f'Аккаунт {login} не бане, продолжаем')
                    database.save_status_to_db(login, 'VALID')

            if (config.REGISTER_USERNAME):
                is_register = register_username.register_username(driver, login)
                progon_info += f'REGISTER_USERNAME: {is_register}\n'

            if (config.SET_SETTINGS):
                is_settings = set_settings.set_settings (driver, login)
                progon_info += f'SET_SETTINGS: {is_settings}\n'

            if (config.STAKING_MIN):
                is_staking_min = staking_min.staking_min (driver)
                progon_info += f'STAKING_MIN: {is_staking_min}\n'

            if (config.MAKE_DONAT):
                is_donat = make_donat.make_donat (driver)
                progon_info += f'MAKE_DONAT: {is_donat}\n'

            if (config.STAKING_MAX):
                is_staking_max = staking_max.staking_max (driver)
                progon_info += f'STAKING_MAX: {is_staking_max}\n'

            if (config.STAKING_BORROW):
                is_staking_borrow = staking_borrow.staking_borrow (driver)
                progon_info += f'STAKING_BORROW: {is_staking_borrow}\n'

            if (config.CLAIM_POINTS):
                is_claim_points = claim_points.claim_points (driver, login)
                progon_info += f'CLAIM_POINTS: {is_claim_points}\n'

            if (config.GET_STATISTIC):
                is_get_statistic = get_statistic.get_statistic (driver, login)
                progon_info += f'GET_STATISTIC: {is_get_statistic}\n'

            print(f"Успешная обработка аккаунта: {login}\n{progon_info}")

            if (config.TELEGRAM_NOTIFICATIONS):
                message = database.get_account_info_from_db(login)
                functions.send_telegram_message(config.BOT_TOKEN, config.CHAT_ID, f'✅ Успешная отработка аккаунта\n\n{message}\n\n{progon_info}')

        except Exception as e:
            print(f"Ошибка при обработке аккаунта {login}: {e}")
            if (config.TELEGRAM_NOTIFICATIONS):
                functions.send_telegram_message(config.BOT_TOKEN, config.CHAT_ID,
                                            f'❌ Ошибка при обработке аккаунта {login}: {e}\n\n{progon_info}')

        finally:
            driver.quit()


if __name__ == "__main__":
    main()
