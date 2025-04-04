import asyncio
import app.keyboards as kb
import datetime

from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    now = datetime.datetime.now().hour
    
    if now >= 6 and now < 12:
        new_msg = await message.answer('Доброе утро! 🌅')
    elif now >= 12 and now < 17:
        new_msg = await message.answer('Добрый день! 🕛')
    elif now >= 17 and now < 21:
        new_msg = await message.answer('Добрый вечер! 🌇')
    else:
        new_msg = await message.answer('Доброй ночи! 🌃')

    await message.delete()
    await asyncio.sleep(20)
    try:
        await new_msg.delete()
    except Exception as e:
        pass
    
@router.message(Command('sites'))
async def handle_sites(message: Message):
    new_msg = await message.answer('Это вот, крутые сайты крутых людей!', reply_markup=kb.sites)
    await message.delete()
    await asyncio.sleep(20)
    try:
        await new_msg.delete()
    except Exception as e:
        pass
    
@router.message(Command('prefix'))
async def handle_prefix(message: Message, command: CommandObject):
    args = command.args
    await message.delete()
    await message.chat.set_administrator_custom_title(user_id=6690746307, custom_title='Hello')
    
@router.message(Command('test'))
async def handle_test(message: Message, bot: Bot):
    await bot.promote_chat_member(chat_id=message.chat.id, user_id=6690746307)
    await message.delete()