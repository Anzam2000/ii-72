def spin_word(tekst):
    words = tekst.split()
    tekst_reverse = []
    for i in words:
        if len(i) >= 5:
            tekst_reverse.append(i[::-1])
        else:
            tekst_reverse.append(i)
    return tekst_reverse
tekst = input()
print(spin_word(tekst))
# Напишите функцию, которая принимает строку из одного или нескольких слов и возвращает ту же строку, но со всеми словами, в которых пять или более букв перевернуты (как в названии этого Ката). Переданные строки будут состоять только из букв и пробелов. Пробелы будут включены только в том случае, если присутствует более одного слова.


