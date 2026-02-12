"""
burawitchaya rongthong
683040492-3
P3
"""

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QVBoxLayout, QWidget, QHBoxLayout,
                                QGridLayout, QFormLayout, QLineEdit,
                                QLabel,QPushButton,QButtonGroup,
                                QRadioButton,QDateEdit,QComboBox,
                                QCheckBox,QTextEdit,QGroupBox,
                                QMessageBox)

from PySide6.QtCore import Qt, QSize, QDate
from PySide6.QtGui import QPixmap, QFont 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: BMI Calculator")
        self.setGeometry(100,100,300,450)

        #color: black; สีตัวอักษร
        #background-color: #F2F2F2; สีพื้นหลัง
        #border: 1px solid #999; ขอบ #สี
        #border-radius: 6px; ความโค้งของขอบ
        #padding: 10px; ขอบห่างจากข้อความ
        #min-width: 40px; ความกว้าง
        #max-height: 40px; ความสูง

        self.setStyleSheet("""
            QMainWindow {
                background-color: #F2F2F2;
            }
            QLabel#output {
                    color: #000000;
            }
            QLabel#title {
                    color: #ffffff;
                    background-color: #A73B24;
                    padding: 4px;
                    border-radius: 1px;
                    max-height: 12px;
            }
            QPushButton {
                    background-color: #ffffff;
                    border: 1px solid #f0f0f0;
                    border-radius: 5px;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget) 
        layout = QVBoxLayout(central_widget) 

        layout.setSpacing(5)
        layout.setContentsMargins(5, 5, 5, 2)

        title = QLabel("Adult and Child BMI Calculator")
        title.setObjectName("title")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addSpacing(20)

        #1 group
        group_cal = QHBoxLayout()
        group_cal.addStretch()

        Calculate_BMI_text = QLabel("BMI age group: ")
        Calculate_BMI_text.setFont(QFont("Arial", 8))
        group_cal.addWidget(Calculate_BMI_text)

        self.Calculate_BMI = QComboBox()  
        self.Calculate_BMI.addItems(sorted(["Adult 20+", "Child 5-19"]))
        self.Calculate_BMI.setFixedSize(200, 20)
        group_cal.addWidget(self.Calculate_BMI)

        layout.addLayout(group_cal)
        layout.addSpacing(5)

        #2 weight
        group_weight = QHBoxLayout()
        group_weight.addStretch()

        weight_text = QLabel("Weight: ")
        weight_text.setFont(QFont("Arial", 8))
        group_weight.addWidget(weight_text)

        self.weight_edit = QLineEdit()
        self.weight_edit.setFont(QFont("Arial", 8))
        self.weight_edit.setFixedSize(100, 20)
        group_weight.addWidget(self.weight_edit)

        self.weight_unit = QComboBox()
        self.weight_unit.addItems(sorted(["kilograms","grams"]))
        self.weight_unit.setCurrentText("kilograms")
        self.weight_unit.setFixedSize(95, 20)
        group_weight.addWidget(self.weight_unit)

        layout.addLayout(group_weight)

        #3 height
        group_height = QHBoxLayout()
        group_height.addStretch()

        self.height_text = QLabel("Height: ")
        self.height_text.setFont(QFont("Arial", 8))
        group_height.addWidget(self.height_text)

        self.height_edit = QLineEdit()
        self.height_edit.setFont(QFont("Arial", 8))
        self.height_edit.setFixedSize(100, 20)
        group_height.addWidget(self.height_edit)

        self.height_unit = QComboBox()
        self.height_unit.addItems(sorted(["meters", "centimeters"]))
        self.height_unit.setCurrentText("centimeters")
        self.height_unit.setFixedSize(95, 20)
        group_height.addWidget(self.height_unit)

        layout.addLayout(group_height)
        layout.addSpacing(25)

        #4 button
        group_button = QHBoxLayout()
        group_button.addStretch()
        group_button.addSpacing(5)
        clear_button = QPushButton("Clear")
        clear_button.setFont(QFont("Arial", 8))
        clear_button.setMinimumSize(150, 20)
        clear_button.clicked.connect(self.clear_form) 
        group_button.addWidget(clear_button)

        

        calculate_button = QPushButton("Submit Registration")
        calculate_button.setFont(QFont("Arial", 8))
        calculate_button.setMinimumSize(150, 20)
        calculate_button.clicked.connect(self.calculate_BMI)  
        group_button.addWidget(calculate_button)
        group_button.addStretch()

        layout.addLayout(group_button)
        layout.addSpacing(15)

        #6 output
        self.output_section = OutputSection()

        result_container = QWidget()
        result_container.setStyleSheet("background-color: #FAF0E6;")
        result_container.setMinimumHeight(220)
        result_layout = QVBoxLayout(result_container)
        result_layout.addWidget(self.output_section)
        layout.addWidget(result_container)

        layout.addStretch()

    def clear_form(self):
        self.weight_edit.clear()
        self.height_edit.clear()
        self.output_section.clear_result()    
        self.output_section.layout_output.addStretch()

    def calculate_BMI(self):
        try:
            # Get values
            weight_val = float(self.weight_edit.text())  
            height_val = float(self.height_edit.text())  
            
            # Convert to kg and cm
            if self.weight_unit.currentText() == "grams":  
                weight_val = weight_val / 100
            
            if self.height_unit.currentText() == "meters":  
                height_val = height_val * 100
            
            # Calculate BMI
            height_m = height_val / 100
            bmi = weight_val / (height_m ** 2)

            
            # Update results
            if bmi > 0:
                age_group = self.Calculate_BMI.currentText()
                self.output_section.update_results(bmi, age_group)
            else:
                QMessageBox.warning(self, "Error", "Negative Value")
                age_group = self.Calculate_BMI.currentText()
                self.output_section.update_results(0, age_group)
        except ValueError:
            QMessageBox.warning(self, "Error", "Wrong Number")
            age_group = self.Calculate_BMI.currentText()
            self.output_section.update_results(0, age_group)
        except ZeroDivisionError:
            QMessageBox.warning(self, "Error", "ZeroDivision")
            age_group = self.Calculate_BMI.currentText()
            self.output_section.update_results(0, age_group)
            
                
class OutputSection(QWidget):
    def __init__(self):
        super().__init__()

        self.layout_output = QVBoxLayout(self)
        self.layout_output.setSpacing(5)
        
        your_bmi_text = QLabel("Your BMI")
        your_bmi_text.setFont(QFont("Arial", 10))
        self.layout_output.addWidget(your_bmi_text, alignment=Qt.AlignCenter)

        self.results = QLabel("0.00")
        self.results.setFont(QFont("Arial", 20, QFont.Bold))
        self.results.setStyleSheet("color: #4F80CD;")
        self.layout_output.addWidget(self.results, alignment=Qt.AlignCenter)
        self.layout_output.addStretch()

    def show_adult_table(self):
        table_layout = QGridLayout()
        
        label = QLabel("BMI")
        label.setObjectName("output")
        label.setFont(QFont("Arial", 10, QFont.Bold))
        table_layout.addWidget(label, 0, 0, Qt.AlignCenter)

        label = QLabel("Condition")
        label.setObjectName("output")
        label.setFont(QFont("Arial", 10, QFont.Bold))
        table_layout.addWidget(label, 0, 1)

        underweight_bmi = QLabel("< 18.5")
        underweight_bmi.setObjectName("output")
        underweight_bmi.setFont(QFont("Arial", 10))
        underweight_bmi.setAlignment(Qt.AlignLeft)
        table_layout.addWidget(underweight_bmi, 1, 0, Qt.AlignCenter)

        underweight_status = QLabel("Thin")
        underweight_status.setObjectName("output")
        underweight_status.setFont(QFont("Arial", 10))
        underweight_status.setAlignment(Qt.AlignLeft)
        table_layout.addWidget(underweight_status, 1, 1)

        # Row 2 - Normal
        normal_bmi = QLabel("18.5 - 25.0")
        normal_bmi.setObjectName("output")
        normal_bmi.setFont(QFont("Arial", 10))
        normal_bmi.setAlignment(Qt.AlignLeft)
        table_layout.addWidget(normal_bmi, 2, 0, Qt.AlignCenter)

        normal_status = QLabel("Normal")
        normal_status.setObjectName("output")
        normal_status.setFont(QFont("Arial", 10))
        normal_status.setAlignment(Qt.AlignLeft)
        table_layout.addWidget(normal_status, 2, 1)

        # Row 3 - Overweight
        overweight_bmi = QLabel("25.1 - 30.0")
        overweight_bmi.setObjectName("output")
        overweight_bmi.setFont(QFont("Arial", 10))
        overweight_bmi.setAlignment(Qt.AlignLeft)
        table_layout.addWidget(overweight_bmi, 3, 0, Qt.AlignCenter)

        overweight_status = QLabel("Overweight")
        overweight_status.setObjectName("output")
        overweight_status.setFont(QFont("Arial", 10))
        overweight_status.setAlignment(Qt.AlignLeft)
        table_layout.addWidget(overweight_status, 3, 1)

        # Row 4 - Obese
        obese_bmi = QLabel("> 30.0")
        obese_bmi.setObjectName("output")
        obese_bmi.setFont(QFont("Arial", 10))
        obese_bmi.setAlignment(Qt.AlignLeft)
        table_layout.addWidget(obese_bmi, 4, 0, Qt.AlignCenter)

        obese_status = QLabel("Obese")
        obese_status.setObjectName("output")
        obese_status.setFont(QFont("Arial", 10))
        obese_status.setAlignment(Qt.AlignLeft)
        table_layout.addWidget(obese_status, 4, 1)

        self.layout_output.addLayout(table_layout)
        self.layout_output.addStretch()

    def show_child_link(self):
        link_layout = QHBoxLayout()
        link_layout.setSpacing(5)
        
        boy_link = QLabel('<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-boys-z-5-19years.pdf?sfvrsn=4007e921_4">BMI graph for BOYS</a>')
        girl_link = QLabel('<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-girls-z-5-19years.pdf?sfvrsn=c708a56b_4">BMI graph for GIRLS</a>')
        
        boy_link.setOpenExternalLinks(True)
        girl_link.setOpenExternalLinks(True)
        
        link_layout.addStretch()
        link_layout.addWidget(boy_link)
        link_layout.addWidget(girl_link) 
        link_layout.addStretch()
        
        self.layout_output.addLayout(link_layout)  

    def update_results(self, bmi, age_group):
        self.clear_result()
        self.results.setText(f"{bmi:.2f}")

        if age_group == "Adult 20+":
            self.show_adult_table()  
        else:
            self.show_child_link()
    
    def clear_result(self):
        while self.layout_output.count() > 2:  
            item = self.layout_output.takeAt(2)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())
        
        self.results.setText("0.00")
    
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()