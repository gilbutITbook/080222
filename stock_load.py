'''File stock_load.py -----------------------------

주식 시세(ticker) 기호를 가져오기 위해서 주식 적재 작업을 수행한다.
의존하고 있는 모듈은 없다.

'''
# pip install pandas_datareader
import pandas_datareader.data as web
def load_stock(ticker_str):
    ''' 주식 적재 함수.
    인수로 주어진 문자열 ticker_str의 정보를 적재한다.
    'MSFT'와 같이 정해진 주식의 정보를 pandas 데이터 프레임에 넣고 반환한다.
    '''
    df = web.DataReader(ticker_str, 'yahoo')
    df = df.reset_index()
    return df

# 데이터 프레임(stock_df)을 가져와서 출력한다.
if __name__ == '__main__':
    stock_df = load_stock('MSFT') 	# 'msft'를 입력해도 괜찮다.
    print(stock_df)
    print(stock_df.columns)
