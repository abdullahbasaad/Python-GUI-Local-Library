from bank_system import BankSystem
from tkinter import messagebox
import tkinter as tk


class transferMoney():
    def __init__(self, name="",bnksys_obj=""):
        self.name = name
        self.bnk_obj = bnksys_obj
        
        self.window = tk.Tk()
        self.window.wm_iconbitmap('BCU.ico')
        self.window.geometry("420x220")
        self.window.resizable(width=False, height=False)
        welString = "Welcom "+ self.name +"- Transfer money"
        self.window.title(welString)
        self.window.after(1, lambda: self.window.focus_force())
        
        self.lblSenderFname   = tk.Label(self.window, text="Please input sender surname: ",font=("Helvetica", 9))
        self.lblAmount        = tk.Label(self.window, text="Please input the amount to be transferred: ",font=("Helvetica", 9))
        self.lblReceiverName  = tk.Label(self.window, text="Please input receiver surname: ",font=("Helvetica", 9))
        self.lblReceiverAccNo = tk.Label(self.window, text="Please input receiver account number: ",font=("Helvetica", 9))
        
        self.txtSenderFname   = tk.Entry(self.window, width = 15,font=("Helvetica", 9))
        self.txtAmount        = tk.Entry(self.window, width = 15,font=("Helvetica", 9))
        self.txtReceiverName  = tk.Entry(self.window, width = 15,font=("Helvetica", 9))
        self.txtReceiverAccNo = tk.Entry(self.window, width = 15,font=("Helvetica", 9))
        
        self.btnTransfer      = tk.Button(self.window, text = "Transfer money...", width = 30, command = self.transferMoney)
        
        self.lblSenderFname.place(x = 30,y= 10)
        self.lblAmount.place(x = 30,y= 40)
        self.lblReceiverName.place(x = 30,y=70)
        self.lblReceiverAccNo.place(x = 30,y= 100)       
        self.txtSenderFname.place(x = 280,y= 10)
        self.txtAmount.place(x = 280,y= 40)
        self.txtReceiverName.place(x = 280,y= 70)
        self.txtReceiverAccNo.place(x = 280,y= 100)        
        self.btnTransfer.place(x = 100,y= 150)   
           
    def transferMoney(self):    
        sndrName = self.txtSenderFname.get()
        amnt     = self.txtAmount.get()
        rcvName  = self.txtReceiverName.get()
        rcvAccnt = self.txtReceiverAccNo.get()
                     
        amnt = self.bnk_obj.validateAmount(amnt)
        if amnt != None:
            rcvAccnt = self.bnk_obj.validateAccntNo(rcvAccnt)
            if rcvAccnt != None:
                senderFound = self.bnk_obj.search_customers_by_name(sndrName)
                rcvFound    = self.bnk_obj.search_customers_by_name(rcvName)
                
                if senderFound != None and rcvFound != None:
                    if int(senderFound.get_account_no()) == int(rcvAccnt):
                        messagebox.showerror("Error!!","Transfer money to same account not allwed !!..")
                    else:
                        if int(rcvFound.get_account_no()) != int(rcvAccnt):
                            messagebox.showerror("Error!!","Please check receiver account No !!..")
                        else:
                            self.doTransfer(sndrName, rcvName, rcvAccnt, float(amnt),senderFound,rcvFound)
            else:
                self.window.after(1, lambda: self.window.focus_force())
        else:
            self.window.after(1, lambda: self.window.focus_force())
            
    def doTransfer(self, sndrName, rcvName, rcvAccnt, amnt,snd_obj,rcv_obj):      
        if snd_obj.get_balance() < amnt:
            if snd_obj.account_type == "1": # saving account
                messagebox.showerror("Error!!","Insufficient funds !!...")
            elif snd_obj.account_type == "2": # Inerest account
                if (snd_obj.withdrawOver(float(amnt))):
                    messagebox.showinfo("Success!!","The operation completed successfully ..")
                    rcv_obj.set_balance(rcv_obj.get_balance() + amnt)
                    self.bnk_obj.tempTransactions(rcv_obj.get_account_no(), rcv_obj.get_account_type(), rcv_obj)
                    self.window.destroy()
                else:
                    messagebox.showerror("!!","Insufficient funds!!.. ")
        else:
            snd_obj.set_balance(snd_obj.get_balance() - amnt)
            rcv_obj.set_balance(rcv_obj.get_balance() + amnt)
            messagebox.showinfo("Success!!","The operation completed successfully ..")
            self.bnk_obj.tempTransactions(snd_obj.get_account_no(), snd_obj.get_account_type(), snd_obj)
            self.bnk_obj.tempTransactions(rcv_obj.get_account_no(), rcv_obj.get_account_type(), rcv_obj)
            self.window.destroy()
                    

        

        
        
        


