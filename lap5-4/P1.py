import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QVBoxLayout, QWidget, QHBoxLayout,
                                QGridLayout, QFormLayout, QLineEdit,
                                QLabel, QPushButton, QButtonGroup,
                                QRadioButton, QDateEdit, QComboBox,
                                QCheckBox, QTextEdit, QGroupBox,
                                QMessageBox, QTableWidget, QTableWidgetItem, 
                                QSpinBox, QMenu, QMenuBar, QStatusBar, 
                                QToolBar, QColorDialog, QFrame)

from PySide6.QtCore import Qt, QSize, QDate
from PySide6.QtGui import QPixmap, QFont, QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Personal Info Card")
        self.setGeometry(100, 100, 300, 450)

        #color: black; สีตัวอักษร
        #background-color: #F2F2F2; สีพื้นหลัง
        #border: 1px solid #999; ขอบ #สี
        #border-radius: 6px; ความโค้งของขอบ
        #padding: 10px; ขอบห่างจากข้อความ
        #min-width: 40px; ความกว้าง
        #max-height: 40px; ความสูง
        self.setStyleSheet("""
            QLineEdit {
                min-height: 25px;
                min-width: 200px;
            }
            QPushButton {
                min-height: 25px;
                min-width: 150px;
            }
            QSpinBox {
                min-height: 25px;
                min-width: 130px;
            }           
        """)
        self.cantal_widget = PersonalInfoCard()
        self.setCentralWidget(self.cantal_widget)

        # ===== Menu Bar =====
        self.menu = self.menuBar()
        file_menu = self.menu.addMenu("&File")

        generate_action = QAction("&Generate", self)
        generate_action.triggered.connect(self.generate_card)
        file_menu.addAction(generate_action)

        save_action = QAction("&Save", self)
        save_action.triggered.connect(self.save_card)
        file_menu.addAction(save_action)

        clear_action = QAction("&Clear", self)
        clear_action.triggered.connect(self.clear_display)
        file_menu.addAction(clear_action)

        exit_action = QAction("E&xit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)
        #------------------------------------
        edit_menu = self.menu.addMenu("&Edit")

        copy_action = QAction("&Copy Card", self)
        edit_menu.addAction(copy_action)

        Clear_action = QAction("&Clear Form", self)
        edit_menu.addAction(Clear_action)

        # ===== Tool Bar =====
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        action1 = QAction(QIcon("lap5-4/a1.png"), "Action 1", self)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("lap5-4/a2.png"), "Action 2", self)
        toolbar.addAction(action2)

        action3 = QAction(QIcon("lap5-4/a3.png"), "Action 3", self)
        toolbar.addAction(action3)

    def generate_card(self):
        self.cantal_widget.update_output()

    def save_card(self):
        self.cantal_widget.add_data()
    
    def clear_display(self):
        self.cantal_widget.fullname_input.clear()
        self.cantal_widget.age_input.setValue(0)
        self.cantal_widget.position_input.clear()
        self.cantal_widget.email_input.clear()
        self.cantal_widget.update_output()

    def copy_card(self):
        pass
    
    def clear_form(self):
        pass

