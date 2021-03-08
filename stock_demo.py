# file stock_demo.py ------------------------------
# stock_plot_v4.py 파일에 의존성이 있다 

from stock_plot_v4 import *

menu_str = ('메뉴 선택:\n' +
'0. 종료\n' +
'1. 간단한 종가 그래프 출력\n' +
'2. 일일 최고가와 최저가 출력 \n' +
'3. 가격/판매량 서브플롯 출력 \n' +
'4. 변동 평균을 추가한 가격 \n')

prompt_msg = '주식 시세 기호를 입력하세요(종료하려면 엔터를 입력하세요): '
def main():
    while True:
        # 유요한 주식을 사용자에게 입력 받을 때까지 프롬프트를 띄운다.
        try:
            s = input(prompt_msg)
            s = s.strip()
            if not s:                           # 빈 문자열이면 루프를 탈출한다.
                return
            stock_df = load_stock(s)
            n = int(input(menu_str + '선택한 메뉴를 입력하세요: '))

            if n < 0 or n > 4:
                n = 0
            if n == 0:
                return

            fn = [do_simple_plot, do_highlow_plot, do_volume_subplot, do_movingavg_plot][n-1]
            fn(stock_df, s)
        except:
            print('주식을 찾지 못했습니다. 다시 시도하세요. ')

main()
