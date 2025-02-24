from DataAccessLayer.Sales_DAL_Module import  Sales_DAL
from Model.SaleModel import SaleModelClass


class Sales_BLL:

    def getStorsList(self):
        SaleDAL_Object = Sales_DAL()
        return SaleDAL_Object.getStorsList()

    def getTitlesList(self):
        SaleDAL_Object = Sales_DAL()
        return SaleDAL_Object.getTitlesList()

    def registerSale(self, SaleObject: SaleModelClass):
        SalesDAL_Object = Sales_DAL()
        SalesDAL_Object.registerSale(SaleObject)

    def getSaleList(self):
        SaleDAL_Object = Sales_DAL()
        return SaleDAL_Object.getSaleList()

    def deleteSale(self, stor_id:str, ord_num:str, title_id:str):
        SalesDAL_Object = Sales_DAL()
        SalesDAL_Object.deleteSale(stor_id, ord_num, title_id)

    def updateSale(self, SaleObject: SaleModelClass):
        SalesDAL_Object = Sales_DAL()
        SalesDAL_Object.updateSale(SaleObject)
