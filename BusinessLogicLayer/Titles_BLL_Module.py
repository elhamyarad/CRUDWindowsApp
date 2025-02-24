from DataAccessLayer.Titles_DAL_Module import  Titles_DAL
from Model.TitlesModel import TitlesModelClass


class Titles_BLL:
    def getTypesList(self):
        TitlesDAL_Object = Titles_DAL()
        return TitlesDAL_Object.getTypesList()

    def getAuthorList(self):
        TitlesDAL_Object = Titles_DAL()
        return TitlesDAL_Object.getAuthorList()

    def getPublishersList(self):
        TitlesDAL_Object = Titles_DAL()
        return TitlesDAL_Object.getPublishersList()

    def registerTitle(self, TitleObject: TitlesModelClass):
        TitlesDAL_Object = Titles_DAL()
        TitlesDAL_Object.registerTitle(TitleObject)

    def getTitleList(self):
        TitleDAL_Object = Titles_DAL()
        return TitleDAL_Object.getTitleList()

    def deleteTitle(self, title_Id: str):
        TitlesDAL_Object = Titles_DAL()
        TitlesDAL_Object.deleteTitle(title_Id)

    def deleteTitleAuthor(self, title_Id: str, au_Id: str):
        TitleAuthor_Object = Titles_DAL()
        TitleAuthor_Object.deleteTitleAuthor(title_Id, au_Id)

    def addTitleAuthor(self, au_Id: str, title_Id: str, au_ord: int, royaltyper: int):
        TitleAuthor_Object = Titles_DAL()
        TitleAuthor_Object.addTitleAuthor(au_Id, title_Id, au_ord, royaltyper)

    def updateTitle(self, TitleObject: TitlesModelClass):
        TitlesDAL_Object = Titles_DAL()
        TitlesDAL_Object.updateTitle(TitleObject)

    def getTitleAuthor(self):
        TitleAuthorDAL_Object = Titles_DAL()
        return TitleAuthorDAL_Object.getTitleAuthor()
