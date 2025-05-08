import sys
import sqlite3
import time
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QComboBox, 
    QLabel, QPushButton, QFrame, QHBoxLayout, QDialog, QLineEdit, QMessageBox)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from collections import Counter
from .base_dashboard import BaseDashboard

class IndustrialLinesDashboard(BaseDashboard):
    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # Add navigation bar for admin users
        if self.is_admin:
            main_layout.addLayout(self.create_nav_bar())

        # Initialize database
        self.init_database()

        # === Header ===
        header = QLabel("🏭 Industrial Lines Dashboard")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        main_layout.addWidget(header)

        # Machine content
        self.content = MachineContent()
        main_layout.addWidget(self.content)
        
        self.setLayout(main_layout)

    def init_database(self):
        # Database initialization
        self.conn = sqlite3.connect("machines.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS machines (
            name TEXT PRIMARY KEY,
            status TEXT,
            function TEXT,
            commissioning TEXT,
            maintenance TEXT
        )
        """)
        self.conn.commit()

        # Add sample machines if table is empty
        self.cursor.execute("SELECT COUNT(*) FROM machines")
        if self.cursor.fetchone()[0] == 0:
            machines_sample = [
                ("Laser Marking", "In production", "Marking", "12/10/2012", "15/2/2024"),
                ("Welding", "In pause", "Welding parts", "05/08/2015", "10/3/2024"),
                ("Cutting", "In maintenance", "Precision cut", "20/04/2018", "01/4/2024"),
                ("Packing", "Poste change", "Packing units", "01/01/2020", "12/5/2024"),
                ("Polishing", "In production", "Surface polish", "15/07/2019", "10/1/2024"),
            ]
            for m in machines_sample:
                self.cursor.execute("INSERT OR IGNORE INTO machines VALUES (?, ?, ?, ?, ?)", m)
            self.conn.commit()

class MachineContent(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
       
        # Machine dropdown
        self.machine_menu = QComboBox()
        self.machine_menu.setStyleSheet("""
            QComboBox {
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                padding: 8px;
                border-radius: 5px;
                font-size: 14px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
            }
        """)
        self.machine_menu.currentIndexChanged.connect(self.update_machine_info)
        self.layout.addWidget(self.machine_menu)
       
        # Info frame
        info_frame = QFrame()
        info_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                padding: 15px;
            }
        """)
        info_layout = QVBoxLayout()

        # Status labels with styling
        self.status_label = QLabel("Status: ")
        self.time_label = QLabel("Time: ")
        self.function_label = QLabel("Function: ")
        self.commissioning_label = QLabel("Commissioning: ")
        self.maintenance_label = QLabel("Maintenance: ")

        for label in [self.status_label, self.time_label, self.function_label, 
                     self.commissioning_label, self.maintenance_label]:
            label.setStyleSheet("color: white; font-size: 14px;")
            info_layout.addWidget(label)

        info_frame.setLayout(info_layout)
        self.layout.addWidget(info_frame)

        # Graph frame
        self.graph_frame = QFrame()
        self.graph_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                padding: 15px;
            }
        """)
        # Initialize the layout for graph_frame
        self.graph_frame.setLayout(QVBoxLayout())
        self.layout.addWidget(self.graph_frame)

        # Control buttons
        button_layout = QHBoxLayout()
        buttons = [
            ("⬅️ Previous", self.previous_machine),
            ("➕ Add", self.add_machine_window),
            ("❌ Delete", self.delete_selected_machine),
            ("➡️ Next", self.next_machine)
        ]

        for text, callback in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #007BFF;
                    color: white;
                    padding: 8px 15px;
                    border-radius: 5px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
                QPushButton:pressed {
                    background-color: #004494;
                }
            """)
            btn.clicked.connect(callback)
            button_layout.addWidget(btn)

        self.layout.addLayout(button_layout)
       
        # Refresh button
        self.refresh_button = QPushButton("🔄 Refresh Graph")
        self.refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 8px 15px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.refresh_button.clicked.connect(self.show_graph)
        self.layout.addWidget(self.refresh_button)
       
        self.setLayout(self.layout)

        # Initialize
        self.load_machines()

    def load_machines(self):
        # Connect to database
        conn = sqlite3.connect("machines.db")
        cursor = conn.cursor()
        
        # Get all machine names
        cursor.execute("SELECT name FROM machines")
        machines = cursor.fetchall()
        
        # Update combobox
        self.machine_menu.clear()
        for machine in machines:
            self.machine_menu.addItem(machine[0])
            
        conn.close()
        
        # Update info if there are machines
        if self.machine_menu.count() > 0:
            self.update_machine_info()

    def update_machine_info(self):
        if self.machine_menu.currentText():
            # Connect to database
            conn = sqlite3.connect("machines.db")
            cursor = conn.cursor()
            
            # Get machine info
            cursor.execute("SELECT * FROM machines WHERE name=?", 
                         (self.machine_menu.currentText(),))
            machine = cursor.fetchone()
            
            if machine:
                # Update labels
                self.status_label.setText(f"Status: {machine[1]}")
                self.function_label.setText(f"Function: {machine[2]}")
                self.commissioning_label.setText(f"Commissioning: {machine[3]}")
                self.maintenance_label.setText(f"Maintenance: {machine[4]}")
                self.time_label.setText(f"Time: {time.strftime('%H:%M:%S')}")
                
                # Update graph
                self.show_graph()
            
            conn.close()

    def show_graph(self):
        # Clear previous graph if it exists
        for i in reversed(range(self.graph_frame.layout().count())): 
            self.graph_frame.layout().itemAt(i).widget().setParent(None)

        # Connect to database and count statuses
        conn = sqlite3.connect("machines.db")
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM machines")
        statuses = [row[0] for row in cursor.fetchall()]
        conn.close()

        # Count machines by status
        status_counts = Counter(statuses)

        # Plot bar chart
        plt.style.use('dark_background')
        fig = plt.figure(figsize=(6, 4), facecolor='none')
        ax = fig.add_subplot(111)
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)

        labels = list(status_counts.keys())
        values = list(status_counts.values())
        bars = ax.bar(labels, values, color='#00C5CD')

        # Add status text above each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, str(yval), 
                    ha='center', va='bottom', color='white', fontsize=10, fontweight='bold')

        # Set title and labels with reduced font sizes
        ax.set_title('Machines by Status', color='white', pad=20, fontsize=10, fontweight='bold')  # Reduced font size
        ax.set_ylabel('Number of Machines', color='white', fontsize=8, labelpad=10)  # Reduced font size
        ax.tick_params(axis='x', colors='white', labelsize=8)  # Reduced font size
        ax.tick_params(axis='y', colors='white', labelsize=8)  # Reduced font size

        # Make the x-axis labels horizontal
        plt.xticks(rotation=0, ha='center')

        # Add gridlines and adjust spines
        ax.grid(True, axis='y', color='white', alpha=0.2, linestyle='--')
        for spine in ax.spines.values():
            spine.set_color('white')

        # Resize the canvas to fit all the labels
        canvas = FigureCanvas(fig)
        canvas.setStyleSheet("background-color: transparent;")
        self.graph_frame.layout().addWidget(canvas)
        canvas.draw()

    def previous_machine(self):
        current_index = self.machine_menu.currentIndex()
        if current_index > 0:
            self.machine_menu.setCurrentIndex(current_index - 1)

    def next_machine(self):
        current_index = self.machine_menu.currentIndex()
        if current_index < self.machine_menu.count() - 1:
            self.machine_menu.setCurrentIndex(current_index + 1)

    def delete_selected_machine(self):
        if self.machine_menu.currentText():
            reply = QMessageBox.question(self, 'Delete Machine', 
                                       f'Are you sure you want to delete {self.machine_menu.currentText()}?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                conn = sqlite3.connect("machines.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM machines WHERE name=?", 
                             (self.machine_menu.currentText(),))
                conn.commit()
                conn.close()
                self.load_machines()

    def add_machine_window(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add New Machine")
        layout = QVBoxLayout()
        
        # Input fields
        name_input = QLineEdit()
        name_input.setPlaceholderText("Machine Name")
        status_input = QLineEdit()
        status_input.setPlaceholderText("Status")
        function_input = QLineEdit()
        function_input.setPlaceholderText("Function")
        commissioning_input = QLineEdit()
        commissioning_input.setPlaceholderText("Commissioning Date (DD/MM/YYYY)")
        maintenance_input = QLineEdit()
        maintenance_input.setPlaceholderText("Maintenance Date (DD/MM/YYYY)")
        
        # Add fields to layout
        for widget in [name_input, status_input, function_input, 
                      commissioning_input, maintenance_input]:
            layout.addWidget(widget)
        
        # Add button
        add_button = QPushButton("Add Machine")
        add_button.clicked.connect(lambda: self.add_machine(
            name_input.text(), status_input.text(), 
            function_input.text(), commissioning_input.text(),
            maintenance_input.text(), dialog
        ))
        layout.addWidget(add_button)
        
        dialog.setLayout(layout)
        dialog.exec_()

    def add_machine(self, name, status, function, commissioning, maintenance, dialog):
        if all([name, status, function, commissioning, maintenance]):
            conn = sqlite3.connect("machines.db")
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO machines VALUES (?, ?, ?, ?, ?)",
                             (name, status, function, commissioning, maintenance))
                conn.commit()
                self.load_machines()
                dialog.accept()
            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Error", "Machine name already exists!")
            finally:
                conn.close()
        else:
            QMessageBox.warning(self, "Error", "Please fill all fields!")
