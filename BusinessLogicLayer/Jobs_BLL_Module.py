from DataAccessLayer.Jobs_DAL_Module import Jobs_DAL
from Model.JobModel import JobModelClass


class Jobs_BLL:
    def registerJob(self, jobObject: JobModelClass):
        jobsDAL_Object = Jobs_DAL()
        jobsDAL_Object.registerJob(jobObject)

    def getJobList(self):
        jobDAL_Object = Jobs_DAL()
        return jobDAL_Object.getJobList()

    def deleteJob(self, job_id:str):
        jobsDAL_Object = Jobs_DAL()
        jobsDAL_Object.deleteJob(job_id)

    def updateJob(self, jobObject: JobModelClass):
        jobsDAL_Object = Jobs_DAL()
        jobsDAL_Object.updateJob(jobObject)
