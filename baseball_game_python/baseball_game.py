import random

class Basball:
    def __init__(self):
        self.rand_list = []
        self.user_list = [None,None,None]
        
    def set_random_list(self):
        self.rand_list = random.sample(range(0,9),3)

    def get_user_number(self, idx):
        num = input(f"{idx+1} 번째 숫자를 입력하세요: ")
        if not num.isdigit():
            print('숫자만 적어주세요')
            return True
        if len(num) != 1:
            print('숫자 하나만 적어주세요')
            return True
        self.user_list[idx] = int(num)
        return False

    def check_nums(self):
        strike = 0
        ball = 0
        while strike<3:
            errValue = False 
            for idx in range(3):
                errValue = self.get_user_number(idx)
            if errValue:
                continue
            for i in range(len(self.user_list)):
                if self.rand_list[i] == self.user_list[i]:
                    strike += 1
                elif self.user_list[i] in self.rand_list:
                    ball += 1
                else:
                    pass
            print(f'{strike}strike, {ball}ball')
        print(f'you win!')

def main():
    ball = Basball()
    ball.set_random_list()
    ball.check_nums()
    
if __name__=="__main__":
    print("숫자 게임을 시작합니다.")
    main()