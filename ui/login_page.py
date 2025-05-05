from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QPainter, QLinearGradient, QColor
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class LoginPage(QWidget):
    login_success = pyqtSignal(str)  # Emits user role

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("background-color: white; border-radius: 5px; padding: 6px;")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet("background-color: white; border-radius: 5px; padding: 6px;")

        login_btn = QPushButton("Login")
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        login_btn.clicked.connect(self.handle_login)

        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_btn)
        self.setLayout(layout)

    def paintEvent(self, event):
        """Draw the same diagonal gradient as the dashboards"""
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, QColor(61, 223, 227))
        gradient.setColorAt(1.0, QColor(12, 31, 100))
        painter.setBrush(gradient)
        painter.drawRect(self.rect())

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "pass":
            self.login_success.emit("production")
            self.login_success.emit("maintenance")
            self.login_success.emit("manufacturing")
        elif username == "Maintenance" and password == "pass1":
            self.login_success.emit("maintenance")
        elif username == "operator" and password == "pass":
            self.login_success.emit("operator")
        else:   
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Invalid credentials")
            msg.setInformativeText("Please check your username and password.")
            msg.setWindowTitle("Login Failed")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setStyleSheet("background-color: #0C1F64; color: white;")
            msg.exec_()