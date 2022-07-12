import telebot
import telebot.types as types
from database import inserter, search_user_mail, search_user_FIO, bool_search_user_FIO
from Program import Read_and_Choice_Name_Bot, random_Number, connect_mail, read_consult_file, Zayavlenie

Name_Bot = Read_and_Choice_Name_Bot()

bot = telebot.TeleBot("Токен")
status = False
FIO = list()
mail = list()
user_data = dict()
Number = random_Number()


class User:
    def __init__(self, last_name, first_name, second_name, mail):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.user_mail = mail


@bot.message_handler(commands=['привет', 'start', 'Помощь', 'Продолжить', 'Консультация', 'Заявка'])
def Welcome(message):
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("/Помощь")
        btn2 = types.KeyboardButton('/Продолжить')
        btn3 = types.KeyboardButton('/Консультация')
        btn4 = types.KeyboardButton('/Заявка')

        keyboard.add(btn1, btn2, btn3, btn4)

        if message.text == '/start':
            bot.send_message(message.chat.id, f"Здравствуйте, меня зовут {Name_Bot} Я ваш персональный консультант "
                                              "банка 'Новый шанс'\n"
                                              "При помощи команды 'Помощь' вы можете узнать о моих возможностях\n"
                                              "При помощи команды 'Продолжить' вы сможете пройти регистрацию и продолжить общение с мной\n"
                                              "При помощи команды 'Консультация', вы сможете узнать ответы на частые вопросы пользвателей\n"
                                              "При помощи команды 'Заявка', вы сможете создать заявку на оформление кредита",
                             reply_markup=keyboard)

        elif message.text == btn1.text:
            bot.send_message(message.chat.id, "Помощь!")
            bot.send_message(message.chat.id, f"Чтобы начать диалог со мной, необходимо написать /start или /привет\n"
                                              "При помощи команды 'Помощь' вы можете узнать о моих возможностях\n"
                                              "При помощи команды 'Продолжить' вы сможете пройти регистрацию и "
                                              "продолжить общение с мной\n "
                                              "При помощи команды 'Консультация', вы сможете узнать ответы на частые "
                                              "вопросы пользвателей\n "
                                              "При помощи команды 'Заявка', вы сможете создать заявку на оформление "
                                              "кредита",reply_markup=keyboard)

            bot.send_message(message.chat.id, f"Я могу помочь вам в следующих вопросах:")

            bot.send_message(message.chat.id,
                             f"1) Вы можете ознакомиться с основными вопросами, которые я могу решить\n"
                             "2) Вы можете оформить заявку на взятие кредита \n")

            bot.send_message(message.chat.id, f"!!! Внимание!!! Если вы не являетесь пользователем нашего банка\n"
                                              "То для оформления заявки на взятие кредита необходимо\n"
                                              "пройти регистраци.\n",reply_markup=keyboard)

        elif message.text == btn2.text:
            bot.send_message(message.chat.id, "Давайте познакомимся", reply_markup=types.ReplyKeyboardRemove())

            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да")
            btn2 = types.KeyboardButton('Нет')
            keyboard.add(btn1, btn2)

            msg = bot.send_message(message.chat.id, f"Вы являетесь пользователем нашего банка?", reply_markup=keyboard)
            bot.register_next_step_handler(msg, main_dialog)

            main_dialog(message)

        elif message.text == btn3.text:
            bot.send_message(message.chat.id, "Перед вами перечь вопросов, для получения ответа введите номер вопроса")
            msg1 = bot.send_message(message.chat.id, "1) Как стать клиентом банка 'Новый шанс'?\n"
                                                     "2) Есть ли у банка свое приложение и банковская карта?\n"
                                                     "3) Как оформить кредит?\n"
                                                     "4) Почему так мало предложенных вопросов?\n"
                                                     "5) Центр консульцатий\n",
                                    reply_markup=keyboard)
            bot.register_next_step_handler(msg1, consultation)

        elif message.text == btn4.text:

            btn = types.KeyboardButton('Продолжить')
            keyboard.add(btn)

            print(message.text)
            user_id_count = bool_search_user_FIO(message.from_user.id)
            print(user_id_count)

            if user_id_count == 1:
                user_id = message.from_user.id
                user_IO = search_user_FIO(user_id)
                IO = f"{user_IO[0]} {user_IO[1]}"
                msg = bot.send_message(message.chat.id,
                                       f"Здравствуйте, {IO}. Вы выбрали пункт создать заявку на оформление кредита", reply_markup=keyboard)
                bot.register_next_step_handler(msg, Zayavka)

            else:

                msg = bot.send_message(message.chat.id,
                                       "Вас не существует в Нашей базе данных, рекомендуем зарегистрироваться")
                bot.register_next_step_handler(msg, Welcome)
    except Exception:
        bot.reply_to(message, "Что-то не понял, ошибка в Welcome")


