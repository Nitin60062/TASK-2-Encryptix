import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basic Calculator')
        self.setGeometry(200, 200, 300, 400)

        self.init_ui()

    def init_ui(self):
        # Create the display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet('font-size: 18px;')
        
        # Layout for the number buttons
        num_layout = QVBoxLayout()
        numbers = [
            '9', '8', '7',
            '6', '5', '4',
            '3', '2', '1',
            '0', '.', '='
        ]
        
        for num in numbers:
            btn = QPushButton(num)
            if num == '=':
                btn.clicked.connect(self.calculate_result)
            else:
                btn.clicked.connect(lambda checked, ch=num: self.on_click(ch))  # Adjusted lambda function
            num_layout.addWidget(btn)
        
        # Layout for the operator buttons
        op_layout = QVBoxLayout()
        operators = [
            '+', '-', '*', '/'
        ]
        
        for op in operators:
            btn = QPushButton(op)
            btn.clicked.connect(lambda checked, ch=op: self.on_click(ch))  # Adjusted lambda function
            op_layout.addWidget(btn)
        
        # Layout for the entire calculator
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        
        # Horizontal layout for numbers and operators
        hbox_layout = QHBoxLayout()
        hbox_layout.addLayout(num_layout)
        hbox_layout.addLayout(op_layout)
        
        main_layout.addLayout(hbox_layout)
        
        self.setLayout(main_layout)

    def on_click(self, btn_text):
        current_text = self.display.text()
        new_text = current_text + btn_text
        self.display.setText(new_text)

    def calculate_result(self):
        try:
            result = str(eval(self.display.text()))
            self.display.setText(result)
        except Exception as e:
            self.display.setText('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
