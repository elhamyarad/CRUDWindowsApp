from DataAccessLayer.Publishers_DAL_Module import Publishers_DAL
from Model.PublisherModel import PublisherModelClass


class Publishers_BLL:
    def registerPublisher(self, publisherObject: PublisherModelClass):
        publishersDAL_Object = Publishers_DAL()
        publishersDAL_Object.registerPublisher(publisherObject)

    def getPublisherList(self):
        publisherDAL_Object = Publishers_DAL()
        return publisherDAL_Object.getPublisherList()

    def deletePublisher(self, pub_id:str):
        publishersDAL_Object = Publishers_DAL()
        publishersDAL_Object.deletePublisher(pub_id)

    def updatePublisher(self, publisherObject: PublisherModelClass):
        publishersDAL_Object = Publishers_DAL()
        publishersDAL_Object.updatePublisher(publisherObject)
