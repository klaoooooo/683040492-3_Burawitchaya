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

student_dict = {}
student = open("P5-3/s.txt", "r")
for i in student:
    stu_id,name = i.split(",")
    student_dict[stu_id.strip()] = name.strip()

class MainMindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("P1: Student scores and grades")
        self.setCentralWidget(scores_and_grades())
        self.setGeometry(100,100,1000,700)
        
        #color: black; สีตัวอักษร
        #background-color: #F2F2F2; สีพื้นหลัง
        #border: 1px solid #999; ขอบ #สี
        #border-radius: 6px; ความโค้งของขอบ
        #padding: 10px; ขอบห่างจากข้อความ
        #min-width: 40px; ความกว้าง
        #max-height: 40px; ความสูง

        self.setStyleSheet("""
            QComboBox{
                padding: 5px;
                min-height: 20px;
                min-width: 100px;     
            }

            QLineEdit{
                padding: 5px;
                min-height: 20px;     
                min-width: 150px;
            }
                           
            QSpinBox{
                min-height: 35px;     
            }
                           
            QPushButton#add{
                background-color: green;
                min-width: 100px;  
                padding: 5px;
            }
            QPushButton#reset{
                background-color: yellow;
                min-width: 100px;  
                padding: 5px;
            }
            QPushButton#clear{
                background-color: red;
                min-width: 100px;  
                padding: 5px;
            }
            
            QTableWidget{
                min-height: 550px;
            }
        """)
        
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
            self.student_id_combo.addItems(student_dict.keys())
            self.student_id_combo.activated.connect(self.auto_name)
            layout_1.addWidget(self.student_id_combo)

        #layout_1
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
            self.math_spin.setMaximum(100)
            self.math_spin.setValue(0)    
            layout_1.addWidget(self.math_spin)

            #science
            self.science = QLabel("Science:")
            layout_1.addWidget(self.science)

            self.science_spin = QSpinBox()
            self.science_spin.setMinimum(0)
            self.science_spin.setMaximum(100)
            self.science_spin.setValue(0)    
            layout_1.addWidget(self.science_spin)

            #english
            self.english = QLabel("English:")
            layout_1.addWidget(self.english)

            self.english_spin = QSpinBox()
            self.english_spin.setMinimum(0)
            self.english_spin.setMaximum(100)
            self.english_spin.setValue(0)    
            layout_1.addWidget(self.english_spin)
            layout_1.addStretch()

            #button
                #add
            self.add_button = QPushButton("Add Student")
            self.add_button.setObjectName("add")
            self.add_button.clicked.connect(self.append_text)
            layout_1.addWidget(self.add_button)

        #add layout1
            layout.addLayout(layout_1)

        #reset layout
            #reset
            reset_layout = QHBoxLayout()
            self.reset_button = QPushButton("Reset Input")
            self.reset_button.setObjectName("reset")
            self.reset_button.clicked.connect(self.reset_input)
            reset_layout.addStretch()
            reset_layout.addWidget(self.reset_button)
            layout.addLayout(reset_layout)

        #clear latout
            #clear
            clear_layout = QHBoxLayout()
            self.clear_button = QPushButton("Clear All")
            self.clear_button.setObjectName("clear")
            self.clear_button.clicked.connect(self.clear)
            clear_layout.addStretch()
            clear_layout.addWidget(self.clear_button)
            layout.addLayout(clear_layout)

            self.table = QTableWidget()
            self.table.setColumnCount(8) 
            self.table.setHorizontalHeaderLabels(["Student ID","Name","math","Science","English","Total","Average","gread"])

            # set additional col properties
            self.table.horizontalHeader().setStretchLastSection(True)#ถ้าไม่มีมันจะมีพื้นที่ว่าง
            self.table.setColumnWidth(0, 100) 
            self.table.setColumnWidth(1, 200) 

            layout.addWidget(self.table)
            layout.addStretch()

        def auto_name(self):
            student_id = self.student_id_combo.currentText().strip()
            self.student_name_edit.setText(student_dict[student_id])

        def append_text(self):
            student_id = self.student_id_combo.currentText().strip()
            name = self.student_name_edit.text().strip()
            math = self.math_spin.value()
            sci = self.science_spin.value()
            eng = self.english_spin.value()

            if not student_id:
                QMessageBox.warning(self, "Error", "Please Select ID")

            if not name:
                QMessageBox.warning(self, "Error", "Please Type Name")
                return
            
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            student_id_item = QTableWidgetItem(student_id)
            name_item = QTableWidgetItem(name)
            math_item = QTableWidgetItem(str(math))
            math_item.setTextAlignment(Qt.AlignCenter)
            sci_item = QTableWidgetItem(str(sci))
            sci_item.setTextAlignment(Qt.AlignCenter)
            eng_item = QTableWidgetItem(str(eng))
            eng_item.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(row_position, 0, student_id_item)
            self.table.setItem(row_position, 1, name_item)

            # math
            if math < 50:
                math_item.setBackground(Qt.red)
            elif math < 60:
                math_item.setBackground(Qt.yellow)
            elif math < 70:
                math_item.setBackground(Qt.yellow)
            elif math < 80:
                math_item.setBackground(Qt.yellow)
            else:
                math_item.setBackground(Qt.green)
            self.table.setItem(row_position, 2, math_item)

            #sci
            if sci < 50:
                sci_item.setBackground(Qt.red)
            elif sci < 60:
                sci_item.setBackground(Qt.yellow)
            elif sci< 70:
                sci_item.setBackground(Qt.yellow)
            elif sci < 80:
                sci_item.setBackground(Qt.yellow)
            else:
                sci_item.setBackground(Qt.green)
            self.table.setItem(row_position, 3, sci_item)
            
            #eng
            if eng < 50:
                eng_item.setBackground(Qt.red)
            elif eng < 60:
                eng_item.setBackground(Qt.yellow)
            elif eng < 70:
                eng_item.setBackground(Qt.yellow)
            elif eng < 80:
                eng_item.setBackground(Qt.yellow)
            else:
                eng_item.setBackground(Qt.green)
            self.table.setItem(row_position, 4, eng_item)

            #total
            total = math + sci + eng
            total_item = QTableWidgetItem(str(total))
            total_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_position, 5, total_item)

            #avg
            avg = total/3
            avg_item = QTableWidgetItem(str(f"{avg:.2f}"))
            avg_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_position, 6, avg_item)

            #grade
            if avg < 50:
                grade = "F"
                grade_item = QTableWidgetItem(grade)
                grade_item.setBackground(Qt.red)
            elif avg < 60:
                grade = "D"
                grade_item = QTableWidgetItem(grade)
                grade_item.setBackground(Qt.yellow)
            elif avg < 70:
                grade = "C"
                grade_item = QTableWidgetItem(grade)
                grade_item.setBackground(Qt.yellow)
            elif avg < 80:
                grade = "B"
                grade_item = QTableWidgetItem(grade)
                grade_item.setBackground(Qt.yellow)
            else:
                grade = "A"
                grade_item = QTableWidgetItem(grade)
                grade_item.setBackground(Qt.green)

            grade_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_position, 7, grade_item)

            self.student_id_combo.setCurrentIndex(-1)
            self.student_name_edit.clear()
            self.math_spin.setValue(0)
            self.science_spin.setValue(0)
            self.english_spin.setValue(0)

        def reset_input(self):
            self.student_id_combo.setCurrentIndex(-1)
            self.student_name_edit.clear()
            self.math_spin.setValue(0)
            self.science_spin.setValue(0)
            self.english_spin.setValue(0)

        def clear(self):
            self.student_id_combo.setCurrentIndex(-1)
            self.student_name_edit.clear()
            self.math_spin.setValue(0)
            self.science_spin.setValue(0)
            self.english_spin.setValue(0)
            self.table.setRowCount(0)
            
          
if __name__ == "__main__":

    app = QApplication(sys.argv) # create app

    window = MainMindow() # selec window
    window.show() # show

    sys.exit(app.exec()) 



