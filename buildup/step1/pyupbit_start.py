import pyupbit as pu

print(pu.Upbit)
# print(pu.get_tickers(fiat="BTC"))

price = pu.get_current_price("KRW-XRP")
print(price)
print(type(price))