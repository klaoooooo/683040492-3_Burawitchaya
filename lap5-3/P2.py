import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QVBoxLayout, QWidget, QHBoxLayout,
                                QGridLayout, QFormLayout, QLineEdit,
                                QLabel,QPushButton,QButtonGroup,
                                QRadioButton,QDateEdit,QComboBox,
                                QCheckBox,QTextEdit,QGroupBox,
                                QMessageBox,QTableWidget, QTableWidgetItem, QSpinBox)

from PySide6.QtCore import Qt, QSize, QDate
from PySide6.QtGui import QPixmap, QFont 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("683040492-3")
        self.setCentralWidget(MonthlySalesChart())
        self.setGeometry(100, 100, 700, 700)
        
        #color: black; สีตัวอักษร
        #background-color: #F2F2F2; สีพื้นหลัง
        #border: 1px solid #999; ขอบ #สี
        #border-radius: 6px; ความโค้งของขอบ
        #padding: 10px; ขอบห่างจากข้อความ
        #min-width: 40px; ความกว้าง
        #max-height: 40px; ความสูง

        self.setStyleSheet("""
            QComboBox{
            }

            QLineEdit{
            }
                           
            QSpinBox{  
            }
                           
            QPushButton#add {
                background-color: green;
                padding: 5px;
            }
                           
            QPushButton#add:hover {
                background-color: lightgreen;
            }

            QPushButton#clear{
                background-color: red;
                min-width: 100px;  
                padding: 5px;
            }
                           
            QPushButton#clear:hover {
                background-color: lightcoral;
            }
            
            QTableWidget{
                min-height: 550px;
            }
        """)

