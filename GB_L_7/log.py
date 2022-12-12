from datetime import datetime
from time import time

string = 'Привет'
def log(string):
   time = datetime.now().strftime('%H:%M')
   with open('logfile.txt', 'a', encoding='utf-8') as log:
      log.write(f'Время записи: {time}; Примечание: ; {string}\n')

