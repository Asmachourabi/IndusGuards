"""
Login Page Module - Version 2.0 (May 2025)
Changes:
- Added background image support
- Improved login form styling and layout
- Enhanced visual feedback for input fields
- Added semi-transparent overlay gradient
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QVBoxLayout, 
    QLabel, QFrame, QHBoxLayout)
from PyQt5.QtGui import QPainter, QLinearGradient, QColor, QFont, QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os

class LoginPage(QWidget):
    login_success = pyqtSignal(str)  # Emits user role

    def __init__(self):
        super().__init__()
        # Load background image
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(current_dir, 'resources', 'Landing.jpg')
        self.background = QPixmap(image_path)
        self.init_ui()

    def init_ui(self):
        # Main layout with smaller margins
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create a centered frame for the login form
        login_frame = QFrame()
        login_frame.setMaximumWidth(400)
        login_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 0.7);
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
        """)
        
        # Login form layout
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(40, 40, 40, 40)
        form_layout.setSpacing(15)
        
        # Title
        title = QLabel("Indus Guards")
        title.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 28px;
                font-weight: bold;
            }
        """)
        title.setAlignment(Qt.AlignCenter)
        
        # Subtitle
        subtitle = QLabel("Industrial Monitoring System")
        subtitle.setStyleSheet("""
            QLabel {
                color: rgba(255, 255, 255, 0.8);
                font-size: 14px;
            }
        """)
        subtitle.setAlignment(Qt.AlignCenter)
        
        # Input style
        input_style = """
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.15);
                border: 2px solid rgba(255, 255, 255, 0.1);
                border-radius: 8px;
                padding: 10px;
                color: white;
                font-size: 14px;
            }
            QLineEdit:focus {
                background-color: rgba(255, 255, 255, 0.2);
                border: 2px solid #007BFF;
            }
            QLineEdit::placeholder {
                color: rgba(255, 255, 255, 0.5);
            }
        """
        
        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet(input_style)
        
        # Password input
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet(input_style)
        
        # Login button with improved styling
        login_btn = QPushButton("Login")
        login_btn.setCursor(Qt.PointingHandCursor)
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
                border: none;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004494;
            }
        """)
        login_btn.clicked.connect(self.handle_login)
        
        # Add widgets to form layout
        form_layout.addWidget(title)
        form_layout.addWidget(subtitle)
        form_layout.addSpacing(20)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.password_input)
        form_layout.addSpacing(10)
        form_layout.addWidget(login_btn)
        
        # Set the form layout to the frame
        login_frame.setLayout(form_layout)
        
        # Center the frame
        center_layout = QHBoxLayout()
        center_layout.addStretch()
        center_layout.addWidget(login_frame)
        center_layout.addStretch()
        
        # Add the centered frame to the main layout
        layout.addStretch()
        layout.addLayout(center_layout)
        layout.addStretch()
        
        self.setLayout(layout)

    def paintEvent(self, event):
        """Draw background image and overlay"""
        painter = QPainter(self)
        
        # Draw background image
        scaled_background = self.background.scaled(
            self.size(), 
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )
        
        # Calculate position to center the image
        x = (self.width() - scaled_background.width()) // 2
        y = (self.height() - scaled_background.height()) // 2
        painter.drawPixmap(x, y, scaled_background)
        
        # Draw semi-transparent overlay gradient
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, QColor(61, 223, 227, 100))
        gradient.setColorAt(0.5, QColor(37, 127, 164, 100))
        gradient.setColorAt(1.0, QColor(12, 31, 100, 100))
        painter.setBrush(gradient)
        painter.drawRect(self.rect())

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "pass":
            self.login_success.emit("admin")
        elif username == "maintenance" and password == "pass1":
            self.login_success.emit("maintenance")
        elif username == "operator" and password == "pass":
            self.login_success.emit("operator")
        elif username == "analyst" and password == "pass2":
            self.login_success.emit("analysis")
        elif username == "industrial" and password == "pass3":
            self.login_success.emit("industrial")
        else:   
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Invalid credentials")
            msg.setInformativeText("Please check your username and password.")
            msg.setWindowTitle("Login Failed")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setStyleSheet("background-color: #0C1F64; color: white;")
            msg.exec_()