from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import random
from Model.EmployeeModel import EmployeeModelClass
from BusinessLogicLayer.Employees_BLL_Module import Employees_BLL


class EmployeesCRUD:
    def EmployeesCRUD_FormLoad(self):
        EmployeesCRUDForm = Tk()
        EmployeesCRUDForm.title('Employee CRUD Form')
        EmployeesCRUDForm.geometry('1350x620')
        x = int(EmployeesCRUDForm.winfo_screenwidth() // 2 - 1350 / 2)
        y = int(EmployeesCRUDForm.winfo_screenheight() // 2 - 620 / 2)
        EmployeesCRUDForm.geometry('+{}+{}'.format(x, y))
        EmployeesCRUDForm.resizable(0, 0)
        EmployeesCRUDForm.iconbitmap('images/Employee.ico')

        EmployeesCRUDForm_background_image = Image.open('images/backgroundMain.jpg')
        EmployeesCRUDForm_background_image = EmployeesCRUDForm_background_image.resize((1350, 620))
        bg_image = ImageTk.PhotoImage(EmployeesCRUDForm_background_image)

        background_label = Label(EmployeesCRUDForm, image=bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        jobsDict = dict()
        jobsValueDict = dict()
        publishersDict = dict()
        jobsLVLDict = dict()

        # region Functions
        def getJobList():
            employeeBLLObject = Employees_BLL()
            jobsList = employeeBLLObject.getJobList()

            if len(jobsList) > 0:
                for job in jobsList:
                    if job[1] not in jobsList:
                        jobsDict[job[1]] = job[0]
                        jobsValueDict[job[0]] = job[1]
            return list(jobsDict.keys())

        def getJobsLVLList():
            employeeBLLObject = Employees_BLL()
            jobsList = employeeBLLObject.getJobList()

            if len(jobsList) > 0:
                for job in jobsList:
                    if job[1] not in jobsList and job[2] not in jobsList and job[3] not in jobsList:
                        jobsLVLDict[job[1]] = (job[2], job[3])

            job_title = txtJobTitle.get()
            new_from, new_to = jobsLVLDict[job_title]
            entJobLVL.config(from_=new_from, to=new_to)
            entJobLVL.set(new_from)

        def getPublishersList():
            employeeBLLObject = Employees_BLL()
            publishersList = employeeBLLObject.getPublisherList()

            if len(publishersList) > 0:
                for publishers in publishersList:
                    if publishers[1] not in publishersList:
                        publishersDict[publishers[1]] = publishers[0]

            return list(publishersDict.keys())

        def registerEmployee():
            EmployeeBLLObject = Employees_BLL()
            emp_Id = ""
            if txtminit.get():
                if intSex.get() == 0:
                    emp_Id = (
                        f'{txtFirstName.get()[0].upper()}{txtminit.get().upper()}{txtLastName.get()[0].upper()}{random.randint(10000, 99999)}{'M'}')
                elif intSex.get() == 1:
                    emp_Id = (
                        f'{txtFirstName.get()[0].upper()}{txtminit.get().upper()}{txtLastName.get()[0].upper()}{random.randint(10000, 99999)}{'F'}')

            else:
                if intSex.get() == 0:
                    emp_Id = (
                        f'{txtFirstName.get()[0].upper()}-{txtLastName.get()[0].upper()}{random.randint(10000, 99999)}{'M'}')
                elif intSex.get() == 1:
                    emp_Id = (
                        f'{txtFirstName.get()[0].upper()}-{txtLastName.get()[0].upper()}{random.randint(10000, 99999)}{'F'}')
            empfName = txtFirstName.get()
            minit = txtminit.get()
            emplName = txtLastName.get()
            job_id = jobsDict[txtJobTitle.get()]
            job_lvl = intJobLVL.get()
            pub_id = publishersDict[txtPublishersList.get()]
            hire_date = txtHireDate.get()

            EmployeeObject = EmployeeModelClass(emp_Id=emp_Id, empfName=empfName, minit=minit,
                                                emplName=emplName,
                                                job_id=job_id, job_lvl=job_lvl, pub_id=pub_id, hire_date=hire_date)

            if not txtEmployeeId.get():
                EmployeeBLLObject.registerEmployee(EmployeeObject)
            resetForm()
            showList()

        def resetForm():
            for widget in lblEmployeeInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)

            for widget in lblEmployeeJob.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)

            txtEmployeeId.set("")
            txtHireDate.set("")
            intSex.set(0)
            intJobLVL.set(0)
            txtJobTitle.set(getJobList()[0])
            txtPublishersList.set(getPublishersList()[0])

        def checkValidationMinit(*args):
            if len(txtminit.get()) > 1:
                txtminit.set(txtminit.get()[:1])

            for char in txtminit.get():
                if not char.isalpha():
                    txtminit.set(txtminit.get().replace(char, ''))
                if not char.isupper():
                    txtminit.set(txtminit.get().upper())

        def showList(*args):
            from BusinessLogicLayer.Employees_BLL_Module import Employees_BLL
            EmployeeBLLObject = Employees_BLL()
            rows = EmployeeBLLObject.getEmployeeList()
            tvEmployeeList.delete(*tvEmployeeList.get_children())
            rowCount = 0
            for row in rows:
                rowCount += 1
                values = [rowCount]
                for value in row:
                    if value == None:
                        values.append("")
                    else:
                        if value == row[7]:
                            value = row[7].strftime("%Y-%m-%d")
                            values.append(value)
                        else:
                            values.append(value)

                tvEmployeeList.insert("", "end", values=values)

        def onTreeSelect(event):
            resetForm()
            index = tvEmployeeList.selection()
            if index:
                selectedValues = tvEmployeeList.item(index)['values']
                txtEmployeeId.set(selectedValues[1])
                txtFirstName.set(selectedValues[2])
                txtminit.set(selectedValues[3])
                txtLastName.set(selectedValues[4])
                txtJobTitle.set(selectedValues[5])
                intJobLVL.set(int(selectedValues[6]))
                txtPublishersList.set(selectedValues[7])
                txtHireDate.set(selectedValues[8])
                if txtEmployeeId.get()[-1] == "F":
                    intSex.set(1)
                elif txtEmployeeId.get()[-1] == "M":
                    intSex.set(0)

        def deleteEmployee():
            emp_Id = txtEmployeeId.get()
            if emp_Id:
                response = msg.askyesno("Delete Warning", "Are you sure?")
                if response:
                    from BusinessLogicLayer.Employees_BLL_Module import Employees_BLL
                    EmployeeBLLObject = Employees_BLL()
                    EmployeeBLLObject.deleteEmployee(emp_Id)

            showList()

        def updateEmployee():
            emp_Id = txtEmployeeId.get()
            empfName = txtFirstName.get()
            minit = txtminit.get()
            emplName = txtLastName.get()
            job_id = jobsDict[txtJobTitle.get()]
            job_lvl = intJobLVL.get()
            pub_id = publishersDict[txtPublishersList.get()]
            hire_date = txtHireDate.get()
            EmployeeObject = EmployeeModelClass(emp_Id, empfName, minit, emplName, job_id, job_lvl
                                            , pub_id, hire_date)

            if emp_Id:
                from BusinessLogicLayer.Employees_BLL_Module import Employees_BLL
                EmployeeBLLObject = Employees_BLL()
                EmployeeBLLObject.updateEmployee(EmployeeObject)

            showList()
            resetForm()

        def BackToHome():
            EmployeesCRUDForm.destroy()
            from UserInterfaceLayer.MainModule import MainForm
            MainForm().mainFormLoad("","")

        # endregion

        lblBasicInfo = LabelFrame(EmployeesCRUDForm, text='Basic Information: ', bg='wheat')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        lblEmployeeInfo = LabelFrame(lblBasicInfo, text="Employee's Information", bg='wheat')
        lblEmployeeInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10, sticky=NSEW)

        lblEmployeeID = Label(lblEmployeeInfo, text='EmployeeID: ', bg='wheat')
        lblEmployeeID.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtEmployeeId = StringVar()
        lblEmployeeIDValue = Label(lblEmployeeInfo, text='EmployeeIDValue: ', textvariable=txtEmployeeId, bg='wheat')
        lblEmployeeIDValue.grid(row=0, column=1, padx=10, pady=10)

        lblFirstName = Label(lblEmployeeInfo, text='FirstName: ', bg='wheat')
        lblFirstName.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtFirstName = StringVar()
        entFirstName = ttk.Entry(lblEmployeeInfo, textvariable=txtFirstName, width=40)
        entFirstName.grid(row=1, column=1, padx=10, pady=10)

        lblminit = Label(lblEmployeeInfo, text='Minit: ', bg='wheat')
        lblminit.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtminit = StringVar()
        txtminit.trace('w', checkValidationMinit)
        entminit = ttk.Entry(lblEmployeeInfo, textvariable=txtminit, width=40)
        entminit.grid(row=2, column=1, padx=10, pady=10)

        lblLastName = Label(lblEmployeeInfo, text='LastName: ', bg='wheat')
        lblLastName.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtLastName = StringVar()
        entLastName = ttk.Entry(lblEmployeeInfo, textvariable=txtLastName, width=40)
        entLastName.grid(row=3, column=1, padx=10, pady=10)

        lblSex = Label(lblEmployeeInfo, text='Sex: ', bg='wheat')
        lblSex.grid(row=4, column=0, padx=10, pady=0, sticky='w')

        intSex = IntVar()
        entMale = ttk.Radiobutton(lblEmployeeInfo, value=0, variable=intSex, text='Male')
        entMale.grid(row=4, column=1, padx=10, pady=0, sticky='w')

        entFemale = ttk.Radiobutton(lblEmployeeInfo, value=1, variable=intSex, text='Female')
        entFemale.grid(row=4, column=1, padx=10, pady=0, sticky='n')
        intSex.set(0)

        lblEmployeeJob = LabelFrame(lblBasicInfo, text="Employee's Job Information", bg='wheat')
        lblEmployeeJob.grid(row=1, column=0, padx=10, pady=0, ipadx=10, ipady=10, sticky=NSEW)

        lblJobTitle = Label(lblEmployeeJob, text='JobTitle: ', bg='wheat')
        lblJobTitle.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtJobTitle = StringVar()
        cmbJobTitle = ttk.Combobox(lblEmployeeJob, values=getJobList(), state='readonly',
                                   textvariable=txtJobTitle, width=36)
        cmbJobTitle.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        cmbJobTitle.bind("<<ComboboxSelected>>", lambda event: getJobsLVLList())
        txtJobTitle.set(getJobList()[0])

        lblJobLVL = Label(lblEmployeeJob, text='JobLevel: ', bg='wheat')
        lblJobLVL.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        intJobLVL = IntVar()
        entJobLVL = Scale(lblEmployeeJob, from_=10, to=10, orient="horizontal", variable=intJobLVL, length=235)
        entJobLVL.grid(row=1, column=1, padx=10, pady=20, sticky='w')
        #
        lblJobLVLShow = Label(lblEmployeeJob, text='JobLVL', textvariable=intJobLVL, width=5)
        lblJobLVLShow.grid(row=1, column=2, padx=10, pady=10, sticky='w')

        lblPublishersList = Label(lblEmployeeJob, text='PublishersList: ', bg='wheat')
        lblPublishersList.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtPublishersList = StringVar()
        entPublishersList = ttk.Combobox(lblEmployeeJob, values=getPublishersList(), state='readonly',
                                         textvariable=txtPublishersList,
                                         width=36)
        entPublishersList.grid(row=2, column=1, padx=10, pady=10)
        txtPublishersList.set(getPublishersList()[0])

        lblHireDate = Label(lblEmployeeJob, text='HireDate: ', bg='wheat')
        lblHireDate.grid(row=3, column=0, padx=10, pady=0, sticky='w')

        txtHireDate = StringVar()
        entHireDate = DateEntry(lblEmployeeJob, textvariable=txtHireDate, width=36)
        entHireDate.grid(row=3, column=1, padx=10, pady=0)

        btnRegisterEmployee = ttk.Button(lblBasicInfo, command=registerEmployee, text='Register Employee', width=20)
        btnRegisterEmployee.grid(row=8, column=0, padx=70, pady=10, sticky='e')

        btnResetForm = ttk.Button(lblBasicInfo, command=resetForm, text='Reset Form', width=20)
        btnResetForm.grid(row=8, column=0, padx=70, pady=10, sticky='w')

        btnDeleteEmployee = ttk.Button(lblBasicInfo, command=deleteEmployee, text='Delete Employee', width=20)
        btnDeleteEmployee.grid(row=9, column=0, padx=70, pady=0, sticky='e')

        btnUpdateEmployee = ttk.Button(lblBasicInfo, command=updateEmployee, text='Update Employee', width=20)
        btnUpdateEmployee.grid(row=9, column=0, padx=70, pady=0, sticky='w')

        btnBack = ttk.Button(lblBasicInfo, command=BackToHome, text='Back', width=16)
        btnBack.grid(row=10, column=0, padx=70, pady=10, sticky='n')

        lblEmployeesList = LabelFrame(EmployeesCRUDForm, text='Employees List: ', bg='wheat')
        lblEmployeesList.grid(row=0, column=1, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        columns = ["Index", "emp_Id", "empfName", "minit", "emplName", "job Title", "job_lvl", "publisher", "hire_date"]
        displaycolumns = ["Index", "empfName", "minit", "emplName", "job Title", "job_lvl", "publisher", "hire_date"]
        tvEmployeeList = ttk.Treeview(lblEmployeesList, columns=columns, selectmode='browse', show='headings'
                                      , displaycolumns=displaycolumns, height=26, )

        tvEmployeeList.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
        tvEmployeeList.bind('<<TreeviewSelect>>', onTreeSelect)

        tvEmployeeList.column("#0", width=0)

        tvEmployeeList.column("Index", width=25, anchor=CENTER)
        tvEmployeeList.heading("Index", text="#", anchor='n')

        tvEmployeeList.column("emp_Id", width=0)
        tvEmployeeList.heading("emp_Id", text="ID")

        tvEmployeeList.column("empfName", width=100)
        tvEmployeeList.heading("empfName", text="First Name", anchor='n')

        tvEmployeeList.column("minit", width=50, anchor=CENTER)
        tvEmployeeList.heading("minit", text="Minit", anchor='n')

        tvEmployeeList.column("emplName", width=100)
        tvEmployeeList.heading("emplName", text="Last Name", anchor='n')

        tvEmployeeList.column("job Title", width=170)
        tvEmployeeList.heading("job Title", text="Job Title", anchor='n')

        tvEmployeeList.column("job_lvl", width=80, anchor=CENTER)
        tvEmployeeList.heading("job_lvl", text="Job Level", anchor='n')

        tvEmployeeList.column("publisher", width=140)
        tvEmployeeList.heading("publisher", text="publisher", anchor='n')

        tvEmployeeList.column("hire_date", width=150, anchor=CENTER)
        tvEmployeeList.heading("hire_date", text="Hiredate", anchor='n')

        entFirstName.focus_set()
        showList()
        EmployeesCRUDForm.mainloop()
