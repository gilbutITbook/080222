'''File stock_plot_v2.py
---------------------------------
두 개의 주식 시세를 그래프를 그린다.
stock_load.py에 의존성이 있다.
'''
import numpy as np
import matplotlib.pyplot as plt
from stock_load import load_stock

def do_duo_plot(stock1_df, stock2_df, name1, name2):
    ''' 두 주식의 그래프를 그린다.
    인수는 데이터 프레임과,
    열의 이름으로 사용할 주식 시세 기호 문자열이다.
    '''
    makeplot(stock1_df, 'Close', name1)
    makeplot(stock2_df, 'Close', name2)
    plt.title(name1 + ' vs. ' + name2)
    plt.show()

# 플롯을 만든다: 지루하고 반복적인 작업을 수행한다.
def makeplot(stock_df, field, my_str):
    column = getattr(stock_df, field)
    column = np.array(column, dtype='float')
    plt.plot(stock_df.Date, column, label=my_str)
    plt.legend()

# 메인 모듈이면 테스트를 수행한다.
if __name__ == '__main__':
    stock1_df = load_stock('IBM')
    stock2_df = load_stock('DIS')
    do_duo_plot(stock1_df, stock2_df, 'IBM', 'Disney')
