#Import Modules 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout,QLineEdit, QGridLayout
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtGui import QPainter, QLinearGradient, QColor
from PIL import Image, ImageFilter,ImageEnhance

 
class GradientBlueWindow():
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        # Create a painter object
        painter = QPainter(self)

        # Define a vertical gradient
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, QColor(61, 223, 227))
        gradient.setColorAt(1.0, QColor(12,31, 100))

        # Set the gradient as the brush for the painter
        painter.setBrush(gradient)

        # Draw the gradient rectangle covering the entire window
        painter.drawRect(self.rect()) 

class IndusGuardsMain(GradientBlueWindow,QWidget):
    def __init__(self):
        super().__init__()  
        #Set window title and size 
        self.setWindowTitle("Indus Guards") 
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.setFixedSize(screen_width, screen_height)

        # Defining UI elements 
        #####Title with its stylsheet
        self.title = QLabel("Indus\nGuards") 
        self.title.setFont(QFont
                           ("Inter", 
                             25,
                            QFont.Weight.ExtraBold)
                           )
        self.title.setStyleSheet("color: white;") 

        #####Home Text , about Text , settings Text  with its stylsheet
        self.home_text = QLabel("Home")
        self.about_text = QLabel("About")
        self.settings_text = QLabel("Settings") 

        self.home_text.setFont(QFont("Inter", 12, QFont.Weight.Bold))
        self.about_text.setFont(QFont("Inter", 12, QFont.Weight.Bold))
        self.settings_text.setFont(QFont("Inter", 12, QFont.Weight.Bold)) 

        self.home_text.setStyleSheet("color: white;")
        self.about_text.setStyleSheet("color: white;")  
        self.settings_text.setStyleSheet("color: white;")

     
        #####Username and password text with its stylsheet
        self.username_text = QLineEdit() 
        self.username_text = QLabel("Username")
        self.username_text.setFont(QFont("Inter", 12, QFont.Weight.Bold))
        self.username_text.setStyleSheet("color: white;")
        self.username_text.setContentsMargins(5, 5, 0, 0) 

        self.password_text = QLineEdit()
        self.password_text = QLabel("Password")
        self.password_text.setFont(QFont("Inter", 12, QFont.Weight.Bold))
        self.password_text.setStyleSheet("color: white;")
        self.password_text.setContentsMargins(5, 5, 0, 0)

        #####Login Pushbutton with its stylsheet
        self.login_button = QPushButton("Login") 
        self.login_button.setFont(QFont("Inter", 12, QFont.Weight.Bold))
        self.login_button.setStyleSheet("background-color: #0D1F64 ; color: white; padding: 5px; border-radius: 10px;")
        self.login_button.setFixedSize(100, 40)
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_button.setToolTip("Click to login")

        #####Quotes with its stylsheet
        self.quote1_text = QLabel("Crafting") 
        self.quote1_text.setFont(QFont("Inter", 40, QFont.Weight.Bold))
        self.quote1_text.setStyleSheet("color: white;")
        

        self.quote2_text = QLabel("Efficiency") 
        self.quote2_text.setFont(QFont("Inter",40, QFont.Weight.Bold))
        self.quote2_text.setStyleSheet("color: white;")


        self.quote3_text = QLabel("Perfecting")
        self.quote3_text.setFont(QFont("Inter", 40, QFont.Weight.Bold))
        self.quote3_text.setStyleSheet("color: white;")

        self.quote4_text = QLabel("Production")
        self.quote4_text.setFont(QFont("Inter", 40, QFont.Weight.Bold))
        self.quote4_text.setStyleSheet("color: white;")



        #####Picture box with its stylsheet 
        master_layout = QVBoxLayout() 
        grid = QGridLayout()
        grid.addWidget(self.title, 0, 0 , alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        grid.addWidget(self.username_text,1, 0)  
        grid.addWidget(self.password_text,2,0) 
        grid.addWidget(self.login_button,3,0)
        grid.addWidget(self.quote1_text,4,0)
        grid.addWidget(self.quote2_text,5,0)
        grid.addWidget(self.quote3_text,6,0) 
        grid.addWidget(self.quote4_text,6,1)
        grid.addWidget(self.home_text,0,1,  alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        grid.addWidget(self.about_text,0,1, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)     
        grid.addWidget(self.settings_text,0,1, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)  
        image_path = "Landing.jpg" 
        image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            image_label.setPixmap(pixmap) 
            image_label.setScaledContents(True)  # Make the image scale to fit the label
        else:
            image_label.setText("Image not found") 
        image_label.setStyleSheet(
            "border: 2px ;"
            "border-radius: 30px;" 
            "background-color: white;"
            "border-color: white;"
            "border-style: solid;"
            "border-width: 2px;"
            "padding: 10px;"
            "width: 400px;"
            "height: 400px;"    
        ) 
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        grid.addWidget(image_label, 1,1)
        
        master_layout.addLayout(grid)
        self.setLayout(master_layout)   


#Events

if __name__ == "__main__":
    app = QApplication([])
    # Create and display the main window
    main_window = IndusGuardsMain() 
    main_window.setWindowTitle("Indus Guards")
    main_window.show()
    # Execute the application
    app.exec()
