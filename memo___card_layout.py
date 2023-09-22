''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QTableWidget, QListWidget, QListWidgetItem,
    QLineEdit, QFormLayout,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel, QSpinBox)
from memo___app import app

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно
menu_btn = QPushButton("Меню")

# кнопка прибирає вікно і повертає його після закінчення таймера
rest_btn = QPushButton("Відпочити")
# введення кількості хвилин
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
min_text = QLabel('хвилин')
# кнопка відповіді "Ок" / "Наступний"
next_btn = QPushButton("Відповісти")
# текст питання
question_text = QLabel("sadasd")
# Опиши групу перемикачів
Group_Btn_Box = QGroupBox("Відповіді на питання")
Group_Radio_Btn = QButtonGroup()

Radio_btn_1 = QRadioButton("")
Radio_btn_2 = QRadioButton("")
Radio_btn_3 = QRadioButton("")
Radio_btn_4 = QRadioButton("")

Group_Radio_Btn.addButton(Radio_btn_1)
Group_Radio_Btn.addButton(Radio_btn_2)
Group_Radio_Btn.addButton(Radio_btn_3)
Group_Radio_Btn.addButton(Radio_btn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(Radio_btn_1)
layout_ans2.addWidget(Radio_btn_3)

layout_ans3.addWidget(Radio_btn_2)
layout_ans3.addWidget(Radio_btn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

Group_Btn_Box.setLayout(layout_ans1)
# Опиши панень з результатами
AnsGroupBox = QGroupBox("Результат теста")
# Напис "правильно"/"неправильно"
lb_Result = QLabel('asd')
lb_Correct = QLabel('asdds')  # Текст правильної відповіді

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
SleepGroupBox = QGroupBox("")
sleep_Lb = QLabel("ПЕРЕРЫВ!!!")
sleep_btn = QPushButton("Возобновить тест")

sleep_layout = QVBoxLayout()
sleep_layout.addWidget(sleep_Lb, alignment= Qt.AlignCenter)
sleep_layout.addWidget(sleep_btn)
SleepGroupBox.setLayout(sleep_layout)
SleepGroupBox.hide()



layout_card = QVBoxLayout()

layout_main_1 = QHBoxLayout()
layout_main_2 = QHBoxLayout()
layout_main_3 = QHBoxLayout()
layout_main_4 = QHBoxLayout()

layout_main_1.addWidget(menu_btn)
layout_main_1.addStretch(1)
layout_main_1.addWidget(rest_btn)
layout_main_1.addWidget(box_Minutes)
layout_main_1.addWidget(min_text)


layout_main_2.addWidget(question_text, alignment=Qt.AlignCenter)

layout_main_3.addWidget(Group_Btn_Box)
layout_main_3.addWidget(AnsGroupBox)
layout_main_3.addWidget(SleepGroupBox)

layout_main_4.addStretch(1)
layout_main_4.addWidget(next_btn, stretch=2)
layout_main_4.addStretch(1)


layout_card.addLayout(layout_main_1, stretch=1)
layout_card.addLayout(layout_main_2, stretch=2)
layout_card.addLayout(layout_main_3, stretch=8)
layout_card.addLayout(layout_main_4, stretch=1)
# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.


def show_result():
    ''' показати панель відповідей '''
    Group_Btn_Box.hide()
    AnsGroupBox.show()
    next_btn.setText("Наступне питання!")


def show_question():
    ''' показати панель запитань '''
    AnsGroupBox.hide()
    Group_Btn_Box.show()

    next_btn.setText("Відповісти")

    Group_Radio_Btn.setExclusive(False)
    Radio_btn_1.setChecked(False)
    Radio_btn_2.setChecked(False)
    Radio_btn_3.setChecked(False)
    Radio_btn_4.setChecked(False)
    Group_Radio_Btn.setExclusive(True)

def sleep_hide():
    menu_btn.hide()
    rest_btn.hide()
    box_Minutes.hide()
    next_btn.hide()
    question_text.hide()
    Group_Btn_Box.hide()
    AnsGroupBox.hide()
    min_text.hide()


def sleep_show():
    menu_btn.show()
    rest_btn.show()
    box_Minutes.show()
    next_btn.show()
    question_text.show()
    min_text.show()
    if next_btn.text() != 'Наступне питання!':
        Group_Btn_Box.show()
    elif next_btn.text() == 'Наступне питання!':
        AnsGroupBox.show()


    
    