import sys

def print_help():
    return '''
    입력 받은 년도를 60갑자로 출력해 주는 툴입니다.
    궁금하신 년도를 입력해 주세요!
    ex) python3 zodiac.py 2023
    '''

def get_zodiac(year):
    ten_zodiac = ['경', '신', '임', '계', '갑', '을', '병', '정', '무', '기']
    twelve_zodiac = ['신', '유', '술', '해', '자', '축', '인', '묘', '진', '사', '오', '미']

    ten = year % 10
    twelve = year % 12

    print(f'{year}년은 {ten_zodiac[ten]}{twelve_zodiac[twelve]}년 입니다.')      

def main():
    args = sys.argv
    if len(args) != 2:
        print(print_help())
        return
    str_year = args[1] 
    if not str_year.isdigit():
        print('숫자만 입력해 주세요')
        print(print_help())
        return
    year = int(str_year)
    get_zodiac(year)

if __name__ == "__main__":
    main()
