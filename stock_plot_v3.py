'''File stock_plot_v3.py
---------------------------------
주식의 일일 최고가와 최저가를 그래프로 표현한다.
stock_load.py에 의존성이 있다.
'''
import numpy as np
import matplotlib.pyplot as plt
from stock_load import load_stock

def do_highlow_plot(stock_df, name_str):
    ''' 일일 최고가와 최저가의 점을 구한다.
    인수로 전달받은 주식 데이터 프레임(stock_df)의 
    일일 주식을 위한 최고가와 최저가 열을 사용한다.
    '''
    makeplot(stock_df, 'High', 'daily highs')
    makeplot(stock_df, 'Low', 'daily lows')
    plt.title('High/Low Prices for ' + name_str)
    plt.show()

# 플롯을 만든다: 지루하고 반복적인 작업을 수행한다.
def makeplot(stock_df, field, my_str):
    column = getattr(stock_df, field)
    column = np.array(column, dtype='float')
    plt.plot(stock_df.Date, column, label=my_str)
    plt.legend()

# 메인 모듈인 경우 테스트를 수행한다.
if __name__ == '__main__':
    stock_df = load_stock('MSFT')
    do_highlow_plot(stock_df, 'MSFT')
