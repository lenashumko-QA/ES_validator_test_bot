# подключение библиотеки telebot
# В google colab добавить: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строку
# 'PyTelegramBotApi'
from telebot import TeleBot, types
import json

bot = TeleBot(token='5864038727:AAFH4aacwL9oGPmVYPa0QlnaPjbK6IPu-T4', parse_mode='html') # создание бота


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    sti=open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Приветствую тебя, мой юный падаван, на светлой стороне силы! JSON умею проверять я и форматировать в текст его красивый...\nВведи JSON в виде строки:', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    try:
        # пытаемся распарсить JSON из текста сообщения
        payload = json.loads(message.text)
    except json.JSONDecodeError as ex:
        # при ошибке взникнет исключение 'json.JSONDecodeError'
        # преобразовываем исключение в строку и выводим пользователю
        sti=open('err.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(
            chat_id=message.chat.id,
            text=f'Мой юный падаван! Ошибка при обработке произошла. Её исправь скорее:\n<code>{str(ex)}</code>'
        )
        # выходим из функции
        return
    
    # если исключения не возникло - значит был введен корректный JSON
    # форматируем его в красивый текст :) (отступ 2 пробела на уровень, сортировать ключи по алфавиту)
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    # и выводим пользователю
    sti=open('win.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Всегда делись тем, чему ты научился! JSON:\n<code>{text}</code>'
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()