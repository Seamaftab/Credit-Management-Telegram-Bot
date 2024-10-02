import json
import telebot
from commands import handle_create, handle_credits, handle_demo, handle_renew, handle_admin_commands

def main():
    with open('config.json') as config_file:
        config = json.load(config_file)

    bot = telebot.TeleBot(config['telegram_bot_token'])

    @bot.message_handler(commands=['create'])
    def create_command(message):
        handle_create(message, bot)

    @bot.message_handler(commands=['credits'])
    def credits_command(message):
        handle_credits(message, bot)

    @bot.message_handler(commands=['demo'])
    def demo_command(message):
        handle_demo(message, bot)

    @bot.message_handler(commands=['renew'])
    def renew_command(message):
        handle_renew(message, bot)

    @bot.message_handler(commands=['add', 'set'])
    def admin_commands(message):
        handle_admin_commands(message, bot)

    bot.polling()

main()