from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")

        #==================== variable ===================================

        self.member_var=StringVar()
        self.prn_no_var=StringVar()
        self.idno_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.pincode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.bookauthor_var=StringVar()
        self.issuedate_var=StringVar()
        self.duedate_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.actualprice_var=StringVar()
        
        
        
        

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="black",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #=========================dataframe left==============================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,text="Member Type:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)


        lblPRN_No=Label(DataFrameLeft,text="PRN NO:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,textvariable=self.prn_no_var,font=("times new roman",15,"bold"),width=23)
        txtPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,text="ID NO:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.idno_var,font=("times new roman",15,"bold"),width=23)
        txtTitle.grid(row=2,column=1)


        lblFirstName=Label(DataFrameLeft,text="First Name",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("times new roman",15,"bold"),width=23)
        txtFirstName.grid(row=3,column=1)


        lblLastName=Label(DataFrameLeft,text="Last Name:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("times new roman",15,"bold"),width=23)
        txtLastName.grid(row=4,column=1)

        lblAddress=Label(DataFrameLeft,text="Address:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry(DataFrameLeft,textvariable=self.address_var,font=("times new roman",15,"bold"),width=23)
        txtAddress.grid(row=5,column=1)

        lblPinCode=Label(DataFrameLeft,text="PinCode:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPinCode.grid(row=6,column=0,sticky=W)
        txtPinCode=Entry(DataFrameLeft,textvariable=self.pincode_var,font=("times new roman",15,"bold"),width=23)
        txtPinCode.grid(row=6,column=1)

        lblMobile=Label(DataFrameLeft,text="Mobile:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMobile.grid(row=7,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman",15,"bold"),width=23)
        txtMobile.grid(row=7,column=1)

        lblBookId=Label(DataFrameLeft,text="BookId:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("times new roman",15,"bold"),width=23)
        txtBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,text="Book Title:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("times new roman",15,"bold"),width=23)
        txtBookTitle.grid(row=1,column=3)

        lblBookAuthor=Label(DataFrameLeft,text="Book Author:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBookAuthor.grid(row=2,column=2,sticky=W)
        txtBookAuthor=Entry(DataFrameLeft,textvariable=self.bookauthor_var,font=("times new roman",15,"bold"),width=23)
        txtBookAuthor.grid(row=2,column=3)

        lblIssueDate=Label(DataFrameLeft,text="Issue Date:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblIssueDate.grid(row=3,column=2,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("times new roman",15,"bold"),width=23)
        txtIssueDate.grid(row=3,column=3)

        lblDueDate=Label(DataFrameLeft,text="Due Date:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDueDate.grid(row=4,column=2,sticky=W)
        txtDueDate=Entry(DataFrameLeft,textvariable=self.duedate_var,font=("times new roman",15,"bold"),width=23)
        txtDueDate.grid(row=4,column=3)

        lblLateReturnFine=Label(DataFrameLeft,text="LateReturnFine:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=5,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("times new roman",15,"bold"),width=23)
        txtLateReturnFine.grid(row=5,column=3)

        lblActualPrice=Label(DataFrameLeft,text="Actual Price:",bg="powder blue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=6,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.actualprice_var,font=("times new roman",15,"bold"),width=23)
        txtActualPrice.grid(row=6,column=3)

        #=============================== data frame right=========================================================

        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Python Programming','Data structure in C','operating system','computer achitecture','Dstl','Elctronics','Mechanics','The secreat of millionaire mind',
                   'Pride and prejudice','The lord of rings','Harry potter','Jane eyre','Java','Automata theory','Internet of things','Machine learning','Super intelligence',
                   'Deep learning','Human capability','The allignment problem','Control system','The art of electronics','Digital electronics','Theory of automata','Law of attraction',
                   'Oops concept','Programming in C','General apptitude','Reasoning','General knowledge','The secreat of happiness','Chemistry','Physics','mtahematics','Poem books',
                   'Social science','Political Science']

        listBox=Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=16)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)


        for item in listBooks:
            listBox.insert(END,item)


        #=================================Button Frame=========================


        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,text="Add Data",font=("times new roman",12,"bold"),width=23,bg="blue",fg="black")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,text="Show Data",font=("times new roman",12,"bold"),width=23,bg="blue",fg="black")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,text="Update",font=("times new roman",12,"bold"),width=23,bg="blue",fg="black")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,text="Delete",font=("times new roman",12,"bold"),width=23,bg="blue",fg="black")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",font=("times new roman",12,"bold"),width=23,bg="blue",fg="black")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",font=("times new roman",12,"bold"),width=23,bg="blue",fg="black")
        btnAddData.grid(row=0,column=5)
        

        #================================information frame======================


        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=200)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=180)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","idno","firstname","lastname","address","pincode","mobile","bookid","booktitle",
                                                "bookauthor","issuedate","duedate","latereturnfine","actualprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN NO")
        self.library_table.heading("idno",text="ID NO")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("pincode",text="Pin Code")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("bookauthor",text="Book Author")
        self.library_table.heading("issuedate",text="Issue Date")
        self.library_table.heading("duedate",text="Due Date")
        self.library_table.heading("latereturnfine",text="Late return fine")
        self.library_table.heading("actualprice",text="Actual price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("pincode",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("bookauthor",width=100)
        self.library_table.column("issuedate",width=100)
        self.library_table.column("duedate",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("actualprice",width=100)



     

            

if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()

        
