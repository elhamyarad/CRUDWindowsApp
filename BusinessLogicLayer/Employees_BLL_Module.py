from DataAccessLayer.Employees_DAL_Module import  Employees_DAL
from Model.EmployeeModel import EmployeeModelClass


class Employees_BLL:
    def getJobList(self):
        EmployeesDAL_Object = Employees_DAL()
        return EmployeesDAL_Object.getJobList()

    def getPublisherList(self):
        EmployeesDAL_Object = Employees_DAL()
        return EmployeesDAL_Object.getPublisherList()

    def registerEmployee(self, EmployeeObject: EmployeeModelClass):
        EmployeesDAL_Object = Employees_DAL()
        EmployeesDAL_Object.registerEmployee(EmployeeObject)

    def getEmployeeList(self):
        EmployeeDAL_Object = Employees_DAL()
        return EmployeeDAL_Object.getEmployeeList()

    def deleteEmployee(self, emp_Id: str):
        EmployeesDAL_Object = Employees_DAL()
        EmployeesDAL_Object.deleteEmployee(emp_Id)

    def updateEmployee(self, EmployeeObject: EmployeeModelClass):
        EmployeesDAL_Object = Employees_DAL()
        EmployeesDAL_Object.updateEmployee(EmployeeObject)
