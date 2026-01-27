import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget)
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QRegularExpressionValidator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Demo App")
        self.setGeometry(100, 100, 400, 500)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 1) Create an instance of LineEdit
        entry = CustomLineEdit()

        # 2) Add LineEdit to layout
        layout.addWidget(entry)

class CustomLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()

        # Basic setup
        self.setPlaceholderText("Enter text here...")
        self.setMaxLength(50)  # Maximum characters

        # Input validation
        # Only allow letters and numbers
        regex = QRegularExpressionValidator(r"[A-Za-z0-9]+")
        self.setValidator(regex)

        # Echo modes
        self.setEchoMode(QLineEdit.Password)  # For passwords

        # Connect signals
        self.textChanged.connect(self.on_text_changed)
        self.returnPressed.connect(self.on_return_pressed)

    def on_text_changed(self, text):
        print(f"Text changed: {text}")

    def on_return_pressed(self):
        print("Enter key pressed")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()