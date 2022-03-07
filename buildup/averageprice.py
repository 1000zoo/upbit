decendingtimes = 10
alpha = 0.98
initprice = 1000
count = 0

averageprice = initprice

for i in range(decendingtimes):
    averageprice = (averageprice + alpha * initprice) / 2
    alpha *= 0.98
    print(averageprice, alpha)
    print('-'*50)