# MovieBot
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-green.svg)](https://t.me/IMDB_movie_fy_bot/)

Чат-бот на базе Telegram, который использует OMDB-API для получения информации о запрошенном фильме или сериале и отправляет ее обратно пользователю в окне чата Telegram, а также подскажет, какой сериал или фильм посмотреть.


## Технологии

Создан с использованием библиотек pyTelegramBotAPI и IMDbPY.

## Как начать

Необходимо скопировать репозиторий на свой локальный компьютер. Для этого перейти в каталог (например, рабочий стол)

```
cd desktop
```

и выполнить команду

```
git clone https://github.com/rufreedomman/telegram_movie_bot
```

Открыть проект в IDE. Создать виртуальное окружение

```
python3 -m venv venv
source venv/bin/activate
```

Установить или скопировать необходимые пакеты, указанные в файле requirements.txt. 

```
pip install pyTelegramBotAPI
pip install IMDbPY
pip install requests
pip install python-dotenv

или

pip install -r requirements.txt
```

Необходимо использовать Ваш токен Telegram бота, сконфигурированный @BotFather и API, полученный на https://www.omdbapi.com/

MovieBot размещен на [Heroku](https://signup.heroku.com/?c=7013A000000ib1xQAA&gclid=Cj0KCQjw4s7qBRCzARIsAImcAxYsAykyEAEp-XvXf4296_Fwvs1rHwDQV_CmB5MD8p6RZ52xdYQNV6gaAmKgEALw_wcB).

## Начало работы с Telegram ботами

Чат-боты Telegram — это небольшие скрипты, которые могут взаимодействовать с API, чтобы получать сообщения от пользователя и отправлять информацию в разные чаты и каналы.

[Документация по pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI#types)
