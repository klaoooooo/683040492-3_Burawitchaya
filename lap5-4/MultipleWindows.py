from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QStackedWidget,
                                QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                                QLineEdit, QFrame)
from PySide6.QtCore import Signal, Qt
import sys


class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        # Title
        title = QLabel("Home Page")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = title.font()
        font.setPointSize(14)
        font.setBold(True)
        title.setFont(font)
        layout.addWidget(title)

        # Divider
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)

        layout.addSpacing(8)

        # Info display
        self._name_label = QLabel("Name: N/A")
        self._email_label = QLabel("Email: N/A")
        layout.addWidget(self._name_label)
        layout.addWidget(self._email_label)

        layout.addStretch()

        # Buttons
        btn_layout = QHBoxLayout()
        self.go_btn = QPushButton("Go to Profile")
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.clear_info)
        btn_layout.addWidget(self.go_btn)
        btn_layout.addWidget(self.clear_btn)
        layout.addLayout(btn_layout)

    def update_info(self, name: str, email: str):
        self._name_label.setText(f"Name: {name}")
        self._email_label.setText(f"Email: {email}")

    def clear_info(self):
        self._name_label.setText("Name: N/A")
        self._email_label.setText("Email: N/A")


class profilePage(QWidget):
    profile_saved = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        # Title
        title = QLabel("profile")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = title.font()
        font.setPointSize(14)
        font.setBold(True)
        title.setFont(font)
        layout.addWidget(title)

        # Divider
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)

        layout.addSpacing(8)

        layout.addWidget(QLabel("Name:"))
        self._name_input = QLineEdit()
        self._name_input.setPlaceholderText("Enter your name...")
        layout.addWidget(self._name_input)

        layout.addSpacing(4)

        layout.addWidget(QLabel("Email:"))
        self._email_input = QLineEdit()
        self._email_input.setPlaceholderText("Enter your email...")
        layout.addWidget(self._email_input)

        layout.addStretch()

        # Buttons
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save and Back")
        save_btn.clicked.connect(self._on_save)
        self.back_btn = QPushButton("Back")
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(self.back_btn)
        layout.addLayout(btn_layout)

    def _on_save(self):
        self.profile_saved.emit(self._name_input.text(), self._email_input.text())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stacked Widget Demo")
        self.setFixedSize(280, 320)

        self._stack = QStackedWidget()
        self._home = HomePage()
        self._profile = profilePage()

        self._stack.addWidget(self._home)       # index 0
        self._stack.addWidget(self._profile)   # index 1

        self._home.go_btn.clicked.connect(lambda: self._stack.setCurrentIndex(1))
        self._profile.back_btn.clicked.connect(lambda: self._stack.setCurrentIndex(0))
        self._profile.profile_saved.connect(self._on_profile_saved)

        self.setCentralWidget(self._stack)

    def _on_profile_saved(self, name: str, email: str):
        self._home.update_info(name, email)
        self._stack.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()