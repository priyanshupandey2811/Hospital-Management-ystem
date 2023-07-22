from tkinter import*
from tkinter import ttk
import time
import random
import datetime
from tkinter import messagebox
import mysql.connector
import sqlite3

class hospital:
    def database(self):
        conn=sqlite3.connect('Hotel_management_system.db')
        cur=conn.cursor()
        cur.execute("insert into Doctor_prescripiton values('"+self.NameOfTablet.get()+"','"+self.Ref.get()+"','"+self.Dose.get()+"','"+self.NumberOfTablet.get()+"','"+self.Lot.get()+"','"+self.IssueDate.get()+"','"+self.ExpData.get()+"','"+self.DailyDose.get()+"','"+self.SideEffect.get()+"','"+self.FurtherInfo.get()+"','"+self.BloodPressure.get()+"','"+self.Storage.get()+"','"+self.Medicine.get()+"','"+self.PatientId.get()+"','"+self.NhsNumber.get()+"','"+self.PatientName.get()+"','"+self.Dob.get()+"','"+self.PatientAddress.get()+"')")
        #cur.execute("INSERT INTO Doctor_prescripiton(Name of the tablet) VALUES(%s)",[self.NameOfTablet.get()])
        #cur.execute("INSERT INTO Doctor_prescripiton(Name of the tablet,Refeerence Number,Dose,Number of tablets,lot,Issue date,Expiry date,Daily dose,Side effect,Further information,Blood pressure,storage advice,Medicines,Patient Name,DOB,Patient address) VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",[self.NameOfTablet.get(),self.Ref.get(),self.Dose.get(),self.NumberOfTablet.get(),self.Lot.get(),self.IssueDate.get(),self.ExpData.get(),self.DailyDose.get(),self.SideEffect.get(),self.FurtherInfo.get(),self.BloodPressure.get(),self.Storage.get(),self.Medicine.get(),self.PatientId.get(),self.NhsNumber.get(),self.PatientName.get(),self.Dob.get(),self.PatientAddress.get()] )          
        conn.commit()
        conn.close()
        print("successfull")
            
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management")
        self.root.geometry('1540x800+0+0')

        self.NameOfTablet=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar()
        self.NumberOfTablet=StringVar()
        self.Lot=StringVar()  
        self.IssueDate=StringVar()
        self.ExpData=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInfo=StringVar()
        self.BloodPressure=StringVar()
        self.Storage=StringVar()
        self.Medicine=StringVar()
        self.PatientId=StringVar()
        self.NhsNumber=StringVar()
        self.PatientName=StringVar()
        self.Dob=StringVar()
        self.PatientAddress=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="cyan",font=("times new roman",50,'bold'))
        lbltitle.pack(side=TOP,fill=X)
        
        
        
    # ==============================DATAFRAME==========================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=120,width=1350,height=370)
        
        
        DataFrameLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,
                                font=("times new roman",30,'bold'),text ='Patient Information')
        DataFrameLeft.place(x=0,y=5,width=900,height=325)


        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,
                                font=("times new roman",30,'bold'),text ='Prescription')
        DataframeRight.place(x=900,y=5,width=370,height=325)
        
   
    # ==============================BUTTONFRAME==========================================
        
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=500,width=1350,height=69)


    # ==============================DETAILSFRAME==========================================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=570,width=1350,height=134)


    # ==============================DATAFRAMELEFT==========================================
    
        
        lblNameTablet=Label(DataFrameLeft,text="Name Of Tablet:",padx=2,pady=6,font=("times new roman",12,'bold'))
        lblNameTablet.grid(row=0,column=0)
    
        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.NameOfTablet,font=("times new roman",12,'bold'),width=33,)
        
        comNameTablet["values"]=("Nice","Corona Vacacine","Paracetamol","Amlodopine","Ativan","Dolo")
        comNameTablet.grid(row=0,column=1)
        
        lblref=Label(DataFrameLeft,text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.Ref,width=32)
        txtref.grid(row=1,column=1)
        
        lblDose=Label(DataFrameLeft,text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.Dose,width=32)
        txtDose.grid(row=2,column=1)
        
        lblNoOfTablet=Label(DataFrameLeft,text="No. Of Tablet:",padx=2,pady=6)
        lblNoOfTablet.grid(row=3,column=0,sticky=W)
        txtNoOfTablet=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.NumberOfTablet,width=32)
        txtNoOfTablet.grid(row=3,column=1)
        
        lblLOt=Label(DataFrameLeft,text="Lot:",padx=2,pady=6)
        lblLOt.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.Lot,width=32)
        txtLot.grid(row=4,column=1)
        
        
        lblIssueDate=Label(DataFrameLeft,text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.IssueDate,width=32)
        txtIssueDate.grid(row=5,column=1)
        
        lblExpDate=Label(DataFrameLeft,text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.ExpData,width=32)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose=Label(DataFrameLeft,text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.DailyDose,width=32)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect=Label(DataFrameLeft,text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.SideEffect,width=32)
        txtSideEffect.grid(row=8,column=1)
        
        lblFurtherInfo=Label(DataFrameLeft,text="Further Information:",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.FurtherInfo,width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataFrameLeft,text="Blood Pressure:",padx=2)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.BloodPressure,width=35)
        txtBloodPressure.grid(row=1,column=3)
 
        lblStorage=Label(DataFrameLeft,text="Storage Advice:",padx=2)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.Storage,width=35)
        txtStorage.grid(row=2,column=3)

        

        lblMedicine=Label(DataFrameLeft,text="Medicine:",padx=2)
        lblMedicine .grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,font=("arial",12,'bold'),width=35)
        txtMedicine.grid(row=3,column=3)
   
        lblPatientId=Label(DataFrameLeft,text="PatientId:",padx=2)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataFrameLeft,text="Nhs Number:",padx=2)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.NhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataFrameLeft,text="Patient Name:",padx=2)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDob=Label(DataFrameLeft,text="Date Of Birth:",padx=2)
        lblDob.grid(row=7,column=2,sticky=W)
        txtDob=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.Dob,width=35)
        txtDob.grid(row=7,column=3)


        lblPatientAddress=Label(DataFrameLeft,text="Patient Address:",padx=2)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",12,'bold'),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

