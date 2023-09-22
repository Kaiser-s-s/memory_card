
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QTableWidget, QListWidget, QListWidgetItem,
    QLineEdit, QFormLayout,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel, QSpinBox, QLineEdit, QFormLayout, QListView)
from memo___app import app

layout_form = QFormLayout()
list_questions = QListView()


txt_Question = QLineEdit("")
txt_Answer = QLineEdit("")
txt_Wrong_answer_1 = QLineEdit('')
txt_Wrong_answer_2 = QLineEdit('')
txt_Wrong_answer_3 = QLineEdit('')

layout_form.addRow('Питання', txt_Question)
layout_form.addRow('Правильна Відповідь', txt_Answer)
layout_form.addRow('Неправильна Відповідь 1', txt_Wrong_answer_1)
layout_form.addRow('Неправильна Відповідь 2', txt_Wrong_answer_2)
layout_form.addRow('Неправильна Відповідь 3', txt_Wrong_answer_3)

btn_del = QPushButton("Видалити питання")
btn_new = QPushButton("Додати питання")
btn_start = QPushButton("Почати тестування")


main_layaut_menu = QVBoxLayout()
layout_H1 = QHBoxLayout()
layout_H2 = QHBoxLayout()
layout_H3 = QHBoxLayout()


layout_H1.addWidget(list_questions)

layout_H2.addWidget(btn_new, stretch=1)
layout_H2.addWidget(btn_del, stretch=1)

layout_H3.addStretch(1)
layout_H3.addWidget(btn_start, stretch=2)
layout_H3.addStretch(1)

layout_H1.addLayout(layout_form)
main_layaut_menu.addLayout(layout_H1)
main_layaut_menu.addLayout(layout_H2)
main_layaut_menu.addLayout(layout_H3)