@bot.message_handler(content_types=['text'], commands=['привет', 'start', 'Помощь', 'Продожить', 'Консультация'])
def consultation(message):
    try:

        if message.text == '1':

            answer = read_consult_file(message.text)
            print(answer)
            bot.send_message(message.chat.id, answer)

        elif message.text == '2':

            answer = read_consult_file(message.text)
            bot.send_message(message.chat.id, answer)

        elif message.text == '3':

            answer = read_consult_file(message.text)
            bot.send_message(message.chat.id, answer)

        elif message.text == '4':

            answer = read_consult_file(message.text)
            bot.send_message(message.chat.id, answer)

        elif message.text == '5':

            answer = read_consult_file(message.text)
            bot.send_message(message.chat.id, answer)

    except Exception:

        bot.reply_to(message, "Проверьте правильность ввода номера вопроса")


def main_dialog(message):
    try:

        print(message.text)

        btn1 = types.KeyboardButton("Да")
        btn2 = types.KeyboardButton('Нет')

        if message.text == btn2.text or message.text.lower() == "нет":

            msg = bot.send_message(message.chat.id, "Напишите ваше ФИО", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, process_FIO_name)


        elif message.text.lower() == btn1.text or message.text.lower() == "да":

            msg = bot.send_message(message.from_user.id,
                                   "Для авторизации на вашу почту был отправлен код. Его необходимо ввести для проверки")
            user_id = message.from_user.id
            email = search_user_mail(user_id)
            email = email[0]
            Num = random_Number()
            connect_mail(email, Num)
            bot.register_next_step_handler(msg, check_Authorization_mail, Num)

    except Exception:
        bot.reply_to(message, "Ошибка в мейн дайлог")


def process_FIO_name(message):
    try:
        print(message.text)

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        keyboard.add(btn1)
        bot.send_message(message.chat.id, f"Для выхода в начальное меню нажмите '/start'", reply_markup=keyboard)

        if message.text == btn1.text:
            msg = bot.send_message(message.chat.id, "Давайте познакомимся")
            bot.register_next_step_handler(msg, main_dialog)
        else:
            temp = message.text.split()
            FIO.append(temp[0])
            FIO.append(temp[1])
            FIO.append(temp[2])
            msg = bot.send_message(message.chat.id,
                                   "Для дальнейшей регистрации и авторизации в будущем необходим ваш email")
            bot.register_next_step_handler(msg, process_mail)
    except Exception:
        bot.reply_to(message, "Error Process_FIO")


def process_mail(message):
    try:
        print(message.text)
        temp = message.text
        temp = temp.replace(' ', '')
        if not temp:
            bot.send_message(message.chat.id, 'Вы ничего не ввели')
        else:
            mail.append(temp)

            bot.send_message(message.chat.id, "Собираю данные из введенной ифнормации")
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Да")
            btn2 = types.KeyboardButton('Нет')
            keyboard.add(btn1, btn2)

            bot.send_message(message.chat.id, f"Вас зовут {FIO[0]} {FIO[1]} {FIO[2]}, ваша почта {mail[0]}?")
            msg = bot.send_message(message.chat.id, f"Необходимо ответить Да или Нет", reply_markup=keyboard)
            bot.register_next_step_handler(msg, checker)
    except Exception:
        bot.reply_to(message, "Error process_mail")


def checker(message):
    try:
        print(message.text)

        print(f"Тут должно быть сообщение {message.text}")

        if message.text.lower() == "да":
            connect_mail(mail[0], Number)
            msg1 = bot.send_message(message.chat.id, "На вашу почту было выслано письмо с кодом, его необходимо ввести",
                                    reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg1, check_reg_mail)

        elif message.text.lower() == "нет":
            msg = bot.send_message(message.from_user.id, "Напишите ваше ФИО", reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, process_FIO_name)
    except Exception:
        bot.reply_to(message, "Я вас не понимаю")


