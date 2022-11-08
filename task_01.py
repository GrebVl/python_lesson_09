from emoji import emojize
import random



def player_turn():
    emoji_list = [emojize(f":keycap_{i}:") for i in range(1, 10)]
    emoji_victori = emojize(":partying_face: :party_popper: :double_exclamation_mark:")
    sheet_output(emoji_list)
    user_first = emojize(":cross_mark:")
    user_second = emojize(":hollow_red_circle:")
    slots_user = [user_first, user_second]
    num_user = random.choice(slots_user)
    count = 9
    while count != 0 and count > 0:
        print(f'Ход игрока {num_user}')
        num_sel = num_select()
        for i in range(len(emoji_list)):
            if i == num_sel - 1:
                if num_user == user_first and emoji_list[i] != user_second:
                    emoji_list[i] = user_first
                    sheet_output(emoji_list)
                    num_user = user_second
                    count -= 1
                    if game_over(emoji_list) == True:
                        print(f'победил игрок {user_first}\n'
                              f'{emoji_victori}')
                        count = 0
                        break
                elif num_user == user_second and emoji_list[i] != user_first:
                    emoji_list[i] = user_second
                    num_user = user_first
                    count -= 1
                    sheet_output(emoji_list)
                    if game_over(emoji_list) == True:
                        print(f'победил игрок {user_second}\n'
                              f'{emoji_victori}')
                        count = 0
                        break
    if game_over(emoji_list) == False:
        print(f'Ничья {emojize(":ghost:")}')

def num_select():
    exit_sel = False
    while exit_sel == False:
        num_sel = str(input('Введите число от 1 до 9: '))
        if num_sel.isdigit() == True:
            num_select = int(num_sel)
            if num_select > 0 and num_select <= 9:
                exit_sel = True
            else:
                print('Введено значение находится в не диапазона от 1 до 9')
        elif num_sel.isdigit() == False:
            print('Введено некоректное значение')
    return num_select

def game_over(list_us):
    list_over = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6))
    for i in list_over:
        if list_us[i[0]] == list_us[i[1]] == list_us[i[2]]:
            return True
    return False

def sheet_output(list_us):
    print(f'{list_us[0]}   |   {list_us[1]}   |  {list_us[2]}\n'
          f'-------------------\n'
          f'{list_us[3]}   |   {list_us[4]}   |  {list_us[5]}\n'
          f'-------------------\n'
          f'{list_us[6]}   |   {list_us[7]}   |  {list_us[8]}\n'
          )

player_turn()