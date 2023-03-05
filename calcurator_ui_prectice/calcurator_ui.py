from PySide2 import QtWidgets, QtCore, QtUiTools
import sys
import os
import re


class Calcu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.expanduser('~/git/sunjunPark/calcurator_ui.ui')
        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()
        self.init_ui()
        self.ui.show()
        # ~/calcurator_ui.ui 가져온다.
        # 해당 파일을 연다
        # Qt designer를 load한다.
        # 파일을 Qt designer에서 실행한다.
        # 가상 메모리의 실행을 닫아준다.
        # init_ui함수를 실행한다.
        # 만든 ui를 보여준다.

    def init_ui(self):
        self.ui.btn_1.clicked.connect(self.button_1)
        self.ui.btn_2.clicked.connect(self.button_2)
        self.ui.btn_3.clicked.connect(self.button_3)
        self.ui.btn_4.clicked.connect(self.button_4)
        self.ui.btn_5.clicked.connect(self.button_5)
        self.ui.btn_6.clicked.connect(self.button_6)
        self.ui.btn_7.clicked.connect(self.button_7)
        self.ui.btn_8.clicked.connect(self.button_8)
        self.ui.btn_9.clicked.connect(self.button_9)
        self.ui.btn_0.clicked.connect(self.button_0)
        self.ui.add.clicked.connect(self.add)
        self.ui.subtract.clicked.connect(self.sub)
        self.ui.multiply.clicked.connect(self.mult)
        self.ui.divide.clicked.connect(self.div)
        self.ui.reset.clicked.connect(self.clear_num)
        self.ui.delt.clicked.connect(self.del_num)
        self.ui.equal.clicked.connect(self.equal)
        self.ui.floating.clicked.connect(self.floating)
        self.ui.percent.clicked.connect(self.per)
        self.ui.quit.clicked.connect(self.quit_clicked)
        # ui의 각 버튼을 연결된 함수값을 클릭한다.

    def oper(self, op):
        exist_text = self.ui.lineEdit_1.text()
        self.ui.lineEdit_1.setText(exist_text + op)
        # lineEdit_1이라는 ui에 텍스트를 넣는다. 그 값을 op와 더해서 값을 띄운다.

    def add(self):
        self.oper("+")

    def sub(self):
        self.oper("-")

    def mult(self):
        self.oper("*")

    def div(self):
        self.oper("/")

    def floating(self):
        self.oper(".")

    def per(self):
        self.oper("%")

    def button_1(self):
        self.oper("1")

    def button_2(self):
        self.oper("2")

    def button_3(self):
        self.oper("3")

    def button_4(self):
        self.oper("4")

    def button_5(self):
        self.oper("5")

    def button_6(self):
        self.oper("6")

    def button_7(self):
        self.oper("7")

    def button_8(self):
        self.oper("8")

    def button_9(self):
        self.oper("9")

    def button_0(self):
        self.oper("0")

    def clear_num(self):
        self.ui.lineEdit_1.setText("")
        self.ui.lineEdit_2.setText("")

    def del_num(self):
        exist_text = self.ui.lineEdit_1.text()
        self.ui.lineEdit_1.setText(exist_text[:len(exist_text) - 1])

    # 각 버튼에 대한 명령 함수

    def equal(self):
        equation = self.ui.lineEdit_1.text()

        list_equ = list(equation)

        if "%" in list_equ and "+" in list_equ:
            add_index = list_equ.index('+')
            per_index = list_equ.index('%')
            front_list = list_equ[:add_index]
            back_list = list_equ[add_index:per_index]
            front_str = ''.join(front_list)
            back_str = ''.join(back_list)
            eual = front_str + "*" + "(" + "1" + back_str + "/" + "100" + ")"
            ans = round(eval(eual), 4)
            self.ui.lineEdit_1.setText("")
        elif "%" in list_equ and "-" in list_equ:
            add_index = list_equ.index('-')
            per_index = list_equ.index('%')
            front_list = list_equ[:add_index]
            back_list = list_equ[add_index:per_index]
            front_str = ''.join(front_list)
            back_str = ''.join(back_list)
            eual = front_str + "*" + "(" + "1" + back_str + "/" + "100" + ")"
            ans = round(eval(eual), 4)
            self.ui.lineEdit_1.setText("")
        elif "%" not in list_equ:
            ans = round(eval(equation), 4)

        abs_ans = abs(ans)
        con_ans = int(abs_ans)
        str_ans = str(con_ans)

        if str_ans.isdigit():
            if self.ui.lineEdit_2.text() == "" and "%" in list_equ:
                self.ui.lineEdit_1.setText(str(ans))
            else:
                self.ui.lineEdit_2.setText(str(ans))
        else:
            self.ui.lineEdit_2.setText("Wrong Input")

    # 사용자가 보기 편하도록 입력하는 칸과 결과 출력하는 칸을 나눴다.
    # try except대신에 if와 else가 나을 것 같다.

    def quit_clicked(self):
        self.ui.close()
    # ui를 닫아주는 함수


def main():
    app = QtWidgets.QApplication()
    mycalc = Calcu()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
