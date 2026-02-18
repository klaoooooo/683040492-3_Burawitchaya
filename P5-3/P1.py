"""
burawitchaya rongthong
683040492-3
P1
"""

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QVBoxLayout, QWidget, QHBoxLayout,
                                QGridLayout, QFormLayout, QLineEdit,
                                QLabel,QPushButton,QButtonGroup,
                                QRadioButton,QDateEdit,QComboBox,
                                QCheckBox,QTextEdit,QGroupBox,
                                QMessageBox,QTableWidget, QTableWidgetItem, QSpinBox)

from PySide6.QtCore import Qt, QSize, QDate
from PySide6.QtGui import QPixmap, QFont 

student_dict = {
                    "653040111-1" : "John Michael Smith",
                    "653040112-2" : "Sarah Elizabeth Johnson",
                    "653040113-3" : "Michael James Williams",
                    "653040115-5" : "David Alexander Jones",
                    "653040116-6" : "Jessica Marie Garcia",
                    "653040117-7" : "Christopher Lee Miller",
                    "653040118-8" : "Amanda Grace Davis",
                    "653040119-9" : "Matthew Thomas Rodriguez",
                    "653040120-0" : "Ashley Nicole Martinez",
                    "653040121-1" : "Daniel Robert Anderson",
                    "653040122-2" : "Jennifer Lynn Taylor",
                    "653040123-3" : "Joshua William Thomas",
                    "653040124-4" : "Megan Elizabeth Hernandez",
                    "653040125-5" : "Andrew James Moore",
                    "653040126-6" : "Stephanie Ann Martin",
                    "653040127-7" : "Ryan Christopher Jackson",
                    "653040128-8" : "Lauren Michelle Thompson",
                    "653040129-9" : "Brandon Scott White",
                    "653040130-0" : "Rachel Marie Lopez",
}

class MainMindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("P1: Student scores and grades")
        self.setCentralWidget(scores_and_grades())
        self.setGeometry(100,100,600,1000)
        

class scores_and_grades(QWidget):
        def __init__(self):
            super().__init__()
            layout = QVBoxLayout()
            self.setLayout(layout)

            layout_1 = QHBoxLayout()
            layout_1.setSpacing(5)
            # student ID
            self.student_id_text = QLabel("Student ID:")
            layout_1.addWidget(self.student_id_text)

            self.student_id_combo = QComboBox()
            self.student_id_combo.setPlaceholderText("Select Student ID")
            self.student_id_combo.addItems(["653040111-1","653040112-2","653040113-3",
                                            "653040114-4",'653040115-5','653040116-6',
                                            "653040117-7","653040118-8","653040119-9",
                                            "653040120-0","653040121-1","653040122-2",
                                            "653040123-3","653040124-4","653040125-5",
                                            "653040126-6","653040127-7","653040128-8",
                                            "653040129-9","653040130-0"])
            layout_1.addWidget(self.student_id_combo)

            #student name
            self.student_name = QLabel("Student Name: ")
            layout_1.addWidget(self.student_name)

            self.student_name_edit = QLineEdit()
            layout_1.addWidget(self.student_name_edit)

            #math
            self.math = QLabel("Math:")
            layout_1.addWidget(self.math)

            self.math_spin = QSpinBox()
            self.math_spin.setMinimum(0)
            self.math_spin.setValue(0)    
            layout_1.addWidget(self.math_spin)

            #science
            self.science = QLabel("Science:")
            layout_1.addWidget(self.science)

            self.science_spin = QSpinBox()
            self.science_spin.setMinimum(0)
            self.science_spin.setValue(0)    
            layout_1.addWidget(self.science_spin)

            #english
            self.english = QLabel("English:")
            layout_1.addWidget(self.english)

            self.english_spin = QSpinBox()
            self.english_spin.setMinimum(0)
            self.english_spin.setValue(0)    
            layout_1.addWidget(self.english_spin)

            #button
                #add
            self.add_button = QPushButton("Add Student")
            layout_1.addWidget(self.add_button)

                #reset
            self.reset_button = QPushButton("Reset Input")
            self.reset_button.
            layout.addWidget(self.reset_button)

                #clear
            self.clear_button = QPushButton("Clear All")
            layout.addWidget(self.clear_button)


            layout_1.addStretch()
            layout.addLayout(layout_1)
            layout.addStretch()

if __name__ == "__main__":

    app = QApplication(sys.argv) # create app

    window = MainMindow() # selec window
    window.show() # show

    sys.exit(app.exec()) 



