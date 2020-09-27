while True:
    string = input("ведите слово:")
    word = ''
    if string == "":
        break
    string = string.lower()
    string = string.strip(".,'!@#$%^*()_-+=:;?")
    string = string.strip('"')
    string = string.strip()
    for i, symbol in enumerate(string):
        if i <= len(string)/2 - 1:
            word += symbol
    print(word)
