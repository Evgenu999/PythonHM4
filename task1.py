# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def raunding(number, number_raund):

    dr = number.split(".")
    str1 = dr[1]
    str2 = ''
    i = 0

    if len(dr[1]) == number_raund:    
        print("Ваше число уже округлено до нужного знака!")
        exit()
    
    while i < number_raund:
        str2 = str2 + str1[i] 
        i += 1

    if int(str1[number_raund]) >= 5:
        a = int(str2[i - 1]) + 1 
        b = list(str2)
        b.insert(i - 1,str(a))
        b.pop() 
        print(dr[0] + "." + "".join(b))
    else:
        print(dr[0]+"."+str2) 

number = input("Введите число, которое вы хотите округлить ")
number_raund = int(input("Введите цифру сколько знаков после точки нужно оставить "))
raunding(number, number_raund)

from math import pi
print(pi)
raunding(str(pi), number_raund=4)
