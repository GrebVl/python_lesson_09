import datetime
from datetime import datetime


def logger(msg, command, res):
    current_time = datetime.now()
    data = str(current_time)
    file_data = open("log.txt", "a", encoding='utf-8')
    file_data.write(f'{data} {", "} {msg} {", "} {command} {", "} {res}\n')
    file_data.close()