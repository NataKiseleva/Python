count = 0
mas = []
while True:
    string = input("ведите слово:")
    if string == '':
        break
    mas.append(string)
for strings in mas:
    word = ''
    for i, symbol in enumerate(strings):
        if i > count:
            word += symbol
    count += 1
    if word != '':
        print(word)
    else:
        print("Были удалены все символы в слове")

