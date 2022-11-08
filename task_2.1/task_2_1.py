import telebot.types
from telebot import TeleBot
from emoji import emojize
import telebot_token as t_t
import re

bot = TeleBot(t_t.telebot_token())
print(f'Запущин {emojize(":grinning_face:")}')

@bot.message_handler(commands=['log'])
def log_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Телефонная книга')
    bot.send_document(chat_id=msg.from_user.id, document=open('phonebook_storege', 'rb'))


@bot.message_handler(commands=['file_down'])
def file_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Введите название фаила')
    bot.register_next_step_handler(callback=file_, message=msg)

def file_(msg: telebot.types.Message):
    bot.send_document(chat_id=msg.from_user.id, document=open(f'{msg.text}', 'rb'))

@bot.message_handler(commands=['copying_log'])
def copying_file_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Введите название фаила для переноса данных из телефонной книги')
    bot.register_next_step_handler(callback=converting_name_file, message=msg)

def converting_name_file(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=copying_file(msg.text))

def copying_file(name):
    fail_name = name
    regex = ';'
    pattern = re.compile(regex)
    file_read = open(f'{fail_name}', 'a', encoding='utf-8')
    file_phonebook = open('phonebook_storege', 'r', encoding='utf-8')
    list_f = file_phonebook.read().split()
    file_read.write('\n')
    for i in range(len(list_f) - 1):
        if pattern.search(list_f[i]):
            file_read.write(list_f[i] + '\n')
        else:
            file_read.write(list_f[i] + ' ')
    file_read.close()
    file_phonebook.close()
    return ('Копирование данных в фаил выполнено!')

@bot.message_handler(commands=['copying_file'])
def file_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Введите название фаила для переноса данных в телефонную книгу')
    bot.register_next_step_handler(callback=converting_name, message=msg)

def converting_name(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=copying_log(msg.text))

def copying_log(name):
    fail_name = name
    regex = ';'
    pattern = re.compile(regex)
    file_read = open(f'{fail_name}', 'r', encoding='utf-8')
    file_phonebook = open('phonebook_storege', 'a', encoding='utf-8')
    list_f = file_read.read().split()
    file_phonebook.write('\n')
    for i in range(len(list_f) - 1):
        if pattern.search(list_f[i]):
            file_phonebook.write(list_f[i] + '\n')
        else:
            file_phonebook.write(list_f[i] + ' ')
    file_read.close()
    file_phonebook.close()
    return ('Копирование данных с фаила выполнено!')


@bot.message_handler(content_types=['document'])
def document_command(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as f_out: f_out.write(downloaded_file)


@bot.message_handler(commands=['add_ver1'])
def add_name_v_1_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Телефонная книга')
    bot.send_message(chat_id=msg.from_user.id, text="Введите ФИО сотовый телефон коментарий через пробел")
    bot.register_next_step_handler(callback=add_items_ver_1, message=msg)

def add_items_ver_1(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=add_names_ver_1(msg.text))

def add_names_ver_1(text_):
    lst = text_.split()
    if len(lst) >= 5:
        for i in range(5, len(lst)):
            lst[4] += ' ' + lst[i]
    file_reading = open('phonebook_storege', 'a', encoding='utf-8')
    file_reading.write(f'{lst[0]} {lst[1]} {lst[2]}: {lst[3]} {lst[4]};\n')
    file_reading.close()
    return 'Данные внесен в телефонную книгу'


@bot.message_handler(commands=['add_ver2'])
def add_name_v_2_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Телефонная книга')
    bot.send_message(chat_id=msg.from_user.id, text="Введите ФИО сотовый телефон коментарий через пробел")
    bot.register_next_step_handler(callback=add_items_ver_2, message=msg)

def add_items_ver_2(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=add_names_ver_2(msg.text))

def add_names_ver_2(text_):
    lst = text_.split()
    if len(lst) >= 5:
        for i in range(5, len(lst)):
            lst[4] += ' ' + lst[i]
    file_reading = open('phonebook_storege', 'a', encoding='utf-8')
    file_reading.write(f'{lst[0]}\n{lst[1]}\n{lst[2]}:\n{lst[3]}\n{lst[4]};\n\n')
    file_reading.close()
    return 'Данные внесены в телефонную книгу'


@bot.message_handler(commands=['creating'])
def creating_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Создание нового фаила')
    bot.send_message(chat_id=msg.from_user.id, text='Введите название')
    bot.register_next_step_handler(callback=name_new_fail, message=msg)

def name_new_fail(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=creating_new_fail(msg.text))

def creating_new_fail(name):
    file_reading = open(f'{name}', 'w', encoding='utf-8')
    file_reading.close()
    return f'Создан новый фаил {name}'

@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="/log - скачать телефонную книгу\n"
                                                    "/document - загрузить документ\n"
                                                    "/creating - создать новый фаил\n"
                                                    "/add_ver1 - добавить ФИО Сот. Комен. в телфонную книгу\n"
                                                    "/add_ver2 - добавить ФИО\n"
                                                    "                    Сот.\n"
                                                    "                    Комен. в телфонную книгу\n"
                                                    "/copying_log - копирование данных с телефонной книги в фаил\n"
                                                    "/copying_file - копирование данных с фаила в телефонной книги\n"
                                                    "/file_down - скачать фаил\n"
                                                    "/help - показывает все команды\n")


bot.polling()