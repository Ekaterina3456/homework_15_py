# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta

def future_date():
    days = int(input('введите количество дней: '))
    date = datetime.now()
    future = date + timedelta(days)
    return future

print(future_date())