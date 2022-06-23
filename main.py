procent = 'процент'
a = 'а'
ov = 'ов'
for i in range (1 , 101 , 1):
    if i < 10:
        namber = i
        if namber == 1:
            sklonenie = procent
        elif namber == 2 or namber == 3 or namber == 4:
            sklonenie = procent + a
        else:
            sklonenie = procent + ov
    elif i > 10 and i < 15:
        sklonenie = procent+ov
    elif i == 10 or i >= 15:
        namber = i % (10 ** (len(str(i)) - 1))
        if namber == 1:
            sklonenie = procent
        elif namber == 2 or namber == 3 or namber == 4:
            sklonenie = procent + a
        else:
            sklonenie = procent + ov
    print (i ,sklonenie)