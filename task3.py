# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

colection = [3, 2, 1, 3, 2, 4, 5, 4, 7, 9]
count1 = 0
colection_one_element = []
for i in colection:
    count1 = colection.count(i)        
    if count1 == 1:
        colection_one_element.append(i)
print(colection_one_element, end=' ')