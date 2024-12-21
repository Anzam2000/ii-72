import telebot
import string
token = "7715079734:AAFiEt054ZeorlXyJHOH4OsWxjvfd-2TIUc"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Даров, я сортирую числа. Напиши их через пробел.')
@bot.message_handler(content_types=['document'])
def handle_file(message):
    if 'txt' == message.document.file_name.split('.')[1]:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src = message.document.file_name
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            downloaded_file = str(downloaded_file.split())
            input_string = downloaded_file.replace(',', ' ')
            input_string = input_string.replace('b', '')
            input_string = input_string.replace('[', '')
            input_string = input_string.replace("'", '')
            input_string = input_string.replace("-", '')
            input_string = input_string.replace("]", '')
            print(input_string)
            numbers = list(map(float, input_string.split()))
            sorted_numbers = radix_sort(numbers)
            bot.send_message(message.chat.id, ' '.join(map(str, sorted_numbers)))
            sorted_numbers = ','.join(map(str, numbers))
            with open('Итоговые.txt', 'w') as file:
                    file.write(f"{sorted_numbers} ,")
            with open("Итоговые.txt", "rb") as file:
                file.read()
            bot.send_document(message.chat.id, open(r'C:\Users\Замараев ИИ 72\PycharmProjects\pythonProject3\Итоговые.txt', 'rb'))

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
        # Преобразуем текст в список чисел
        numbers = list(map(float, message.text.split()))
        sorted_numbers = radix_sort(numbers)
        bot.send_message(message.chat.id, ' '.join(map(str, sorted_numbers)))


def radix_sort(arr):
    # находим размер самого длинного числа
    max_digits = max(len(str(int(x))) for x in arr)

    # основание системы счисления
    base = 10

    # перебираем все разряды, начиная с нулевого
    for i in range(max_digits):
        # создаём промежуточный пустой массив из 10 элементов
        bins = [[] for _ in range(base)]

        # перебираем все элементы в массиве
        for x in arr:
            # получаем цифру, стоящую на текущем разряде в каждом числе массива
            digit = int(x // (base ** i)) % base
            # отправляем число в промежуточный массив в ячейку, которая совпадает со значением этой цифры
            bins[digit].append(x)

        # собираем в исходный массив все ненулевые значения из промежуточного массива
        arr = [x for queue in bins for x in queue]

    # возвращаем отсортированный массив
    return arr
bot.polling(none_stop=True)
