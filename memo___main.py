from memo___card_layout import *
from memo_edit_layout import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer


from memo_data import *

card_width, card_height = 600, 500  # начальные размеры окна "карточка"
# начальные размеры окна "карточка"
card_width_menu, card_height_menu = 1000, 600

time_unit = 60000
timer = QTimer()

frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong_answer_1, txt_Wrong_answer_2, txt_Wrong_answer_3)


questions_listmodel = QuestionListModel()
radio_list = [Radio_btn_1, Radio_btn_2, Radio_btn_3, Radio_btn_4,]



def testlist():
    frm = Question('Яблоко', 'apple', 'application', 'pinapple', 'apply')
    questions_listmodel.form_list.append(frm)
    frm = Question('Дом', 'house', 'horse', 'hurry', 'hour')
    questions_listmodel.form_list.append(frm)
    frm = Question('Мышь', 'mouse', 'mouth', 'muse', 'museum')
    questions_listmodel.form_list.append(frm)
    frm = Question('Число', 'number', 'digit', 'amount', 'summary')
    questions_listmodel.form_list.append(frm)


def new_Question():
    global Q1View
    Q1View = random_AnswerCheck(questions_listmodel,question_text,radio_list,lb_Result,show_result,lb_Correct)

def click_OK():
    if next_btn.text() != 'Наступне питання!':
        Q1View.check_result()

    else:
        new_Question()
        show_question()


win_card = QWidget()
win_card.resize(card_width, card_height)

win_card.move(300, 300)
win_card.setWindowTitle("Memory Card")

next_btn.clicked.connect(click_OK)
win_card.setLayout(layout_card)


win_card_menu = QWidget()
win_card_menu.resize(card_width_menu, card_height_menu)

win_card_menu.move(300, 300)
win_card_menu.setWindowTitle("Memory Card")
win_card_menu.setLayout(main_layaut_menu)

def edit_question(index):
    ''' загружает в форму редактирования вопрос и ответы, соответствующие переданной строке '''
    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()



def del_form():
    ''' удаляет вопрос и переключает фокус '''
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())



def add_question():
    questions_listmodel.insertRows()
    last = questions_listmodel.rowCount(0) - 1
    index = questions_listmodel.index(last)
    list_questions.setCurrentIndex(index) 
    edit_question(index)
    txt_Question.setFocus(Qt.TabFocusReason)



def menu_show():
    win_card_menu.show()
    win_card.hide()


def start_test():
    win_card_menu.hide()
    win_card.show()
    new_Question()


def sleep_card():
    sleep_hide()
    SleepGroupBox.show()
    timer.start()
    timer.setInterval(box_Minutes.value() * time_unit)

def show_card():
    sleep_show()
    SleepGroupBox.hide()
    timer.stop()

timer.timeout.connect(show_card)
rest_btn.clicked.connect(sleep_card)
sleep_btn.clicked.connect(show_card)

testlist()
menu_btn.clicked.connect(menu_show)
btn_start.clicked.connect(start_test)
list_questions.setModel(questions_listmodel)


btn_del.clicked.connect(del_form)
btn_new.clicked.connect(add_question)
list_questions.clicked.connect(edit_question)

win_card_menu.show()
app.exec_()