class MonthlySalesChart(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        # ====== File input ======
        layout_input = QHBoxLayout()

        file_text = QLabel("File Name:")
        layout_input.addWidget(file_text)

        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("lap5-3/sales_data.txt")
        layout_input.addWidget(self.file_input)

        import_button = QPushButton("Import data")
        import_button.setObjectName("add")
        import_button.clicked.connect(self.import_data)
        layout_input.addWidget(import_button)

        # ===== Data input ======
        layout_data = QHBoxLayout()

        month_text = QLabel("Month:")
        layout_data.addWidget(month_text)

        self.month_input = QComboBox()
        self.month_input.setPlaceholderText("Select Month")
        months = open("lap5-3/month.txt", "r")
        month_list = []
        for line in months:
            for m in line.split(","):
                month = m.strip()
                month_list.append(month)
        self.month_input.addItems(month_list)
        self.month_order = {month: i for i, month in enumerate(month_list)} # สร้าง dict สำหรับเก็บลำดับของเดือน
        layout_data.addWidget(self.month_input)

        sales_text = QLabel("Sales:")
        layout_data.addWidget(sales_text)

        self.sales_input = QSpinBox()   
        self.sales_input.setMinimum(0)
        self.sales_input.setMaximum(999999999)
        self.sales_input.setValue(0)
        layout_data.addWidget(self.sales_input)

        product_text = QLabel("Product Category:")
        layout_data.addWidget(product_text)

        self.product_input = QComboBox()
        self.product_input.setPlaceholderText("Select Product Category")
        products = open("lap5-3/product.txt", "r")
        for line in products:
            for p in line.split(","):
                product = p.strip()
                self.product_input.addItem(product)
        layout_data.addWidget(self.product_input)

        add_button = QPushButton("Add Data")
        add_button.setObjectName("add")
        add_button.clicked.connect(self.add_data)
        layout_data.addWidget(add_button)

        layout_data.addStretch()

        # ====== Table Widget ======
        self.table = QTableWidget()
        self.table.setColumnCount(12)
        self.table.setHorizontalHeaderLabels(["Sales"] + month_list)

        # ===== Clear Button ======
        layout_button = QHBoxLayout()
        clear_button = QPushButton("Clear Chart")
        clear_button.clicked.connect(self.clear)
        clear_button.setFont(QFont("Arial", 18, QFont.Bold))
        clear_button.setObjectName("clear")
        layout_button.addWidget(clear_button)

        # add all layouts to the main layout
        layout.addLayout(layout_input)
        layout.addLayout(layout_data)
        layout.addWidget(self.table)
        layout.addLayout(layout_button)

        layout.addStretch()

    def import_data(self):
        file = self.file_input.text().strip()
        if not file:
            QMessageBox.warning(self, "Error", "Please Enter File Name")    
            return
        try:
            file_open = open(file, "r")
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "File Not Found")
            return
        
        for line in file_open:
            line = line.strip()
            if not line:
                continue
            data = line.split(",")
            if len(data) != 3:
                QMessageBox.warning(self, "Error", "Data format error in file")
                continue

            month = data[0].strip()
            sales = data[1].strip()
            product = data[2].strip()

            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            
            sales_item = QTableWidgetItem(str(sales))
            product_item = QTableWidgetItem(product)

            self.table.setItem(row_position, 0, sales_item)

            month_index = 1
            for i in range(self.table.columnCount()):
                if self.table.horizontalHeaderItem(i).text() == month:
                    month_index = i
                    break

            if product == "Electronics":
                product_item.setBackground(Qt.blue)
            elif product == "Clothing":
                product_item.setBackground(Qt.yellow)
            elif product == "Food":
                product_item.setBackground(Qt.red)
            else:
                product_item.setBackground(Qt.green)

            self.table.setItem(row_position, month_index, product_item)

        self.sort_by_month()
        self.file_input.clear()

    def add_data(self):
        month = self.month_input.currentText().strip()
        sales = self.sales_input.value()
        product = self.product_input.currentText().strip()

        if not month:
            QMessageBox.warning(self, "Error", "Please Select Month")
            return

        if not product:
            QMessageBox.warning(self, "Error", "Please Select Product Category")
            return

        # find month index
        month_index = 1
        for i in range(self.table.columnCount()):
            if self.table.horizontalHeaderItem(i).text() == month:
                month_index = i
                break

        # check if month and product already exists in the table
        existing_row = -1
        for row in range(self.table.rowCount()): # วนลูปเช็คทุกแถวในตารางว่ามีข้อมูลเดือนและสินค้านี้อยู่แล้วหรือไม่
            item = self.table.item(row, month_index) 
            if item is not None and item.text() == product:  
                existing_row = row # ถ้ามีข้อมูลเดือนและสินค้านี้อยู่แล้ว ให้เก็บแถวนั้นไว้ในตัวแปร existing_row
                break

        if existing_row != -1:
            row_position = existing_row # ถ้ามีข้อมูลเดือนและสินค้านี้อยู่แล้ว ให้ใช้แถวนั้นแทนการเพิ่มแถวใหม่
        else:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

        sales_item = QTableWidgetItem(str(sales))
        product_item = QTableWidgetItem(product)

        self.table.setItem(row_position, 0, sales_item)

        if product == "Electronics":
            product_item.setBackground(Qt.blue)
        elif product == "Clothing":
            product_item.setBackground(Qt.yellow)
        elif product == "Food":
            product_item.setBackground(Qt.red)
        else:
            product_item.setBackground(Qt.green)
        
        self.table.setItem(row_position, month_index, product_item)

        self.sort_by_month()

        self.month_input.setCurrentIndex(-1)
        self.sales_input.setValue(0)
        self.product_input.setCurrentIndex(-1)

    def clear(self):
        self.file_input.clear()
        self.month_input.setCurrentIndex(-1)
        self.sales_input.setValue(0)
        self.product_input.setCurrentIndex(-1)
        self.table.setRowCount(0)

    def sort_by_month(self): # สร้างฟังก์ชันสำหรับเรียงลำดับแถวในตารางตามลำดับของเดือน
        rows = []
        for row in range(self.table.rowCount()): # วนลูปเช็คทุกแถวในตารางเพื่อเก็บข้อมูลของแต่ละแถวไว้ในตัวแปร rows
            row_data = []
            for col in range(self.table.columnCount()): # วนลูปเช็คทุกคอลัมน์ในแถวนั้นเพื่อเก็บข้อมูลของแต่ละเซลล์ไว้ในตัวแปร row_data
                item = self.table.item(row, col)
                if item is not None: # ถ้าเซลล์นั้นมีข้อมูล ให้เก็บข้อความและสีพื้นหลังของเซลล์นั้นไว้ในตัวแปร row_data
                    row_data.append((item.text(), item.background().color()))  
                else:
                    row_data.append(None)
            
            month_idx = 0
            for col in range(1, self.table.columnCount()): # วนลูปเช็คทุกคอลัมน์ในแถวนั้นเพื่อหาคอลัมน์ที่เป็นเดือนและเก็บลำดับของเดือนนั้นไว้ในตัวแปร month_idx
                if self.table.item(row, col) is not None: 
                    header = self.table.horizontalHeaderItem(col).text()
                    month_idx = self.month_order.get(header, 0)
                    break
            
            rows.append((month_idx, row_data))
        
        rows.sort(key=lambda x: x[0])
        
        for row_idx, (_, row_data) in enumerate(rows):
            for col_idx, item_data in enumerate(row_data):
                if item_data is not None:
                    text, color = item_data
                    new_item = QTableWidgetItem(text)
                    if col_idx != 0: 
                        new_item.setBackground(color)
                    self.table.setItem(row_idx, col_idx, new_item)
                else:
                    self.table.setItem(row_idx, col_idx, None)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())