import sys
import pyperclip
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QVBoxLayout, QWidget, QHBoxLayout,
                                QGridLayout, QFormLayout, QLineEdit,
                                QLabel, QPushButton, QButtonGroup,
                                QRadioButton, QDateEdit, QComboBox,
                                QCheckBox, QTextEdit, QGroupBox,
                                QMessageBox, QTableWidget, QTableWidgetItem, 
                                QSpinBox, QMenu, QMenuBar, QStatusBar, 
                                QToolBar, QColorDialog, QFrame,
                                QFileDialog)

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
            QComboBox {
                min-height: 25px;
                min-width: 130px;
            }
        """)
        self.cantal_widget = PersonalInfoCard(self)
        self.setCentralWidget(self.cantal_widget)

        self.last_saved_file = None

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
        copy_action.triggered.connect(self.copy_card)
        edit_menu.addAction(copy_action)

        Clear_action = QAction("&Clear Form", self)
        Clear_action.triggered.connect(self.clear_form)
        edit_menu.addAction(Clear_action)

        # ===== Tool Bar =====
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        action1 = QAction(QIcon("lap5-4/a1.png"), "Action 1", self)
        action1.triggered.connect(self.generate_card)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("lap5-4/a2.png"), "Action 2", self)
        action2.triggered.connect(self.save_card)
        toolbar.addAction(action2)

        action3 = QAction(QIcon("lap5-4/a3.png"), "Action 3", self)
        action3.triggered.connect(self.clear_all)
        toolbar.addAction(action3)

        # ====== Status Bar =====
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Fill in your details and click generate")

    def generate_card(self):
        self.cantal_widget.update_output()

    def save_card(self):
        self.cantal_widget.add_data()
    
    def clear_display(self):
        self.cantal_widget.output_section.fullname_output.setText("Your name here")
        self.cantal_widget.output_section.age_output.setText("(Age)")
        self.cantal_widget.output_section.position_output.setText("Your position here")
        self.cantal_widget.output_section.email_output.setText("✉️ your_username@domain.com")
        self.status_bar.showMessage("Display cleared!", 5000)


    def copy_card(self):
        name = self.cantal_widget.fullname_input.text()
        age = self.cantal_widget.age_input.value()
        position = self.cantal_widget.position.currentText()
        email = self.cantal_widget.email_input.text()

        card_text = f"Name: {name}\nAge: {age}\nPosition: {position}\nEmail: {email}"
        pyperclip.copy(card_text)
        self.status_bar.showMessage("Card copied to clipboard!", 5000)

    def clear_form(self):
        self.cantal_widget.fullname_input.clear()
        self.cantal_widget.age_input.setValue(0)
        self.cantal_widget.position.setCurrentIndex(-1)
        self.cantal_widget.email_input.clear()
        self.status_bar.showMessage("Form cleared!", 5000)
    
    def clear_all(self):
        self.clear_display()
        self.clear_form()
        self.status_bar.showMessage("Form and display cleared!", 5000)

class PersonalInfoCard(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

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
        self.position = QComboBox()
        self.position.addItems(["Teaching Staff","Supporting Staff","Student","Visitor"])
        self.position.setPlaceholderText("Choose your position")
        self.position.setCurrentIndex(-1)
        layout_row4.addWidget(self.position, alignment=Qt.AlignRight)
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
        self.main_window.status_bar.showMessage(f"Selected color: {color.name()}", 5000)
        
    def update_output(self):
        name = self.fullname_input.text()
        age = self.age_input.value()
        position = self.position.currentText()
        email = self.email_input.text()

        try:
            age = int(age)
            if age < 1 or age > 149:  # แก้ logic ให้ถูก
                QMessageBox.warning(self, "Input Error", "Please enter a valid age between 1 and 149.")
                return
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid age value.")
            return

        if "@" not in email or "." not in email.split("@")[-1] :
            QMessageBox.warning(self, "Input Error", "Please enter a valid email address.")
            return

        if not name or not position or not email:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return
        
        if not self.fullname_input.text() or not self.position.currentText() or not self.email_input.text():
            QMessageBox.warning(self, "Input Error", "Please fill in all fields before generating the card.")
            return
        self.output_section.fullname_output.setText(name)
        self.output_section.age_output.setText(f"({str(age)})")
        self.output_section.position_output.setText(position)
        self.output_section.email_output.setText(f"✉️ {email}")

    def add_data(self):
        name = self.output_section.fullname_output.text()
        age = self.output_section.age_output.text().strip("()")
        position = self.output_section.position_output.text()
        email = self.output_section.email_output.text().replace("✉️ ", "")

        try:
            age = int(age)
            if age < 1 or age > 149:  # แก้ logic ให้ถูก
                QMessageBox.warning(self, "Input Error", "Please enter a valid age between 1 and 149.")
                return
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid age value.")
            return

        if "@" not in email or "." not in email.split("@")[-1]:
            QMessageBox.warning(self, "Input Error", "Please enter a valid email address.")
            return

        if not name or not position or not email:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return


        try:
            file, _ = QFileDialog.getSaveFileName(self, "Save Card Data", "my_card.txt", "Text Files (*.txt);;All Files (*)")
            if file:  
                with open(file, "w") as output_file:
                    output_file.write(f"{name}\n({age})\n{position}\nEmail: {email}\n")
                self.main_window.last_saved_file = file
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
