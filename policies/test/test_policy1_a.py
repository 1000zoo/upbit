import pyupbit as pu

#최대 10분 안에서 최소값이면 매수
#0.3% 이득, 또는 0.7% 손해 까지는 매도 X

H = 60
D = 24
M = 30
XRP = 'KRW-XRP'
BTC = 'KRW-BTC'
ETH = 'KRW-ETH'

FEE = 0.9995

def main():
    candles = pu.get_ohlcv(BTC, interval='minute1', count=H*D*M)

    init_bal = 1_000_000
    curr_bal = init_bal
    coin_bal = 0
    avg_price = 0
    target_rate = 1.01
    loss_rate = 0.95
    cnt = 0
    trade_count = 0

    for time, low, close in zip(candles.index, candles['low'], candles['close']):
        #(1)
        if curr_bal != 0:
            if cnt == 0:
                min_price = low
                cnt += 1
            elif cnt < 10:
                min_price = min(min_price, low)
                cnt += 1
            #25분 지나면 그냥 매수 (2)
            elif cnt > 25 or min_price > low:
                avg_price, coin_bal, curr_bal = buycoin(low, curr_bal)
                print(str(time) + " : buy at " + str(avg_price))
                cnt = 0
            else:
                cnt += 1
            continue
        #(3),(4)
        else:
            if target_rate*avg_price < low or low < loss_rate*avg_price:
                rate, coin_bal, curr_bal = sellcoin(avg_price, close, coin_bal)
                print(str(time) + " : sell at " + str(low))
                print("earn rate : " + str(rate))
                print("current money : " + str(curr_bal))
                trade_count += 1
                print("trade_count %s" %trade_count)
    print(pu.get_current_price(BTC) / avg_price * coin_bal)

def buycoin(price, bal):
    return price, bal*FEE, 0

def sellcoin(avg_price, curr_price, coin_bal):
    rate = curr_price / avg_price
    curr = FEE * coin_bal * rate
    return rate, 0, curr

if __name__ == '__main__':
    main()