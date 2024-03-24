




import asyncio


from aiogram import Router, F,types
from aiogram.filters import CommandStart

user = Router(name=__name__)




@user.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer(f'Привет <u>{message.from_user.username}</u>!\n'
                                                ,parse_mode='html')

@user.message(F.text.as_('mes'))
async def repeat(message:types.Message,mes:str):
    await message.answer(mes)