class PersonalInfoCard(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setSpacing(15)

        # Row 1: Full Name
        layout_row1 = QHBoxLayout()
        fullname_text = QLabel("Full Name:")
        layout_row1.addWidget(fullname_text, alignment=Qt.AlignLeft)
        #------------------------------------------------
        self.fullname_input = QLineEdit()
        self.fullname_input.setPlaceholderText("Firstname and Lastname")
        layout_row1.addWidget(self.fullname_input, alignment=Qt.AlignRight)
        layout.addLayout(layout_row1)

        # Row 2: Age
        layout_row2 = QHBoxLayout()
        age_text = QLabel("Age:")
        layout_row2.addWidget(age_text, alignment=Qt.AlignLeft)
        #------------------------------------------------
        self.age_input = QSpinBox()
        layout_row2.addWidget(self.age_input, alignment=Qt.AlignRight)
        layout.addLayout(layout_row2)

        # Row 3: Email
        layout_row3 = QHBoxLayout()
        email_text = QLabel("Email:")
        layout_row3.addWidget(email_text, alignment=Qt.AlignLeft)
        #------------------------------------------------
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("username@domain.com")
        layout_row3.addWidget(self.email_input, alignment=Qt.AlignRight)
        layout.addLayout(layout_row3)

        # Row 4: Position
        layout_row4 = QHBoxLayout()
        position_text = QLabel("Position:")
        layout_row4.addWidget(position_text, alignment=Qt.AlignLeft)
        #------------------------------------------------
        self.position_input = QLineEdit()
        self.position_input.setPlaceholderText("Your current position")
        layout_row4.addWidget(self.position_input, alignment=Qt.AlignRight)
        layout.addLayout(layout_row4)

        # Row 5: Favorite Color
        layout_row5 = QHBoxLayout()
        color_text = QLabel("Favorite Color:")
        layout_row5.addWidget(color_text)
        #------------------------------------------------
        self.color_preview = QLabel()
        self.color_preview.setFixedSize(25, 25)
        self.color_preview.setStyleSheet("background-color: green; border: 1px solid; border-color: black;")
        layout_row5.addWidget(self.color_preview)
        layout.addLayout(layout_row5)
        #------------------------------------------------
        self.pick_color_button = QPushButton("Pick New Color")
        self.pick_color_button.setStyleSheet("background-color: rgba(147, 162, 229, 40); color: green; border: 1px solid; border-color: green;")
        self.pick_color_button.clicked.connect(self.pick_color)
        layout_row5.addWidget(self.pick_color_button)

        # Line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        layout.addWidget(line)

        # Output Section
        self.output_section = OutputSection()
        layout.addWidget(self.output_section)

        self.result_container = QWidget()
        self.result_container.setStyleSheet("background-color: green;")
        result_layout = QVBoxLayout(self.result_container)
        result_layout.addWidget(self.output_section)
        result_layout.addStretch()
        layout.addWidget(self.result_container)

        layout.addStretch()

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_preview.setStyleSheet(f"background-color: {color.name()}; border: 1px solid; border-color: black;")
            self.result_container.setStyleSheet(f"background-color: {color.name()};")
            self.pick_color_button.setStyleSheet(f"background-color: rgba({color.red()}, {color.green()}, {color.blue()}, 40); color: {color.name()}; border: 1px solid; border-color: {color.name()};")
    
    def update_output(self):
        self.output_section.fullname_output.setText(self.fullname_input.text())
        self.output_section.age_output.setText(f"({str(self.age_input.value())})")
        self.output_section.position_output.setText(self.position_input.text())
        self.output_section.email_output.setText(f"✉️ {self.email_input.text()}")

    def add_data(self):
        name = self.fullname_input.text()
        age = self.age_input.value()
        position = self.position_input.text()
        email = self.email_input.text()

        if not name or not position or not email:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        try:
            with open("my_card.txt", "w") as output_file:
                output_file.write(f"{name}\n({age})\n{position}\nEmail: {email}\n")
            QMessageBox.information(self, "Success", "Card saved successfully!")
        except Exception as e:
            QMessageBox.critical(self, "File Error", f"Could not save file: {e}")

class OutputSection(QWidget):
    def __init__(self):
        super().__init__()

        self.output_layout = QVBoxLayout(self)
        
        self.fullname_output = QLabel("Your name here")
        self.fullname_output.setFont(QFont("Arial", 18, QFont.Bold))
        self.output_layout.addWidget(self.fullname_output, alignment=Qt.AlignLeft)

        self.age_output = QLabel("(Age)")
        self.age_output.setFont(QFont("Arial", 8))
        self.output_layout.addWidget(self.age_output, alignment=Qt.AlignLeft)

        self.position_output = QLabel("Your position here")
        self.position_output.setFont(QFont("Arial", 12))
        self.output_layout.addWidget(self.position_output, alignment=Qt.AlignLeft)

        self.email_output = QLabel("✉️ your_username@domain.name")
        self.email_output.setFont(QFont("Arial", 8))
        self.output_layout.addWidget(self.email_output, alignment=Qt.AlignLeft)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
