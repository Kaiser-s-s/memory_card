from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle

# такая строка будет устанавливаться по умолчанию для новых вопросов
new_quest_templ = 'Новый вопрос'
new_answer_templ = 'Новый ответ'  # то же для ответов

text_wrong = 'Неверно'
text_correct = 'Верно'


class Question():
    ''' хранит информацию про один вопрос'''

    def __init__(self, question=new_quest_templ, answer=new_answer_templ,
                 wrong_answer1='', wrong_answer2='', wrong_answer3=''):
        self.question = question  # вопрос
        self.answer = answer  # правильный ответ
        # считаем, что всегда пишется три неверных варианта
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.is_active = True  # продолжать ли задавать этот вопрос?
        self.attempts = 0  # сколько раз этот вопрос задавался
        self.correct = 0  # количество верных ответов

    def got_right(self):
        ''' меняет статистику, получив правильный ответ'''
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        ''' меняет статистику, получив неверный ответ'''
        self.attempts += 1


class QuestionView():
    ''' сопоставляет данные и виджеты для отображения вопроса'''

    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # конструктор получает и запоминает объект с данными и виджеты, соответствующие полям анкеты
        self.frm_model = frm_model  # может получить и None - ничего страшного не случится,
        # но для метода show нужно будет предварительно обновить данные методом change
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

    def change(self, frm_model):
        ''' обновление данных, уже связанных с интерфейсом '''
        self.frm_model = frm_model

    def show(self):
        ''' выводит на экран все данные из объекта '''
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)


class QuestionEdit(QuestionView):
    def save_question(self):
        ''' сохраняет текст вопроса '''
        self.frm_model.question = self.question.text()  # копируем данные из виджета в объект

    def save_answer(self):
        self.frm_model.answer = self.answer.text()

    def save_wrong_answer(self):
        self.frm_model.wrong_answer1 = self.wrong_answer1.text()
        self.frm_model.wrong_answer2 = self.wrong_answer2.text()
        self.frm_model.wrong_answer3 = self.wrong_answer3.text()

    def set_content(self):
        self.question.editingFinished.connect(self.save_question)
        self.answer.editingFinished.connect(self.save_answer)
        self.wrong_answer1.editingFinished.connect(self.save_wrong_answer)
        self.wrong_answer2.editingFinished.connect(self.save_wrong_answer)
        self.wrong_answer3.editingFinished.connect(self.save_wrong_answer)

    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        super().__init__(frm_model, question, answer,
                         wrong_answer1, wrong_answer2, wrong_answer3)
        self.set_content()


class AnswerCheck(QuestionView):
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, lb_Result, final_func, lb_Correct):
        super().__init__(frm_model, question, answer,
                         wrong_answer1, wrong_answer2, wrong_answer3)
        self.lb_Result = lb_Result
        self.final_func = final_func
        self.text_wrong = 'Неправильно'
        self.text_correct = 'Правильно'
        self.lb_Correct = lb_Correct

    def check_result(self):
        self.lb_Correct.setText(self.frm_model.answer)
        if self.answer.isChecked():
            self.lb_Result.setText(text_correct)
            self.final_func()
        else:
            if self.wrong_answer1.isChecked() or self.wrong_answer2.isChecked() or self.wrong_answer3.isChecked():
                self.lb_Result.setText(text_wrong)
                self.final_func()


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
        self.form_list.append(Question())
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


def random_AnswerCheck(list_model, w_question, widgets_list, w_result, w_final_func, w_showed_answer):
    frm = list_model.random_question()
    shuffle(widgets_list)
    frm_model = AnswerCheck(frm, w_question, widgets_list[0], widgets_list[1],
                            widgets_list[2], widgets_list[3], w_result, w_final_func, w_showed_answer)
    frm_model.show()
    return frm_model
