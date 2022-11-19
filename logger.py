from datetime import datetime as dt
import view as v
from  time import time

def logger_calc(data, result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        data = ''.join(data)
        result = ''.join(result)
        file.write(f'Time: {time} Expression: {data} Result: {result}\n')
def get_logger():
    with open('log.csv', 'r') as file:
        v.logger = []
        for line in file:
            v.logger.append(line)


