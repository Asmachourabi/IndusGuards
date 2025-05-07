"""
Analysis Page 2 Module - Version 2.0 (May 2025)
Changes:
- Disabled control panel buttons while maintaining visual appearance
- Updated button styling with opacity for disabled state
- Added control buttons for data export and reporting
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QFrame, 
    QHBoxLayout, QTableWidget, QHeaderView, QTableWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtChart import (QChartView, QChart, QPieSeries, QLineSeries,
    QValueAxis, QBarSeries, QBarSet)
from PyQt5.QtGui import QPainter, QColor
from .custom_widget import CustomProgressBar, ControlButton

class AnalysisPage2(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Production Volume and Quality Section
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.create_volume_section(), 1)
        top_layout.addWidget(self.create_quality_section(), 1)
        layout.addLayout(top_layout)
        
        # Performance Metrics
        layout.addWidget(self.create_performance_section())
        
        # Export Controls
        layout.addLayout(self.create_control_panel())

        self.setLayout(layout)

    def create_volume_section(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        
        title = QLabel("📊 Production Volume")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        
        chart = QChart()
        chart.setBackgroundVisible(False)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        
        series = QLineSeries()
        series.setName("Daily Volume")
        
        # Hourly production data
        volume_data = [
            (8, 120), (9, 150), (10, 180), (11, 165),
            (12, 140), (13, 155), (14, 190), (15, 175),
            (16, 160), (17, 145)
        ]
        
        for hour, volume in volume_data:
            series.append(hour, volume)
        
        chart.addSeries(series)
        
        axisX = QValueAxis()
        axisX.setRange(8, 17)
        axisX.setLabelFormat("%d:00")
        axisX.setLabelsColor(Qt.white)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)
        
        axisY = QValueAxis()
        axisY.setRange(0, 200)
        axisY.setLabelFormat("%d")
        axisY.setLabelsColor(Qt.white)
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)
        
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.setStyleSheet("background: transparent;")
        
        layout.addWidget(title)
        layout.addWidget(chart_view)
        frame.setLayout(layout)
        return frame

    def create_quality_section(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        
        title = QLabel("🎯 Quality Metrics")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        
        chart = QChart()
        chart.setBackgroundVisible(False)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        
        series = QPieSeries()
        series.append("Pass", 92)
        series.append("Minor Issues", 6)
        series.append("Major Issues", 2)
        
        # Customize slice colors
        series.slices()[0].setColor(QColor("#28a745"))
        series.slices()[1].setColor(QColor("#ffc107"))
        series.slices()[2].setColor(QColor("#dc3545"))
        
        chart.addSeries(series)
        chart.legend().setVisible(True)
        chart.legend().setLabelColor(Qt.white)
        
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.setStyleSheet("background: transparent;")
        
        layout.addWidget(title)
        layout.addWidget(chart_view)
        frame.setLayout(layout)
        return frame

    def create_performance_section(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        
        title = QLabel("📈 Performance vs Targets")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        
        table = QTableWidget(4, 4)
        table.setHorizontalHeaderLabels(["Metric", "Target", "Actual", "Status"])
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
        
        performance_data = [
            ("Production Rate", "175/hr", "182/hr", "✅ Above Target"),
            ("Quality Score", "95%", "92%", "⚠️ Below Target"),
            ("Efficiency", "90%", "93%", "✅ Above Target"),
            ("Uptime", "98%", "97.5%", "⚠️ Below Target")
        ]
        
        for row, (metric, target, actual, status) in enumerate(performance_data):
            table.setItem(row, 0, QTableWidgetItem(metric))
            table.setItem(row, 1, QTableWidgetItem(target))
            table.setItem(row, 2, QTableWidgetItem(actual))
            table.setItem(row, 3, QTableWidgetItem(status))
            
            status_color = "#28a745" if "Above" in status else "#dc3545"
            table.item(row, 3).setForeground(QColor(status_color))
        
        layout.addWidget(title)
        layout.addWidget(table)
        frame.setLayout(layout)
        return frame

    def create_control_panel(self):
        layout = QHBoxLayout()
        layout.setSpacing(10)
        layout.addStretch(1)

        buttons = ["Export Data", "Print Report", "Share Analysis"]
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