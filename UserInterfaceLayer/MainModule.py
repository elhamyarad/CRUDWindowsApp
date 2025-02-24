from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image, ImageTk

class MainForm:
    def mainFormLoad(self, firstName, lastName):
        mainForm = Tk()
        mainForm.title('Login Form')
        mainForm.geometry('655x430')
        x = int(mainForm.winfo_screenwidth() // 2 - 655 / 2)
        y = int(mainForm.winfo_screenheight() // 2 - 430 / 2)
        mainForm.geometry('+{}+{}'.format(x, y))
        mainForm.resizable(0, 0)
        mainForm.iconbitmap('images/mainForm.ico')

        MainForm_background_image = Image.open('images/backgroundMain.jpg')
        MainForm_background_image = MainForm_background_image.resize((655, 430))
        bg_image = ImageTk.PhotoImage(MainForm_background_image)

        background_label = Label(mainForm, image=bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def setClock():
            from datetime import datetime
            currentDateTime = datetime.today()
            currentDateTime = currentDateTime.strftime('%Y-%m-%d %H:%M:%S')
            txtCurrentDateTime.set(currentDateTime)
            mainForm.after(1000, setClock)

        def authorsCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.AuthorsModule import AuthorsCRUD
            AuthorsCRUDObject = AuthorsCRUD()
            AuthorsCRUDObject.AuthorsCRUD_FormLoad()

        def employeesCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.EmployeesModule import EmployeesCRUD
            employeesCRUDObject = EmployeesCRUD()
            employeesCRUDObject.EmployeesCRUD_FormLoad()

        def storsCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.StorsModule import StorsCRUD
            storsCRUDObject = StorsCRUD()
            storsCRUDObject.StorsCRUD_FormLoad()

        def salesCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.SalesModule import SalesCRUD
            salesCRUDObject = SalesCRUD()
            salesCRUDObject.SalesCRUD_FormLoad()

        def jobsCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.JobsModule import JobsCRUD
            jobsCRUDObject = JobsCRUD()
            jobsCRUDObject.JobsCRUD_FormLoad()

        def publishersCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.PublishersModule import PublishersCRUD
            pubsCRUDObject = PublishersCRUD()
            pubsCRUDObject.PublishersCRUD_FormLoad()

        def titlesCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.TitlesModule import TitlesCRUD
            titlesCRUDObject = TitlesCRUD()
            titlesCRUDObject.TitlesCRUD_FormLoad()

        lblWelcomeMessage = Label(mainForm, text=f'Welcome {firstName} {lastName}', bg='wheat')
        lblWelcomeMessage.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        txtCurrentDateTime = StringVar()
        lblCurrentDateTime = Label(mainForm, textvariable=txtCurrentDateTime, bg='wheat')
        lblCurrentDateTime.grid(row=0, column=3, padx=10, pady=10, sticky='e')

        authorsImage = PhotoImage(file='images/authors.png')
        btnAuthorsCRUD = Button(mainForm,relief='groove',compound='top',command=authorsCRUD , text='Authors CRUD',
                                image=authorsImage, bg='wheat')
        btnAuthorsCRUD.grid(row=1, column=0, padx=20, pady=10)

        employeeImage = PhotoImage(file='images/employee.png')
        btnemployeeCRUD = Button(mainForm,relief='groove',compound='top',command=employeesCRUD, text='Employee CRUD',
                                 image=employeeImage, bg='wheat')
        btnemployeeCRUD.grid(row=1, column=1, padx=10, pady=10)

        storesImage = PhotoImage(file='images/stors.png')
        btnstoresCRUD = Button(mainForm,relief='groove',compound='top', command=storsCRUD, text='Stores CRUD',
                               image=storesImage, bg='wheat')
        btnstoresCRUD.grid(row=1, column=2, padx=10, pady=10)

        salesImage = PhotoImage(file='images/sales.png')
        btnSalesCRUD = Button(mainForm,relief='groove',compound='top', command=salesCRUD, text='Sales CRUD',
                               image=salesImage, bg='wheat')
        btnSalesCRUD.grid(row=1, column=3, padx=10, pady=10)

        publishersImage = PhotoImage(file='images/publishers.png')
        btnpublishersCRUD = Button(mainForm,relief='groove',compound='top', command=publishersCRUD, text='PublishersCRUD',
                                   image=publishersImage, bg='wheat')
        btnpublishersCRUD.grid(row=2, column=0, padx=20, pady=10)

        titlesImage = PhotoImage(file='images/titles.png')
        btntitlesCRUD = Button(mainForm,relief='groove',compound='top', command=titlesCRUD, text='Titles CRUD',
                               image=titlesImage, bg='wheat')
        btntitlesCRUD.grid(row=2, column=1, padx=10, pady=10)

        jobsImage = PhotoImage(file='images/jobs.png')
        btnjobsCRUD = Button(mainForm,relief='groove',compound='top', command=jobsCRUD, text='Jobs CRUD',
                             image=jobsImage, bg='wheat')
        btnjobsCRUD.grid(row=2, column=2, padx=10, pady=10)

        txtsignature = StringVar()
        signatureImage = PhotoImage(file='images/signature.png')
        lblsignature = Label(mainForm, textvariable=txtsignature, image=signatureImage, bg='wheat')
        lblsignature.grid(row=2, column=3, padx=10, pady=10, sticky='n')

        mainForm.after(0,setClock)
        mainForm.mainloop()


mainformload = MainForm()
# mainformload.mainFormLoad("firstName", "lastName")