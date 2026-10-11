amount = int(input("Введите сумму сдачи: "))

coins = [50, 10, 5, 2, 1]

for coin in coins:
    count = amount // coin
    amount = amount % coin
    print("Монет по", coin, ":", count)