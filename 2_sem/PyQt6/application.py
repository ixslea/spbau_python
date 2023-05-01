"""
PyQT6 application with my university assignment about analyzing the work time of different algorithms for harmonic numbers calculation
"""

import sys, os
from random import randint
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import *
import PyQt6.QtCore
from PyQt6 import QtGui

"""For pyinstaller to load images"""
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

img_dir = os.path.join(os.path.dirname(__file__), "img")
img_dir = resource_path("img")


class PopWindows(QWidget):

    """
    Class of some pop windows that you will see on the starting of program. Just enjoy!
    """

    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(PyQt6.QtCore.Qt.WindowType.FramelessWindowHint)
        self.setGeometry(randint(0, 1400), randint(0, 600), 300, 240)

        self.label = QLabel(self)
        self.label.setObjectName("label")

        self.movie = QMovie("img/full.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        PyQt6.QtCore.QTimer.singleShot(9500, self.hide)


    
class MainWindow(QMainWindow):

    """
    Main window's class. First window you will see.
    One button, calling for 25 pop windows. 
    """

    def __init__(self):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon('img/lol.jpg'))
        self.setWindowTitle("мяу!")

        self.PopWindowsAmount = 25
        self.PopWinds = []
        for i in range(self.PopWindowsAmount):
            self.PopWinds.append(PopWindows())

        self.next = None

        l = QVBoxLayout()
        self.button = QPushButton("Нажми меня!")
        self.button.clicked.connect(self.CallingPopWindows)
        l.addWidget(self.button)
        self.setCentralWidget(self.button)
        

    def CallingPopWindows(self, checked):
        for window in self.PopWinds:
            window.show()

        self.next = ScreenProject()

        PyQt6.QtCore.QTimer.singleShot(0, self.hide)
        PyQt6.QtCore.QTimer.singleShot(9500, self.next.show)

"""
Some classes for the assingment part.
"""

