from tkinter import*
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox

class Hospital:

    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management Systems")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        cmbNameTablets=StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot=StringVar()
        IssuedDate=StringVar()
        ExpDate=StringVar()
        DailyDose=StringVar()
        PossibleSideEffects=StringVar()
        FurtherInformation=StringVar()
        StorageAdvice=StringVar()
        DrivingUsingMachines=StringVar()
        HowtoUseMedication=StringVar()
        PatientID=StringVar()
        PatientNHSNo=StringVar()
        PatientName = StringVar()
        DateofBirth = StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()

        #=================================================Function mdeclaration=========================================================#
        
        def iExit():
            iExit=tkinter.messagebox.askyesno("Hospital Management Systems","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def iPrescription():
                self.txtPrescription.insert(END,'Name of Tablets: \t\t\t' + cmbNameTablets.get() + "\n")
                self.txtPrescription.insert(END,'Reference No: \t\t\t' + Ref.get() + "\n")
                self.txtPrescription.insert(END,'Dose: \t\t\t' + Dose.get() + "\n")
                self.txtPrescription.insert(END,'Number of Tablets: \t\t\t' + NumberTablets.get() + "\n")
                self.txtPrescription.insert(END,'Lot: \t\t\t' + Lot.get() + "\n")
                self.txtPrescription.insert(END,'Issued Date: \t\t\t' + IssuedDate.get() + "\n")
                self.txtPrescription.insert(END,'Expiry Date: \t\t\t' + ExpDate.get() + "\n")
                self.txtPrescription.insert(END,'Daily Dose: \t\t\t' + DailyDose.get() + "\n")
                self.txtPrescription.insert(END,'Possible Side Effects: \t\t\t' + PossibleSideEffects.get() + "\n")
                self.txtPrescription.insert(END,'Further Information: \t\t\t' + FurtherInformation.get() + "\n")
                self.txtPrescription.insert(END,'Storage Advice: \t\t\t' + StorageAdvice.get() + "\n")
                self.txtPrescription.insert(END,'Driving or Using Machines: \t\t\t' + DrivingUsingMachines.get() + "\n")
                self.txtPrescription.insert(END,'How to use Medication: \t\t\t' + HowtoUseMedication.get() + "\n")
                self.txtPrescription.insert(END,'Patient ID: \t\t\t' + PatientID.get() + "\n")
                self.txtPrescription.insert(END,'Patient NHS Number: \t\t\t' + PatientNHSNo.get() + "\n")
                self.txtPrescription.insert(END,'Patient Name: \t\t\t' + PatientName.get() + "\n")
                self.txtPrescription.insert(END,'Date of Birth: \t\t\t' + DateofBirth.get() + "\n")
                self.txtPrescription.insert(END,'Patient Address: \t\t\t' + PatientAddress.get() + "\n")
                return

        def iPrescriptionData():                   
                         self.txtFrameDetail.insert(END, cmbNameTablets.get()+"\t"+
                                                              Ref.get() +"\t"+
                                                              Dose.get() +"\t"+
                                                              NumberTablets.get() +"\t"+
                                                              Lot.get() +"\t"+
                                                              IssuedDate.get() +"\t"+
                                                              ExpDate.get() +"\t"+
                                                              DailyDose.get()+"\t"+
                                                              StorageAdvice.get() +"\t"+
                                                              PatientNHSNo.get() + "\t"+
                                                              PatientName.get() + "\t"+
                                                              DateofBirth.get() + "\t"+
                                                              PatientAddress.get() +"\n" )

        def iDelete():
                cmbNameTablets.set("")
                self.cboNameTablet.current(0)
                Ref.set("")
                Dose = StringVar()
                NumberTablets.set("")
                Lot.set("")
                IssuedDate.set("")
                ExpDate.set("")
                DailyDose.set("")
                PossibleSideEffects.set("")
                FurtherInformation.set("")
                StorageAdvice.set("")
                DrivingUsingMachines.set("")
                HowtoUseMedication.set("")
                PatientID.set("")
                PatientNHSNo.set("")
                PatientName.set("")
                DateofBirth.set("")
                PatientAddress.set("")
                self.txtPrescription.delete("1.0",END)
                self.txtFrameDetail.delete("1.0",END)
                
                return

        def iReset():
                cmbNameTablets.set("")
                self.cboNameTablet.current(0)
                Ref.set("")
                Dose = StringVar()
                NumberTablets.set("")
                Lot.set("")
                IssuedDate.set("")
                ExpDate.set("")
                DailyDose.set("")
                PossibleSideEffects.set("")
                FurtherInformation.set("")
                StorageAdvice.set("")
                DrivingUsingMachines.set("")
                HowtoUseMedication.set("")
                PatientID.set("")
                PatientNHSNo.set("")
                PatientName.set("")
                DateofBirth.set("")
                PatientAddress.set("")
                self.txtPrescription.delete("1.0",END)
                #self.txtFrameDetail.delete("1.0",END)
                
                return
        #=================================================Frame=========================================================#
        MainFrame =Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame, font=('arial', 40, 'bold'), text="Hospital Management Systems",padx=2)
        self.lblTitle.grid()

        FrameDetail= Frame(MainFrame, bd=20, width=1350,height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=20, width=1350,height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame= Frame(MainFrame, bd=20, width=1350,height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)     
        
        DataFrameLEFT= LabelFrame(DataFrame, bd=10, width=800,height=300, padx=20, relief=RIDGE,font=('arial', 12, 'bold'), text="Patient Information:")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT= LabelFrame(DataFrame, bd=10, width=450,height=300, padx=20, relief=RIDGE, font=('arial', 12, 'bold'), text="Prescription:")
        DataFrameRIGHT.pack(side=RIGHT)

         #====================================DataFrameLEFT================================================================================#

        self.lblNameTablet =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Name of Tablets:",padx=2,pady=2)
        self.lblNameTablet.grid(row=0,column=0,sticky=W)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets,state='readonly',font=('arial', 12, 'bold'),width=23)
        self.cboNameTablet['value']=('','Ibuprofen', 'Co-codamol', 'Paracetamol', 'Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1)

        self.lblFurtherInfo =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Further Information:",padx=2,pady=2)
        self.lblFurtherInfo.grid(row=0,column=2,sticky=W)
        self.txtFurtherInfo=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=FurtherInformation,width=25)
        self.txtFurtherInfo.grid(row=0,column=3)

        self.lblRef =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Reference No:",padx=2,pady=2)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.txtRef=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=Ref,width=25)
        self.txtRef.grid(row=1,column=1)

        self.lblStorage =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Storage Advice:",padx=2,pady=2)
        self.lblStorage.grid(row=1,column=2,sticky=W)
        self.txtStorage=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=StorageAdvice,width=25)
        self.txtStorage.grid(row=1,column=3)

        self.lblDose =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Dose:",padx=2,pady=2)
        self.lblDose.grid(row=2,column=0,sticky=W)
        self.txtDose=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=Dose,width=25)
        self.txtDose.grid(row=2,column=1)

        self.lblDUseMachine =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Driving Machines:",padx=2,pady=2)
        self.lblDUseMachine.grid(row=2,column=2,sticky=W)
        self.txtDUseMachine=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=DrivingUsingMachines,width=25)
        self.txtDUseMachine.grid(row=2,column=3)

        self.lblNoOfTablets =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="No. of Tablets",padx=2,pady=2)
        self.lblNoOfTablets.grid(row=3,column=0,sticky=W)
        self.txtNoOfTablets=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=NumberTablets,width=25)
        self.txtNoOfTablets.grid(row=3,column=1)

        self.lblUseMedication =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Medication:",padx=2,pady=2)
        self.lblUseMedication.grid(row=3,column=2,sticky=W)
        self.txtUseMedication=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=HowtoUseMedication,width=25)
        self.txtUseMedication.grid(row=3,column=3)

        self.lblLot =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Lot:",padx=2,pady=2)
        self.lblLot.grid(row=4,column=0,sticky=W)
        self.txtLot=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=Lot,width=25)
        self.txtLot.grid(row=4,column=1)

        self.lblPatientID =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient ID:",padx=2,pady=2)
        self.lblPatientID.grid(row=4,column=2,sticky=W)
        self.txtPatientID=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=PatientID,width=25)
        self.txtPatientID.grid(row=4,column=3)

        self.lblIssuedDate =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Issued Date:",padx=2,pady=2)
        self.lblIssuedDate.grid(row=5,column=0,sticky=W)
        self.txtIssuedDate=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=IssuedDate,width=25)
        self.txtIssuedDate.grid(row=5,column=1)

        self.lblNHSNumber =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="NHS Number:",padx=2,pady=2)
        self.lblNHSNumber.grid(row=5,column=2,sticky=W)
        self.txtNHSNumber=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=PatientNHSNo,width=25)
        self.txtNHSNumber.grid(row=5,column=3)
        
        self.lblExpDate =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Exp Date:",padx=2,pady=2)
        self.lblExpDate.grid(row=6,column=0,sticky=W)
        self.txtExpDate=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=ExpDate,width=25)
        self.txtExpDate.grid(row=6,column=1)

        self.lblPatientName =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patients Name:",padx=2,pady=2)
        self.lblPatientName.grid(row=6,column=2,sticky=W)
        self.txtPatientName=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=PatientName,width=25)
        self.txtPatientName.grid(row=6,column=3)

        self.lblDailyDose =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Daily Dose:",padx=2,pady=2)
        self.lblDailyDose.grid(row=7,column=0,sticky=W)
        self.txtDailyDose=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=DailyDose,width=25)
        self.txtDailyDose.grid(row=7,column=1)

        self.lblDateofBirth =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date of Birth:",padx=2,pady=2)
        self.lblDateofBirth.grid(row=7,column=2,sticky=W)
        self.txtDateofBirth=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=DateofBirth,width=25)
        self.txtDateofBirth.grid(row=7,column=3)

        self.lblSideEffects =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Side Effects:",padx=2,pady=2)
        self.lblSideEffects.grid(row=8,column=0,sticky=W)
        self.txtSideEffects=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=PossibleSideEffects,width=25)
        self.txtSideEffects.grid(row=8,column=1)

        self.lblPatientAddress =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Address:",padx=2,pady=2)
        self.lblPatientAddress.grid(row=8,column=2,sticky=W)
        self.txtPatientAddress=Entry(DataFrameLEFT,font=('arial', 12, 'bold'),textvariable=PatientAddress,width=25)
        self.txtPatientAddress.grid(row=8,column=3)

        #===================================================DataFrameRIGHT==========================================================#

        self.txtPrescription=Text(DataFrameRIGHT, font=('arial', 12, 'bold'),width=43,height=14,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #===================================================FrameDetail============================================================#

        self.lblLabel=Label(FrameDetail, font=('arial', 10, 'bold'), text="NameofTablets\tReferenceNo.\tDoseage\t  No.ofTablets\tLot\tIssuedDate\tExp.Date\tDailyDose\tStorageAdv.\tNHS Number\tPatientsName\tDOB\tAddress",pady=8)
        
        self.lblLabel.grid(row=0,column=0)


        self.txtFrameDetail=Text(FrameDetail, font=('arial', 12, 'bold'),width=141,height=4,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)

        #=======================================================ButtonFrame============================================================#

        self.btnPrescription=Button(ButtonFrame, text='Prescription',font=('arial', 12, 'bold'),width=24,bd=4,command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)
        
        self.btnPrescriptionData=Button(ButtonFrame, text='Prescription Data',font=('arial', 12, 'bold'),width=24,bd=4,command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0,column=1)

        self.btnDelete=Button(ButtonFrame, text='Delete',font=('arial', 12, 'bold'),width=24,bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=2)

        self.btnReset=Button(ButtonFrame, text='Reset',font=('arial', 12, 'bold'),width=24,bd=4,command=iReset)
        self.btnReset.grid(row=0,column=3)

        self.btnExit=Button(ButtonFrame, text='Exit',font=('arial', 12, 'bold'),width=24,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=4)
        
if __name__=='__main__':
          root = Tk()
          application = Hospital(root)
          root.mainLoop()


