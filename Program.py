import random as rn
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version


def Read_and_Choice_Name_Bot():
    bot_name = list()
    with open("Bot_Name.txt", 'r', encoding='utf-8') as file:
        for line in file:
            bot_name.append(line)
        file.close()
    rand_name_bot = rn.choice(bot_name)
    return rand_name_bot


def Zayavlenie(USER_FIO, user_id, email):
    temp1 = f"ПАО 'Новый шанс'\n Адресс банка \n ФИО заявителя: {USER_FIO[2]} {USER_FIO[0]} {USER_FIO[1]}\n Адресс проживания:__________________\n"
    temp2 = "Заявление на предоставление потребительского кредита\n"
    temp3 = f"Прошу предоставить мне _________________________________________________\n кредит в размере _______________ \nна срок с '__'_______ 20__ года по '__'________ 20__\n"
    temp4 = "Под ставку __________________ процентов годовых. \nИсточником погашения является __________________________\n"
    temp5 = "ФИО _______________________ подпись ___________________ дата _______________\n"
    temp6 = f"Почта заявителя {email}"

    with open(f"{user_id}.txt", 'w', encoding="utf8") as file:
        file.write(temp1)
        file.write(temp2)
        file.write(temp3)
        file.write(temp4)
        file.write(temp5)
        file.write(temp6)
        file.close()


def read_consult_file(number):
    with open(f"{number}.txt", 'r', encoding='utf-8') as file:
        temp = file.read()
        file.close()
    return temp


def random_Number():
    random_num = ""
    for i in range(6):
        temp = str(rn.randint(0, 9))
        random_num += temp

    return random_num


def connect_mail(mail, Number):
    server = 'smtp.mail.ru'
    user = 'telegramm.bot@mail.ru'
    password = 'RaDist12+'
    recipients = [mail]
    print(recipients)
    sender = user
    subject = 'Проверочный код'
    html = f'<html><head></head><body><h1>{Number}<h1></body>></html>'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f'PythonScript <{sender}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(Number, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()
