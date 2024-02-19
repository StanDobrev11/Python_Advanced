from collections import deque

money = [int(x) for x in input().split()]
food_prices = deque(int(x) for x in input().split())

food_eaten = 0
change = 0
while True:
    try:
        cash = money.pop() + change
        food = food_prices.popleft()
    except IndexError:
        break

    change = 0
    if cash >= food:
        change = cash - food
        food_eaten += 1

if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif food_eaten > 0:
    if food_eaten == 1:
        print(f"Henry ate: {food_eaten} food.")
    else:
        print(f"Henry ate: {food_eaten} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")
