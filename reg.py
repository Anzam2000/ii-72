try:
  import random
  def binary_search(data, elem):
      low = 0
      high = len(data) - 1
      while low <= high:
          middle = (low + high)//2
          if data[middle] == elem:
              return middle

          elif data[middle] == elem:
              high = middle - 1

          else:
             low = middle + 1
      return -1
  list = list(set([random.randint(1, 10) for i in range(10)]))
  list.sort()
  index = random.randint(0, len(list) - 1)
  print(list)
  number = int(input("Пиши число: "))
  while index != binary_search(list, number):
      if index > binary_search(list, number):
          print("Число больше")
      elif index < binary_search(list, number):
          print("Число меньше")
      number = int(input("По новой: "))
  print("угадал")
except:
    print('Нужно цифры писать')