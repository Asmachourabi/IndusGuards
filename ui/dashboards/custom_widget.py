from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton 

class CustomProgressBar(QProgressBar):
        def __init__(self):
            super().__init__()
            self.setStyleSheet("""
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
                        stop:0 #00BFFF, stop:1 #007BFF
                    );
                    border-radius: 4px;
                }
            """)

class ControlButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                padding: 8px 12px;
                border-radius: 5px;
                font-weight: bold;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004494;
            }
        """)