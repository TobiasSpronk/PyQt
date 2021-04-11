from PyQt5 import QtSql
from PyQt5.QtSql import *

class Database:
    isinstaniated = False
    def __init__(self):
        if not Database.isinstaniated:
            print("Database has been instaniated:")
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName("database/database.db")
            self.db.open()
            Database.isinstaniated = True
        else:
            print("Database has been created")

    def getEmployee_full_info(self):
        query = QSqlQuery()
        query_string = """SELECT    employee.id as "ID", employee.first_name as "First Name", employee.last_name as "Last Name", 
		                            employee.birthday as "Birthday", employee.department_name as "Department Name", 
		                            log_position.position as "Position", log_salary.salary as "Salary" FROM employee, log_position, log_salary 
		                            WHERE employee.id = log_position.employee_id  AND employee.id = log_salary.employee_id 
		                            AND log_salary.date= (SELECT max(date) FROM log_salary WHERE employee_id = employee.id) 
		                            AND log_position.date= (SELECT max(date) FROM log_position WHERE employee_id = employee.id)"""
        res =query.exec(query_string)
        record = query.record()   
        column_number = query.record().count()
        header_list = []
        for i in range(column_number):
            header_list.append(record.field(i).name())

        result_list = []

        while query.next():
            sublist = []
            for i in range(column_number):
                sublist.append(query.value(i))
            result_list.append(sublist)
        return [header_list, result_list]


        