import numpy as np

count = 0
number = np.random.randint(1, 101)
print("Загадано число от 1 до 100")
min = 0
max = 100
while True:
    predict = round((min+max)/2)
    #predict = int(input())
    count += 1
    if number == predict:
        break
    elif number > predict:
        min = predict
        round((max + min) / 2)
    elif number < predict:
        max = predict
        (round((max+min)/2))


print(f"Вы угадали число {number} за {count} попыток.")