print('Укажите время в секундах:')
duration = int (input())
if duration < 60:
    print (duration,'сек')
elif duration < (60*60):
    min = duration // 60
    sec = duration % 60
    print (min, 'мин', sec, 'сек')
elif duration < (3600*24):
    hour = duration // 3600
    ostatok = duration % 3600
    if ostatok >= 60:
        min = ostatok // 60
        sec = ostatok % 60
    else:
        min = 0
        sec = ostatok
    print (hour, 'час', min, 'мин', sec, 'сек')
else:
    day = duration // (3600*24)
    ostatok_hour = duration % (3600*24)
    if ostatok_hour >= 3600:
        hour = ostatok_hour // 3600
        ostatok = duration % 3600
        if ostatok >= 60:
            min = ostatok // 60
            sec = ostatok % 60
        else:
            min = 0
            sec = ostatok
    else:
        hour = 0
    print (day, 'дн', hour, 'час', min, 'мин', sec, 'сек')