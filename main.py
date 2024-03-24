import sys
import logging
import asyncio
import os
from aiogram import Bot,Dispatcher,Router


from client import user
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())



ALLOWED_UPDATES=['message','edited_message','callback_query']

bot = Bot (token=str(os.getenv('TOKEN')))
dp = Dispatcher ()


dp.include_router(user)


async def on_startup(bot):
    print ('bot is carring out')

async def on_shutdown(bot):
    print('бот лег')



async def main():
    dp.startup.register (on_startup)
    dp.shutdown.register (on_shutdown)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot,allowed_updates=ALLOWED_UPDATES)

if __name__=='__main__':
    asyncio.run(main())