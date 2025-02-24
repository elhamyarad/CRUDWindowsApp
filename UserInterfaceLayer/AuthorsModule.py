from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import random
from PIL import Image, ImageTk
from Model.AuthorModel import AuthorModelClass

from BusinessLogicLayer.Authors_BLL_Module import Authors_BLL


class AuthorsCRUD:
    def AuthorsCRUD_FormLoad(self):
        AuthorsCRUDForm = Tk()
        AuthorsCRUDForm.title('Author CRUD Form')
        AuthorsCRUDForm.geometry('1350x620')
        x = int(AuthorsCRUDForm.winfo_screenwidth() // 2 - 1350 / 2)
        y = int(AuthorsCRUDForm.winfo_screenheight() // 2 - 620 / 2)
        AuthorsCRUDForm.geometry('+{}+{}'.format(x, y))
        AuthorsCRUDForm.resizable(0, 0)
        AuthorsCRUDForm.iconbitmap('images/authors.ico')
        
        AuthorsCRUDForm_background_image = Image.open('images/backgroundMain.jpg')
        AuthorsCRUDForm_background_image = AuthorsCRUDForm_background_image.resize((1350, 620))
        bg_image = ImageTk.PhotoImage(AuthorsCRUDForm_background_image)

        background_label = Label(AuthorsCRUDForm, image=bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # region Functions
        def registerAuthor():
            authorBLLObject = Authors_BLL()
            auId = f'{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}'
            auFirstName = txtFirstName.get()
            auLastName = txtLastName.get()
            auPhone = txtPhoneNumber.get()
            auAddress = txtAddress.get()
            auCity = txtCity.get()
            auState = txtState.get()
            auZip = txtZipCode.get()
            auContract = intContract.get()
            authorObject = AuthorModelClass(auId=auId, auFirstName=auFirstName, auLastName=auLastName, auPhone=auPhone,
                                            auAddress=auAddress, auCity=auCity, auState=auState, auZip=auZip,
                                            auContract=auContract)

            if not txtAuthorId.get():
                authorBLLObject.registerAuthor(authorObject)
            resetForm()
            showList()

        def resetForm():
            for widget in lblAuthorInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)

            for widget in lblAuthorAddress.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)

            intContract.set(0)
            txtAuthorId.set("")

        def checkValidation(*args):
            if len(txtPhoneNumber.get()) > 10:
                txtPhoneNumber.set(txtPhoneNumber.get()[:10])

            for char in txtPhoneNumber.get():
                if not char.isnumeric():
                    txtPhoneNumber.set(txtPhoneNumber.get().replace(char, ''))

        def checkValidationZipCode(*args):
            if len(txtZipCode.get()) > 5:
                txtZipCode.set(txtZipCode.get()[:5])

            for zipCode in txtZipCode.get():
                if not zipCode.isnumeric():
                    txtZipCode.set(txtZipCode.get().replace(zipCode, ''))

        def checkValidationState(*args):
            if len(txtState.get()) > 2:
                txtState.set(txtState.get()[:2])

            for state in txtState.get():
                if not state.isalpha():
                    txtState.set(txtState.get().replace(state, ''))

        def showList(*args):
            from BusinessLogicLayer.Authors_BLL_Module import Authors_BLL
            authorBLLObject = Authors_BLL()
            rows = authorBLLObject.getAuthorList()
            tvAuthorList.delete(*tvAuthorList.get_children())
            rowCount = 0
            for row in rows:
                rowCount += 1
                values = [rowCount]
                for value in row:
                    if value == None:
                        values.append("")
                    else:
                        values.append(value)
                tvAuthorList.insert("", "end", values=values)

        def onTreeSelect(event):
            resetForm()
            index = tvAuthorList.selection()
            if index:
                selectedValues = tvAuthorList.item(index)['values']
                txtAuthorId.set(selectedValues[1])
                txtFirstName.set(selectedValues[3])
                txtLastName.set(selectedValues[2])
                txtPhoneNumber.set(selectedValues[4])
                txtAddress.set(selectedValues[5])
                txtCity.set(selectedValues[6])
                txtState.set(selectedValues[7])
                txtZipCode.set(selectedValues[8])
                contract = selectedValues[9]
                if contract == 'Yes':
                    intContract.set(1)
                elif contract == 'No':
                    intContract.set(0)

        def deleteAuthor():
            auId = txtAuthorId.get()
            if auId:
                msg.askyesno("Delete Warning", "Are you sure?")
            if auId:
                from BusinessLogicLayer.Authors_BLL_Module import Authors_BLL
                authorBLLObject = Authors_BLL()
                authorBLLObject.deleteAuthor(auId)
            showList()

        def updateAuthor():
            auId = txtAuthorId.get()
            auLastName = txtLastName.get()
            auFirstName = txtFirstName.get()
            auPhoneNumber = txtPhoneNumber.get()
            auAddress = txtAddress.get()
            auCity = txtCity.get()
            auState = txtState.get()
            auZipCode = txtZipCode.get()
            auContract = intContract.get()
            authorObject = AuthorModelClass(auId, auLastName, auFirstName, auPhoneNumber, auAddress, auCity
                                            , auState, auZipCode, auContract)

            if auId:
                from BusinessLogicLayer.Authors_BLL_Module import Authors_BLL
                authorBLLObject = Authors_BLL()
                authorBLLObject.updateAuthor(authorObject)

            showList()
            resetForm()

        def BackToHome():
            AuthorsCRUDForm.destroy()
            from UserInterfaceLayer.MainModule import MainForm
            MainForm().mainFormLoad("","")

        # endregion

        lblBasicInfo = LabelFrame(AuthorsCRUDForm, text='Basic Information: ', bg='wheat')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        lblAuthorInfo = LabelFrame(lblBasicInfo, text="Author's Information", bg='wheat')
        lblAuthorInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10, sticky=NSEW)

        lblAuthorID = Label(lblAuthorInfo, text='AuthorID: ', bg='wheat')
        lblAuthorID.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtAuthorId = StringVar()
        lblAuthorIDValue = Label(lblAuthorInfo, text='AuthorIDValue', textvariable=txtAuthorId, bg='wheat')
        lblAuthorIDValue.grid(row=0, column=1, padx=10, pady=10)

        lblFirstName = Label(lblAuthorInfo, text='FirstName: ', bg='wheat')
        lblFirstName.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtFirstName = StringVar()
        entFirstName = ttk.Entry(lblAuthorInfo, textvariable=txtFirstName, width=40)
        entFirstName.grid(row=1, column=1, padx=10, pady=10)

        lblLastName = Label(lblAuthorInfo, text='LastName: ', bg='wheat')
        lblLastName.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtLastName = StringVar()
        entLastName = ttk.Entry(lblAuthorInfo, textvariable=txtLastName, width=40)
        entLastName.grid(row=2, column=1, padx=10, pady=10)

        lblPhoneNumber = Label(lblAuthorInfo, text='Phone Number: ', bg='wheat')
        lblPhoneNumber.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtPhoneNumber = StringVar()
        txtPhoneNumber.trace('w', checkValidation)
        entPhoneNumber = ttk.Entry(lblAuthorInfo, textvariable=txtPhoneNumber, width=40)
        entPhoneNumber.grid(row=3, column=1, padx=10, pady=10)

        lblContract = Label(lblAuthorInfo, text='Contract: ', bg='wheat')
        lblContract.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        intContract = IntVar()
        entHaveContract = ttk.Radiobutton(lblAuthorInfo, value=0, variable=intContract, text='No')
        entHaveContract.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        entHaveNotContract = ttk.Radiobutton(lblAuthorInfo, value=1, variable=intContract, text='Yes')
        entHaveNotContract.grid(row=4, column=1, padx=10, pady=10, sticky='n')
        intContract.set(0)

        lblAuthorAddress = LabelFrame(lblBasicInfo, text="Author's Address Information", bg='wheat')
        lblAuthorAddress.grid(row=1, column=0, padx=10, pady=0, ipadx=10, ipady=10, sticky=NSEW)

        lblAddress = Label(lblAuthorAddress, text='Address: ', bg='wheat')
        lblAddress.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtAddress = StringVar()
        entAddress = ttk.Entry(lblAuthorAddress, textvariable=txtAddress, width=40)
        entAddress.grid(row=0, column=1, padx=10, pady=10)

        lblCity = Label(lblAuthorAddress, text='City: ', bg='wheat')
        lblCity.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtCity = StringVar()
        entCity = ttk.Entry(lblAuthorAddress, textvariable=txtCity, width=40)
        entCity.grid(row=1, column=1, padx=10, pady=10)

        lblState = Label(lblAuthorAddress, text='State: ', bg='wheat')
        lblState.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtState = StringVar()
        txtState.trace('w', checkValidationState)
        entState = ttk.Entry(lblAuthorAddress, textvariable=txtState, width=40)
        entState.grid(row=2, column=1, padx=50, pady=10)

        lblZipCode = Label(lblAuthorAddress, text='ZipCode: ', bg='wheat')
        lblZipCode.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtZipCode = StringVar()
        txtZipCode.trace('w', checkValidationZipCode)
        entZipCode = ttk.Entry(lblAuthorAddress, textvariable=txtZipCode, width=20)
        entZipCode.grid(row=3, column=1, padx=50, pady=10, sticky='w')

        btnRegisterAuthor = ttk.Button(lblBasicInfo, command=registerAuthor, text='Register Author', width=16)
        btnRegisterAuthor.grid(row=8, column=0, padx=70, pady=10, sticky='e')

        btnResetForm = ttk.Button(lblBasicInfo, command=resetForm, text='Reset Form', width=16)
        btnResetForm.grid(row=8, column=0, padx=70, pady=10, sticky='w')

        btnDeleteAuthor = ttk.Button(lblBasicInfo, command=deleteAuthor, text='Delete Author', width=16)
        btnDeleteAuthor.grid(row=9, column=0, padx=70, pady=0, sticky='e')

        btnUpdateAuthor = ttk.Button(lblBasicInfo, command=updateAuthor, text='Update Authorr', width=16)
        btnUpdateAuthor.grid(row=9, column=0, padx=70, pady=0, sticky='w')

        btnBack = ttk.Button(lblBasicInfo, command=BackToHome, text='Back', width=16)
        btnBack.grid(row=10, column=0, padx=70, pady=0, sticky='n')

        lblAuthorsList = LabelFrame(AuthorsCRUDForm, text='Authors List: ', bg='wheat')
        lblAuthorsList.grid(row=0, column=1, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        columns = ["Index", "au_id", "au_lname", "au_fname", "phone", "address", "city", "state", "zip", "contract"]
        displaycolumns = ["Index", "au_lname", "au_fname", "phone", "address", "city", "state", "zip", "contract"]
        tvAuthorList = ttk.Treeview(lblAuthorsList, columns=columns, selectmode='browse', show='headings'
                                    , displaycolumns=displaycolumns, height=26, )

        tvAuthorList.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
        tvAuthorList.bind('<<TreeviewSelect>>', onTreeSelect)

        tvAuthorList.column("#0", width=0)

        tvAuthorList.column("Index", width=20, anchor=CENTER)
        tvAuthorList.heading("Index", text="#", anchor='n')

        tvAuthorList.column("au_id", width=0)
        tvAuthorList.heading("au_id", text="ID")

        tvAuthorList.column("au_lname", width=100)
        tvAuthorList.heading("au_lname", text="Last Name", anchor='n')

        tvAuthorList.column("au_fname", width=100)
        tvAuthorList.heading("au_fname", text="First Name", anchor='n')

        tvAuthorList.column("phone", width=100, anchor=CENTER)
        tvAuthorList.heading("phone", text="Phone", anchor='n')

        tvAuthorList.column("address", width=150)
        tvAuthorList.heading("address", text="Address", anchor='n')

        tvAuthorList.column("city", width=100)
        tvAuthorList.heading("city", text="City", anchor='n')

        tvAuthorList.column("state", width=70, anchor=CENTER)
        tvAuthorList.heading("state", text="State", anchor='n')

        tvAuthorList.column("zip", width=70, anchor=CENTER)
        tvAuthorList.heading("zip", text="Zip", anchor='n')

        tvAuthorList.column("contract", width=100, anchor=CENTER)
        tvAuthorList.heading("contract", text="Contract", anchor='n')

        entFirstName.focus_set()
        showList()
        AuthorsCRUDForm.mainloop()

