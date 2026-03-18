import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout,
    QLabel,       # ข้อความ
    QPushButton,  # ปุ่ม
    QLineEdit,    # ช่องกรอกข้อความ
)
from PySide6.QtCore import Qt, QSize, QDate
from PySide6.QtGui import QPixmap, QFont
import os 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN")
        self.setGeometry(100, 100, 350, 500)  # กว้าง 350, สูง 500 pixel
        

        # ✅ ต้องสร้าง central widget แล้ว set เสมอ
        central = QWidget()
        self.setCentralWidget(central)

        #layout
        layout = QVBoxLayout(central)
        layout.setSpacing(10)          # ระยะห่างระหว่าง Widget
        layout.setContentsMargins(20, 20, 20, 20)  # ขอบ left, top, right, bottom

        # สร้าง Widget 
        self.label = QLabel("login")
        self.label.setFont(QFont("Arial", 20, QFont.Weight.Bold))

        row1 = QHBoxLayout()
        self.user_input = QLineEdit()

        row1.addWidget(QLabel("Username:"))
        row1.addWidget(self.user_input)
        
        row2 = QHBoxLayout()
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        row2.addWidget(QLabel("Password:"))
        row2.addWidget(self.pass_input)

        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addSpacing(10)
        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addSpacing(10)
        layout.addWidget(QPushButton("Login"), alignment=Qt.AlignCenter)
        layout.addStretch()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())