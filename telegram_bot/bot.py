import os

from aiogram import Bot, Dispatcher
import asyncio


bot_obj = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher()


async def main():
    await dp.start_polling(bot_obj)


if __name__ == "__main__":
    asyncio.run(main())
