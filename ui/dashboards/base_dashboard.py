"""
Base Dashboard Module - Version 2.0 (May 2025)
Changes:
- Modified navigation bar behavior
- Updated styling for disabled state
"""

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QLinearGradient, QColor
from PyQt5.QtCore import pyqtSignal

class BaseDashboard(QWidget):
    switch_dashboard = pyqtSignal(str)  # Signal to switch dashboards

    def __init__(self, is_admin=False):
        super().__init__()
        self.is_admin = is_admin
        self.init_ui()

    def init_ui(self):
        """Initialize UI components (to be overridden in subclasses)"""
        pass

    def create_nav_bar(self):
        """Create navigation bar for admin users"""
        nav_layout = QHBoxLayout()
        nav_layout.setSpacing(10)

        nav_style = """
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                padding: 8px 15px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #007BFF;
            }
            QPushButton:checked {
                background-color: #007BFF;
            }
        """

        buttons = [
            ("🏭 Production", "production"),
            ("🔧 Maintenance", "maintenance"),
            ("📊 Analysis", "analysis"),
            ("⚙️ Industrial Lines", "industrial")
        ]

        for text, role in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(nav_style)
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, r=role: self.switch_dashboard.emit(r))
            nav_layout.addWidget(btn)

        nav_layout.addStretch()
        return nav_layout

    def paintEvent(self, event):
        """Draw a diagonal gradient background"""
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, QColor(61, 223, 227))  # Cyan
        gradient.setColorAt(1.0, QColor(12, 31, 100))   # Dark Blue
        painter.setBrush(gradient)
        painter.drawRect(self.rect())