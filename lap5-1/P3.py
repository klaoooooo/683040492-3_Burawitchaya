import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QVBoxLayout, QWidget, QHBoxLayout,
                                QGridLayout, QFormLayout, QLineEdit,
                                QLabel,QPushButton,QButtonGroup,
                                QRadioButton,QDateEdit,QComboBox,
                                QCheckBox,QTextEdit) # นำเข้าไลบรารีที่จำเป็นสำหรับสร้าง GUI

from PySide6.QtCore import Qt, QSize, QDate # นำเข้าโมดูลที่ใช้จัดการกับแกนกลางของแอพพลิเคชัน
from PySide6.QtGui import QPixmap, QFont 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P3")
        self.setGeometry(100, 100, 300, 500)
        
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;
            }
            QLabel {
                color: #333333;
            }
            QLabel#title {
                color: #ffffff;
                background-color: #A73B24;
            }
        """)
        

        central_widget = QWidget() # บอกว่าใช้ QWidget เป็น central widget เพื่อบอกว่า widget ตัวนี้จะเป็นตัวหลัก
        self.setCentralWidget(central_widget) 
        layout = QVBoxLayout(central_widget) 

        title = QLabel("Adult and Child BMI Calculator")
        title.setObjectName("title")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        #1    
        group_cal = QHBoxLayout()
        Calculate_BMI_text = QLabel("Calculate BMI for:")
        Calculate_BMI_text.setFont(QFont("Arial", 12))
        group_cal.addWidget(Calculate_BMI_text)
        Calculate_BMI = QComboBox()
        Calculate_BMI.addItems(sorted(["Adult Age 20+", "Child Age <20"]))
        group_cal.addWidget(Calculate_BMI)
        layout.addLayout(group_cal)

        #2
        group_weight = QHBoxLayout()
        weight_text = QLabel("Weight:")
        weight_text.setFont(QFont("Arial", 12))
        group_weight.addWidget(weight_text)
        weight = QLineEdit()
        weight.setFont(QFont("Arial", 12))
        group_weight.addWidget(weight)
        weight_unit = QComboBox()
        weight_unit.addItems(sorted(["pounds", "kg"]))
        group_weight.addWidget(weight_unit)
        layout.addLayout(group_weight)

        #3
        group_height = QHBoxLayout()
        height_text = QLabel("Height:")
        height_text.setFont(QFont("Arial", 12))
        group_height.addWidget(height_text)
        height = QLineEdit()
        height.setFont(QFont("Arial", 12))
        group_height.addWidget(height)
        height_unit = QComboBox()
        height_unit.addItems(sorted(["feet", "cm"]))
        group_height.addWidget(height_unit)
        layout.addLayout(group_height)

        #4
        group_inches = QHBoxLayout()
        inches = QLineEdit()
        inches.setFont(QFont("Arial", 12))
        group_inches.addWidget(inches)
        inches_text = QLabel("Inches")
        inches_text.setFont(QFont("Arial", 12))
        group_inches.addWidget(inches_text)
        layout.addLayout(group_inches)

        #5
        group_button = QHBoxLayout()
        clear_button =QPushButton("Clear")
        clear_button.setFont(QFont("Arial", 12))
        group_button.addWidget(clear_button)
        
        group_button.addSpacing(20)

        calculate_button =QPushButton("Calculate")
        calculate_button.setFont(QFont("Arial", 12))
        group_button.addWidget(calculate_button)

        layout.addLayout(group_button)

        layout.addStretch()

def main():
    app = QApplication(sys.argv) # สร้างแอพพลิเคชัน
    window = MainWindow() # สร้างหน้าต่างหลักของแอพพลิเคชัน
    window.show() # แสดงหน้าต่างหลัก
    sys.exit(app.exec()) # เริ่มต้นลูปเหตุการณ์ของแอพพลิเคชัน

if __name__ == "__main__":
    main()