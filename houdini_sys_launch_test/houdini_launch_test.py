import os

class Hou_lauch_1:
    def __init__(self):
        self.home = ""
        self.version = ""
        self.ver_list = []

    def user_input(self):
        self.home = input("설치한 경로를 적어주세요.:\n")
        self.version_list()
        if not self.ver_list:
            return
        self.show_list()
        num = input("번호를 선택하세요:\n")
        self.version = self.ver_list[int(num)-1]

    def install_path(self):
        list_home_path = list(self.home)
        if list_home_path[0] != list_home_path[-1]:
            # remerge_path = os.path.join(self.home)           
            list_home_path.append(os.sep)
            list_home_path.insert(0, os.sep)
            remerge_path = ''.join(list_home_path)
        return remerge_path

    def version_list(self):
            root_dir = self.install_path()
            if not os.path.exists(root_dir):
                return
            dir_list = os.listdir(root_dir)
            for dirs in dir_list:
                if dirs.startswith('Houdini'):
                    self.ver_list.append(dirs)
 
    def show_list(self):
        for idx, ver in enumerate(self.ver_list):
            print(idx+1, " : ", ver.replace('Houdini', ''))

    def lau(self):
        while True:
            self.user_input()
            self.path = f'{self.install_path()}' + f'{self.version}'+ os.sep + 'bin'+ os.sep+ 'houdini'
            if not os.path.exists(self.path):
                print('경로를 다시 확인 후 입력해주세요.')
            else:
                os.system(self.path)
                break

#########################################################################################################

class Hou_lauch_2:
    def __init__(self):
        self.path = "/opt"
        self.ver_list = []
        self.version = ""

    def user_input(self):
        print(f"기본 경로 : {self.path}")
        user_input = input("설치한 경로에 실행파일이 존재하나요? (y/n)\n")        
        if user_input == 'n':
            self.path = input('변경된 경로를 적어주세요.\n')
        elif user_input == 'y':
            self.path

    def check_user_input(self):
        if not os.path.exists(self.path):
            return True
        return False

    def show_version_list(self):
        for d in os.listdir(self.path):
            if d.startswith('Houdini'):
                self.ver_list.append(d)

    def user_input_num(self):
        while True:
            num = input("번호를 선택하세요.:\n")
            if not num.isdigit():
                print("번호로 선택하세요.")
                continue
            num = int(num)
            if num > len(self.ver_list):
                print("상기된 번호만 입력하세요.")
                continue
            self.version = self.ver_list[num]
            break

    def go(self):
        while True:
            self.user_input()
            errCheck = self.check_user_input()
            if errCheck:
                print("현재 경로가 없습니다.")
                continue
            self.show_version_list()
            if not self.ver_list:
                print("해당 버전이 없습니다.")
                continue
            for i, v in enumerate(self.ver_list):
                print(i, " : ", v.replace('Houdini', ''))
            self.user_input_num()
            path = os.path.join(self.path, self.version, 'bin', 'houdini')
            # path = f'{self.path}' + f'{self.version}'+ os.sep + 'bin'+ os.sep+ 'houdini'
            if not os.path.exists(path):
                print('경로를 다시 확인 후 입력해주세요.')
            else:
                os.system(path)
                break

def main():
    h = Hou_lauch_1()()
    h.lau()
    # h = Hou_lauch_2()
    # h.go()

if __name__=='__main__':
    main()