from PyQt6.QtWidgets import QMainWindow
from  maingui import Ui_MainWindow



#IMPORTANT VARAIBLES
#maximumsize(width) = 64: leftMenuContainer
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
# Creating the window transitions for the settings window and the profile window
        # self.centerMenuContainer.setMaximumWidth( 0 )
        self.centerMenuContainer.setVisible( False )
        self.rightMenuContainer.setVisible( False )

        self.pushButton_7.clicked.connect( lambda: self.toggleCenterMenu( self.pushButton_7 ) )
        self.pushButton_10.clicked.connect( self.animateCenterMenuOut )
        self.pushButton_16.clicked.connect( self.profileOut )
        self.pushButton_14.clicked.connect( self.toggleProfile )

    def toggleCenterMenu(self, button):
        if self.centerMenuContainer.isVisible():
            self.animateCenterMenuOut()
        else:
            if button == self.pushButton_7:
                self.animateCenterMenuIn( self.pushButton_7 )

    def animateCenterMenuIn(self, buttons):
        if buttons == self.pushButton_7:
            self.centerMenuContainer.show()

    def animateCenterMenuOut(self):
        self.centerMenuContainer.setVisible( False )

    def toggleProfile(self):
        if self.rightMenuContainer.isVisible():
            self.profileOut()
        else:
            self.profileIn()

    def profileIn(self):
        self.rightMenuContainer.show()

    def profileOut(self):
        self.rightMenuContainer.setVisible( False )