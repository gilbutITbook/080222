# file stock_plot_v4.py ------------------------------

import numpy as np
import matplotlib.pyplot as plt
from stock_load import load_stock

def do_simple_plot(stock_df, name_str):
    ''' 플롯을 수행하는 함수.
    간단한 종가 그래프를 그린다.
    '''
    makeplot(stock_df,'Close', 'closing price')
    plt.title(name_str + ' Stock Price')
    plt.show()

def do_highlow_plot(stock_df, name_str):
    ''' 최고가/최저가 플롯을 수행하는 함수.
    주식의 최고가와 최저가를 그래프로 그리고, 보여준다.
    '''
    makeplot(stock_df, 'High', 'daily highs')
    makeplot(stock_df, 'Low', 'daily lows')
    plt.title('High/Low Graph for ' + name_str)
    plt.show()

def do_volume_subplot(stock_df, name_str):
    ''' 판매량 서브플롯을 수행하는 함수.
    종가와 판매량 서브플롯을 그래프로 그린다.
    '''
    plt.subplot(2, 1, 1) 			# 위쪽 그래프를 그린다.
    makeplot(stock_df, 'Close', 'price')
    plt.title(name_str + ' Price/Volume')
    plt.subplot(2, 1, 2) 			# 아래쪽 그래프를 그린다.
    makeplot(stock_df, 'Volume', 'volume')
    plt.show()

def do_movingavg_plot(stock_df, name_str):
    ''' 변동-평균 플롯을 수행하는 함수.
    180간의 변동 평균 선을 가격과 함께 그래프로 그린다.
    '''
    makeplot(stock_df,'Close', 'closing price')
    makeplot(stock_df,'Close', '180 day average', 180)
    plt.title(name_str + ' Stock Price')
    plt.show()

# 지루하고 반복되는 작업을 수행한다.
def makeplot(stock_df, field, my_str, avg=0):
    column = getattr(stock_df, field)
    if avg: # Only plot avg if not 0!
        column = column.rolling(avg, min_periods=1).mean()
    column = np.array(column, dtype='float')
    plt.plot(stock_df.Date, column, label=my_str)
    plt.legend()

if __name__ == '__main__':
    name_str = 'GOOGL'
    stock_df = load_stock(name_str)
    do_movingavg_plot(stock_df, name_str)
    do_simple_plot(stock_df, name_str)
    do_volume_subplot(stock_df, name_str)
    do_highlow_plot(stock_df, name_str)
