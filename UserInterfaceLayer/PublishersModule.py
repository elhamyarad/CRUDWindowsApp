from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import random
from Model.PublisherModel import PublisherModelClass

from BusinessLogicLayer.Publishers_BLL_Module import Publishers_BLL


class PublishersCRUD:
    def PublishersCRUD_FormLoad(self):
        PublishersCRUDForm = Tk()
        PublishersCRUDForm.title('Publisher CRUD Form')
        PublishersCRUDForm.geometry('1000x440')
        x = int(PublishersCRUDForm.winfo_screenwidth() // 2 - 1000 / 2)
        y = int(PublishersCRUDForm.winfo_screenheight() // 2 - 440 / 2)
        PublishersCRUDForm.geometry('+{}+{}'.format(x, y))
        PublishersCRUDForm.resizable(0, 0)
        PublishersCRUDForm.iconbitmap('images/publishers.ico')
        
        PublishersCRUDForm_background_image = Image.open('images/backgroundMain.jpg')
        PublishersCRUDForm_background_image = PublishersCRUDForm_background_image.resize((1000, 440))
        bg_image = ImageTk.PhotoImage(PublishersCRUDForm_background_image)

        background_label = Label(PublishersCRUDForm, image=bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # region Functions
        def registerPublisher():
            publisherBLLObject = Publishers_BLL()
            pub_id = f'{99}{random.randint(0, 9)}{random.randint(0, 9)}'
            pub_name = txtPublisherName.get()
            city = txtPublisherCity.get()
            state = txtPublisherState.get()
            country = txtPublisherCountry.get()

            publisherObject = PublisherModelClass(pub_id=pub_id, pub_name=pub_name, city=city, state=state, country=country)

            if not txtPublisherId.get():
                publisherBLLObject.registerPublisher(publisherObject)
            resetForm()
            showList()

        def resetForm():
            for widget in lblPublisherInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)

            txtPublisherId.set("")

        def checkValidationState(*args):
            if len(txtPublisherState.get()) > 2:
                txtPublisherState.set(txtPublisherState.get()[:2])

            for states in txtPublisherState.get():
                if not states.isalpha():
                    txtPublisherState.set(txtPublisherState.get().replace(states, ''))

        def showList(*args):
            from BusinessLogicLayer.Publishers_BLL_Module import Publishers_BLL
            publisherBLLObject = Publishers_BLL()
            rows = publisherBLLObject.getPublisherList()
            tvPublisherList.delete(*tvPublisherList.get_children())
            rowCount = 0
            for row in rows:
                rowCount += 1
                values = [rowCount]
                for value in row:
                    if value == None:
                        values.append("")
                    else:
                        values.append(value)
                tvPublisherList.insert("", "end", values=values)

        def onTreeSelect(event):
            resetForm()
            index = tvPublisherList.selection()
            if index:
                selectedValues = tvPublisherList.item(index)['values']
                txtPublisherId.set(selectedValues[1])
                txtPublisherName.set(selectedValues[2])
                txtPublisherCity.set(selectedValues[3])
                txtPublisherState.set(selectedValues[4])
                txtPublisherCountry.set(selectedValues[5])

        def deletePublisher():
            pub_id = txtPublisherId.get()
            if pub_id:
                msg.askyesno("Delete Warning", "Are you sure?")
            if pub_id:
                from BusinessLogicLayer.Publishers_BLL_Module import Publishers_BLL
                publisherBLLObject = Publishers_BLL()
                publisherBLLObject.deletePublisher(pub_id)
            showList()

        def updatePublisher():
            pub_id = txtPublisherId.get()
            pub_name = txtPublisherName.get()
            city = txtPublisherCity.get()
            state = txtPublisherState.get()
            country = txtPublisherCountry.get()

            publisherObject = PublisherModelClass(pub_id, pub_name, city, state, country)

            if pub_id:
                from BusinessLogicLayer.Publishers_BLL_Module import Publishers_BLL
                publisherBLLObject = Publishers_BLL()
                publisherBLLObject.updatePublisher(publisherObject)

            showList()
            resetForm()

        def BackToHome():
            PublishersCRUDForm.destroy()
            from UserInterfaceLayer.MainModule import MainForm
            MainForm().mainFormLoad("","")

        # endregion

        lblBasicInfo = LabelFrame(PublishersCRUDForm, text='Basic Information: ', bg='wheat')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        lblPublisherInfo = LabelFrame(lblBasicInfo, text="Publisher's Information", bg='wheat')
        lblPublisherInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10, sticky=NSEW)

        lblPublisherID = Label(lblPublisherInfo, text='PublisherID: ', bg='wheat')
        lblPublisherID.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtPublisherId = StringVar()
        lblPublisherIDValue = Label(lblPublisherInfo, text='PublisherIDValue', textvariable=txtPublisherId, bg='wheat')
        lblPublisherIDValue.grid(row=0, column=1, padx=10, pady=10)

        lblPublisherName = Label(lblPublisherInfo, text='PublisherName: ', bg='wheat')
        lblPublisherName.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtPublisherName = StringVar()
        entPublisherName = ttk.Entry(lblPublisherInfo, textvariable=txtPublisherName, width=40)
        entPublisherName.grid(row=1, column=1, padx=10, pady=10)

        lblPublisherCity = Label(lblPublisherInfo, text='PublisherCity: ', bg='wheat')
        lblPublisherCity.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtPublisherCity = StringVar()
        entPublisherCity = ttk.Entry(lblPublisherInfo, textvariable=txtPublisherCity, width=40)
        entPublisherCity.grid(row=2, column=1, padx=10, pady=10)

        lblPublisherState = Label(lblPublisherInfo, text='PublisherState: ', bg='wheat')
        lblPublisherState.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtPublisherState = StringVar()
        txtPublisherState.trace('w', checkValidationState)
        entPublisherState = ttk.Entry(lblPublisherInfo, textvariable=txtPublisherState, width=20)
        entPublisherState.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lblPublisherCountry = Label(lblPublisherInfo, text='PublisherCountry: ', bg='wheat')
        lblPublisherCountry.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        txtPublisherCountry = StringVar()
        entPublisherCountry = ttk.Entry(lblPublisherInfo, textvariable=txtPublisherCountry, width=40)
        entPublisherCountry.grid(row=4, column=1, padx=10, pady=10, sticky='w')


        btnRegisterPublisher = ttk.Button(lblBasicInfo, command=registerPublisher, text='Register Publisher', width=18)
        btnRegisterPublisher.grid(row=5, column=0, padx=70, pady=10, sticky='e')

        btnResetForm = ttk.Button(lblBasicInfo, command=resetForm, text='Reset Form', width=18)
        btnResetForm.grid(row=5, column=0, padx=70, pady=10, sticky='w')

        btnDeletePublisher = ttk.Button(lblBasicInfo, command=deletePublisher, text='Delete Publisher', width=18)
        btnDeletePublisher.grid(row=6, column=0, padx=70, pady=0, sticky='e')

        btnUpdatePublisher = ttk.Button(lblBasicInfo, command=updatePublisher, text='Update Publisher', width=18)
        btnUpdatePublisher.grid(row=6, column=0, padx=70, pady=0, sticky='w')

        btnBack = ttk.Button(lblBasicInfo, command=BackToHome, text='Back', width=18)
        btnBack.grid(row=7, column=0, padx=70, pady=10, sticky='n')

        lblPublishersList = LabelFrame(PublishersCRUDForm, text='Publishers List: ', bg='wheat')
        lblPublishersList.grid(row=0, column=1, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        columns = ["Index", "pub_id", "pub_name", "city", "state", "country"]
        displaycolumns = ["Index", "pub_name", "city", "state", "country"]
        tvPublisherList = ttk.Treeview(lblPublishersList, columns=columns, selectmode='browse', show='headings'
                                    , displaycolumns=displaycolumns, height=17, )

        tvPublisherList.grid(row=0, column=0, padx=10, pady=0, sticky=NSEW)
        tvPublisherList.bind('<<TreeviewSelect>>', onTreeSelect)

        tvPublisherList.column("#0", width=0)

        tvPublisherList.column("Index", width=20, anchor=CENTER)
        tvPublisherList.heading("Index", text="#", anchor='n')

        tvPublisherList.column("pub_id", width=0)
        tvPublisherList.heading("pub_id", text="publisherID")

        tvPublisherList.column("pub_name", width=150)
        tvPublisherList.heading("pub_name", text="PublisherName", anchor='n')

        tvPublisherList.column("city", width=100)
        tvPublisherList.heading("city", text="city", anchor='n')

        tvPublisherList.column("state", width=100)
        tvPublisherList.heading("state", text="state", anchor='n')

        tvPublisherList.column("country", width=100)
        tvPublisherList.heading("country", text="country", anchor='n')


        entPublisherName.focus_set()
        showList()
        PublishersCRUDForm.mainloop()
