chisla = []
mainsumm = 0
for i in range(1, 1000, 2):
    chisla.append (i**3)
    k = int ((i-1)/2)
    sum = 0
    a = chisla [k]
    for j in range (len (str (a)) -1 , -1, -1):
        b = a//(10**j)
        sum = sum + b
        a = a - b * (10**j)
    if sum % 7 == 0:
        mainsumm = mainsumm + chisla [k]
print (mainsumm)