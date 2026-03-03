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
                                QFileDialog, QStackedWidget)

from PySide6.QtCore import Qt, QSize, QDate,Signal
from PySide6.QtGui import QPixmap, QFont, QIcon, QAction

class LastPage(QWidget):
    last_save = Signal(int, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24,24,24,24)
        layout.setSpacing(12)

        #spinbox
        layout.addWidget(QLabel("Age"))
        self.spin = QSpinBox()
        self.spin.setValue(0)
        layout.addWidget(self.spin)

        #major
        layout.addWidget(QLabel("Major"))
        self.combo = QComboBox()
        self.combo.addItems(["DME", "CoE"])
        layout.addWidget(self.combo)

        btn_group = QHBoxLayout()
        self.done_btn = QPushButton("Done")
        self.done_btn.clicked.connect(self.save)
        btn_group.addWidget(self.done_btn)

        self.home_btn = QPushButton("Home")
        self.home_btn.clicked.connect(lambda: parent.go_to(0))
        btn_group.addWidget(self.home_btn)

        self.profile = QPushButton("Profile")
        self.profile.clicked.connect(lambda: parent.go_to(1))
        btn_group.addWidget(self.profile)

        layout.addLayout(btn_group)
        layout.addStretch()
    
    def save(self):
        self.last_save.emit(self.spin.value(), self.combo.currentText())

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        home_text = QLabel("Home")
        home_text.setFont(QFont("Arial", 14, QFont.Bold))

        #lay1
        layout_1 = QHBoxLayout()

        name_text = QLabel("Name:")
        layout_1.addWidget(name_text)

        self.name_input = QLabel("N/A")
        layout_1.addWidget(self.name_input)

        #lay2
        layout_2 = QHBoxLayout()

        email_text = QLabel("Email:")
        layout_2.addWidget(email_text)

        self.email_input = QLabel("N/A")
        layout_2.addWidget(self.email_input)

        #lay3
        layout_3 = QHBoxLayout()

        age_text = QLabel("Age:")
        layout_3.addWidget(age_text)

        self.age_input = QLabel("N/A")
        layout_3.addWidget(self.age_input)

        #lay4
        layout_4 = QHBoxLayout()

        major_text = QLabel("Major:")
        layout_4.addWidget(major_text)

        self.major_input = QLabel("N/A")
        layout_4.addWidget(self.major_input)

        #add
        layout.addLayout(layout_1)
        layout.addLayout(layout_2)
        layout.addLayout(layout_3)
        layout.addLayout(layout_4)

        btn_group = QHBoxLayout()
        self.profile = QPushButton("Profile")
        self.profile.clicked.connect(lambda: parent.go_to(1))
        btn_group.addWidget(self.profile)

        self.last_btn = QPushButton("Last")
        self.last_btn.clicked.connect(lambda: parent.go_to(2))
        btn_group.addWidget(self.last_btn)

        layout.addLayout(btn_group)
        layout.addStretch()

class ProfilePage(QWidget):
    profile_save = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        profile_text = QLabel("Profile")
        profile_text.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(profile_text, alignment=Qt.AlignCenter)

        layout.addWidget(QLabel("Name:"))
        self.name_edit = QLineEdit()
        layout.addWidget(self.name_edit)

        layout.addWidget(QLabel("Email:"))
        self.email_edit = QLineEdit()
        layout.addWidget(self.email_edit)

        btn_group = QHBoxLayout()
        self.done_btn = QPushButton("Done")
        self.done_btn.clicked.connect(self.save)
        btn_group.addWidget(self.done_btn)

        self.last_btn = QPushButton("Last")
        self.last_btn.clicked.connect(lambda: parent.go_to(2))
        btn_group.addWidget(self.last_btn)

        layout.addLayout(btn_group)
        layout.addStretch()

    def save(self):
        self.profile_save.emit(self.name_edit.text(), self.email_edit.text())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stacked Widget Demo")
        self.setFixedSize(280, 320)

        self._stack = QStackedWidget()
        self.home = HomePage(self)
        self.profile = ProfilePage(self)
        self.last = LastPage(self)

        self._stack.addWidget(self.home) # index 0
        self._stack.addWidget(self.profile) # index 1
        self._stack.addWidget(self.last) # index 2

        self.setCentralWidget(self._stack)
        
        self.profile.profile_save.connect(self.change_name_email)
        self.last.last_save.connect(self.change_age_major)
    
    def change_age_major(self, age: int, major: str):
        self.home.age_input.setText(str(age))
        self.home.major_input.setText(major)
        self._stack.setCurrentIndex(0)

    def change_name_email(self, name: str, email: str):
        self.home.name_input.setText(name)
        self.home.email_input.setText(email)
        self._stack.setCurrentIndex(0)

    def go_to(self, page):
        self._stack.setCurrentIndex(page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())