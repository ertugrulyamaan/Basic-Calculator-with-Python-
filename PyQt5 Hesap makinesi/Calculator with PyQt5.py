import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
result=0
result_list=[]
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap makinesi yapımı")
        self.setGeometry(850,200,380,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
    def UI(self):
        ################Entry Field#########################

        self.entrybox=QLineEdit(self)
        self.entrybox.resize(335,30)
        self.entrybox.setAlignment(Qt.AlignRight)
        self.entrybox.setStyleSheet("font:14pt Arial Bold;border:3px solid gray;border-radius:5px;background-color:#e5e5fa")
        self.entrybox.setText("O")
        self.entrybox.move(20,30)
        ################Number Buttons###################################
        button_number=[]
        for i in range(1,10):
            i=QPushButton(str(i),self)
            i.setFont(QFont("Arial",15))
            i.resize(70,40)
            i.setStyleSheet("background-color:white")
            i.clicked.connect(self.enterNumbers)
            button_number.append(i)

        btn_index=0
        for i in range(0,3):
            for j in range(0,3):
                button_number[btn_index].move(25+j*90,70+i*70)
                btn_index+=1



        ####################Operator Buttons######################
        button_operator=[]
        for i in range(4):
            i=QPushButton(self)
            i.resize(70,40)
            i.setStyleSheet("background-color:white")
            i.setFont(QFont("Arial",15))
            i.clicked.connect(self.enterOperator)
            button_operator.append(i)
        button_operator[0].setText("+")
        button_operator[1].setText("-")
        button_operator[2].setText("*")
        button_operator[3].setText("/")

        for i in range(4):
            button_operator[i].move(290,70+i*70)
        ##################Other Buttons#################
        buttonzero=QPushButton("0",self)
        buttonzero.setStyleSheet("background-color:white")
        buttonzero.setFont(QFont("Arial",20))
        buttonzero.resize(250,40)
        buttonzero.clicked.connect(self.enterNumbers)
        buttonzero.move(25,280)
        ###########################################
        buttonClear=QPushButton("C",self)
        buttonClear.setStyleSheet("background-color:white")
        buttonClear.setFont(QFont("Arial",20))
        buttonClear.clicked.connect(self.funcClear)
        buttonClear.resize(70,40)
        buttonClear.move(25,340)
        ###########################################
        button_dot=QPushButton(".",self)
        button_dot.setStyleSheet("background-color:white")
        button_dot.setFont(QFont("Arial",15))
        button_dot.resize(70, 40)
        button_dot.clicked.connect(self.enterNumbers)
        button_dot.move(110, 340)
        ##########################################
        button_equal=QPushButton("=",self)
        button_equal.setStyleSheet("background-color:white")
        button_equal.setFont(QFont("Arial",20))
        button_equal.resize(70, 40)
        button_equal.clicked.connect(self.funcOperator)
        button_equal.move(200, 340)
        ############################################
        button_delete=QPushButton(self)
        button_delete.setIcon(QIcon("arrow.png"))
        button_delete.resize(70, 40)
        button_delete.clicked.connect(self.funcDelete)
        button_delete.move(290, 340)
        ###################Status Bar###################
        self.status_bar=QStatusBar()
        self.setStatusBar(self.status_bar)

    def enterNumbers(self):
        button_text=self.sender().text()
        print(button_text)
        if self.entrybox.text()=="O":
            self.entrybox.setText("")
            self.entrybox.setText(button_text)
        else:
            self.entrybox.setText(self.entrybox.text()+button_text)
    def enterOperator(self):
        buttontext=self.sender().text()
        if self.entrybox.text()!="O":
            self.entrybox.setText(self.entrybox.text()+buttontext)

    def funcClear(self):
        self.entrybox.setText("O")
    def funcDelete(self):
        x=self.entrybox.text()

        x=x[:-1]
        self.entrybox.setText(x)
        if len(x)==0:
            self.entrybox.setText("O")
    def funcOperator(self):
        content=self.entrybox.text()
        result=eval(content)
        self.entrybox.setText(str(result))
        result_list.append(content)
        result_list.reverse()
        self.status_bar.showMessage("History:"+"|".join(result_list[:5]))
        self.status_bar.setFont(QFont("Times",12))
def main():
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()







