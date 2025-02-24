from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import random
import string
from Model.SaleModel import SaleModelClass
from BusinessLogicLayer.Sales_BLL_Module import Sales_BLL


class SalesCRUD:
    def SalesCRUD_FormLoad(self):
        SalesCRUDForm = Tk()
        SalesCRUDForm.title('Sale CRUD Form')
        SalesCRUDForm.geometry('1350x620')
        x = int(SalesCRUDForm.winfo_screenwidth() // 2 - 1350 / 2)
        y = int(SalesCRUDForm.winfo_screenheight() // 2 - 620 / 2)
        SalesCRUDForm.geometry('+{}+{}'.format(x, y))
        SalesCRUDForm.resizable(0, 0)
        SalesCRUDForm.iconbitmap('images/Sales.ico')

        SalesCRUDForm_background_image = Image.open('images/backgroundMain.jpg')
        SalesCRUDForm_background_image = SalesCRUDForm_background_image.resize((1350, 620))
        bg_image = ImageTk.PhotoImage(SalesCRUDForm_background_image)

        background_label = Label(SalesCRUDForm, image=bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        storsDict = dict()
        titlesDict = dict()

        # region Functions

        def getStorsList():
            storBLLObject = Sales_BLL()
            storsList = storBLLObject.getStorsList()

            if len(storsList) > 0:
                for stor in storsList:
                    if stor[1] not in storsList:
                        storsDict[stor[1]] = stor[0]
            return list(storsDict.keys())

        def getTitlesList():
            titleBLLObject = Sales_BLL()
            titlesList = titleBLLObject.getTitlesList()

            if len(titlesList) > 0:
                for title in titlesList:
                    if title[1] not in titlesList:
                        titlesDict[title[1]] = title[0]
            return list(titlesDict.keys())

        def registerSale():
            SaleBLLObject = Sales_BLL()
            ord_num = txtOrderNumber.get()
            stor_id = storsDict[txtStoreName.get()]
            ord_date = txtOrderDate.get()
            qty = txtQuantity.get()
            payterms = txtPayTerms.get()
            title_id = titlesDict[txtTitleName.get()]

            SaleObject = SaleModelClass(stor_id=stor_id, ord_num=ord_num, ord_date=ord_date, qty=qty,
                                        payterms=payterms, title_id=title_id)

            SaleBLLObject.registerSale(SaleObject)
            resetForm()
            showList()

        def resetForm():
            for widget in lblSaleInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)

            txtOrderNumber.set("")
            txtOrderDate.set("")
            txtStoreName.set("")
            txtTitleName.set("")

        def checkValidationQTY(*args):
            if len(txtQuantity.get()) > 2:
                txtQuantity.set(txtQuantity.get()[:2])

            for num in txtQuantity.get():
                if not num.isnumeric():
                    txtQuantity.set(txtQuantity.get().replace(num, ''))

        def showList(*args):
            from BusinessLogicLayer.Sales_BLL_Module import Sales_BLL
            SaleBLLObject = Sales_BLL()
            rows = SaleBLLObject.getSaleList()
            tvSaleList.delete(*tvSaleList.get_children())
            rowCount = 0
            for row in rows:
                rowCount += 1
                values = [rowCount]
                for value in row:
                    if value == None:
                        values.append("")
                    else:
                        if value == row[2]:
                            value = row[2].strftime("%Y-%m-%d")
                            values.append(value)
                        else:
                            values.append(value)

                tvSaleList.insert("", "end", values=values)

        def onTreeSelect(event):
            resetForm()
            index = tvSaleList.selection()
            if index:
                selectedValues = tvSaleList.item(index)['values']
                txtOrderNumber.set(selectedValues[2])
                txtStoreName.set(selectedValues[1])
                txtOrderDate.set(selectedValues[3])
                txtQuantity.set(selectedValues[4])
                txtPayTerms.set(selectedValues[5])
                txtTitleName.set(selectedValues[6])

        def deleteSale():
            ord_num = txtOrderNumber.get()
            stor_id = storsDict[txtStoreName.get()]
            title_id = titlesDict[txtTitleName.get()]

            if ord_num and stor_id and title_id:
                response = msg.askyesno("Delete Warning", "Are you sure?")
                if response:
                    from BusinessLogicLayer.Sales_BLL_Module import Sales_BLL
                    SaleBLLObject = Sales_BLL()
                    SaleBLLObject.deleteSale(stor_id, ord_num, title_id)

            showList()

        def updateSale():
            ord_num = txtOrderNumber.get()
            stor_id = storsDict[txtStoreName.get()]
            ord_date = txtOrderDate.get()
            qty = txtQuantity.get()
            payterms = txtPayTerms.get()
            title_id = titlesDict[txtTitleName.get()]

            SaleObject = SaleModelClass(ord_num=ord_num, stor_id=stor_id, ord_date=ord_date, qty=qty,
                                        payterms=payterms, title_id=title_id)

            if ord_num and stor_id and title_id:
                from BusinessLogicLayer.Sales_BLL_Module import Sales_BLL
                SaleBLLObject = Sales_BLL()
                SaleBLLObject.updateSale(SaleObject)

            showList()
            resetForm()

        def BackToHome():
            SalesCRUDForm.destroy()
            from UserInterfaceLayer.MainModule import MainForm
            MainForm().mainFormLoad("", "")

        # endregion

        lblBasicInfo = LabelFrame(SalesCRUDForm, text='Basic Information: ', bg='wheat')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        lblSaleInfo = LabelFrame(lblBasicInfo, text="Sale's Information", bg='wheat')
        lblSaleInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10, sticky=NSEW)

        lblOrderNumber = Label(lblSaleInfo, text='OrderNumber: ', bg='wheat')
        lblOrderNumber.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        txtOrderNumber = StringVar()
        entOrderNumberValue = ttk.Entry(lblSaleInfo, textvariable=txtOrderNumber, width=40)
        entOrderNumberValue.grid(row=0, column=1, padx=10, pady=10)

        lblStoreName = Label(lblSaleInfo, text='StoreName: ', bg='wheat')
        lblStoreName.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        txtStoreName = StringVar()
        cmbStoreName = ttk.Combobox(lblSaleInfo, textvariable=txtStoreName, values=getStorsList(), state='readonly',
                                    width=36)
        cmbStoreName.grid(row=1, column=1, padx=10, pady=10)

        lblOrderDate = Label(lblSaleInfo, text='OrderDate: ', bg='wheat')
        lblOrderDate.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        txtOrderDate = StringVar()
        entOrderDate = DateEntry(lblSaleInfo, textvariable=txtOrderDate, width=36)
        entOrderDate.grid(row=2, column=1, padx=10, pady=10)

        lblQuantity = Label(lblSaleInfo, text='Quantity: ', bg='wheat')
        lblQuantity.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        txtQuantity = StringVar()
        txtQuantity.trace('w', checkValidationQTY)
        entQuantity = ttk.Entry(lblSaleInfo, textvariable=txtQuantity, width=40)
        entQuantity.grid(row=3, column=1, padx=10, pady=10)

        lblPayTerms = Label(lblSaleInfo, text='PayTerms: ', bg='wheat')
        lblPayTerms.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        txtPayTerms = StringVar()
        valuesPayTerms = ["Net 60", "Net 30", "ON invoice"]
        cmbPayTerms = ttk.Combobox(lblSaleInfo, textvariable=txtPayTerms, values=valuesPayTerms, state='readonly',
                                   width=36)
        cmbPayTerms.grid(row=4, column=1, padx=10, pady=10)

        lblTitleName = Label(lblSaleInfo, text='TitleName: ', bg='wheat')
        lblTitleName.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        txtTitleName = StringVar()
        cmbTitleName = ttk.Combobox(lblSaleInfo, textvariable=txtTitleName, values=getTitlesList(), state='readonly',
                                    width=36)
        cmbTitleName.grid(row=5, column=1, padx=10, pady=10)

        btnRegisterSale = ttk.Button(lblBasicInfo, command=registerSale, text='Register Sale', width=20)
        btnRegisterSale.grid(row=8, column=0, padx=70, pady=10, sticky='e')

        btnResetForm = ttk.Button(lblBasicInfo, command=resetForm, text='Reset Form', width=20)
        btnResetForm.grid(row=8, column=0, padx=70, pady=10, sticky='w')

        btnDeleteSale = ttk.Button(lblBasicInfo, command=deleteSale, text='Delete Sale', width=20)
        btnDeleteSale.grid(row=9, column=0, padx=70, pady=10, sticky='e')

        btnUpdateSale = ttk.Button(lblBasicInfo, command=updateSale, text='Update Sale', width=20)
        btnUpdateSale.grid(row=9, column=0, padx=70, pady=10, sticky='w')

        btnBack = ttk.Button(lblBasicInfo, command=BackToHome, text='Back', width=16)
        btnBack.grid(row=10, column=0, padx=70, pady=10, sticky='n')

        lblSalesList = LabelFrame(SalesCRUDForm, text='Sales List: ', bg='wheat')
        lblSalesList.grid(row=0, column=1, padx=10, pady=10, ipadx=0, ipady=10, sticky=NSEW)

        columns = ["Index", "stor_id", "ord_num", "ord_date", "qty", "payterms", "title_id"]
        displaycolumns = ["Index", "stor_id", "ord_date", "qty", "payterms", "title_id"]
        tvSaleList = ttk.Treeview(lblSalesList, columns=columns, selectmode='browse', show='headings'
                                  , displaycolumns=displaycolumns, height=26, )

        tvSaleList.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
        tvSaleList.bind('<<TreeviewSelect>>', onTreeSelect)

        tvSaleList.column("#0", width=0)

        tvSaleList.column("Index", width=25, anchor=CENTER)
        tvSaleList.heading("Index", text="#", anchor='n')

        tvSaleList.column("ord_num", width=0)
        tvSaleList.heading("ord_num", text="ord_num")

        tvSaleList.column("stor_id", width=150)
        tvSaleList.heading("stor_id", text="Store Name", anchor='n')

        tvSaleList.column("ord_date", width=100, anchor=CENTER)
        tvSaleList.heading("ord_date", text="OrderDate", anchor='n')

        tvSaleList.column("qty", width=100, anchor=CENTER)
        tvSaleList.heading("qty", text="Quantity", anchor='n')

        tvSaleList.column("payterms", width=120)
        tvSaleList.heading("payterms", text="PayTerms", anchor='n')

        tvSaleList.column("title_id", width=380)
        tvSaleList.heading("title_id", text="Title", anchor='n')

        entOrderNumberValue.focus_set()
        showList()
        SalesCRUDForm.mainloop()
