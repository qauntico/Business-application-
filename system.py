from PyQt6.QtWidgets import QMainWindow
from  maingui import Ui_MainWindow
from PyQt6 import QtGui
from dbconnection import *
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


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
        #various pages button
        self.pushButton_2.clicked.connect( lambda: self.mainMenuController( self.pushButton_2 ) )
        self.pushButton_3.clicked.connect( lambda: self.mainMenuController( self.pushButton_3 ) )
        self.pushButton_12.clicked.connect( lambda: self.mainMenuController( self.pushButton_12 ) )
        self.pushButton_9.clicked.connect( lambda: self.mainMenuController( self.pushButton_9 ) )
        self.pushButton_4.clicked.connect( lambda: self.mainMenuController( self.pushButton_4 ) )
        self.pushButton.clicked.connect( lambda: self.mainMenuController( self.pushButton ) )
        self.pushButton_8.clicked.connect( lambda: self.mainMenuController( self.pushButton_8 ) )
        self.pushButton_7.clicked.connect( lambda: self.toggleCenterMenu( self.pushButton_7 ) )
        self.pushButton_5.clicked.connect( lambda: self.toggleCenterMenu( self.pushButton_5 ))
        self.pushButton_6.clicked.connect( lambda: self.toggleCenterMenu(self.pushButton_6 ))
        self.pushButton_10.clicked.connect( self.animateCenterMenuOut )
        #profile icons
        self.pushButton_16.clicked.connect( self.profileOut )
        self.pushButton_14.clicked.connect( self.toggleProfile )
        #menu icons
        self.menuBtn.clicked.connect( self.changeMenuIcon)
        db = databaseConnection()
        self.model = QSqlTableModel( db=db )
        self.tableView_2.setModel( self.model )
        self.model.setTable( "Track" )
        self.model.select()


    def toggleCenterMenu(self, button):
        if self.centerMenuContainer.isVisible() == False:
            self.centerMenuContainer.show()
        self.animateCenterMenuIn( button )

    def animateCenterMenuIn(self, button):
        if button == self.pushButton_7:
            self.stackedWidget.setCurrentIndex(0)
            self.pushButton_7.setStyleSheet('background-color: white;')
            self.pushButton_5.setStyleSheet('background-color: transparent;')
            self.pushButton_6.setStyleSheet('background-color: transparent;')
        if button == self.pushButton_5:
            self.stackedWidget.setCurrentIndex(1)
            self.pushButton_7.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_5.setStyleSheet( 'background-color: white;' )
            self.pushButton_6.setStyleSheet( 'background-color: transparent;' )
        if button == self.pushButton_6:
            self.stackedWidget.setCurrentIndex(2)
            self.pushButton_7.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_5.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_6.setStyleSheet( 'background-color: white;' )

    def animateCenterMenuOut(self):
        self.centerMenuContainer.setVisible( False )
        self.pushButton_7.setStyleSheet( 'background-color: transparent;' )
        self.pushButton_5.setStyleSheet( 'background-color: transparent;' )
        self.pushButton_6.setStyleSheet( 'background-color: transparent;' )

    def toggleProfile(self):
        if self.rightMenuContainer.isVisible():
            self.profileOut()
        else:
            self.profileIn()
    def profileIn(self):
        self.rightMenuContainer.show()
    def profileOut(self):
        self.rightMenuContainer.setVisible( False )
    def mainMenuController(self,button):
        if button == self.pushButton_2:
            self.stackedWidget_3.setCurrentIndex(0)
            self.pushButton_2.setStyleSheet( 'background-color: white;' )
            self.pushButton_3.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_12.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_9.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_4.setStyleSheet( 'background-color: transparent;' )
            self.pushButton.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_8.setStyleSheet( 'background-color: transparent;' )
        if button == self.pushButton_3:
            self.stackedWidget_3.setCurrentIndex(1)
            self.pushButton_2.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_3.setStyleSheet( 'background-color: white;' )
            self.pushButton_12.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_9.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_4.setStyleSheet( 'background-color: transparent;' )
            self.pushButton.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_8.setStyleSheet( 'background-color: transparent;' )
        if button == self.pushButton_12:
            self.stackedWidget_3.setCurrentIndex(2)
            self.pushButton_2.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_3.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_12.setStyleSheet( 'background-color: white;' )
            self.pushButton_9.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_4.setStyleSheet( 'background-color: transparent;' )
            self.pushButton.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_8.setStyleSheet( 'background-color: transparent;' )
        if button == self.pushButton_9:
            self.stackedWidget_3.setCurrentIndex(4)
            self.pushButton_2.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_3.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_12.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_9.setStyleSheet( 'background-color: white;' )
            self.pushButton_4.setStyleSheet( 'background-color: transparent;' )
            self.pushButton.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_8.setStyleSheet( 'background-color: transparent;' )
        if button == self.pushButton_4:
            self.stackedWidget_3.setCurrentIndex(3)
            self.pushButton_2.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_3.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_12.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_9.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_4.setStyleSheet( 'background-color: white;' )
            self.pushButton.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_8.setStyleSheet( 'background-color: transparent;' )
        if button == self.pushButton:
            self.stackedWidget_3.setCurrentIndex(5)
            self.pushButton_2.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_3.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_12.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_9.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_4.setStyleSheet( 'background-color: transparent;' )
            self.pushButton.setStyleSheet( 'background-color: white;' )
            self.pushButton_8.setStyleSheet( 'background-color: transparent;' )
        if button == self.pushButton_8:
            self.stackedWidget_3.setCurrentIndex(6)
            self.pushButton_2.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_3.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_12.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_9.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_4.setStyleSheet( 'background-color: transparent;' )
            self.pushButton.setStyleSheet( 'background-color: transparent;' )
            self.pushButton_8.setStyleSheet( 'background-color: white;' )

    def changeMenuIcon(self):
        icon = QtGui.QIcon()
        if self.icon == "icons/align-justify.svg":
            self.icon = "icons/chevron-right.svg"
            icon.addPixmap( QtGui.QPixmap(self.icon), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off )
            self.menuBtn.setIcon( icon )
            self.leftMenuContainer.setMaximumWidth(78)
        elif self.icon == "icons/chevron-right.svg":
            self.icon = "icons/align-justify.svg"
            icon.addPixmap( QtGui.QPixmap( self.icon), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off )
            self.menuBtn.setIcon( icon )
            self.leftMenuContainer.setMaximumWidth(200)
