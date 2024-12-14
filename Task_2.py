# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

from datetime import datetime
from time import strftime

date = datetime.now()
weekday = strftime('%A')
count = date.isocalendar()[1]

print(f'{date}, {weekday}, week_number - {count}')