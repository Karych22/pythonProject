#L = [i for i in range(10)]
#M = [i for i in range(10,0,-1)]
#N = [a*b for a,b in zip(L,M)]
#print(N)

#text = input()  # получаем строку
#last = text[0]  # сохраняем первый символ
#count = 0  # заводим счётчик
#result = ''  # и результирующую строку
#for c in text:
#    if c == last:  # если символ совпадает с сохранённым,
#        count += 1  # то увеличиваем счётчик
#    else:
#        result += last + str(count)  # иначе записываем в результат
#        last = c  # и обновляем сохранённый символ с его счётчиком
#        count = 1
#result += last + str(count)  # и добавляем в результат последний символ
#print(result)


a = ["asd", "bbd", "ddfa", "mcsa"]
print(len(a, key=len))