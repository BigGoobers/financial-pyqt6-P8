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
        widget.setLayout(layout)

        # Appsize
        self.setCentralWidget(widget)
        self.setFixedSize(400,300)

        # Title of the calculator
        title_label = QLabel("Financial Calculator")
        layout.addWidget(title_label, 0,6)

        Frequency_combobox = QComboBox()
        layout.addWidget(Frequency_combobox, 2,1)
        Frequency_combobox.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
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

        principle_input = QSpinBox()
        layout.addWidget(principle_input, 1,1)
        principle_input.setSuffix("$")
        principle_input.setMaximum(2147483647)

        percentage_input = QSpinBox()
        percentage_input.setSuffix("%")
        percentage_input.setMaximum(100)
        percentage_input.setMinimum(-100)
        layout.addWidget(percentage_input, 3,1)
        percentage_input.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        
        space1 = QWidget()
        layout.addWidget(space1, 0,0)

        space2 = QWidget()
        layout.addWidget(space2, 5,0)

        push_calculate = QPushButton()
        layout.addWidget(push_calculate, 5,0)
        push_calculate.setText("CALCULATE")

        push_reset = QPushButton("CLEAR")
        layout.addWidget(push_reset, 5, 1)

        duration_input = QLineEdit()
        layout.addWidget(duration_input, 4,1)
       



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
 QPushButton:hover{background-color: #FFFFFF; color: #FF2D00; font-size: 15px;
    
                  }



                  """)
window = MainWindow()
window.show()

app.exec() 