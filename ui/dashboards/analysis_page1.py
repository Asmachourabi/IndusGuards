from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QFrame, 
    QHBoxLayout, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtChart import (QChartView, QLineSeries, QChart, QBarSeries,
    QBarSet, QValueAxis, QCategoryAxis)
from PyQt5.QtGui import QPainter, QColor
from .custom_widget import CustomProgressBar

class AnalysisPage1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Line Efficiency Section
        layout.addWidget(self.create_efficiency_section())
        
        # Defect Rate Trends
        layout.addWidget(self.create_defect_trends())

        self.setLayout(layout)

    def create_efficiency_section(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        
        title = QLabel("⚡ Line Efficiency")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        
        chart = QChart()
        chart.setBackgroundVisible(False)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        
        series = QBarSeries()
        
        efficiency_data = [
            ("Assembly", 92),
            ("Packaging", 88),
            ("Testing", 95),
            ("Quality", 90)
        ]
        
        bars = QBarSet("Efficiency %")
        bars.append([eff for _, eff in efficiency_data])
        series.append(bars)
        
        chart.addSeries(series)
        
        axisX = QCategoryAxis()
        for i, (name, _) in enumerate(efficiency_data):
            axisX.append(name, i + 0.5)
        axisX.setLabelsColor(Qt.white)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)
        
        axisY = QValueAxis()
        axisY.setRange(0, 100)
        axisY.setLabelFormat("%d%%")
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

    def create_defect_trends(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        
        title = QLabel("📉 Defect Rate Trends")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        
        chart = QChart()
        chart.setBackgroundVisible(False)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        
        series = QLineSeries()
        series.setName("Defect Rate")
        
        # Weekly defect rate data points
        defect_data = [
            (1, 2.8),
            (2, 2.5),
            (3, 2.2),
            (4, 2.3),
            (5, 2.0),
            (6, 1.8),
            (7, 1.5)
        ]
        
        for week, rate in defect_data:
            series.append(week, rate)
        
        chart.addSeries(series)
        
        axisX = QValueAxis()
        axisX.setRange(1, 7)
        axisX.setLabelFormat("Week %d")
        axisX.setLabelsColor(Qt.white)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)
        
        axisY = QValueAxis()
        axisY.setRange(0, 3)
        axisY.setLabelFormat("%.1f%%")
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