from tkinter import messagebox
import tkinter as tk

class depositWithdraw:
    def __init__(self, name="",cust_obj="", bnksys_obj="", opr=""):
        self.name = name
        self.bnksys_obj = bnksys_obj
        self.cust_obj = cust_obj
        self.opr = opr
        
        self.window = tk.Tk()
        self.window.geometry("350x120")
        self.window.resizable(width=False, height=False)
        welString = "Welcom "+ self.name +" - Deposit"
        self.window.wm_iconbitmap('BCU.ico')
        self.window.title(welString)
        self.window.after(1, lambda: self.window.focus_force())
        
        self.lblHolder = tk.Label(self.window, text="Please enter amount to be deposited : ",font=("Helvetica", 9))
        self.txtHolder = tk.Entry(self.window, width = 10,font=("Helvetica", 9))
        self.btnCommit = tk.Button(self.window,text = "Deposit", width = 12, height = 1, command = self.commit)     
            
        self.lblHolder.place(x = 10,y= 15)
        self.txtHolder.place(x = 230,y= 15)
        self.btnCommit.place(x = 140,y= 60) 
        
        if self.opr == 2:
            self.lblHolder.config(text="Please enter amount to be withdrawed: ")
            self.btnCommit.config(text="Withdraw",command = self.commit, width = 12)
            self.txtHolder.place(x = 230,y= 15)
            self.txtHolder.config(width = 12)
            welString = "Welcom "+ self.name +" - Withdraw"
            self.window.title(welString)
        
        self.txtHolder.delete(0, tk.END)
        self.txtHolder.insert(0, "")
        
        tk.mainloop()      
        
    def commit(self):
        if self.opr == 1:
            chkResult = self.bnksys_obj.validateAmount(self.txtHolder.get())
            if chkResult != "None":
                self.cust_obj.deposit(float(self.txtHolder.get()))
                self.bnksys_obj.tempTransactions(self.cust_obj.get_account_no(), self.cust_obj.get_account_type(), self.cust_obj)
                messagebox.showinfo("Success!!","The operation completed successfully ..")
                self.window.destroy()
                
        elif self.opr == 2:
            chkResult = self.bnksys_obj.validateAmount(self.txtHolder.get())
            if chkResult != "None":
                if self.cust_obj.account_type == "1":
                    if (self.cust_obj.withdraw(float(self.txtHolder.get()))):
                        self.bnksys_obj.tempTransactions(self.cust_obj.get_account_no(), self.cust_obj.get_account_type(), self.cust_obj)
                        messagebox.showinfo("Success!!","The operation completed successfully ..")
                        self.window.destroy()
                    else:
                        messagebox.showerror("Error !!..","Insufficient funds!!.. ")
                elif self.cust_obj.account_type == "2":
                    if (self.cust_obj.withdrawOver(float(self.txtHolder.get()))):
                        self.bnksys_obj.tempTransactions(self.cust_obj.get_account_no(), self.cust_obj.get_account_type(), self.cust_obj)
                        messagebox.showinfo("Confirmed !!","The operation completed successfully ..")
                        self.window.destroy()
                    else:
                        messagebox.showerror("Error !!..","Insufficient funds!!.. ")
            
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
                messagebox.showinfo("Notice..","The account number is does not exist!!..") 
            else:
                messagebox.showinfo("Confirm","The account has been deleted!!..")
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
            



