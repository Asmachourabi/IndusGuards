from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QFrame, 
    QHBoxLayout, QCalendarWidget, QTableWidget, QHeaderView, QTableWidgetItem)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QColor
from .custom_widget import CustomProgressBar

class MaintenancePage1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Equipment Health Overview
        layout.addLayout(self.create_health_overview())
        
        # Calendar and Overdue Items
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.create_calendar_section(), 2)
        bottom_layout.addWidget(self.create_overdue_section(), 1)
        layout.addLayout(bottom_layout)

        self.setLayout(layout)

    def create_health_overview(self):
        row_layout = QHBoxLayout()
        
        # Equipment Health Cards
        statuses = [
            ("Assembly Line", 95, "#28a745"),
            ("Packaging Unit", 78, "#ffc107"),
            ("Test Station", 65, "#dc3545"),
            ("Robotic Arm", 88, "#17a2b8")
        ]
        
        for name, health, color in statuses:
            health_card = self.create_health_card(name, health, color)
            row_layout.addWidget(health_card)
        
        return row_layout

    def create_health_card(self, name, health, color):
        card = QFrame()
        card.setStyleSheet(f"""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
            border-left: 5px solid {color};
        """)
        
        layout = QVBoxLayout()
        
        name_label = QLabel(name)
        name_label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        
        health_bar = CustomProgressBar()
        health_bar.setMaximum(100)
        health_bar.setValue(health)
        health_bar.setStyleSheet(f"""
            QProgressBar {{
                border-radius: 8px;
                background-color: rgba(255, 255, 255, 0.1);
                text-align: center;
                font-weight: bold;
                color: white;
            }}
            QProgressBar::chunk {{
                background-color: {color};
                border-radius: 4px;
            }}
        """)
        
        layout.addWidget(name_label)
        layout.addWidget(health_bar)
        card.setLayout(layout)
        
        return card

    def create_calendar_section(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        
        title = QLabel("📅 Maintenance Schedule")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        
        calendar = QCalendarWidget()
        calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: transparent;
                color: white;
            }
            QCalendarWidget QTableView {
                background-color: transparent;
                selection-background-color: #007BFF;
                selection-color: white;
            }
            QCalendarWidget QMenu {
                background-color: #0C1F64;
                color: white;
            }
        """)
        
        layout.addWidget(title)
        layout.addWidget(calendar)
        frame.setLayout(layout)
        return frame

    def create_overdue_section(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        
        title = QLabel("⚠️ Overdue Tasks (3%)")
        title.setStyleSheet("color: #dc3545; font-size: 18px; font-weight: bold;")
        
        table = QTableWidget(4, 2)
        table.setHorizontalHeaderLabels(["Equipment", "Days Overdue"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setStyleSheet("""
            QTableWidget {
                background-color: transparent;
                color: white;
                border: none;
            }
            QHeaderView::section {
                background-color: transparent;
                color: #00C5CD;
                font-weight: bold;
                padding: 8px;
            }
        """)
        
        overdue_items = [
            ("Test Station #2", "5"),
            ("Conveyor Belt A", "3"),
            ("Hydraulic Press", "2"),
            ("Control Panel B", "1")
        ]
        
        for row, (equipment, days) in enumerate(overdue_items):
            table.setItem(row, 0, QTableWidgetItem(equipment))
            table.setItem(row, 1, QTableWidgetItem(days))
            table.item(row, 1).setForeground(QColor("#dc3545"))
        
        layout.addWidget(title)
        layout.addWidget(table)
        frame.setLayout(layout)
        return frame