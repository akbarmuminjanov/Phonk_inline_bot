from aiogram import types
from data.config import ADMINS
from loader import bot, dp
from utils.manage_db import add_music

@dp.channel_post_handler(content_types="audio")
async def get_music(message: types.Message):
    await add_music(dict(message.audio))
    await bot.send_message(chat_id=ADMINS[0], text=f"""Musiqa qo'shildi""")