from asyncio import run as async_run

from src import bot, dispatcher


async def main() -> None:
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    async_run(main())
