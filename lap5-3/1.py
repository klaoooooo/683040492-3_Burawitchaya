## For Student ##

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QSpinBox)
from PySide6.QtCore import Qt
import sys


class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Inventory Manager")
        self.setGeometry(100, 100, 600, 400)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Input section layout
        input_layout = QHBoxLayout()
        input_layout.setSpacing(5)
        # Product Name input
        self.product_name = QLabel("Product Name")
        input_layout.addWidget(self.product_name)

        self.product = QLineEdit()
        self.product.setFixedSize(200,20)
        input_layout.addWidget(self.product)

        # Quantity input
        self.quantity = QLabel("Quantity:")
        input_layout.addWidget(self.quantity)

        self.quantity_spin = QSpinBox()
        self.quantity_spin.setMinimum(0)
        self.quantity_spin.setValue(0)
        input_layout.addWidget(self.quantity_spin)


        # Add Product button
        self.add_pro = QPushButton("Add Product:")
        # connect clicking with the instant function
        self.add_pro.clicked.connect(self.add_product)
        input_layout.addWidget(self.add_pro)

        # Clear All button
        self.clear = QPushButton("clear")
        # connect clicking with the instant function
        self.clear.clicked.connect(self.clear_all)
        input_layout.addWidget(self.clear)


        # add input layout to the main layout
        input_layout.addStretch()
        main_layout.addLayout(input_layout)

        # Table widget
        # create table widget, set col, set headers
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Product Name","Quantity","Status"])

        # set additional col properties
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0, 200) # name col
        self.table.setColumnWidth(1, 100) # quantity col
        self.table.setColumnWidth(2, 200)

        # add table to the main layout
        main_layout.addWidget(self.table)

    def add_product(self):
        """Add a new product to the inventory table"""

        # get product data from the class object
        # LineEditWidget.text().strip()
        # SpinBoxWidget.value()
        name = self.product.text().strip()
        amount = self.quantity_spin.value()

        # Validate input: product name


        # Determine status based on quantity
        if not name:
            print("Please Type Name")
            return

        # Add new row to table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Add items to the row
        name_item = QTableWidgetItem(name)

        amount_item = QTableWidgetItem(str(amount))
        amount_item.setTextAlignment(Qt.AlignCenter)

        # QTableItemWidget.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(row_position, 0, name_item)
        self.table.setItem(row_position, 1, amount_item)
        # Color code the status
        # QTableItemWidget.setBackground(Qt.red)
        if amount < 10:
            status = "Low Stock"
            status_itme = QTableWidgetItem(status)
            status_itme.setBackground(Qt.red)
        else:
            status = "In Stock"
            status_itme = QTableWidgetItem(status)
            status_itme.setBackground(Qt.green)

        status_itme.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(row_position, 2, status_itme)

          
        # Clear input fields
        # Move the focus to the product input
        # product_input.setFocus()
        self.product.clear()
        self.quantity_spin.setValue(0)
        self.table.setFocus()

    def clear_all(self):
        """Clear all rows from the table"""
        self.table.setRowCount(0)


def main():
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()