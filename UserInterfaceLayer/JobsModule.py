from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import random
from Model.JobModel import JobModelClass

from BusinessLogicLayer.Jobs_BLL_Module import Jobs_BLL


class JobsCRUD:
    def JobsCRUD_FormLoad(self):
        JobsCRUDForm = Tk()
        JobsCRUDForm.title('Job CRUD Form')
        JobsCRUDForm.geometry('900x400')
        x = int(JobsCRUDForm.winfo_screenwidth() // 2 - 900 / 2)
        y = int(JobsCRUDForm.winfo_screenheight() // 2 - 400 / 2)
        JobsCRUDForm.geometry('+{}+{}'.format(x, y))
        JobsCRUDForm.resizable(0, 0)
        JobsCRUDForm.iconbitmap('images/jobs.ico')
        
        JobsCRUDForm_background_image = Image.open('images/backgroundMain.jpg')
        JobsCRUDForm_background_image = JobsCRUDForm_background_image.resize((900, 400))
        bg_image = ImageTk.PhotoImage(JobsCRUDForm_background_image)

        background_label = Label(JobsCRUDForm, image=bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # region Functions
        def registerJob():
            jobBLLObject = Jobs_BLL()
            job_id = ""
            job_desc =txtJobDesc.get()
            min_lvl = txtJobMinLVL.get()
            max_lvl = txtJobMaxLVL.get()

            jobObject = JobModelClass(job_id=job_id, job_desc=job_desc, min_lvl=min_lvl, max_lvl=max_lvl)

            if not txtJobId.get():
                jobBLLObject.registerJob(jobObject)
            resetForm()
            showList()

        def resetForm():
            for widget in lblJobInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)

            txtJobId.set("")

        def checkValidationMinLVL(*args):
            if len(txtJobMinLVL.get()) > 3:
                txtJobMinLVL.set(txtJobMinLVL.get()[:3])

            for minLVL in txtJobMinLVL.get():
                if not minLVL.isnumeric():
                    txtJobMinLVL.set(txtJobMinLVL.get().replace(minLVL, ''))

            if txtJobMinLVL.get() and int(txtJobMinLVL.get()) > 250:
                msg.showerror('Invalid Min Level', 'Your min level must be less than 250!')

        def checkValidationMaxLVL(*args):
            if len(txtJobMaxLVL.get()) > 3:
                txtJobMaxLVL.set(txtJobMaxLVL.get()[:3])

            for maxLVL in txtJobMaxLVL.get():
                if not maxLVL.isnumeric():
                    txtJobMaxLVL.set(txtJobMaxLVL.get().replace(maxLVL, ''))


            if txtJobMaxLVL.get() and int(txtJobMaxLVL.get()) > 250:
                msg.showerror('Invalid Max Level', 'Your max level must be less than 250!')

        def showList(*args):
            from BusinessLogicLayer.Jobs_BLL_Module import Jobs_BLL
            jobBLLObject = Jobs_BLL()
            rows = jobBLLObject.getJobList()
            tvJobList.delete(*tvJobList.get_children())
            rowCount = 0
            for row in rows:
                rowCount += 1
                values = [rowCount]
                for value in row:
                    if value == None:
                        values.append("")
                    else:
                        values.append(value)
                tvJobList.insert("", "end", values=values)

        def onTreeSelect(event):
            resetForm()
            index = tvJobList.selection()
            if index:
                selectedValues = tvJobList.item(index)['values']
                txtJobId.set(selectedValues[1])
                txtJobDesc.set(selectedValues[2])
                txtJobMinLVL.set(selectedValues[3])
                txtJobMaxLVL.set(selectedValues[4])

        def deleteJob():
            job_id = txtJobId.get()
            if job_id:
                msg.askyesno("Delete Warning", "Are you sure?")
            if job_id:
                from BusinessLogicLayer.Jobs_BLL_Module import Jobs_BLL
                jobBLLObject = Jobs_BLL()
                jobBLLObject.deleteJob(job_id)
            showList()

        def updateJob():
            job_id = txtJobId.get()
            job_desc = txtJobDesc.get()
            min_lvl = txtJobMinLVL.get()
            max_lvl = txtJobMaxLVL.get()

            jobObject = JobModelClass(job_id, job_desc, min_lvl, max_lvl)

            if job_id:
                from BusinessLogicLayer.Jobs_BLL_Module import Jobs_BLL
                jobBLLObject = Jobs_BLL()
                jobBLLObject.updateJob(jobObject)

            showList()
            resetForm()

        def BackToHome():
            JobsCRUDForm.destroy()
            from UserInterfaceLayer.MainModule import MainForm
            MainForm().mainFormLoad("","")

        # endregion

        lblBasicInfo = LabelFrame(JobsCRUDForm, text='Basic Information: ', bg='wheat')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        lblJobInfo = LabelFrame(lblBasicInfo, text="Job's Information", bg='wheat')
        lblJobInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10, sticky=NSEW)

        lblJobID = Label(lblJobInfo, text='JobID: ', bg='wheat')
        lblJobID.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtJobId = StringVar()
        lblJobIDValue = Label(lblJobInfo, text='JobIDValue', textvariable=txtJobId, bg='wheat')
        lblJobIDValue.grid(row=0, column=1, padx=10, pady=10)

        lblJobDesc = Label(lblJobInfo, text='JobDesc: ', bg='wheat')
        lblJobDesc.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtJobDesc = StringVar()
        entJobDesc = ttk.Entry(lblJobInfo, textvariable=txtJobDesc, width=40)
        entJobDesc.grid(row=1, column=1, padx=10, pady=10)

        lblJobMinLVL = Label(lblJobInfo, text='JobMinLVL: ', width= 10, bg='wheat')
        lblJobMinLVL.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtJobMinLVL = StringVar()
        txtJobMinLVL.trace('w', checkValidationMinLVL)
        entJobMinLVL = ttk.Entry(lblJobInfo, textvariable=txtJobMinLVL, width=10)
        entJobMinLVL.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lblJobMaxLVL = Label(lblJobInfo, text='JobMaxLVL: ', bg='wheat')
        lblJobMaxLVL.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtJobMaxLVL = StringVar()
        txtJobMaxLVL.trace('w', checkValidationMaxLVL)
        entJobMaxLVL = ttk.Entry(lblJobInfo, textvariable=txtJobMaxLVL, width=10)
        entJobMaxLVL.grid(row=3, column=1, padx=10, pady=10, sticky='w')


        btnRegisterJob = ttk.Button(lblBasicInfo, command=registerJob, text='Register Job', width=16)
        btnRegisterJob.grid(row=8, column=0, padx=70, pady=10, sticky='e')

        btnResetForm = ttk.Button(lblBasicInfo, command=resetForm, text='Reset Form', width=16)
        btnResetForm.grid(row=8, column=0, padx=70, pady=10, sticky='w')

        btnDeleteJob = ttk.Button(lblBasicInfo, command=deleteJob, text='Delete Job', width=16)
        btnDeleteJob.grid(row=9, column=0, padx=70, pady=0, sticky='e')

        btnUpdateJob = ttk.Button(lblBasicInfo, command=updateJob, text='Update Job', width=16)
        btnUpdateJob.grid(row=9, column=0, padx=70, pady=0, sticky='w')

        btnBack = ttk.Button(lblBasicInfo, command=BackToHome, text='Back', width=16)
        btnBack.grid(row=10, column=0, padx=70, pady=10, sticky='n')

        lblJobsList = LabelFrame(JobsCRUDForm, text='Jobs List: ', bg='wheat')
        lblJobsList.grid(row=0, column=1, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        columns = ["Index", "job_id", "job_desc", "min_lvl", "max_lvl"]
        displaycolumns = ["Index", "job_desc", "min_lvl", "max_lvl"]
        tvJobList = ttk.Treeview(lblJobsList, columns=columns, selectmode='browse', show='headings'
                                    , displaycolumns=displaycolumns, height=15, )

        tvJobList.grid(row=0, column=0, padx=10, pady=0, sticky=NSEW)
        tvJobList.bind('<<TreeviewSelect>>', onTreeSelect)

        tvJobList.column("#0", width=0)

        tvJobList.column("Index", width=20, anchor=CENTER)
        tvJobList.heading("Index", text="#", anchor='n')

        tvJobList.column("job_id", width=0)
        tvJobList.heading("job_id", text="jobID")

        tvJobList.column("job_desc", width=150)
        tvJobList.heading("job_desc", text="Job Name", anchor='n')

        tvJobList.column("min_lvl", width=100, anchor=CENTER)
        tvJobList.heading("min_lvl", text="Job Min LVL", anchor='n')

        tvJobList.column("max_lvl", width=100, anchor=CENTER)
        tvJobList.heading("max_lvl", text="Job Max LVL", anchor='n')


        entJobDesc.focus_set()
        showList()
        JobsCRUDForm.mainloop()
