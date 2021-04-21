from bank_system import BankSystem
from updateAdminDetails import updAdmnDtls
from allCustomerData import allCustomerData
from delete_get_customer import deleteCustomer
from transfer_money import transferMoney
from managment_Report import managmentReport
from Admin_change_pass import AdminChangePass
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import time, os

class adminMenu:
    def __init__(self, name="", bnksys = "", admin_obj = ""):
        self.name = name
        self.bnksys = bnksys
        self.admin_obj = admin_obj
        
        self.window = tk.Tk()
        self.window.geometry("500x400")
        self.window.resizable(width=False, height=False)
        self.window.overrideredirect(True)
        self.window.wm_iconbitmap('BCU.ico')
        welString = "Welcom "+ self.name +"- Main menu"
        self.window.title(welString)
        self.window.after(1, lambda: self.window.focus_force())
                
        self.btnTransferMoney         = tk.Button(self.window, text = "Transfer money", width = 50, command = self.transferMoney)
        self.btnGetCustomerAccount    = tk.Button(self.window, text = "Customer account operations & profile settings", width = 50, command = self.getCustomerAccount)
        self.btnDeleteCustomer        = tk.Button(self.window, text = "Delete customer", width = 50, command = self.deleteCustomer)
        self.btnPrintCustomersDetails = tk.Button(self.window, text = "Print all customers detail", width = 50, command = self.printCustomersDetails)
        self.btnUpdateAdminName       = tk.Button(self.window, text = "Update admin name", width = 50, command = self.updateAdminName)
        self.btnUpdateAdminAddress    = tk.Button(self.window, text = "Update admin address", width = 50, command = self.updateAdminAddress)
        self.btnShowAdminDetails      = tk.Button(self.window, text = "Show admin details", width = 50, command = self.showAdminDetails)
        self.btnImportCustomerData    = tk.Button(self.window, text = "Import customers data", width = 50, command = self.importCustomerData)
        self.btnExportCustomerData    = tk.Button(self.window, text = "Export customers data", width = 50, command = self.exportCustomerData)
        self.btnCallReport            = tk.Button(self.window, text = "Management report...", width = 50, command = self.callReport)
        self.btnSignOut               = tk.Button(self.window, text = "Sign out", width = 50, command = self.signOut)
        
        self.lblAdminFname   = tk.Label(self.window, text="Admin first name:",font=("Helvetica", 9))
        self.lblAdminLname   = tk.Label(self.window, text="Admin last name:",font=("Helvetica", 9))
        self.lblAdminAddress = tk.Label(self.window, text="Address:",font=("Helvetica", 11))
        self.lblAdminAdd0    = tk.Label(self.window, text="Door number:",font=("Helvetica", 9))
        self.lblAdminAdd1    = tk.Label(self.window, text="Road:",font=("Helvetica", 9))
        self.lblAdminAdd2    = tk.Label(self.window, text="City:",font=("Helvetica", 9))
        self.lblAdminAdd3    = tk.Label(self.window, text="Postcode:",font=("Helvetica", 9))          
        self.txtAdminFname   = tk.Label(self.window, text= self.admin_obj.fname,font=("Helvetica", 9),fg="#0000cc")
        self.txtAdminLname   = tk.Label(self.window, text= self.admin_obj.lname,font=("Helvetica", 9),fg="#0000cc")
        self.txtAdminAdd0    = tk.Label(self.window, text=self.admin_obj.address[0],font=("Helvetica", 9),fg="#0000cc")
        self.txtAdminAdd1    = tk.Label(self.window, text=self.admin_obj.address[1],font=("Helvetica", 9),fg="#0000cc")
        self.txtAdminAdd2    = tk.Label(self.window, text=self.admin_obj.address[2],font=("Helvetica", 9),fg="#0000cc")
        self.txtAdminAdd3    = tk.Label(self.window, text=self.admin_obj.address[3],font=("Helvetica", 9),fg="#0000cc")
        self.lblTime         = tk.Label(self.window, text="",font=("Helvetica", 8),fg="#0000cc")
        self.btnChangePass   = tk.Button(self.window, text = "Change password", width = 30, command = self.changePassword)
        
        self.lblTime.place(x = 2,y= 2)
        self.lblAdminFname.place(x = 500,y= 30)
        self.lblAdminLname.place(x = 500,y= 60)
        self.lblAdminAddress.place(x = 500,y= 90)
        self.lblAdminAdd0.place(x = 500,y= 120)
        self.lblAdminAdd1.place(x = 500,y= 150)
        self.lblAdminAdd2.place(x = 500,y= 180)
        self.lblAdminAdd3.place(x = 500,y= 210)            
        self.txtAdminFname.place(x = 600,y= 30)
        self.txtAdminLname.place(x = 600,y= 60)
        self.txtAdminAdd0.place(x = 600,y= 120)
        self.txtAdminAdd1.place(x = 600,y= 150)
        self.txtAdminAdd2.place(x = 600,y= 180)
        self.txtAdminAdd3.place(x = 600,y= 210) 
        self.btnChangePass.place(x = 500,y= 280) 
             
        self.btnTransferMoney.place(x = 70,y= 30)
        self.btnGetCustomerAccount.place(x = 70,y= 55)
        self.btnDeleteCustomer.place(x = 70,y=80)
        self.btnPrintCustomersDetails.place(x = 70,y= 105)
        self.btnUpdateAdminName.place(x = 70,y= 130)
        self.btnUpdateAdminAddress.place(x = 70,y= 155)
        self.btnShowAdminDetails.place(x = 70,y= 180)
        self.btnImportCustomerData.place(x = 70,y= 250)
        self.btnExportCustomerData.place(x = 70,y= 275)
        self.btnCallReport.place(x = 70,y= 300)
        self.btnSignOut.place(x = 70,y= 325) 
        
        self.update_clock()
        self.mouseHover()

        tk.mainloop()
                   
    def transferMoney(self):
        self.window.geometry("500x400")
        trnsMoney = transferMoney(self.name,self.bnksys)
                   
    def getCustomerAccount(self):
        self.window.geometry("500x400")
        dltCust = deleteCustomer(self.name, self.bnksys,self.admin_obj, 1)
    
    def deleteCustomer(self):
        self.window.geometry("500x400")

        if self.admin_obj.has_full_admin_right() == "True":
            dltCust = deleteCustomer(self.name, self.bnksys,self.admin_obj, 2)
        else:
            messagebox.showinfo("Notice..","The Admin has no full privilege!!..")
               
    def printCustomersDetails(self):
        self.window.geometry("500x400")
        alCust = allCustomerData(self.name,self.bnksys)
    
    def updateAdminName(self):
        self.window.geometry("500x400")
        admDtls = updAdmnDtls(self.name,self.admin_obj,self.bnksys,1)
    
    def updateAdminAddress(self): 
        self.window.geometry("500x400")
        admDtls = updAdmnDtls(self.name,self.admin_obj,self.bnksys,2)

    def importCustomerData(self):
        self.window.geometry("500x400")
        self.window.fileName = filedialog.askopenfilename(filetypes = (("BCU banks files", "*.bnk"),("All files","*.*")))
        
        if (self.window.fileName):
            
            tmp = messagebox.askokcancel("Warning !!","You may lose stored customer data !!..")
            
            if (tmp):
                self.bnksys.accounts_list.clear()
                countImported,countUnimported = self.bnksys.import_customer_information(self.window.fileName)
                messagebox.showinfo("Information", str(abs(countImported-countUnimported))+"/"+str(countImported) +" Accounts have been imported..")
            
            if countUnimported > 0:
                messagebox.showerror("Import error","Please check the imported Log file !!")
            
    
    def exportCustomerData(self):
        self.window.geometry("500x400")
        countExported = self.bnksys.export_customer_informations() 
        if countExported > 0:
            messagebox.showinfo("Information", str(countExported) +" Accounts have been exported..")
    
    def callReport(self):
        self.window.geometry("500x400")
        mngReport = managmentReport(self.name, self.bnksys)
    
    def signOut(self):
        self.window.geometry("500x400")
        self.bnksys.exportAllData()
        if os.path.isfile('tempTrans') == 1:
            os.remove('tempTrans')
        self.window.destroy()
       
    def showAdminDetails(self):
        if self.window.winfo_width() == 500:
            self.window.geometry("800x400")        
        else:
            self.window.geometry("500x400")
        
        self.txtAdminFname.config(text=self.admin_obj.fname)
        self.txtAdminLname.config(text=self.admin_obj.lname)
        
        self.txtAdminAdd0.config(text=self.admin_obj.address[0])
        self.txtAdminAdd1.config(text=self.admin_obj.address[1])
        self.txtAdminAdd2.config(text=self.admin_obj.address[2])
        self.txtAdminAdd3.config(text=self.admin_obj.address[3])
        
    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.lblTime.configure(text=now)
        self.window.after(1000, self.update_clock)
        
    def changePassword(self):
        admChangePass = AdminChangePass(self.name, self.bnksys, self.admin_obj)
        self.bnksys.exportAdminInfo()
        
    def mouseHover(self):
        self.btnTransferMoney.bind("<Enter>", lambda event, h=self.btnTransferMoney: h.configure(bg="#77aaff"))
        self.btnTransferMoney.bind("<Leave>", lambda event, h=self.btnTransferMoney: h.configure(bg="SystemButtonFace"))
        self.btnGetCustomerAccount.bind("<Enter>", lambda event, h=self.btnGetCustomerAccount: h.configure(bg="#77aaff"))
        self.btnGetCustomerAccount.bind("<Leave>", lambda event, h=self.btnGetCustomerAccount: h.configure(bg="SystemButtonFace"))  
        self.btnDeleteCustomer.bind("<Enter>", lambda event, h=self.btnDeleteCustomer: h.configure(bg="#77aaff"))
        self.btnDeleteCustomer.bind("<Leave>", lambda event, h=self.btnDeleteCustomer: h.configure(bg="SystemButtonFace"))       
        self.btnPrintCustomersDetails.bind("<Enter>", lambda event, h=self.btnPrintCustomersDetails: h.configure(bg="#77aaff"))
        self.btnPrintCustomersDetails.bind("<Leave>", lambda event, h=self.btnPrintCustomersDetails: h.configure(bg="SystemButtonFace"))      
        self.btnUpdateAdminName.bind("<Enter>", lambda event, h=self.btnUpdateAdminName: h.configure(bg="#77aaff"))
        self.btnUpdateAdminName.bind("<Leave>", lambda event, h=self.btnUpdateAdminName: h.configure(bg="SystemButtonFace"))       
        self.btnUpdateAdminAddress.bind("<Enter>", lambda event, h=self.btnUpdateAdminAddress: h.configure(bg="#77aaff"))
        self.btnUpdateAdminAddress.bind("<Leave>", lambda event, h=self.btnUpdateAdminAddress: h.configure(bg="SystemButtonFace"))
        self.btnShowAdminDetails.bind("<Enter>", lambda event, h=self.btnShowAdminDetails: h.configure(bg="#77aaff"))
        self.btnShowAdminDetails.bind("<Leave>", lambda event, h=self.btnShowAdminDetails: h.configure(bg="SystemButtonFace"))       
        self.btnImportCustomerData.bind("<Enter>", lambda event, h=self.btnImportCustomerData: h.configure(bg="#77aaff"))
        self.btnImportCustomerData.bind("<Leave>", lambda event, h=self.btnImportCustomerData: h.configure(bg="SystemButtonFace"))       
        self.btnExportCustomerData.bind("<Enter>", lambda event, h=self.btnExportCustomerData: h.configure(bg="#77aaff"))
        self.btnExportCustomerData.bind("<Leave>", lambda event, h=self.btnExportCustomerData: h.configure(bg="SystemButtonFace"))       
        self.btnCallReport.bind("<Enter>", lambda event, h=self.btnCallReport: h.configure(bg="#77aaff"))
        self.btnCallReport.bind("<Leave>", lambda event, h=self.btnCallReport: h.configure(bg="SystemButtonFace"))      
        self.btnSignOut.bind("<Enter>", lambda event, h=self.btnSignOut: h.configure(bg="#77aaff"))
        self.btnSignOut.bind("<Leave>", lambda event, h=self.btnSignOut: h.configure(bg="SystemButtonFace"))
        

            
        
            


        

        
        
            
            
        
        

        
        
        


