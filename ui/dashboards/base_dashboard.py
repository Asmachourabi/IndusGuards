from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QLinearGradient, QColor

class BaseDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize UI components (to be overridden in subclasses)"""
        pass

    def paintEvent(self, event):
        """Draw a diagonal gradient background"""
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, QColor(61, 223, 227))  # Cyan
        gradient.setColorAt(1.0, QColor(12, 31, 100))   # Dark Blue

        painter.setBrush(gradient)
        painter.drawRect(self.rect())