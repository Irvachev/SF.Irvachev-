money = int(input())
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
a = money * (per_cent['ТКБ'] / 100)
deposit.append(a)
a = money * (per_cent['СКБ'] / 100)
deposit.append(a)
a = money * (per_cent['ВТБ'] / 100)
deposit.append(a)
a = money * (per_cent['СБЕР'] / 100)
deposit.append(a)
deposit = list(map(round, deposit))
print(deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))