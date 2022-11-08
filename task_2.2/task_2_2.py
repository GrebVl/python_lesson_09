import telebot.types
from telebot import TeleBot
from emoji import emojize
import telebot_token as t_t
import lst_sorting as l_s
import result as r
import logger as log

bot = TeleBot(t_t.telebot_token())
print(f'Запущин {emojize(":grinning_face:")}')



@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="/help - Выводит все команды программы\n"
                                                    "/log - скачить фаил с историей операций\n"
                                                    "/sum - команда сложения 2 2i 3 4i == 5 + 6i\n"
                                                    "/diff - команда разности 2 2i 3 4i == -1 - 2i\n"
                                                    "/div - команда деления 2 2i 3 4i == 0.666667 + 0.5i\n"
                                                    "/mult - команда умнажения 2 2i 3 4i == 6 + 8i\n"
                                                    "калькулятор не работает с комплексными числами разной степени и разными переменными\n"
                                                    "даныые(числа) указываются через пробел: пример 2 2i 3 4i или 4i2 2 2i2 3")


@bot.message_handler(commands=['sum'])
def sum_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=sum_items, message=msg)

def sum_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summation(msg.text))

def summation(msg):
    msg = l_s.list_replace(msg)
    list_us = msg
    list_ = list_us.split()
    numbers_lst = l_s.list_nums(list_)
    complex_lst = l_s.list_complex(list_)
    sum_num = sum_nums(numbers_lst)
    sum_complex = sum_com(complex_lst)
    res = r.resukt(sum_num, sum_complex)
    log.logger(msg, 'summation', res)
    return res

def sum_nums(num_list):
    if num_list == None:
        return None
    elif len(num_list) > 0:
        sum_n = num_list[0]
        for i in range(1, len(num_list)):
            sum_n += num_list[i]
    else:
        sum_n = num_list[0]
    return sum_n

def sum_com(com_list):
    sum_c = float(com_list[0][1])
    sym = str(com_list[0][0])
    for i in range(1, len(com_list)):
        if sym == com_list[i][0]:
            sum_c += float(com_list[i][1])
        else:
            return 'Данные ведены не верно'
    if sum_c >= 0:
        return f'+{sum_c}{sym}'
    elif sum_c < 0:
        return f'{sum_c}{sym}'

@bot.message_handler(commands=['diff'])
def diff_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=diff_items, message=msg)

def diff_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=difference(msg.text))

def difference(msg):
    msg = l_s.list_replace(msg)
    list_us = msg
    list_ = list_us.split()
    numbers_lst = l_s.list_nums(list_)
    complex_lst = l_s.list_complex(list_)
    diff_num = diff_nums(numbers_lst)
    diff_complex = diff_com(complex_lst)
    res = r.resukt(diff_num, diff_complex)
    log.logger(msg, 'difference', res)
    return res

def diff_nums(num_list):
    if num_list == None:
        return None
    elif len(num_list) > 0:
        diff_n = num_list[0]
        for i in range(1, len(num_list)):
            diff_n -= num_list[i]
    else:
        diff_n = num_list[0]
    return diff_n

def diff_com(com_list):
    diff_c = float(com_list[0][1])
    sym = str(com_list[0][0])
    for i in range(1, len(com_list)):
        if sym == com_list[i][0]:
            diff_c -= float(com_list[i][1])
        else:
            return 'Данные ведены не верно'
    if diff_c >= 0:
        return f'+{diff_c}{sym}'
    elif diff_c < 0:
        return f'{diff_c}{sym}'


@bot.message_handler(commands=['div'])
def div_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=div_items, message=msg)

def div_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=division(msg.text))

def division(msg):
    msg = l_s.list_replace(msg)
    list_us = msg
    list_ = list_us.split()
    numbers_lst = l_s.list_nums(list_)
    complex_lst = l_s.list_complex(list_)
    div_num = div_nums(numbers_lst)
    div_complex = div_com(complex_lst)
    res = r.resukt(div_num, div_complex)
    log.logger(msg, 'division', res)
    return res

def div_nums(num_list):
    if num_list == None:
        return None
    elif len(num_list) > 0:
        div_n = num_list[0]
        for i in range(1, len(num_list)):
            div_n /= num_list[i]
    else:
        div_n = num_list[0]
    return div_n

def div_com(com_list):
    div_c = float(com_list[0][1])
    sym = str(com_list[0][0])
    for i in range(1, len(com_list)):
        if sym == com_list[i][0]:
            div_c /= float(com_list[i][1])
        else:
            return 'Данные ведены не верно'
    if div_c >= 0:
        return f'+{div_c}{sym}'
    elif div_c < 0:
        return f'{div_c}{sym}'

@bot.message_handler(commands=['mult'])
def mult_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=mult_items, message=msg)

def mult_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=multiplication(msg.text))

def multiplication(msg):
    msg = l_s.list_replace(msg)
    list_us = msg
    list_ = list_us.split()
    numbers_lst = l_s.list_nums(list_)
    complex_lst = l_s.list_complex(list_)
    mult_num = mult_nums(numbers_lst)
    mult_complex = mult_com(complex_lst)
    res = r.resukt(mult_num, mult_complex)
    log.logger(msg, 'multiplication', res)
    return res

def mult_nums(num_list):
    if num_list == None:
        return None
    elif len(num_list) > 0:
        mult_n = num_list[0]
        for i in range(1, len(num_list)):
            mult_n *= num_list[i]
    else:
        mult_n = num_list[0]
    return mult_n

def mult_com(com_list):
    mult_c = float(com_list[0][1])
    sym = str(com_list[0][0])
    for i in range(1, len(com_list)):
        if sym == com_list[i][0]:
            mult_c *= float(com_list[i][1])
        else:
            return 'Данные ведены не верно'
    if mult_c >= 0:
        return f'+{mult_c}{sym}'
    elif mult_c < 0:
        return f'{mult_c}{sym}'

@bot.message_handler(commands=['log'])
def log_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='logg')
    bot.send_document(chat_id=msg.from_user.id, document=open('log.txt', 'rb'))

@bot.message_handler()
def log_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Введите команду /help')

bot.polling()