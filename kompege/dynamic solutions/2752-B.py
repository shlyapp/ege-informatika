file = open('kompege/files/27B-2752.txt')
N = int(file.readline())
# буффер чисел, которые мы не учитываем в статистике
buffer = [int(file.readline()) for i in range(5)]
end = [0 for i in range(10)]
counter = 0

for i in range(N - 5):
    num = int(file.readline())
    
    # тройка на конце в двух случаях (1 * 3, 7 * 9), но еще перестановка
    if num % 10 == 3: counter += end[1]
    elif num % 10 == 7: counter += end[9]
    elif num % 10 == 1: counter += end[3]
    elif num % 10 == 9: counter += end[7]

    # нулевой элемент буффера на след.итерации выйдет, значит добавляем его в статистику
    end[buffer[0] % 10] += 1
    # двигаем буффер
    buffer.append(num)
    buffer.pop(0)

print(counter)

