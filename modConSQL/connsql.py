#!/usr/bin/python
"""
    References
        1. INPUT YOUR REFERENCE PAGES
"""
import MySQLdb

class PythonSQL:
    def __init__(self):
        """
            WRITE YOUR DESCIPTION DOWN HERE
        """
        self.dbName = "kernel_apis"
        self.tableName = "apis_in_kernel"

    def connectSQL(self):
        try:
            db = MySQLdb.connect("127.0.0.1", "root", "root", self.dbName)
            cursor = db.cursor()
        except:
            print " SQL Connection Failed."
            break



