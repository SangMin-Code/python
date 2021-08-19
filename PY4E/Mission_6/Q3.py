from typing import List

def profit_rate(stocks:str,sells:List[int]):

    stocks_list = stocks.split(',')

    rates = []
    for idx, stock in enumerate(stocks_list):
        name,amount,purchase = stock.split('/')
        amount,purchase = int(amount),int(purchase)
        rates.append([name,(sells[idx]/purchase)*100-100])
    rates = sorted(rates,key=lambda x:x[1],reverse=True)

    for name,rate in rates:
        print(f'{name}의 수익률 : {rate:.3}')



stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

profit_rate(stocks,sells)