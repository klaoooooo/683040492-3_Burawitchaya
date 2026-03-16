import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QLineEdit, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN")
        self.setGeometry(100, 100, 350, 500)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.label = QLabel("LOGIN")
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

        self.btn = QPushButton("Login")
        self.btn.clicked.connect(self.on_login)   # ✅ เชื่อม Signal

        self.btn_clear = QPushButton("Clear")
        self.btn_clear.clicked.connect(self.clear)

        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addSpacing(10)
        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addSpacing(10)
        layout.addWidget(self.btn, alignment=Qt.AlignCenter)
        layout.addWidget(self.btn_clear, alignment=Qt.AlignCenter)
        layout.addStretch()

    def on_login(self):                            # ✅ Slot
        username = self.user_input.text()
        password = self.pass_input.text()

        if not username or not password:
            QMessageBox.warning(self, "แจ้งเตือน", "กรุณากรอกข้อมูลให้ครบ")
            return 

        if username == "admin" and password == "1234":
            QMessageBox.information(self, "สำเร็จ", "เข้าสู่ระบบสำเร็จ!")
        else:
            QMessageBox.warning(self, "ผิดพลาด", "Username หรือ Password ไม่ถูกต้อง")

        """
        QMessageBox.information(self, "หัวข้อ", "ข้อความ")  # ℹ️ แจ้งข้อมูล
        QMessageBox.warning(self, "หัวข้อ", "ข้อความ")      # ⚠️ เตือน
        QMessageBox.critical(self, "หัวข้อ", "ข้อความ")     # ❌ Error
        QMessageBox.question(self, "หัวข้อ", "ข้อความ")     # ❓ ถาม Yes/No
        """

    def clear(self):
        self.user_input.clear()
        self.pass_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())