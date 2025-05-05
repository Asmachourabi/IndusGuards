from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QProgressBar,QPushButton 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QLinearGradient, QPainter
from PyQt5.QtChart import QChartView, QBarSeries, QBarSet, QCategoryAxis, QValueAxis, QChart

from .custom_widget import CustomProgressBar

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Top Info Row (Shift Total + Current Batch + Progress)
        layout.addLayout(self.create_top_info_row())

        # Line Status Section
        layout.addWidget(self.create_line_status_section())

        # Chart Section
        layout.addWidget(self.create_shift_chart_section())

        self.setLayout(layout)

    def create_top_info_row(self):
        row_layout = QHBoxLayout()
        
        # Shift Total
        shift_total = self.create_info_card("Shift Total", "8,457 pcs", "#00BFFF")
        row_layout.addWidget(shift_total, 1)

        # Current Batch
        current_batch = self.create_info_card("Current Batch", "MAN 005 | Product: 007", "#28a745")
        row_layout.addWidget(current_batch, 1)

        # Progress Bar
        progress_frame = QFrame()
        progress_layout = QVBoxLayout()
        
        label = QLabel("Progress (826/1000)")
        label.setStyleSheet("color: white; font-weight: bold;font-size: 40px;")
        
        progress_bar = CustomProgressBar()
        progress_bar.setMaximum(1000)
        progress_bar.setValue(826) 
        progress_bar.setStyleSheet("""
            QProgressBar {
                border-radius: 8px;
                background-color: rgba(255, 255, 255, 0.1);
                text-align: center;
                font-weight: bold;
                color: white;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #7FFFD4, stop:1 #00C5CD
                );
                border-radius: 4px;
            }
        """) 

        
        progress_layout.addWidget(label)
        progress_layout.addWidget(progress_bar)
        progress_frame.setLayout(progress_layout)
        row_layout.addWidget(progress_frame, 2)
        
        return row_layout

    def create_info_card(self, title, value, color):
        card = QFrame()
        card.setStyleSheet(f"""
            background-color: rgba(255, 255, 255, 0.1);
            font-size: 40px;
            border-radius: 10px;
            padding: 15px;
            border-left: 5px solid {color};
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(5)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("color: white; font-size: 40px; font-weight: bold;")
        
        value_label = QLabel(value)
        value_label.setStyleSheet("color: white; font-size: 18px;")
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        card.setLayout(layout)
        
        return card

    def create_line_status_section(self):
        frame = QFrame()
        frame.setStyleSheet("""
            background-color: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #7FFFD4, stop:1 #0C1F64
                );
            border-radius: 40px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        title = QLabel("⚠️ Line Status")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        lines_layout = QHBoxLayout()
        
        lines = [
            ("PACKAGING LINE ", "⚠", "Low Material"),
            ("ASSEMBLY LINE" , "✅", "Running"),
            (" ELECTRICAL LINE", "🛑", "Stopped")
        ]
        
        for name, icon, status in lines:
            line_widget = self.create_line_status_widget(name, icon, status)
            lines_layout.addWidget(line_widget)
        
        layout.addLayout(lines_layout)
        frame.setLayout(layout)
        return frame

    def create_line_status_widget(self, name, icon, status):
        widget = QFrame()
        widget.setStyleSheet("""
            background-color: rgba(30, 30, 30, 0.7);
            border-radius: 8px;
            padding: 10px;
            margin: 4px;
            color: white;
        """)
        
        layout = QVBoxLayout()
        
        name_label = QLabel(f"🧩 {name}")
        name_label.setStyleSheet("color: #00BFFF; font-weight: bold;")
        
        status_layout = QHBoxLayout()
        
        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 24px; color: white;")
        
        status_text = QLabel(status)
        status_text.setStyleSheet("color: white; font-weight: bold;")
        
        status_layout.addWidget(icon_label)
        status_layout.addWidget(status_text)
        
        layout.addWidget(name_label)
        layout.addLayout(status_layout)
        widget.setLayout(layout)
        return widget

    def create_shift_chart_section(self):
        chart_frame = QFrame()
        chart_frame.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 15px;
        """)
        
        layout = QVBoxLayout()
        title = QLabel("📊 Today's Shift Performance")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        chart_view = self.create_shift_chart()
        layout.addWidget(chart_view)
        chart_frame.setLayout(layout)
        return chart_frame

    def create_shift_chart(self):
        series = QBarSeries()
        
        set_a = QBarSet("Shift A")
        set_b = QBarSet("Shift B")
        
        set_a << 60 << 85 << 35
        set_b << 90 << 60 << 25
        
        series.append(set_a)
        series.append(set_b)
        
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        
        axisX = QCategoryAxis()
        axisX.append("Line 1", 0.0)
        axisX.append("Line 2", 1.0)
        axisX.append("Line 3", 2.0)
        axisX.setTitleText("Production Lines")
        axisX.setTitleBrush(Qt.white)
        axisX.setLabelsBrush(Qt.white)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)
        
        axisY = QValueAxis()
        axisY.setLabelFormat("%d units")
        axisY.setTitleText("Units Produced")
        axisY.setTitleBrush(Qt.white)
        axisY.setLabelsBrush(Qt.white)
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)
        
        chart.setBackgroundVisible(False)
        chart.legend().setVisible(True)
        chart.legend().setLabelColor(Qt.white)
        
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.setStyleSheet("background: transparent;")
        
        return chart_view 
    
   