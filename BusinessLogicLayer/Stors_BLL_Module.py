from DataAccessLayer.Stors_DAL_Module import Stors_DAL
from Model.StorModel import StorModelClass


class Stors_BLL:
    def registerStor(self, storObject: StorModelClass):
        storsDAL_Object = Stors_DAL()
        storsDAL_Object.registerStor(storObject)

    def getStorList(self):
        storDAL_Object = Stors_DAL()
        return storDAL_Object.getStorList()

    def deleteStor(self, stor_id:str):
        storsDAL_Object = Stors_DAL()
        storsDAL_Object.deleteStor(stor_id)

    def updateStor(self, storObject: StorModelClass):
        storsDAL_Object = Stors_DAL()
        storsDAL_Object.updateStor(storObject)
