from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle
from memo___card_layout import *
from memo_edit_layout import *
class Form():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
class FormView():
    def __init__(self, frm_model, question, answer, wrong_answer1 = '', wrong_answer2 = '', wrong_answer3 = ''):
        self.frm_model = frm_model
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
    def show(self):
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)
class QuestionListModel(QAbstractListModel):
    ''' в данных находится список объектов типа Question, 
    а также список активных вопросов, чтобы показывать его на экране '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_list = []
    def rowCount(self, index):
        ''' число элементов для показа: обязательный метод для модели, с которой будет связан виджет "список"'''
        return len(self.form_list)
    def data(self, index, role):
        ''' обязательный метод для модели: какие данные она дает по запросу от интерфейса'''
        if role == Qt.DisplayRole:
            form = self.form_list[index.row()]
            return form.question
    def insertRows(self, parent=QModelIndex()):
        ''' этот метод вызывается, чтобы вставить в список объектов новые данные;
        генерируется и вставляется один пустой вопрос.'''
        position = len(self.form_list) 
        self.beginInsertRows(parent, position, position) 
        self.form_list.append(question())
        self.endInsertRows()
        QModelIndex()
        return True 
    def removeRows(self, position, parent=QModelIndex()):
        ''' стандартный метод для удаления строк - после удаления из модели строка автоматически удаляется с экрана'''
        self.beginRemoveRows(parent, position, position) 
        self.form_list.pop(position) 
        self.endRemoveRows() 
        return True 
    def random_question(self):
        ''' Выдаёт случайный вопрос '''
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]
class AnswerCheck(FormView):
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, lb_Result, correct, showw):
        super.__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.lb_Result = lb_Result
        self.showw = showw
        self.text_correct = 'Правильно'
        self.text_wrong = 'Неправильно'
        self.correct = correct
    def check_result(self):
        pass
        

def random_AnswerCheck(frm, question, radio_list, correct, lb_Result):
    frm = list_questions.random_question()
    shuffle(radio_list)
    frm_card = AnswerCheck(frm, question, radio_list[0], radio_list[1], radio_list[2], radio_list[3], correct, lb_Result)
    return frm_card

