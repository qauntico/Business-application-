import os
import sys
from PyQt6.QtSql import QSqlDatabase

def databaseConnection():
    basedir = os.path.dirname( __file__ )
    db = QSqlDatabase( "QSQLITE" )
    db.setDatabaseName( os.path.join( basedir, "chinook_Sqlite.db" ) )
    db.open()
    return db
