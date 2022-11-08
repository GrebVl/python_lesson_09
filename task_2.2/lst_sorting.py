def list_replace(text_):
    text_ = str(text_)
    text_ = text_.replace(",", ".")
    return text_

def num_float(num):
    if num.isdigit():
        return True
    else:
        try:
            float(num)
            return True
        except ValueError:
            return False

def list_nums(list_user):
    list_n = []
    for i in range(len(list_user)):
        if num_float(list_user[i]) == True:
            list_n.append(float(list_user[i]))
    if len(list_n) > 0:
        return list_n
    else:
        return None

def list_complex(list_user):
    list_c = []
    for i in range(len(list_user)):
        str_c = str(list_user[i])
        for j in range(len(str_c)):
            if num_float(str_c[j]) == False and str_c[j] != '.' and str_c[j] != '-':
                if j == 0:
                    list_c.append((str_c[j:len(str_c)], '1'))
                else:
                    list_c.append((str_c[j:len(str_c)], str_c[0:j]))
    if len(list_c) > 0:
        return list_c
    else:
        return None

