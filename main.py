from config.logging import setup_logging
setup_logging()

from bot import ModularBot


if __name__=="__main__":
    bot = ModularBot()
    bot.run()
