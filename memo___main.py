from memo___card_layout import *
from memo_data import *
from memo_edit_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # будем перемешивать ответы в карточке вопроса

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


card_width, card_height = 600, 500 # начальные размеры окна "карточка"


questions_listmodel = QuestionListModel()

frm = Form('Яблуко', 'apple', 'caterpillar', 'application', 'building')
questions_listmodel.form_list.append(frm)
frm = Form('Будинок', 'house', 'horse', 'harry', 'hour')
questions_listmodel.form_list.append(frm)
frm = Form('Миша', 'mouse', 'mouth', 'mase', 'museum')
questions_listmodel.form_list.append(frm)
frm = Form('Число', 'number', 'digit', 'amount', 'summary')
questions_listmodel.form_list.append(frm)

def add_question():
    questions_listmodel.insertRows()
    last = questions_listmodel.rowCount(0) - 1
    index = questions_listmodel.index(last)
    list_questions.setCurrentIndex(index)
    edit_question(index)
    txt_answer1.setFocus(Qt.TabFocusReason)
    
def edit_question(index):
    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        list_questions.change(frm)
        list_questions.show()
        
def del_question():
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())



def show_random(questions_listmodel, question, radio_list, correct, lb_Result):
    global frm_card
    frm_card = random_AnswerCheck(questions_listmodel, question, radio_list, correct, lb_Result)
    
    frm_card.show()
    show_question()
    
text_correct = 'Правильно'
text_wrong = 'Неправильно'
def check_result():
    global text_correct, text_wrong 
    correct = rbtn_2.isChecked()
    if correct:
        lb_Result.setText(text_correct)
        show_result()
    else:
        incorrect = rbtn_1.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked()
        if incorrect:
            lb_Result.setText(text_wrong)
            right_answer.setText(answer)
            show_result()


def check():
    if button.text() != 'Наступне питання': 
        check_result()
    elif button.text() == 'Наступне питання':
        show_question()
button.clicked.connect(check)

def abc():
    card.hide()
    win_card.show()

but3.clicked.connect(abc)

def ab():
    card.show()
    win_card.hide()

button2.clicked.connect(ab)

card = QWidget()
card.setWindowTitle('Список питань')
card.resize(800, 500)
card.setLayout(QVb1)
card.show()

win_card = QWidget()
win_card.setWindowTitle("Memory Card")
win_card.resize(card_width, card_height)
win_card.setLayout(QVb3)
win_card.hide()
app.exec_()

#здесь должны быть параметры окна