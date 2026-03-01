from quopri import EMPTYSTRING

from aiogram.exceptions import TelegramBadRequest
from discord_webhook import DiscordWebhook, DiscordEmbed
from aiogram import Bot, Dispatcher, types, Router
import asyncio
from datetime import datetime
from os import remove
from time import sleep

file = open("hook_key.txt", "r")  # Reading the urls for discord-webhook
keys = file.readlines()
key1 = keys[0].replace("\n","")
key2 = keys[1].replace("\n","")
file.close()

file = open("bot_token.txt", "r")  # Reading the token for telegram-bot
token_bot = file.read()
file.close()

bot = Bot(token=token_bot)
dp = Dispatcher()
rt = Router()
dp.include_router(rt)


async def main(): # initialize telegram bot
    await dp.start_polling(bot)


#     --- Create function for main webhook ---
def hook_message(content: str, usr: str, url: str):  # function for create webhook message
    webhook = DiscordWebhook(url=key1, content=content, username=usr, avatar_url=url)
    return webhook.execute()
#     ----------------------------------------


#     --- Create function for file sender ---
def file_sender(file_name: str): # function for send user avatar image
    sender = DiscordWebhook(url=key2)
    with open(file_name, "rb") as f:
        sender.add_file(file=f.read(), filename=file_name)
    response = sender.execute()

    attachments = response.json().get("attachments", [])
    if attachments:
        return attachments[0]["url"]
    return None
#     ---------------------------------------


@rt.message()
async def echo(message: types.Message):
    await message.answer("Please wait a bit")

    #     --- Get user avatar file id ---
    try:
        user_avatar_data = await bot.get_user_profile_photos(message.from_user.id)
        user_avatar_data = str(user_avatar_data)
        user_avatar_id = user_avatar_data.find("file_id='")
        file_id = user_avatar_data[user_avatar_id + 9:user_avatar_id + 88]
    #    --------------------------------


    #    --- Main telegram bot ---
        user_avatar = await message.bot.get_file(file_id) # download user avatar image
        file_path = user_avatar.file_path
        print(user_avatar_data)
        username = message.from_user.username
        nickname = str(username) + ".png" # create file name @Yomayes -> "Yomayes.png"
        await message.bot.download_file(file_path, nickname)
        response = file_sender(nickname)  # initialize the file sender
        url = file_sender(nickname)  # get the avatar url
    except TelegramBadRequest    as e:
        print(f"ОШИБКА: {e}")
        url = ""
    print(url)
    try:
        name = message.from_user.full_name
        content = message.text
        response = hook_message(content,name,url)
        if response == 'Webhook status code 400: {"message": "Cannot send an empty message", "code": 50006}':
            await message.answer(f"Message has been sent to Discord! \n"
                                 f"Sending time: [{datetime.now().strftime('%H:%M')}]")
        else:
            await message.answer(f"Message was not sent to Discord :( \n"
                                 f"Sending time: [{datetime.now().strftime('%H:%M')}]")
    except Exception as e:
        await message.answer(f"Message was not sent to Discord :( \n"
                             f"Sending time: [{datetime.now().strftime('%H:%M')}]")
    sleep(1)
    try:
        remove(nickname) # remove user avatar
    except UnboundLocalError or FileNotFoundError:
        print('Nickname does not exist')
#    ----------------------------



if __name__ == "__main__": # initialize telegram bot
    asyncio.run(main())