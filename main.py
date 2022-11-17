print("Введите кол-во билетов:")
all_tickets = int(input())
total_price = 0
if all_tickets > 3:
    discount = True
else:
    discount = False
while all_tickets != 0:
    print("Введите возраст посетителя:")
    age = int(input())
    if age >= 25:
        total_price += 1390
    elif age >= 18:
        total_price += 990
    all_tickets -= 1
if discount:
    total_price *= 0.9
print("К оплате:", round(total_price), "руб.")