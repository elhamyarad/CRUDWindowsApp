from DataAccessLayer.Authors_DAL_Module import Authors_DAL
from Model.AuthorModel import AuthorModelClass


class Authors_BLL:
    # def getCityList(self):
    #     AuthorsDAL_Object = Authors_DAL()
    #     return AuthorsDAL_Object.getCityList()
    #
    # def getStateList(self):
    #     AuthorsDAL_Object = Authors_DAL()
    #     return AuthorsDAL_Object.getStateList()

    def registerAuthor(self, authorObject: AuthorModelClass):
        authorsDAL_Object = Authors_DAL()
        authorsDAL_Object.registerAuthor(authorObject)

    def getAuthorList(self):
        authorDAL_Object = Authors_DAL()
        return authorDAL_Object.getAuthorList()

    def deleteAuthor(self, auId: str):
        authorsDAL_Object = Authors_DAL()
        authorsDAL_Object.deleteAuthor(auId)

    def updateAuthor(self, authorObject: AuthorModelClass):
        authorsDAL_Object = Authors_DAL()
        authorsDAL_Object.updateAuthor(authorObject)
