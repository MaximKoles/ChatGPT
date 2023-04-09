# ChatGPT: Telegram-бот на базе OpenAI GPT-3.5-turbo
ChatGPT - это бот для Telegram, который использует языковую модель OpenAI GPT-3.5 для генерации человекоподобных ответов на сообщения пользователей. Бот может быть использован для непринужденных бесед, мозгового штурма идей или даже в образовательных целях.

# Bot
The bot online (GPT3.5)
<h3 align="left">Telegram:</h3> <a href="https://t.me/ChatGPTtesting_robot"><img src="https://img.shields.io/website?color=9400d3&down_message=Tr3ble_AI&label=Telegram&logo=telegram&style=for-the-badge&up_message=ChatGPTtesting_robot&url=https%3A%2F%2Ft.me%2https://t.me/ChatGPTtesting_robot"></a>

# Installation
Чтобы использовать бота ChatGPT, вам необходимо иметь учетную запись Telegram и ключ API OpenAI. API-ключ можно получить, подписавшись на программу OpenAI GPT-3.5.

Получив API-ключ, вы можете загрузить исходный код бота и установить необходимые зависимости с помощью следующих команд:
```sh
git clone https://github.com/MaximKoles/ChatGPT.git

cd ChatGPT

pip install -r requirements.txt
```
# Configuration
Перед запуском бота вам нужно будет обновить переменные bot_token и api_key в файле main.py собственным токеном бота Telegram и ключом API OpenAI соответственно.

# Usage
Чтобы запустить бота ChatGPT, выполните следующую команду:
```sh
python main.py
```
Когда бот запущен, вы можете взаимодействовать с ним, отправляя сообщения на его аккаунт в Telegram. Бот будет отвечать на ваши сообщения человекоподобными ответами, генерируемыми моделью GPT-3.5.

В настоящее время бот поддерживает следующие команды:

/start: Инициализирует бота и начинает новую тему разговора.

/newtopic: Начинает новую тему разговора в текущей теме разговора.

/image: Генерировать изображение с поддержкой DALL-E

# Interface 
![image](https://user-images.githubusercontent.com/69369034/225102009-ede09ac4-1c1e-4ac5-9cef-e3da6bfcf2d9.png)![image](https://user-images.githubusercontent.com/69369034/229245783-e8c48a79-a294-4f62-af28-69474842a270.png)


# Contributing
Если вы хотите внести свой вклад в проект ChatGPT, пожалуйста, отправьте запрос на исправление с предлагаемыми изменениями. Мы приветствуем любой вклад, включая исправления ошибок, новые возможности и улучшение документации.

# License
Проект ChatGPT лицензируется по лицензии MIT License. Для получения дополнительной информации смотрите файл LICENSE.
