from bank_system import BankSystem
from tkinter import messagebox
import tkinter as tk
from tkinter import *


class allCustomerData():
    def __init__(self, name, bnksys_obj):
        self.name = name
        self.bnksys_obj = bnksys_obj
        self.dataStr = ""
        self.window = tk.Tk()
        self.window.geometry("400x350")
        self.window.resizable(width=False, height=False)
        welString = "Welcom "+ self.name +" All customers' details"
        self.window.wm_iconbitmap('BCU.ico')
        self.window.title(welString)
        self.window.after(1, lambda: self.window.focus_force())
        
        txt_frm = tk.Frame(self.window , width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        txt_frm.grid_propagate(False)
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

        self.txtCustomerData = tk.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txtCustomerData.config(font=("consolas", 12), undo=True, wrap='word')
        self.txtCustomerData.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        scrollb = tk.Scrollbar(txt_frm, command=self.txtCustomerData.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txtCustomerData['yscrollcommand'] = scrollb.set

        self.print_all_accounts_details()
        self.txtCustomerData.config(state = 'disabled')
        
        tk.mainloop()   
        
    def print_all_accounts_details(self):
        
        i = 0
        
        for c in self.bnksys_obj.accounts_list:
            i+=1
            self.dataStr = str(i)+"  "+"  Frst name: "+c.fname+"\n"+"     Last name: "+c.lname+"\n"+"     Account No: "+c.account_no+"\n"+"     Address: "+"     "+c.address[0]+"\n"+"     "+c.address[1]+"\n"+"     "+c.address[2]+"\n"+"     "+c.address[3]+"\n\n\n"        
            
            self.txtCustomerData.insert(tk.END,self.dataStr)
            
        custAccount = str(i)+ " Customers..."
        self.txtCustomerData.insert(tk.END, custAccount)

        
   
    
        
        
    
            
            
       

        
        

        
        
            
            
        
        

        
        
        


