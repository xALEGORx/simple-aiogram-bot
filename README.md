# Simple Aiogram Bot 🤖
Simple framework for writing a good bot using the **aiogram** and **sqlite** library

## Installation ✍️
1. Clone the repository in your folder `git clone https://github.com/xALEGORx/simple-aiogram-bot.git`
2. Rename `settings.ini.example` to `settings.ini`
3. Set your bot token in the `token` field in `settings.ini`
4. Install need libraries `pip3 install -r requirements.txt`
5. Run bot with `python3 app.py`

## Bot structure 📁
Folder  | Description
------------- | -------------
data  | Configuration files, logs, database
handlers  | Handlers of errors, commands, callbacks
middlewares  | Middlewares for check exists user, antispam
services  | Custom libraries
utils  | Functions that run multiple times
