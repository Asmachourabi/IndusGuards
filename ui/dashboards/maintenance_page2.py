"""
Maintenance Page 2 Module - Version 2.0 (May 2025)
Changes:
- Disabled control panel buttons while maintaining visual appearance
- Updated button styling with opacity for disabled state
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QFrame, 
    QHBoxLayout, QTableWidget, QHeaderView, QTableWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont
from .custom_widget import ControlButton

class MaintenancePage2(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Maintenance History Log
        layout.addWidget(self.create_history_log())
        
        # Alert Resolution Section
        layout.addWidget(self.create_alert_section())
        
        # Control Panel
        layout.addLayout(self.create_control_panel())

        self.setLayout(layout)

    def create_history_log(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        
        title = QLabel("📋 Maintenance History")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        
        table = QTableWidget(6, 4)
        table.setHorizontalHeaderLabels(["Date", "Equipment", "Type", "Technician"])
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
        
        history_data = [
            ("2025-05-07", "Assembly Line", "Preventive", "John Smith"),
            ("2025-05-06", "Test Station #2", "Repair", "Maria Garcia"),
            ("2025-05-06", "Robotic Arm", "Calibration", "Alex Wong"),
            ("2025-05-05", "Packaging Unit", "Inspection", "Sarah Johnson"),
            ("2025-05-04", "Control Panel B", "Repair", "John Smith"),
            ("2025-05-03", "Conveyor Belt A", "Preventive", "Maria Garcia")
        ]
        
        for row, (date, equipment, type_, tech) in enumerate(history_data):
            table.setItem(row, 0, QTableWidgetItem(date))
            table.setItem(row, 1, QTableWidgetItem(equipment))
            table.setItem(row, 2, QTableWidgetItem(type_))
            table.setItem(row, 3, QTableWidgetItem(tech))
            
            if type_ == "Repair":
                table.item(row, 2).setForeground(QColor("#dc3545"))
            elif type_ == "Preventive":
                table.item(row, 2).setForeground(QColor("#28a745"))
            
        layout.addWidget(title)
        layout.addWidget(table)
        frame.setLayout(layout)
        return frame

    def create_alert_section(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        
        title = QLabel("🚨 Active Alerts")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        
        table = QTableWidget(4, 4)
        table.setHorizontalHeaderLabels(["Time", "Equipment", "Alert", "Status"])
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
        
        alert_data = [
            ("09:15", "Test Station #2", "High Temperature", "🔴 Critical"),
            ("08:45", "Conveyor Belt A", "Speed Variance", "🟡 Pending"),
            ("08:30", "Assembly Line", "Pressure Low", "🟢 Resolved"),
            ("08:00", "Packaging Unit", "Material Low", "🟡 Pending")
        ]
        
        for row, (time, equipment, alert, status) in enumerate(alert_data):
            table.setItem(row, 0, QTableWidgetItem(time))
            table.setItem(row, 1, QTableWidgetItem(equipment))
            table.setItem(row, 2, QTableWidgetItem(alert))
            table.setItem(row, 3, QTableWidgetItem(status))
            
            status_color = "#dc3545" if "Critical" in status else "#ffc107" if "Pending" in status else "#28a745"
            table.item(row, 3).setForeground(QColor(status_color))
            
        layout.addWidget(title)
        layout.addWidget(table)
        frame.setLayout(layout)
        return frame

    def create_control_panel(self):
        layout = QHBoxLayout()
        layout.setSpacing(10)
        layout.addStretch(1)

        buttons = ["Schedule Maintenance", "Generate Report", "Clear Resolved"]
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