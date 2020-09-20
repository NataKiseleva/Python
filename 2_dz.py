wrd = input("Введите слово: ")
wrd2 = ' '
for i, sy in enumerate(wrd):
    if (i+1) % 2 == 0 and sy != 'а' and sy != 'к':
        wrd2 += sy
print(wrd2)