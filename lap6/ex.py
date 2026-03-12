import sys
import csv
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem,
    QFileDialog, QLineEdit, QMessageBox
)
from PySide6.QtCore import Qt


class StudentManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Score Manager")
        self.resize(700, 500)
        self.current_path = None

        # ── Central widget & layout ──────────────────
        widget = QWidget()
        main_layout = QVBoxLayout(widget)
        self.setCentralWidget(widget)

        # ── Toolbar: Load / Save buttons ─────────────
        toolbar = QHBoxLayout()
        self.btn_load = QPushButton("Load CSV")
        self.btn_save = QPushButton("Save CSV")
        self.lbl_file = QLabel("No file loaded")

        toolbar.addWidget(self.btn_load)
        toolbar.addWidget(self.btn_save)
        toolbar.addWidget(self.lbl_file)
        toolbar.addStretch()

        # ── Table ─────────────────────────────────────
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Score", "Grade"])
        self.table.horizontalHeader().setStretchLastSection(True)

        # ── Add new student row ───────────────────────
        add_layout = QHBoxLayout()
        self.input_name  = QLineEdit()
        self.input_score = QLineEdit()
        self.input_grade = QLineEdit()
        self.input_name.setPlaceholderText("Name")
        self.input_score.setPlaceholderText("Score")
        self.input_grade.setPlaceholderText("Grade")
        self.btn_add = QPushButton("Add Row")

        add_layout.addWidget(self.input_name)
        add_layout.addWidget(self.input_score)
        add_layout.addWidget(self.input_grade)
        add_layout.addWidget(self.btn_add)

        # ── Status bar ────────────────────────────────
        self.statusBar().showMessage("Ready")

        # ── Assemble layout ───────────────────────────
        main_layout.addLayout(toolbar)
        main_layout.addWidget(self.table)
        main_layout.addLayout(add_layout)

        # ── Connect signals ───────────────────────────
        self.btn_load.clicked.connect(self.load_file)
        self.btn_save.clicked.connect(self.save_file)
        self.btn_add.clicked.connect(self.add_row)

    # ──────────────────────────────────────────────────
    # TODO 1: Open a file dialog, read the CSV,
    #         and populate self.table with the data
    # ──────────────────────────────────────────────────
    def load_file(self):
        with open('lap5-5/klao.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for i in reader:
                name = i["name"].strip()
                score = i["score"].strip()
                grade = i["grade"].strip()

                if not name or not score or not grade:
                    QMessageBox.warning(self, "Missing Data", "Please fill in all fields")
                    return

                r = self.table.rowCount()
                self.table.insertRow(r)
                self.table.setItem(r, 0, QTableWidgetItem(name))
                self.table.setItem(r, 1, QTableWidgetItem(score))
                self.table.setItem(r, 2, QTableWidgetItem(grade))

                self.input_name.clear()
                self.input_score.clear()
                self.input_grade.clear()

                self.statusBar().showMessage(f"Added {name}")

    # ──────────────────────────────────────────────────
    # TODO 2: Read all rows from self.table,
    #         and write them to a CSV file
    # ──────────────────────────────────────────────────
    def save_file(self):
        self.table
        data = []
        for r in range(self.table.rowCount()):
            name_item = self.table.item(r, 0)
            score_item = self.table.item(r, 1)
            grade_item = self.table.item(r, 2)

            data_row = {
                    'name' : name_item.text(),
                    'score' : score_item.text(),
                    'grade' : grade_item.text()
            }
            data.append(data_row)

        with open('lap5-5/klao.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'score', 'grade'])
            writer.writeheader()
            writer.writerows(data)


    # ──────────────────────────────────────────────────
    # Read the three input fields,
    #      and add a new row to self.table
    # ──────────────────────────────────────────────────
    def add_row(self):
        name  = self.input_name.text().strip()
        score = self.input_score.text().strip()
        grade = self.input_grade.text().strip()

        if not name or not score or not grade:
            QMessageBox.warning(self, "Missing Data", "Please fill in all fields")
            return

        r = self.table.rowCount()
        self.table.insertRow(r)
        self.table.setItem(r, 0, QTableWidgetItem(name))
        self.table.setItem(r, 1, QTableWidgetItem(score))
        self.table.setItem(r, 2, QTableWidgetItem(grade))

        self.input_name.clear()
        self.input_score.clear()
        self.input_grade.clear()

        self.statusBar().showMessage(f"Added {name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = StudentManager()
    win.show()
    sys.exit(app.exec())