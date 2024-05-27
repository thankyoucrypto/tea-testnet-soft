
# ----------------------- CONFIG PARAMETERS --------------------------

MOBILE_PROXY = 'http://login:pass@ip:port' # Мобильная прокси http в формате http://login:pass@ip:port

CHANGE_IP_LINKS = [
    'link1',
    'link2',
    'link3'
]

DELAY = [3, 15]              # Задержка между действиями на сайтах [от, до]

LOGIN = True                # Выполнение вход в аккаунты (всегда выполняем!)
REGISTER_USERNAME = True    # Регистрация username для аккаунтов где нет username в БД
SET_SETTINGS = True         # Установка настроек в аккаунте (уровень новичок, вписать почту для уведомлений, скопировать приватник и рефералку)
STAKING_MIN = True          # Закинуть в тейкинг рандомному валидатору от 20% до 40% от депозита
MAKE_DONAT = True           # Отправить донат от 5 до 15 tea рандомному валидатору
STAKING_MAX = True          # Закинуть в тейкинг рандомному валидатору от 70% до 90% от депозита
STAKING_BORROW = False      # Забрать из стейкинга 25% от суммы стейка (доступно после 5 дней после заноса!)
CLAIM_POINTS = False         # Клеймить поинты за стейкинг если есть доступные
GET_STATISTIC = True        # Получить статистику аккаунта (balance, staking, rewards, points)

SHUFFLE_ACCOUNTS = True     # Перемешивать аккаунты между собой
FETCH_ALL_ACCOUNTS = False  # Запускать все аккаунты из БД - (True), или только те, которые указаны в файле mails.txt - (False)

TRY_TO_RECOVER_BAN = True   # Пробовать восстановить аккаунты из бана (в которые не удалось войти по почте). То есть пробовать заново входить. Рекомендуется спустя пару часов/дней пробовать.

BROWSER_VISIBLE = True      # Отображать окно браузера или работать в фоновом режиме (модуль set_settings работает только с True)

TELEGRAM_NOTIFICATIONS = True                                   # Присылать уведомления в телеграм или нет
BOT_TOKEN = ''    # Token tg-бота
CHAT_ID = ''                                      # id чата для отстуков (добавьте бота администратором)

# ----------------------------------------------------------------------
