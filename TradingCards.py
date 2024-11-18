import numpy as np
import random

numPeople = 10;
numProducts = 20;

#Define the current exchange_rates
exchange = []


# Everything starts at an even exchange
for i in range(numProducts):
        exchange.append(1)

#Define each person's starting wealth
holdings = np.zeros((numPeople, numProducts));
worth = []
for i in range(numPeople):
    worth.append(100 * numProducts)
    for j in range(numProducts):
        holdings[i,j] = 100

print ("Starting worth")
print (worth)

for rounds in range(10000000):
    #For each round, first change the price of one item
    i = random.randint(0, numProducts-1);
    up = (1 == random.randint(0,1));
    if up == True:
          exchange[i] *= 1.10;
    else:
        exchange[i] *= (1/1.10);
    if exchange[i] < 0.2:
        exchange[i] = 1;
    if exchange[i] > 5:
        exchange[i] = 1;
    exchange[i] = 0.5 + random.randint(0,10) * 0.1

    #Pick two people, have them exchange a random product
    p1 = random.randint(0, numPeople-1)
    p2 = random.randint(0, numPeople-1)
    if p1 != p2 :
        prod1 = random.randint(0,numProducts-1)
        prod2 = random.randint(0,numProducts-1)
        if prod1 != prod2:
            # how much does the p2 have of prod2 (in the units of p1)
            p2_has = holdings[p2,prod2] * exchange[prod2]
            p1_has = holdings[p1,prod1] * exchange[prod1]
            # Each trade no more than a third of the holdings
            trade = min(p1_has,p2_has)/3
            trade_p1 = trade / exchange[prod1]
            trade_p2 = trade / exchange[prod2]
            holdings[p1, prod1] -= trade_p1
            holdings[p1, prod2] += trade_p2
            holdings[p2, prod1] += trade_p1
            holdings[p2, prod2] -= trade_p2

for i in range(numPeople):
    worth_total = 0
    for j in range(numProducts):
        worth_total += holdings[i,j] * exchange[j]
    worth[i] = int(worth_total)

print("Ending worth")
print(worth)
# print(exchange)
