<div align="center">

# Telegram -> Discord

### _Forward messages from Telegram directly to Discord_
### _Пересылай сообщения из Telegram прямо в Discord_

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![aiogram](https://img.shields.io/badge/aiogram-3.25.0-blue?style=for-the-badge)
![discord-webhook](https://img.shields.io/badge/discord--webhook-1.4.1-7289DA?style=for-the-badge&logo=discord)

</div>

---

## 🌐 Language / Язык

- ᴇɴɢ [English](#-english)
- ʀᴜ [Русский](#-русский)

---

<br>

# ᴇɴɢ English

## 📖 About

This bot listens for messages in **Telegram** and forwards them to **Discord** via webhooks. The sender's profile picture gets automatically downloaded and used as the message avatar in Discord.

---

## ⚙️ How It Works

```
User sends a message in Telegram
        ↓
Bot downloads the user's profile picture
        ↓
Avatar is uploaded to a private Discord channel (webhook 2)
        ↓
Bot retrieves the direct image URL
        ↓
Message + username + avatar are posted to the public Discord channel (webhook 1)
        ↓
Temporary avatar file gets deleted
```

---

## 🔗 Two Webhooks — Why?

| Webhook       | Purpose | Where to add |
|---------------|---------|--------------|
| `key1`(first) | **Message posting** — all forwarded Telegram messages land here | Public Discord channel |
| `key2`(second) | **Avatar storage** — acts as an image host for profile pictures | Private Discord channel (no members) |

> 💡 **Why two?** Discord doesn't let you pass an image directly as a webhook avatar. So the second webhook is used as a temporary file storage — the picture gets uploaded there, and the resulting URL is then used by the first webhook.

---

## 🛠 Setup

### 1. Clone the repository

```bash
git clone https://github.com/Yomayez/Telegram-to-Discord.git
cd Telegram-to-Discord
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Open `bot_token.txt` and paste your bot token

#### Example:
```
1234567890:ABCdefGhIJKlmNoPQRsTUVwxYZ
```

> You can grab your token from [@BotFather](https://t.me/BotFather) on Telegram.

### 4. Open `hook_key.txt` and paste your 2 webhook URLs

#### Examples:
```
https://discord.com/api/webhooks/XXXXXXXXXX/YYYYYYY   <- first webhook (message posting)
https://discord.com/api/webhooks/XXXXXXXXXX/ZZZZZZZ   <- second webhook (avatar storage)
```

> ⚠️ Each webhook goes on its **own line**. The second webhook should be in a **private channel** with no members.

### 5. Run the bot

```bash
python main.py
```

---

## 📁 Project Structure

```
📦 project/
 ┣ 📄 main.py           — main bot code
 ┣ 📄 bot_token.txt     — Telegram bot token
 ┗ 📄 hook_key.txt      — Discord webhook URLs
```

---

## 🔍 Code Breakdown

### `hook_message(content, usr, url)`
Sends a text message to Discord via the first webhook.  
Parameters: message content, username, avatar URL.

### `file_sender(file_name)`
Uploads a file (avatar) via the second webhook and returns the direct image URL.

---

## ⚠️ Things to Know

- If the user **has no profile picture**, the bot will keep on running — it'll just send the message without an avatar icon.
- Sending **GIFs or Stickers** will throw an error back to the user in chat, since those aren't supported.
- `sleep(1)` is there to make sure the file has time to be released before it gets deleted.

---

<br>

# 🇷🇺 Русский

## 📖 Описание

Этот бот получает сообщения пользователей в **Telegram** и пересылает их в **Discord** через вебхуки. Аватарка отправителя автоматически скачивается и используется как иконка сообщения в Discord.

---

## ⚙️ Как это работает

```
Пользователь пишет в Telegram
        ↓
Бот скачивает аватарку пользователя
        ↓
Аватарка отправляется в закрытый Discord-канал (webhook 2)
        ↓
Бот получает прямую ссылку на аватарку
        ↓
Сообщение + имя + аватарка отправляются в общий Discord-канал (webhook 1)
        ↓
Временный файл аватарки удаляется
```

---

## 🔗 Два вебхука — зачем?

| Вебхук | Назначение | Куда добавлять |
|--------|-----------|----------------|
| `key1` (первый) | **Постинг сообщений** — сюда летят все пересланные сообщения из Telegram | Общий Discord-канал |
| `key2` (второй) | **Хранение аватарок** — используется как хостинг для изображений профилей | Закрытый Discord-канал (без участников) |

> 💡 **Почему два?** Discord не позволяет напрямую передать изображение как аватар вебхука. Поэтому второй вебхук используется как временное файловое хранилище — картинка загружается туда, а затем ссылка на неё используется в первом вебхуке.

---

## 🛠 Установка

### 1. Клонируй репозиторий

```bash
git clone https://github.com/Yomayez/Telegram-to-Discord.git
cd Telegram-to-Discord
```

### 2. Установи зависимости

```bash
pip install -r requirements.txt
```

### 3. Открой файл `bot_token.txt` и вставь туда токен бота

#### пример:
```
1234567890:ABCdefGhIJKlmNoPQRsTUVwxYZ
```

> Токен получить можно у [@BotFather](https://t.me/BotFather) в Telegram.

### 4. Открой файл `hook_key.txt` и вставь туда 2 ссылки вебхуков

#### примеры:
```
https://discord.com/api/webhooks/XXXXXXXXXX/YYYYYYY   <- первый вебхук (постинг сообщений)
https://discord.com/api/webhooks/XXXXXXXXXX/ZZZZZZZ   <- второй вебхук (хранение аватарок)
```

> ⚠️ Каждый вебхук — на **отдельной строке**. Второй вебхук должен быть в **закрытом канале** без участников.

### 5. Запусти бота

```bash
python main.py
```

---

## 📁 Структура проекта

```
📦 project/
 ┣ 📄 main.py           — основной код бота
 ┣ 📄 bot_token.txt     — токен Telegram-бота
 ┗ 📄 hook_key.txt      — ссылки на Discord-вебхуки
```

---

## 🔍 Разбор кода

### `hook_message(content, usr, url)` 
Отправляет текстовое сообщение в Discord через первый вебхук.  
Параметры: текст сообщения, имя пользователя, ссылка на аватарку.

### `file_sender(file_name)`
Загружает файл (аватарку) через второй вебхук и возвращает прямую ссылку на изображение.

---

## ⚠️ Особенности

- Если у пользователя **нет аватарки**, бот продолжит работу — просто отправит сообщение без иконки.
- При попытке отправки GIF / Стикеров бот выдаст ошибку собеседнику в чат, т.к нельзя отправлять GIF / Стикеры.
- `sleep(1)` добавлен для того, чтобы файл успел "освободиться" перед удалением.
