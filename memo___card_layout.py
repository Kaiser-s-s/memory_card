''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from PyQt5.QtCore import QTimer
from memo___app import app 

timer = QTimer()
timer.setInterval()


question = 'Яблуко'
answer = 'apple'
wrong_answer1 = 'caterpillar'
wrong_answer2 = 'application'
wrong_answer3 = 'building'
answers = [answer]
questions = [answer, wrong_answer1, wrong_answer2, wrong_answer3]

QHb1 = QHBoxLayout()
QHb2 = QHBoxLayout()
QHb3 = QHBoxLayout()
QHb4 = QHBoxLayout()
QVb1 = QVBoxLayout()
QVb2 = QVBoxLayout()
QVb3 = QVBoxLayout()
QVb4 = QVBoxLayout()
QVb5 = QVBoxLayout()
QVb6 = QVBoxLayout()

button = QPushButton("Відповісти")
button.setFixedSize(300, 30)
button2 = QPushButton("Меню")
button3 = QPushButton("Відпочити")

RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()
AnsGroupBox = QGroupBox("Результат теста")

rbtn_1 = QRadioButton(wrong_answer1)
rbtn_2 = QRadioButton(answer)
rbtn_3 = QRadioButton(wrong_answer2)
rbtn_4 = QRadioButton(wrong_answer3)

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

spinbox = QSpinBox()
RadioGroupBox.setFixedHeight(265)
AnsGroupBox.setFixedHeight(265)
spinbox.setFixedWidth(35) 
label = QLabel("хвилин")
lb_Result = QLabel('')
ques = QLabel(question)
abc = QLabel('')
ab = QLabel('')
right_answer = QLabel('')

QHb4.addWidget(button2, alignment=Qt.AlignTop | Qt.AlignLeft)
QHb4.addWidget(ab, alignment=Qt.AlignTop | Qt.AlignRight)
QHb4.addWidget(button3, alignment=Qt.AlignTop | Qt.AlignRight)
QHb4.addWidget(spinbox)
QHb4.addWidget(label)

QVb2.addWidget(abc)
QVb6.addWidget(lb_Result)
QVb6.addWidget(right_answer, alignment=Qt.AlignTop | Qt.AlignCenter)
QHb1.addWidget(rbtn_1)
QHb1.addWidget(rbtn_2)
QHb2.addWidget(rbtn_3)
QHb2.addWidget(rbtn_4)

QHb3.addWidget(ques, alignment=Qt.AlignCenter)

QVb2.addWidget(button, alignment=Qt.AlignTop | Qt.AlignCenter)

QHb4.addLayout(QVb5)
QHb4.addLayout(QVb4)
QVb3.addLayout(QHb4)
QVb3.addLayout(QHb3)
QVb1.addLayout(QHb1)
QVb1.addLayout(QHb2)
QVb3.addWidget(RadioGroupBox)
QVb3.addWidget(AnsGroupBox)
QVb3.addLayout(QVb2)

AnsGroupBox.setLayout(QVb6)
RadioGroupBox.setLayout(QVb1)

AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText("Наступне питання")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText("Відповісти")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def sleep_card():
    pass

def show_card():
    pass


# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.