def check_reg_mail(message):
    try:
        print(f"Проверяю мэйл {message.text} , {Number}")
        if message.text == Number:
            user_id = message.from_user.id

            user_data[user_id] = User(FIO[0], FIO[1], FIO[2], mail[0])

            print(user_data.items())
            inserter(user_id, FIO[1], FIO[2], FIO[0], mail[0])
            FIO.clear()
            mail.clear()
            user_data.clear()

            bot.send_message(message.chat.id, f"Вы успешно зарегистрированы")

            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('/Консультация')
            btn2 = types.KeyboardButton('/Заявка')
            btn3 = types.KeyboardButton('/start')
            keyboard.add(btn1, btn2, btn3)

            msg = bot.send_message(message.chat.id, "Выбирете дальнейшее действие\n"
                                                    "Консультация, созадать заявку на кредит\n"
                                                    "Или вернуться в начало", reply_markup=keyboard)
            bot.register_next_step_handler(msg, choice)
    except Exception:
        bot.reply_to(message, "Проверьте правильность введенного кода")


def check_Authorization_mail(message, num):
    try:

        if message.text == num:
            bot.send_message(message.chat.id, f"Вы авторизованы")

            user_id = message.from_user.id

            Name = search_user_FIO(user_id)

            bot.send_message(message.chat.id, f"Здравствуйте, {Name[1]} {Name[0]}")

            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Консультация')
            btn2 = types.KeyboardButton('/Заявка')
            btn3 = types.KeyboardButton('/start')
            keyboard.add(btn1, btn2, btn3)

            msg = bot.send_message(message.chat.id, "Выбирете дальнейшее действие"
                                                    "Консультация, созадать заявку на кредит", reply_markup=keyboard)
            bot.register_next_step_handler(msg, choice)
            if message.text == btn3.text:
                bot.register_next_step_handler(message.text, Welcome)
    except Exception:
        bot.reply_to(message, "Проверьте правильность введенного кода")


def choice(message):
    try:
        btn1 = types.KeyboardButton('/Консультация')
        btn2 = types.KeyboardButton('/Заявка')
        btn3 = types.KeyboardButton('/start')
        if message.text == btn1.text:
            bot.send_message(message.chat.id, "Перед вами перечь вопросов, для получения ответа введите номер вопроса")
            msg1 = bot.send_message(message.chat.id, "1) Как стать клиентом банка 'Новый шанс'?\n"
                                                     "2) Есть ли у банка свое приложение и банковская карта?\n"
                                                     "3) Как оформить кредит?\n"
                                                     "4) Почему так мало предложенных вопросов?\n"
                                                     "5) Центр консульцатий\n")
            bot.register_next_step_handler(msg1, consultation)

        elif message.text == btn2.text:

            user_id = bool_search_user_FIO(message.from_user.id)

            if user_id == 1:

                user_IO = search_user_FIO(message.from_user.id)
                IO = f"{user_IO[0]} {user_IO[1]}"

                msg = bot.send_message(message.chat.id,
                                       f"Здравствуйте, {IO}. Вы выбрали пункт создать заявку на оформление кредита")

                USER_FIO = search_user_FIO(message.from_user.id)

                email = search_user_mail(message.from_user.id)
                email = email[0]

                Zayavlenie(USER_FIO, message.from_user.id, email)

                bot.register_next_step_handler(msg, Zayavka)
            else:
                msg = bot.send_message(message.chat.id,
                                       "Вас не существует в Нашей базе данных, рекомендуем зарегистрироваться")
                bot.register_next_step_handler(msg, Welcome)

        elif message.text == btn3.text:
            bot.register_next_step_handler(message.text, Welcome)
    except Exception:
        bot.reply_to(message, "Error checker")


def Zayavka(message):
    try:
        user_id = message.from_user.id
        print(user_id)
        User_FIO = search_user_FIO(user_id)
        print(User_FIO)
        email = search_user_mail(user_id)
        email = email[0]
        print(email)
        Zayavlenie(User_FIO, user_id, email)
        bot.send_message(message.chat.id, "Ваша заявка создана на рассмотрение")
        bot.send_message(message.chat.id, "Ожидайте письма для связи с вашим юристом")
        bot.register_next_step_handler(message.text, Welcome)
    except Exception:
        bot.reply_to(message, "Вернемся к истокам")


if __name__ == '__main__':
    bot.polling()