# ==================================dataframeright===================================

        self.txtPrescription=Text(DataframeRight,font=("arial",12,'bold'),width=35,height=13,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


# ===============================button======================================================
        btnPrescription=Button(Buttonframe,font=("arial",12,'bold'),width=22,text="Prescription",fg='violet',bg="purple",padx=2,pady=6,command=self.database)
        btnPrescription.grid(row=0,column=0)
       
        btnPrescription=Button(Buttonframe,font=("arial",12,'bold'),width=22,text="Prescription Data",fg='violet',bg="green",padx=2,pady=6)
        btnPrescription.grid(row=0,column=1)
       
        btnPrescription=Button(Buttonframe,font=("arial",12,'bold'),width=22,text="Update",fg='violet',bg="yellow",padx=2,pady=6)
        btnPrescription.grid(row=0,column=2)
       
        btnPrescription=Button(Buttonframe,font=("arial",12,'bold'),width=22,text="Delete",fg='violet',bg="pink",padx=2,pady=6)
        btnPrescription.grid(row=0,column=3)
       
        btnPrescription=Button(Buttonframe,font=("arial",12,'bold'),width=22,text="clear",fg='violet',bg="cyan",padx=2,pady=6)
        btnPrescription.grid(row=0,column=4)
       
        btnPrescription=Button(Buttonframe,font=("arial",12,'bold'),width=22,text="Exit",fg='violet',bg="green",padx=2,pady=6)
        btnPrescription.grid(row=0,column=5)
        
    # ==================================Table=========================================

        
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        
        self.Hospital_Table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablet","lot","issuedate","expdate","dailydose","storage","nhsnumber",'pname',"dateofbirth","patietaddress"),xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
        scroll_x.pack=("side=BOTTOM,fill=X")
        scroll_y.pack=("side=RIGHT,fill=Y")
        
        scroll_x=ttk.Scrollbar(command=self.Hospital_Table.xview)
        scroll_y=ttk.Scrollbar(command=self.Hospital_Table.yview)
        
        self.Hospital_Table.heading("nameoftable",text="Name Of Tablet:")
        self.Hospital_Table.heading("ref",text="Reference No:")
        self.Hospital_Table.heading("dose",text="Dose")
        self.Hospital_Table.heading("nooftablet",text="No. Of Tablet")
        self.Hospital_Table.heading("lot",text="Lot")
        self.Hospital_Table.heading("issuedate",text="Issue Date")
        self.Hospital_Table.heading("expdate",text="Exp Date")
        self.Hospital_Table.heading("dailydose",text="Daily Dose")
        self.Hospital_Table.heading("storage",text="Storage")
        self.Hospital_Table.heading("nhsnumber",text="NhsNumber")
        self.Hospital_Table.heading("pname",text="Patient Name")
        self.Hospital_Table.heading("dateofbirth",text="Dob")
        self.Hospital_Table.heading("patietaddress",text="Patiet Address")
        

        self.Hospital_Table["show"]="headings"


        self.Hospital_Table.column("nameoftable",width=170)
        self.Hospital_Table.column("ref",width=170)
        self.Hospital_Table.column("dose",width=170)
        self.Hospital_Table.column("nooftablet",width=170)
        self.Hospital_Table.column("lot",width=170)
        self.Hospital_Table.column("issuedate",width=170)
        self.Hospital_Table.column("expdate",width=170)
        self.Hospital_Table.column("dailydose",width=170)
        self.Hospital_Table.column("storage",width=170)
        self.Hospital_Table.column("nhsnumber",width=170)
        self.Hospital_Table.column("pname",width=170)
        self.Hospital_Table.column("dateofbirth",width=170)
        self.Hospital_Table.column("patietaddress",width=170)


        self.Hospital_Table.pack(fill=BOTH,expand=1)


    # ==================================Functionality=========================================
'''
        def iPrescriptionData(self):
            if self.NameOftablet.grt()=="" or self.ref.get()=="":
                 print("ERROR,All Field Are Required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="test@123",database="Mydata")

                my_cursor=conn.cursor()






'''

        

root=Tk()
ob=hospital(root)

root.mainloop()
ob.database()
