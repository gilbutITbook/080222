'''File stock_plot_v1.py ---------------------------

두 개의 지정 주식에 대한 종장 시세로 최소 그래프를 그린다.
stock_load.py에 의존성이 있다.
'''
import numpy as np
import matplotlib.pyplot as plt
from stock_load import load_stock

def do_plot(stock_df):
    ''' 플롯을 수행하는 함수.
    stock_df를 사용하여, 웹에서 주식 데이터 프레임을 읽어 온다.
    '''
    column = stock_df.Close 			# 가격 추출.
    column = np.array(column, dtype='float')
    plt.plot(stock_df.Date, column, label = 'closing price')
    plt.legend()
    plt.title('MSFT Stock Price')

    plt.show()                                  # 그래프 출력.

# 두 개의 테스트 케이스 수행.
if __name__ == '__main__':
    stock_df = load_stock('MSFT')
    do_plot(stock_df)
    stock_df = load_stock('AAPL')
    do_plot(stock_df)
