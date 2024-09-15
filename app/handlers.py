import asyncio
import app.keyboards as kb

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    new_msg = await message.answer('Доброе утро!')
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