from deposit_withdraw import depositWithdraw
from update_customer_details import updCustDtls
from tkinter import messagebox
import tkinter as tk


class customerMenuGui:
    def __init__(self, name="",cust_obj="",bnksys_obj=""):
        self.cust_obj = cust_obj
        self.bnksys_obj = bnksys_obj
        self.name = name
        
        self.window = tk.Tk()
        self.window.geometry("500x300")
        self.window.resizable(width=False, height=False)
        self.window.wm_iconbitmap('BCU.ico')
        welString = self.name +" this is your transaction options .."
        self.window.title(welString)
        self.window.after(1, lambda: self.window.focus_force())

        self.btnDeposit          = tk.Button(self.window, text = "Deposit money", width = 50, command = self.depositMoney)
        self.btnWithdraw         = tk.Button(self.window, text = "Withdraw money", width = 50, command = self.withdrawMoney)
        self.btnCheckbalance     = tk.Button(self.window, text = "Check balance", width = 50, command = self.checkBalance)
        self.btnUpdCustomerNmae  = tk.Button(self.window, text = "Update customer name", width = 50, command = self.updateCustomerName)
        self.btnUpdCustomerAddr  = tk.Button(self.window, text = "Update customer address", width = 50, command = self.updateCustomerAddress)
        self.btnShowCustomerDtls = tk.Button(self.window, text = "Show customer details", width = 50, command = self.showCustomerDetails)
        self.btnGoback           = tk.Button(self.window, text = "Back", width = 50, command = self.goBack)
        
        self.btnDeposit.place(x = 70,y= 40)
        self.btnWithdraw.place(x = 70,y= 65)
        self.btnCheckbalance.place(x = 70,y=90)
        self.btnUpdCustomerNmae.place(x = 70,y= 115)
        self.btnUpdCustomerAddr.place(x = 70,y= 140)
        self.btnShowCustomerDtls.place(x = 70,y= 165)
        self.btnGoback.place(x = 70,y= 190) 
        
        self.lblCustFname   = tk.Label(self.window, text="Customer first name:",font=("Helvetica", 9))
        self.lblCustLname   = tk.Label(self.window, text="Customer last name:",font=("Helvetica", 9))
        self.lblCustAddress = tk.Label(self.window, text="Address:",font=("Helvetica", 11))
        self.lblCustAdd0    = tk.Label(self.window, text="Door number:",font=("Helvetica", 9))
        self.lblCustAdd1    = tk.Label(self.window, text="Road:",font=("Helvetica", 9))
        self.lblCustAdd2    = tk.Label(self.window, text="City:",font=("Helvetica", 9))
        self.lblCustAdd3    = tk.Label(self.window, text="Postcode:",font=("Helvetica", 9))          
        self.txtCustFname   = tk.Label(self.window, text= self.cust_obj.fname,font=("Helvetica", 9),fg="#0000cc")
        self.txtCustLname   = tk.Label(self.window, text= self.cust_obj.lname,font=("Helvetica", 9),fg="#0000cc")
        self.txtCustAdd0    = tk.Label(self.window, text=self.cust_obj.address[0],font=("Helvetica", 9),fg="#0000cc")
        self.txtCustAdd1    = tk.Label(self.window, text=self.cust_obj.address[1],font=("Helvetica", 9),fg="#0000cc")
        self.txtCustAdd2    = tk.Label(self.window, text=self.cust_obj.address[2],font=("Helvetica", 9),fg="#0000cc")
        self.txtCustAdd3    = tk.Label(self.window, text=self.cust_obj.address[3],font=("Helvetica", 9),fg="#0000cc")

        self.lblCustFname.place(x = 500,y= 30)
        self.lblCustLname.place(x = 500,y= 60)
        self.lblCustAddress.place(x = 500,y= 90)
        self.lblCustAdd0.place(x = 500,y= 120)
        self.lblCustAdd1.place(x = 500,y= 150)
        self.lblCustAdd2.place(x = 500,y= 180)
        self.lblCustAdd3.place(x = 500,y= 210)            
        self.txtCustFname.place(x = 620,y= 30)
        self.txtCustLname.place(x = 620,y= 60)
        self.txtCustAdd0.place(x = 620,y= 120)
        self.txtCustAdd1.place(x = 620,y= 150)
        self.txtCustAdd2.place(x = 620,y= 180)
        self.txtCustAdd3.place(x = 620,y= 210) 
        
        if self.window.winfo_width() == 800:
            welString = self.name +"- Customer details .."
            self.window.title(welString)
        else:
            welString = self.name +" this is your transaction options .."
            self.window.title(welString)
        
        self.mouseHover()
        tk.mainloop()

    def depositMoney(self):
        self.window.geometry("500x300")
        self.getFormAddress()
        dewith = depositWithdraw(self.name,self.cust_obj,self.bnksys_obj,1)
    
    def withdrawMoney(self):
        self.window.geometry("500x300")
        self.getFormAddress()
        dewith = depositWithdraw(self.name,self.cust_obj,self.bnksys_obj,2)
    
    def checkBalance(self):
        self.window.geometry("500x300")
        self.getFormAddress()
        if self.cust_obj.account_type == "1":
            strbalance = "The account balance is £"+self.bnksys_obj.formatString(str(self.cust_obj.get_balance()))                   
        elif self.cust_obj.account_type == "2":
            strbalance = "The account balance is £"+self.bnksys_obj.formatString(str(self.cust_obj.get_balance()))+"\n\n Over draft amount is "+self.bnksys_obj.formatString(str(self.cust_obj.get_overdraft_amount()))+"\n Over draft limit is "+ self.bnksys_obj.formatString(str(self.cust_obj.get_overdraft_limit()))                    
        
        messagebox.showinfo("Balance info",strbalance)
    
    def updateCustomerName(self):
        self.window.geometry("500x300")
        self.getFormAddress()
        updCust = updCustDtls(self.name,self.cust_obj,self.bnksys_obj,1)
    
    def updateCustomerAddress(self):
        self.window.geometry("500x300")
        updCust = updCustDtls(self.name,self.cust_obj,self.bnksys_obj,2)
    
    def showCustomerDetails(self):
        if self.window.winfo_width() == 500:
            self.window.geometry("800x300")
            welString = self.name +"- Customer details .."
            self.window.title(welString)
        else:
            self.window.geometry("500x300")
            welString = self.name +" this is your transaction options .."
            self.window.title(welString)
        
        self.txtCustFname.config(text=self.cust_obj.fname)
        self.txtCustLname.config(text=self.cust_obj.lname)
        
        self.txtCustAdd0.config(text=self.cust_obj.address[0])
        self.txtCustAdd1.config(text=self.cust_obj.address[1])
        self.txtCustAdd2.config(text=self.cust_obj.address[2])
        self.txtCustAdd3.config(text=self.cust_obj.address[3])
    
    def goBack(self):
        self.window.destroy()
        
    def getFormAddress(self):
        if self.window.winfo_width() == 800:
            welString = self.name +"- Customer details .."
            self.window.title(welString)
        else:
            welString = self.name +" this is your transaction options .."
            self.window.title(welString)

    def mouseHover(self):
        self.btnDeposit.bind("<Enter>", lambda event, h=self.btnDeposit: h.configure(bg="#77aaff"))
        self.btnDeposit.bind("<Leave>", lambda event, h=self.btnDeposit: h.configure(bg="SystemButtonFace"))
        self.btnWithdraw.bind("<Enter>", lambda event, h=self.btnWithdraw: h.configure(bg="#77aaff"))
        self.btnWithdraw.bind("<Leave>", lambda event, h=self.btnWithdraw: h.configure(bg="SystemButtonFace"))  
        self.btnCheckbalance.bind("<Enter>", lambda event, h=self.btnCheckbalance: h.configure(bg="#77aaff"))
        self.btnCheckbalance.bind("<Leave>", lambda event, h=self.btnCheckbalance: h.configure(bg="SystemButtonFace"))       
        self.btnUpdCustomerNmae.bind("<Enter>", lambda event, h=self.btnUpdCustomerNmae: h.configure(bg="#77aaff"))
        self.btnUpdCustomerNmae.bind("<Leave>", lambda event, h=self.btnUpdCustomerNmae: h.configure(bg="SystemButtonFace"))      
        self.btnUpdCustomerAddr.bind("<Enter>", lambda event, h=self.btnUpdCustomerAddr: h.configure(bg="#77aaff"))
        self.btnUpdCustomerAddr.bind("<Leave>", lambda event, h=self.btnUpdCustomerAddr: h.configure(bg="SystemButtonFace"))       
        self.btnShowCustomerDtls.bind("<Enter>", lambda event, h=self.btnShowCustomerDtls: h.configure(bg="#77aaff"))
        self.btnShowCustomerDtls.bind("<Leave>", lambda event, h=self.btnShowCustomerDtls: h.configure(bg="SystemButtonFace"))
        self.btnGoback.bind("<Enter>", lambda event, h=self.btnGoback: h.configure(bg="#77aaff"))
        self.btnGoback.bind("<Leave>", lambda event, h=self.btnGoback: h.configure(bg="SystemButtonFace"))       
        