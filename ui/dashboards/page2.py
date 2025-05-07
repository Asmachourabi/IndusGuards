from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QPushButton, QSpacerItem, QSizePolicy, QHBoxLayout, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont
from .custom_widget import ControlButton  

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Recent Batches Table
        self.table = self.create_recent_batches_table()
        layout.addWidget(self.table)

        # Control Panel
        layout.addLayout(self.create_control_panel())

        self.setLayout(layout)

    def create_recent_batches_table(self):
        table = QTableWidget(16, 5)
        table.setHorizontalHeaderLabels(["Batch ID", "Start Time", "End Time", "Units", "Status"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setSortingEnabled(False)
        table.setStyleSheet("""
            QTableWidget {
                background-color: transparent;
                color: white;
                font-size: 14px;
                border: none;
            } 
            
            QHeaderView::section {
                background-color: transparent;
                color: #00C5CD;
                font-weight: bold;
                padding: 8px;
            }
        """)

        dummy_data = [
            ["PB001", "08:00", "10:30", "1200", "Completed"],
            ["PB002", "10:30", "13:00", "1150", "In Progress"],
            ["PB003", "13:00", "15:30", "1300", "Pending"],
            ["PB004", "15:30", "18:00", "1270", "Scheduled"],
            ["PB005", "18:00", "20:30", "1100", "Completed"],
            ["PB006", "20:30", "23:00", "1250", "In Progress"],
            ["PB007", "23:00", "01:30", "1400", "Pending"],
            ["PB008", "01:30", "04:00", "1350", "Scheduled"],
            ["PB009", "04:00", "06:30", "1280", "Completed"],
            ["PB010", "06:30", "08:00", "1220", "In Progress"],
            ["PB011", "08:00", "10:30", "1200", "Completed"],
            ["PB012", "10:30", "13:00", "1150", "In Progress"],
            ["PB013", "13:00", "15:30", "1300", "Pending"],
            ["PB014", "15:30", "18:00", "1270", "Scheduled"],
            ["PB015", "18:00", "20:30", "1100", "Completed"],
            ["PB016", "20:30", "23:00", "1250", "In Progress"]
        ]

        for row, rowData in enumerate(dummy_data):
            for col, cellData in enumerate(rowData):
                item = QTableWidgetItem(cellData)
                item.setTextAlignment(Qt.AlignCenter)

                if col == 4:
                    if cellData == "Completed":
                        item.setText("Completed ✅")
                        bold_font = QFont()
                        bold_font.setBold(True)
                        item.setFont(bold_font)
                    elif cellData == "In Progress":
                        item.setText("🔄 In Progress")
                        bold_font = QFont()
                        bold_font.setBold(True)
                        item.setFont(bold_font)
                        item.setBackground(QColor("#4A9179"))
                    elif cellData == "Pending":
                        item.setText("⚠ Pending")
                        bold_font = QFont()
                        bold_font.setBold(True)
                        item.setFont(bold_font)
                        item.setBackground(QColor("#40E0D0"))
                    elif cellData == "Scheduled":
                         item.setText("📅 Scheduled")
                         bold_font = QFont()
                         bold_font.setBold(True)
                         item.setFont(bold_font)
                         item.setBackground(QColor("#008080"))

                table.setItem(row, col, item)

        table.resizeRowsToContents()
        return table

    def create_control_panel(self):
        layout = QHBoxLayout()
        layout.setSpacing(10)
        layout.addStretch(1)

        buttons = ["Start New Batch", "Pause Production", "Export Report"]
        for btn_text in buttons:
            btn = ControlButton(btn_text)
            btn.setMinimumHeight(40)
            btn.setMinimumWidth(150)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #007BFF;
                    color: white;
                    padding: 8px 12px;
                    border-radius: 5px;
                    font-weight: bold;
                    min-width: 120px;
                }
                QPushButton:disabled {
                    background-color: #007BFF;
                    opacity: 0.7;
                }
            """)
            btn.setEnabled(False)
            layout.addWidget(btn)

        layout.addStretch(1)
        return layout


