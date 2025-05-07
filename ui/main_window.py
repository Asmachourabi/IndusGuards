from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication
from ui.login_page import LoginPage
from ui.dashboards.production_dashboard import ProductionDashboard
from ui.dashboards.maintenance_dashboard import MaintenanceDashboard
from ui.dashboards.analysis_dashboard import AnalysisDashboard
from ui.dashboards.industrial_lines import IndustrialLinesDashboard

class IndustrialApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Indus Guards")
        self.set_window_to_screen_size()
        self.current_user_role = None

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Initialize pages
        self.login_page = LoginPage()
        
        # Initialize dashboards with is_admin=False by default
        self.production_dashboard = ProductionDashboard(is_admin=False)
        self.maintenance_dashboard = MaintenanceDashboard(is_admin=False)
        self.analysis_dashboard = AnalysisDashboard(is_admin=False)
        self.industrial_lines_dashboard = IndustrialLinesDashboard(is_admin=False)

        # Connect dashboard switching signals
        self.production_dashboard.switch_dashboard.connect(self.switch_dashboard)
        self.maintenance_dashboard.switch_dashboard.connect(self.switch_dashboard)
        self.analysis_dashboard.switch_dashboard.connect(self.switch_dashboard)
        self.industrial_lines_dashboard.switch_dashboard.connect(self.switch_dashboard)

        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.production_dashboard)
        self.stacked_widget.addWidget(self.maintenance_dashboard)
        self.stacked_widget.addWidget(self.analysis_dashboard)
        self.stacked_widget.addWidget(self.industrial_lines_dashboard)

        # Connect login signal
        self.login_page.login_success.connect(self.handle_login)
        
        # Start with login page
        self.stacked_widget.setCurrentIndex(0)

    def handle_login(self, user_role):
        self.current_user_role = user_role
        is_admin = user_role == "admin"
        
        # Create new dashboard instances with correct admin status
        self.stacked_widget.removeWidget(self.production_dashboard)
        self.stacked_widget.removeWidget(self.maintenance_dashboard)
        self.stacked_widget.removeWidget(self.analysis_dashboard)
        self.stacked_widget.removeWidget(self.industrial_lines_dashboard)
        
        self.production_dashboard = ProductionDashboard(is_admin=is_admin)
        self.maintenance_dashboard = MaintenanceDashboard(is_admin=is_admin)
        self.analysis_dashboard = AnalysisDashboard(is_admin=is_admin)
        self.industrial_lines_dashboard = IndustrialLinesDashboard(is_admin=is_admin)
        
        # Reconnect dashboard switching signals
        self.production_dashboard.switch_dashboard.connect(self.switch_dashboard)
        self.maintenance_dashboard.switch_dashboard.connect(self.switch_dashboard)
        self.analysis_dashboard.switch_dashboard.connect(self.switch_dashboard)
        self.industrial_lines_dashboard.switch_dashboard.connect(self.switch_dashboard)
        
        # Add new dashboard instances
        self.stacked_widget.insertWidget(1, self.production_dashboard)
        self.stacked_widget.insertWidget(2, self.maintenance_dashboard)
        self.stacked_widget.insertWidget(3, self.analysis_dashboard)
        self.stacked_widget.insertWidget(4, self.industrial_lines_dashboard)
        
        # Show appropriate dashboard
        if user_role == "admin":
            self.stacked_widget.setCurrentIndex(1)  # Default to Production Dashboard
        elif user_role == "production":
            self.stacked_widget.setCurrentIndex(1)
        elif user_role == "maintenance":
            self.stacked_widget.setCurrentIndex(2)
        elif user_role == "analysis":
            self.stacked_widget.setCurrentIndex(3)
        elif user_role == "industrial":
            self.stacked_widget.setCurrentIndex(4)
        elif user_role == "operator":
            self.stacked_widget.setCurrentIndex(1)

    def switch_dashboard(self, dashboard_type):
        if self.current_user_role == "admin":
            if dashboard_type == "production":
                self.stacked_widget.setCurrentIndex(1)
            elif dashboard_type == "maintenance":
                self.stacked_widget.setCurrentIndex(2)
            elif dashboard_type == "analysis":
                self.stacked_widget.setCurrentIndex(3)
            elif dashboard_type == "industrial":
                self.stacked_widget.setCurrentIndex(4)

    def set_window_to_screen_size(self):
        screen = QApplication.primaryScreen()
        screen_rect = screen.geometry()
        self.setGeometry(screen_rect)