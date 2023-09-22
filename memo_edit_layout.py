from PyQt5.QtWidgets import QLineEdit, QFormLayout, QListView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 

layout_form = QFormLayout()
list_view = QListView()
txt_answer1 = QLineEdit('')
txt_answer2 = QLineEdit('')
txt_answer3 = QLineEdit('')
txt_answer4 = QLineEdit('')
txt_answer5 = QLineEdit('')
layout_form.addRow("Питання:", txt_answer1)
layout_form.addRow("Правильна відповідь:", txt_answer2)
layout_form.addRow("Неправильний варіант №1:", txt_answer3)
layout_form.addRow("Неправильний варіант №2:", txt_answer4)
layout_form.addRow("Неправильний варіант №3:", txt_answer5)

list_questions = [txt_answer1, txt_answer2, txt_answer3, txt_answer4, txt_answer5]

but1 = QPushButton("Нове питання")
but2 = QPushButton("Видалити питання")
but3 = QPushButton("Почати тренування")

but3.setFixedWidth(450)
list_view.setFixedWidth(375)

QVb1 = QVBoxLayout()
QHb1 = QHBoxLayout()
QHb2 = QHBoxLayout()
QHb3 = QHBoxLayout()

QVb1.addLayout(QHb3)
QVb1.addLayout(QHb1)
QVb1.addLayout(QHb2)

QHb3.addWidget(list_view, alignment=Qt.AlignLeft)
QHb3.addLayout(layout_form)
QHb1.addWidget(but1)
QHb1.addWidget(but2)
QHb2.addWidget(but3)


