def resukt(res_a, res_b):
    if res_a == None:
        return str(res_b)
    elif res_b == None:
        return str(res_a)
    elif res_b == 'Данные ведены не верно':
        return 'Данные ведены не верно'
    else:
        return str(res_a) + str(res_b)