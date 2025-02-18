cost = int(input())

money_list = [500,100,50,10,5,1]
money_list.sort(reverse=True)

money = 1000
change = money - cost
count = 0

for coin in money_list:
    count += change // coin
    change %= coin

print(count)