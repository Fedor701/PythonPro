@bot.message_handler(commands=['start'])
def send_start(message):
    welcome_text = (
                    "/start - Список всех команд\n"
                    "/hello - Приветствие\n"
                    "/password - Генерация пароля\n"
                    "/bye - Прощание\n"              
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['password'])
def send_password(message):
    password = gen_pass(10)
    bot.reply_to(message, f'Ваш сгенерированный пароль: {password}') 

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    username = message.from_user.username if message.from_user.username else "Неизвестный пользователь"
    user_message = message.text
    print(f"Получено сообщение от {username}: {user_message}")
   

print('Bot started')
bot.polling()
