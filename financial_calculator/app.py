import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QGridLayout,
    QWidget,
    QSizePolicy,
)

from controller import get_answer


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Financial Calculator")

        layout = QGridLayout()
        widgets = [
            QComboBox,
            QDoubleSpinBox,
            QLabel,
            QLineEdit,
            QPushButton,
            QSpinBox,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setStyleSheet = ("QWidget {linearGrad = QLinearGradient(QPointF(100, 100), QPointF(200, 200))linearGrad.setColorAt(0, Qt.black)linearGrad.setColorAt(1, Qt.white))}")
        widget.setLayout(layout)

        # Appsize
        self.setCentralWidget(widget)
        self.setFixedSize(400,300)

        # Title of the calculator
        title_label = QLabel("Financial Calculator")
        title_label.setStyleSheet(" QLabel{ font-size: 15px; }")
        layout.addWidget(title_label, 0,5)
        
        Frequency_combobox = QComboBox()
        layout.addWidget(Frequency_combobox, 2,1)
        Frequency_combobox.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        Frequency_combobox.addItem("Select ")
        Frequency_combobox.addItem("Monthly")
        Frequency_combobox.addItem("Annually")
        Frequency_combobox.addItem("Semi-Anually")
        Frequency_combobox.addItem("Quarterly")


        principle_label = QLabel("Starting Value:")
        layout.addWidget(principle_label, 1,0)

        frequency_label = QLabel("Frequency:")
        layout.addWidget(frequency_label, 2,0)

        #Percentage input
        percentage_label = QLabel("Percentage: ")
        layout.addWidget(percentage_label, 3,0 )

        duration_label = QLabel("Duration:")
        layout.addWidget(duration_label, 4,0)
        
        end_label = QLabel("Output:")
        layout.addWidget(end_label, 3,4)

        self.principle_input = QSpinBox()
        layout.addWidget(self.principle_input, 1,1)
        self.principle_input.setSuffix("$")
        self.principle_input.setMaximum(2147483647)

        self.percentage_input = QSpinBox()
        self.percentage_input.setSuffix("%")
        self.percentage_input.setMaximum(100)
        self.percentage_input.setMinimum(-100)
        layout.addWidget(self.percentage_input, 3,1)
        self.percentage_input.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        
        space1 = QWidget()
        layout.addWidget(space1, 0,0)

        space2 = QWidget()
        layout.addWidget(space2, 5,0)

        push_calculate = QPushButton()
        layout.addWidget(push_calculate, 5,0)
        push_calculate.setText("CALCULATE")
        push_calculate.setStyleSheet("  QPushButton:hover{color: #0000FF; font-size: 14px;}")

        push_reset = QPushButton("CLEAR")
        push_reset.setStyleSheet(" QPushButton:hover{color: #FF2D00; font-size: 14px;}")

        layout.addWidget(push_reset, 5, 1)

        self.duration_input = QSpinBox()
        layout.addWidget(self.duration_input, 4,1)

        output_answer = QLabel("")
        layout.addWidget(output_answer, 3,5)
        output_answer.setStyleSheet(" QLabel{background-color: white; font-color: black;}")

       
        
        #Formula and calculations
        def calculate_financial():
            """Calculate Financial"""
            principle = self.principle_input.value()
            print(principle)

            percentage = self.percentage_input.value()
            print(percentage)

            duration = self.duration_input.value()
            print(duration)

            compound = Frequency_combobox.currentText()

            if compound == "Monthly":
                
            elif compound == "Semi-Annually":
                compound = 2

            elif compound == "Quarterly":

            elif compound == "Annually":
            


            output_answer.setText(get_answer(principle, percentage, duration, compound))


        
        push_calculate.clicked.connect(calculate_financial)
        layout.addWidget(output_answer, 3,5)
        output_answer.setStyleSheet(" QLabel{background-color: white; font-color: black;}")


        push_calculate.clicked.connect(calculate_financial)

        



app = QApplication(sys.argv)
app.setStyleSheet("""

QWidget {
    background-color: black;
}


QComboBox {
    background-color:white;

}  

QLabel {
    color:white;
    font-size: 13px;
    float: right;
}
                  
QSpinBox {
    background-color: white;
}
                  
QLineEdit {
    background-color: white;
    font-size: 13px;
}
                  
QDoubleSpinBox {
    border-width: 10px;
    background-color: white;
}
                  
QPushButton {
    background-color:white;
    padding: 10px;
                  
}


QComboBox:items {
    background-color: rgb(255,255,255);
}
                  

QListView {
    color: rgb(255,255,255);
}
                  


                  
                  """)
window = MainWindow()
window.show()

app.exec() 