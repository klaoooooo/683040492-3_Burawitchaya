import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QLineEdit, QMessageBox
)
from PySide6.QtWidgets import QStackedWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

"""
# 1. สร้าง QStackedWidget
self.stack = QStackedWidget()

# 2. สร้างแต่ละหน้าเป็น QWidget
page_login = QWidget()
page_home  = QWidget()

# 3. เพิ่มเข้า stack (index เริ่มที่ 0)
self.stack.addWidget(page_login)   # index 0
self.stack.addWidget(page_home)    # index 1

# 4. สลับหน้า
self.stack.setCurrentIndex(1)      # ไปหน้า Home
self.stack.setCurrentIndex(0)      # กลับหน้า Login

# 5. ดู index ปัจจุบัน
self.stack.currentIndex()          # คืนค่า int
"""
"""
# สลับด้วยชื่อ Widget แทน index (ปลอดภัยกว่า)
self.stack.setCurrentWidget(self.page_home)

# นับจำนวนหน้าทั้งหมด
self.stack.count()

# ดึง Widget ของหน้าที่ต้องการ
self.stack.widget(0)   # ได้ Widget ของ index 0
"""

# แต่ละหน้าเป็น Class ของตัวเอง → โค้ดสะอาด อ่านง่าย
class LoginPage(QWidget):
    name = Signal(str)
    def __init__(self):
        super().__init__()       
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Login"))

        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        self.btn = QPushButton("เข้าสู่ระบบ")
        self.btn.clicked.connect(lambda: self.save())
        layout.addWidget(self.btn)

    def save(self):
        self.name.emit(self.name_input.text())

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("ยินดีต้อนรับ!"))

        self.text_name = QLabel("N/A")
        layout.addWidget(self.text_name)

        self.btn = QPushButton("กลับ")
        layout.addWidget(self.btn)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 350, 500)

        # สร้าง stack แล้ว set เป็น central widget เลย
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        #ตั้งชื่อ 
        self.login = LoginPage()
        self.home = HomePage()

        # สร้างหน้าแล้วส่ง stack เข้าไป
        self.stack.addWidget(self.login)   # index 0
        self.stack.addWidget(self.home)    # index 1

        self.stack.setCurrentIndex(0)  # เริ่มที่หน้า Login

        self.home.btn.clicked.connect(lambda: self.go_to_login())
        self.login.btn.clicked.connect(lambda: self.go_to_home())

        self.login.name.connect(self.change_text_home)

    def go_to_login(self):
        self.stack.setCurrentIndex(0)

    def go_to_home(self):
        self.stack.setCurrentIndex(1)

    def change_text_home(self, text:str):
        self.home.text_name.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())