import asyncio
import app.keyboards as kb
import datetime

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    now = datetime.datetime.now().hour
    
    if now >= 6 and now < 12:
        new_msg = await message.answer('Доброе утро!', reply_markup=kb.start)
    elif now >= 12 and now < 17:
        new_msg = await message.answer('Добрый день!', reply_markup=kb.start)
    elif now >= 17 and now < 21:
        new_msg = await message.answer('Добрый вечер!', reply_markup=kb.start)
    else:
        new_msg = await message.answer('Доброй ночи!', reply_markup=kb.start)
        
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