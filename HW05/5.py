print("Введите название файла с расширением: ")
file = input()
with open(file) as f:
    lines = f.readlines()
    count = 0
    const = 0
    words = 0
    Over_f_words = 0
    max_word = 0
    min_word = 0
    for line in lines:
        if line != '\n':
            for symbol in line:
                if symbol == ' ':
                    words += 1
            words += 1
            if max_word < words:
                max_word = words
            if min_word > words or min_word == 0:
                min_word = words
            if words > 5:
                Over_f_words += 1
            count += words
            const += 1
            words = 0
    avg_word = count/const
    pr_f_words = (Over_f_words/const) * 100
    print("Среднее количество слов в строке: ", avg_word)
    print('Процент строк, количество слов в которых больше 5: ', pr_f_words)
    print('Отношение количества слов в короткой строке к количеству слов в длинной: ', max_word/min_word)
