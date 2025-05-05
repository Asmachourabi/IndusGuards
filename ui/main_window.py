from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication
from ui.login_page import LoginPage
from ui.dashboards.production_dashboard import ProductionDashboard
#from ui.dashboards.maintenance_dashboard import MaintenanceDashboard

class IndustrialApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indus Guards")
        self.set_window_to_screen_size()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_page = LoginPage()
        self.production_dashboard = ProductionDashboard()
        #self.maintenance_dashboard = MaintenanceDashboard()

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.production_dashboard)
        #self.stacked_widget.addWidget(self.maintenance_dashboard)

        self.login_page.login_success.connect(self.handle_login)

    def handle_login(self, user_role):
        if user_role == "production":
            self.stacked_widget.setCurrentIndex(1)
        elif user_role == "maintenance":
            self.stacked_widget.setCurrentIndex(2) 
    def set_window_to_screen_size(self):
        screen = QApplication.primaryScreen()
        screen_rect = screen.geometry()  # Includes taskbar
        self.setGeometry(screen_rect)