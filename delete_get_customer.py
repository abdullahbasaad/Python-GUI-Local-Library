from tkinter import messagebox
from customer_menu_gui import customerMenuGui
import tkinter as tk

class deleteCustomer:
    
    def __init__(self, name="",bnksys_obj="",admin_obj="", opr=""):
        self.name = name
        self.bnksys_obj = bnksys_obj
        self.admin_obj = admin_obj
        self.opr = opr
        
        self.window = tk.Tk()
        self.window.geometry("370x120")
        self.window.resizable(width=False, height=False)
        welString = "Delete customer account"
        self.window.wm_iconbitmap('BCU.ico')
        self.window.title(welString)
        self.window.after(1, lambda: self.window.focus_force())
        
        self.lblHolder = tk.Label(self.window, text="Please enter the account number to be deleted: ",font=("Helvetica", 9))
        self.txtHolder = tk.Entry(self.window, width = 10,font=("Helvetica", 9))
        self.btnCommit = tk.Button(self.window,text = "Submitt", width = 10, height = 1, command = self.checkDeletePriv)     
            
        self.lblHolder.place(x = 10,y= 30)
        self.txtHolder.place(x = 275,y= 30)
        self.btnCommit.place(x = 150,y= 80) 
        
        if self.opr == 1:
            self.lblHolder.config(text="Please enter the customer name: ")
            self.btnCommit.config(text="Customer menu.. ",command = self.getCustomerMenu, width = 15)
            self.txtHolder.place(x = 210,y= 30)
            self.txtHolder.config(width = 15)
            welString = "Get customer menu"
            self.window.title(welString)
        
        self.txtHolder.delete(0, tk.END)
        self.txtHolder.insert(0, "")
        
        tk.mainloop()      
        
    def checkDeletePriv(self):
        if self.opr == 2:
            result = messagebox.askyesno("Confirm", "Are you sure?")    
        
            if result == True:
                self.deleteAccount()
            
    def deleteAccount(self):
        try:
            int(self.txtHolder.get())
            accntFlag = False
            index = 0
            for a in self.bnksys_obj.accounts_list:
                if int(self.txtHolder.get()) == int(a.get_account_no()):
                    self.bnksys_obj.accounts_list.pop(index)
                    accntFlag = True
                    break
            
                index +=1
            if accntFlag == False:
                messagebox.showinfo("Notice..","The account number does not exist!!..") 
            else:
                messagebox.showinfo("Confirmed","The account has been deleted!!..")
                self.bnksys_obj.exportAllData()
        except ValueError:
            messagebox.showinfo("Notice..","The account number should be integer number !!..")
            
        self.window.destroy()
        
    def getCustomerMenu(self):
        customer_account = self.bnksys_obj.search_customers_by_name(self.txtHolder.get())  
                
        if customer_account != None:
            custName = self.txtHolder.get()
            cust_obj = customer_account
            bnk_obj = self.bnksys_obj
            self.window.destroy()
            custGui = customerMenuGui(custName,cust_obj,bnk_obj)
        else:
            self.txtHolder.delete(0, tk.END)
            



