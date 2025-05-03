from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QButtonGroup, QApplication, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QMessageBox
from random import shuffle, randint

app = QApplication([])
win = QWidget()
# счетчики
win.score = 0
win.total = 0

# класс хранилище
class Quesion():
    def __init__(self, vopros, yes_otvet, no_1, no_2, no_3):
        self.vopros = vopros
        self.yes_otvet = yes_otvet
        self.no_1 = no_1
        self.no_2 = no_2
        self.no_3 = no_3
# функции
def show_result():
    group1.hide()
    group2.show()
    otvet.setText('Следующий вопрос')
def show_quesion():
    group2.hide()
    group1.show()
    otvet.setText('Ответить')
    RadioButton.setExclusive(False)
    otvet_1.setChecked(False)
    otvet_2.setChecked(False)
    otvet_3.setChecked(False)
    otvet_4.setChecked(False)
    RadioButton.setExclusive(True)
def test():
    if 'Ответить' == otvet.text():
        check_answer()
    else:
        next_quesion()
def ask(q):
    shuffle(r_button)
    r_button[0].setText(q.yes_otvet)
    r_button[1].setText(q.no_1)
    r_button[2].setText(q.no_2)
    r_button[3].setText(q.no_3)
    vopros1.setText(q.vopros)
    otvet_main.setText(q.yes_otvet)
    show_quesion()
def check_answer():
    if r_button[0].isChecked():
        show_correct('Правильно')
        win.score += 1
    else:
        show_correct('Неправильно')
def show_correct(res):
    result.setText(res)
    show_result()
def next_quesion():
    cur_quesion = randint(0, len(spisok_vopr)- 1)
    voprosik = spisok_vopr[cur_quesion]
    win.total += 1
    ask(voprosik)
    print(f'Статистика\n-Всего вопросов - {win.total}\n-Всего правильных ответов {win.score}\n-Рейтинг {win.score / win.total * 100}')
# кнопки
RadioButton = QButtonGroup()
otvet_1 =QRadioButton('1613')
otvet_2 =QRadioButton('1609')
otvet_3 =QRadioButton('1611')
otvet_4 =QRadioButton('1598')
RadioButton.addButton(otvet_1)
RadioButton.addButton(otvet_2)
RadioButton.addButton(otvet_3)
RadioButton.addButton(otvet_4)

# список кнопок
r_button =[otvet_1, otvet_2, otvet_3, otvet_4]

# линии
main_Vline = QVBoxLayout()
Hline_1 = QHBoxLayout()
Hline_2 = QHBoxLayout()
Hline_3 = QHBoxLayout()
Vline_1 = QVBoxLayout()
Vline_2 = QVBoxLayout()
Vline_2group = QVBoxLayout()

vopros1 = QLabel('В каком году начала править династия рамановых?')
otvet = QPushButton('Ответить')

result = QLabel('ес/ноу')
otvet_main = QLabel('правильно')

group1 = QGroupBox('Варианты ответов')
group2 = QGroupBox('Результаты теста')

Vline_1.addWidget(otvet_1)
Vline_1.addWidget(otvet_3)
Vline_2.addWidget(otvet_4)
Vline_2.addWidget(otvet_2)
Vline_2group.addWidget(result, alignment= Qt.AlignTop | Qt.AlignLeft)
Vline_2group.addWidget(otvet_main, alignment= Qt.AlignCenter)

Hline_2.addLayout(Vline_1)
Hline_2.addLayout(Vline_2)

group1.setLayout(Hline_2)
group2.setLayout(Vline_2group)

Hline_1.addWidget(vopros1)

Hline_3.addStretch(1)
Hline_3.addWidget(otvet, stretch = 3)
Hline_3.addStretch(1)

main_Vline.addLayout(Hline_1)
main_Vline.addLayout(Hline_2)
main_Vline.addWidget(group1)
main_Vline.addWidget(group2)
main_Vline.addLayout(Hline_3)

group2.hide()

# список
spisok_vopr = []
spisok_vopr.append(Quesion('В каком году начала править династия рамановых?', '1613', '1609', '1611', '1698'))
spisok_vopr.append(Quesion('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
spisok_vopr.append(Quesion('какой язык главный в python?', 'Английский', 'Китайский', 'Итальянский', 'Русский'))
# запуск функций
otvet.clicked.connect(test)
answer = Quesion('В каком году начала править династия рамановых?', '1613', '1609', '1611', '1698')
win.setLayout(main_Vline)

win.show()
app.exec_()