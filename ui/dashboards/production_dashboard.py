from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget,
    QPushButton, QHeaderView, QFrame, QProgressBar, QLabel,
    QToolTip, QComboBox, QSpacerItem, QSizePolicy, QStackedWidget 
) 
from PyQt5.QtChart import QChartView, QLineSeries, QChart, QBarSeries,QBarSet, QCategoryAxis, QChart, QValueAxis
from PyQt5.QtGui import QColor, QFont, QPixmap, QPainter, QLinearGradient
from PyQt5.QtCore import Qt, QTimer, QDate, QTime, QMargins
from ui.dashboards.base_dashboard import BaseDashboard
from PyQt5.QtWidgets import QTableWidgetItem

from .page1 import Page1
from .page2 import Page2

class ProductionDashboard(BaseDashboard):
    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # === Header ===
        header = QLabel("🏭 Production Dashboard")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        main_layout.addWidget(header)

        # === Stacked Pages ===
        self.stacked_pages = QStackedWidget()

        # Page 1 - KPIs, Chart
        self.page1 = Page1()
        self.stacked_pages.addWidget(self.page1)

        # Page 2 - Table, Alerts
        self.page2 = Page2()
        self.stacked_pages.addWidget(self.page2)

        main_layout.addWidget(self.stacked_pages)

        # Navigation Arrows
        nav_layout = QHBoxLayout()
        nav_layout.addStretch(1)

        self.btn_prev = QPushButton("⮜")  # Left arrow
        self.btn_next = QPushButton("⮞")  # Right arrow

        arrow_style = """
            QPushButton {
                font-size: 20px;
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                padding: 8px 12px;
                border-radius: 5px;
                min-width: 40px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #007BFF;
            }
            QPushButton:disabled {
                background-color: rgba(255, 255, 255, 0.05);
                color: rgba(255, 255, 255, 0.3);
            }
        """
        self.btn_prev.setStyleSheet(arrow_style)
        self.btn_next.setStyleSheet(arrow_style)

        self.btn_prev.clicked.connect(self.navigate_previous)
        self.btn_next.clicked.connect(self.navigate_next)

        nav_layout.addWidget(self.btn_prev)
        nav_layout.addWidget(self.btn_next)
        nav_layout.addStretch(1)

        main_layout.addLayout(nav_layout)
        self.setLayout(main_layout)

        self.update_navigation_buttons()

    def navigate_previous(self):
        current_index = self.stacked_pages.currentIndex()
        if current_index > 0:
            self.stacked_pages.setCurrentIndex(current_index - 1)
            self.update_navigation_buttons()

    def navigate_next(self):
        current_index = self.stacked_pages.currentIndex()
        if current_index < 1:
            self.stacked_pages.setCurrentIndex(current_index + 1)
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        index = self.stacked_pages.currentIndex()
        self.btn_prev.setEnabled(index > 0)
        self.btn_next.setEnabled(index < 1) 
