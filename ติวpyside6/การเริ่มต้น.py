import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN")
        self.setGeometry(100, 100, 350, 500)  # กว้าง 350, สูง 500 pixel

        # ✅ ต้องสร้าง central widget แล้ว set เสมอ
        central = QWidget()
        self.setCentralWidget(central)

if __name__ == "__main__":
    app = QApplication(sys.argv) # สร้าง "เครื่องยนต์"
    window = MainWindow()        # สร้างหน้าต่าง
    window.show()                # แสดงหน้าต่าง
    sys.exit(app.exec())         # วนรับ event จนกว่าจะปิด
    #app.exec() คือ "event loop" — โปรแกรมจะค้างอยู่ตรงนี้และรอรับการคลิก/พิมพ์ของผู้ใช้


    