class OnlyPython(QWidget):

    """
    Class of one stacked window about analyzing the work time of different algorithms for harmonic numbers calculation on Python
    """

    def __init__(self, parent=None):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon('img/lol.jpg'))

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        self.About = QLabel()
        self.About.setText("<h1>Будем исследовать два алгоритма (рекурсивный и линейный) подсчёта гармонических чисел.</h1> Построим для каждого алгоритма график, показывающий время работы в наносекундах каждого из них для подсчёта первых 20 гармонических чисел.")        
        self.About.setStyleSheet("""font: bold;""")
        self.AboutAddition = QLabel()
        self.AboutAddition.setText("Также построим третий график, который будет нам демонстрировать минимальное время из работы двух алгоритмов для каждого из 20 чисел соответственно.")
        self.AboutAddition.setStyleSheet("""font: bold;""")

        self.MovieLabel = QLabel(self)
        self.MovieLabel.setGeometry(PyQt6.QtCore.QRect(0, 0, 800, 343))
        self.movie = QMovie("img/OnlyPython.gif")
        self.MovieLabel.setMovie(self.movie)
        self.movie.start()

        self.AboutCode = QLabel()
        self.AboutCode.setOpenExternalLinks(True)
        self.AboutCode.setText("<a href=\"https://github.com/ixslea/spbau_python/blob/main/2_sem/find_out.ipynb\"> Исходный код с алгоритмами и специальным таймером посмотрите по ссылке на JupiterNotebook</a>")
        self.AboutCode.setStyleSheet("""font: bold;""")
        
        self.Result = QLabel()
        self.Result.setText("Можно заметить, что рекурсивный алгоритм справляется быстрее при вычислении нескольких первых гармонических чисел. \n Минимальное время работы колеблется в пределах 1000-3000 и больше нс")
        self.Result.setStyleSheet("""font-style: italic;""")

        formLayout.addRow(self.About)
        formLayout.addRow(self.AboutAddition)
        formLayout.addRow(self.MovieLabel)
        formLayout.addRow(self.AboutCode)
        formLayout.addRow(self.Result)
        groupBox.setLayout(formLayout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

class addMyPy(QWidget):
    
    """
    Class of one stacked window about analyzing the work time of different algorithms for harmonic numbers calculation on Python with MyPy
    """

    def __init__(self, parent=None):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon('img/lol.jpg'))
        
        formLayout = QFormLayout()
        groupBox = QGroupBox()

        self.MovieLabel = QLabel(self)
        self.MovieLabel.setGeometry(PyQt6.QtCore.QRect(0, 0, 800, 343))
        self.movie = QMovie("img/withMyPy.gif")
        self.MovieLabel.setMovie(self.movie)
        self.movie.start()

        self.About = QLabel()
        self.About.setText("<h1> Будем исследовать два алгоритма (рекурсивный и линейный) подсчёта гармонических чисел.</h1> Построим для каждого алгоритма график, показывающий время работы в наносекундах каждого из них для подсчёта первых 20 гармонических чисел. ")
        self.About.setStyleSheet("""font: bold;""")
        self.AboutAddition = QLabel()
        self.AboutAddition.setText("Также построим третий график, который будет нам демонстрировать минимальное время из работы двух алгоритмов для каждого из 20 чисел соответственно.")
        self.AboutAddition.setStyleSheet("""font: bold;""")

        self.Label = QLabel()
        self.Label.setText("<h1>Воспользуемся MyPy...</h1>")
        self.Label.setStyleSheet("""font: italic;""")

        self.AboutCode = QLabel()
        self.AboutCode.setOpenExternalLinks(True)
        self.AboutCode.setText("<a href=\"https://github.com/ixslea/spbau_python/blob/main/2_sem/find_out.ipynb\"> Исходный код с алгоритмами и специальным таймером посмотрите по ссылке на JupiterNotebook</a>")
        self.AboutCode.setStyleSheet("""font: bold;""")

        self.Result = QLabel()
        self.Result.setText("<h1> И вот! MyPy ускоряет работу наших алгоритмов!</h1> Также рекурсивный алгоритм справляется быстрее при вычислении нескольких первых гармонических чисел. \nМинимальное время работы колеблется в пределах 750-2500 нс")
        self.Result.setStyleSheet("""font: italic;""")
        
        formLayout.addRow(self.About)
        formLayout.addRow(self.AboutAddition)
        formLayout.addRow(self.Label)
        formLayout.addRow(self.MovieLabel)
        formLayout.addRow(self.AboutCode)
        formLayout.addRow(self.Result)
        groupBox.setLayout(formLayout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

class addCython(QWidget):

    """
    Class of one stacked window about analyzing the work time of different algorithms for harmonic numbers calculation on Python with Cython
    """

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('img/lol.jpg'))

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        self.About = QLabel()
        self.About.setText("<h1>Будем исследовать два алгоритма (рекурсивный и линейный) подсчёта гармонических чисел.</h1> Построим для каждого алгоритма график, показывающий время работы в наносекундах каждого из них для подсчёта первых 20 гармонических чисел. ")
        self.About.setStyleSheet("""font: bold;""")
        self.AboutAddition = QLabel()
        self.AboutAddition.setText("Также построим третий график, который будет нам демонстрировать минимальное время из работы двух алгоритмов для каждого из 20 чисел соответственно.")
        self.AboutAddition.setStyleSheet("""font: bold;""")

        self.MovieLabel = QLabel(self)
        self.MovieLabel.setGeometry(PyQt6.QtCore.QRect(0, 0, 800, 343))
        self.movie = QMovie("img/withCython.gif")
        self.MovieLabel.setMovie(self.movie)
        self.movie.start()

        self.AboutCode = QLabel()
        self.AboutCode.setOpenExternalLinks(True)
        self.AboutCode.setText("<a href=\"https://github.com/ixslea/spbau_python/blob/main/2_sem/find_out.ipynb\"> Исходный код с алгоритмами и специальным таймером посмотрите по ссылке на JupiterNotebook</a>")
        self.AboutCode.setStyleSheet("""font: bold;""")

        self.Label = QLabel()
        self.Label.setText("<h1>Пришёл черёд Cython! Погрузимся в исследование:</h1>")
        self.Label.setStyleSheet("""font: italic;""")

        self.Result = QLabel()
        self.Result.setText("<h1> А вот и результаты! Cython немного уступает MyPy, но иногда быстрее Python'a</h1> Удивительно, но теперь рекурсивный алгоритм справляется в некоторых случаях быстрее, чем линейный! \nМинимальное время работы колеблется в пределах 750-3000 нс.")
        self.Result.setStyleSheet("""font-style: italic;""")

        formLayout.addRow(self.About)
        formLayout.addRow(self.AboutAddition)
        formLayout.addRow(self.Label)
        formLayout.addRow(self.MovieLabel)
        formLayout.addRow(self.AboutCode)
        formLayout.addRow(self.Result)
        groupBox.setLayout(formLayout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

class addNumba(QWidget):

    """
    Class of one stacked window about analyzing the work time of different algorithms for harmonic numbers calculation on Python with Numba
    """

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('img/lol.jpg'))

        formLayout = QFormLayout()
        groupBox = QGroupBox()

        self.About = QLabel()
        self.About.setText("<h1>Будем исследовать два алгоритма (рекурсивный и линейный) подсчёта гармонических чисел.</h1> Построим для каждого алгоритма график, показывающий время работы в наносекундах каждого из них для подсчёта первых 20 гармонических чисел. ")
        self.About.setStyleSheet("""font: bold;""")
        self.AboutAddition = QLabel()
        self.AboutAddition.setText("Также построим третий график, который будет нам демонстрировать минимальное время из работы двух алгоритмов для каждого из 20 чисел соответственно.")
        self.AboutAddition.setStyleSheet("""font: bold;""")

        self.MovieLabel = QLabel(self)
        self.MovieLabel.setGeometry(PyQt6.QtCore.QRect(0, 0, 800, 343))
        self.movie = QMovie("img/withNumba.gif")
        self.MovieLabel.setMovie(self.movie)
        self.movie.start()

        self.Label = QLabel()
        self.Label.setText("<h1>Проверим теперь, как работает Numba:</h1>")
        self.Label.setStyleSheet("""font: italic;""")
        
        self.AboutCode = QLabel()
        self.AboutCode.setOpenExternalLinks(True)
        self.AboutCode.setText("<a href=\"https://github.com/ixslea/spbau_python/blob/main/2_sem/find_out.ipynb\"> Исходный код с алгоритмами и специальным таймером посмотрите по ссылке на JupiterNotebook</a>")
        self.AboutCode.setStyleSheet("""font: bold;""")

        self.Result = QLabel()
        self.Result.setText("<h1>Итак, в нашем случае Numba вроде бы справляется хуже своих конкурентов.... 🤯</h1>") 
        self.Result.setStyleSheet("""font: italic;""")
        self.AboutResult = QLabel()
        self.AboutResult.setText("Перечислим несколько полученных выводов: \n    Вычисление первого числа занимает самое большое количество времени, а остальных - гораздо меньше. \n    Рекурсивный алгоритм быстрее в некоторых отдельных точках. \n    Минимальное время работы достигает 2-3 * 1е8 нс \nНемного изучим первый вывод: \n    не будем выводить на третьем графике время вычисления первого числа.\n \n За какое же время вычисляются остальные числа?")
        self.AboutResult.setStyleSheet("""font: italic;""")

        self.SecondMovieLabel = QLabel(self)
        self.SecondMovieLabel.setGeometry(PyQt6.QtCore.QRect(0, 0, 800, 343))
        self.Secondmovie = QMovie("img/withNumbaTwo.gif")
        self.SecondMovieLabel.setMovie(self.Secondmovie)
        self.Secondmovie.start()

        self.SecondResult = QLabel()
        self.SecondResult.setText("<h1>О, чудо! Оказывается Numba справляется быстрее MyPy!</h1> При вычислении чисел (кроме первого) минимальное время колеблется в пределах 600-1000 нс!")
        self.SecondResult.setStyleSheet("""font: italic;""")

        formLayout.addRow(self.About)
        formLayout.addRow(self.AboutAddition)
        formLayout.addRow(self.Label)
        formLayout.addRow(self.MovieLabel)
        formLayout.addRow(self.AboutCode)
        formLayout.addRow(self.Result)
        formLayout.addRow(self.AboutResult)
        formLayout.addRow(self.SecondMovieLabel)
        formLayout.addRow(self.AboutCode)
        formLayout.addRow(self.SecondResult)
        groupBox.setLayout(formLayout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)



