class Employee:
    def __init__(self,emp_name,emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def getdetails(self):
        print("Name :",self.emp_name)
        print("Epmloyee ID :",self.emp_id)

class QA(Employee):
    def __init__(self,emp_dept,emp_name,emp_id):
        self.emp_dept = emp_dept
        Employee .__init__(self, emp_name, emp_id)

    def getdept(self):
        print("Department :",self.emp_dept)

class DEV(Employee):
    def __init__(self,emp_dept,emp_name,emp_id):
        self.emp_dept = emp_dept
        Employee .__init__(self, emp_name, emp_id)

    def getdept(self):
        print("Department :",self.emp_dept)

employee1 = QA('Automation', 'Ayub', '73201')
employee1.getdetails()
employee1.getdept()
employee2 = DEV('Development', 'Renatta', '43981')
employee2.getdetails()
employee2.getdept()