class ScreenProject(QWidget):

    """
    Main class for all previous stacked windows
    """

    def __init__(self, parent=None):
        super(ScreenProject, self).__init__(parent)

        self.setWindowIcon(QtGui.QIcon('img/lol.jpg'))

        self.setWindowTitle("Воспроизведение замеров с помощью MyPy, Cython, Numba при подсчёте гармонических чисел")
        self.resize(1200, 600)

        self.btnPress1 = QPushButton("База: только Python")
        self.btnPress2 = QPushButton("С MyPy")
        self.btnPress3 = QPushButton("С Cython")
        self.btnPress4 = QPushButton("С Numba")

        self.chapter1 = OnlyPython()
        self.chapter2 = addMyPy()
        self.chapter3 = addCython()
        self.chapter4 = addNumba()


        widget = QWidget()
        self.stacked_layout = QStackedLayout()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:white;")
        self.stacked_layout.addWidget(self.chapter1)
        self.stacked_layout.addWidget(self.chapter2)
        self.stacked_layout.addWidget(self.chapter3)
        self.stacked_layout.addWidget(self.chapter4)

        layout = QVBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        layout.addWidget(self.btnPress3)
        layout.addWidget(self.btnPress4)

        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnPress3.clicked.connect(self.btnPress3_Clicked)
        self.btnPress4.clicked.connect(self.btnPress4_Clicked)


    def btnPress1_Clicked(self):
        self.stacked_layout.setCurrentIndex(0)

    def btnPress2_Clicked(self):
        self.stacked_layout.setCurrentIndex(1)
    
    def btnPress3_Clicked(self):
        self.stacked_layout.setCurrentIndex(2)

    def btnPress4_Clicked(self):
        self.stacked_layout.setCurrentIndex(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    app.exec()

