from bank_system import BankSystem
from tkinter import messagebox
from adminMenuForm import adminMenu
import tkinter as tk
import os

class Login():
    def __init__(self): 
        self.bnksys_obj = BankSystem()
        self.window = tk.Tk()
        self.window.wm_iconbitmap('BCU.ico')
        self.window.geometry("400x300")
        self.window.title("Welcom to BCU Bank System")
        self.window.after(1, lambda: self.window.focus_force())
        self.window.resizable(width=False, height=False)
        
        fname = "index.png"
        bg_image = tk.PhotoImage(file=fname)
        tk.Canvas()
        cv = tk.Canvas(width=400,heigh=400)
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image(12, 30, image=bg_image, anchor='nw')
    
        self.lblUserName  = tk.Label(self.window, text="User name:",font=("Helvetica", 10))
        self.txtUserName  = tk.Entry(self.window, width = 14,font=("Helvetica", 12))
        self.lblPassword  = tk.Label(self.window, text="Password:",font=("Helvetica", 10))
        self.txtPassword  = tk.Entry(self.window, width = 14,font=("Helvetica", 12),show='*')
        self.btnLogin     = tk.Button(self.window, text = "Login",width = 15, height = 3, command = self.callAdminMenu,font=("Calibri Light (Headings)", 10))
        self.lblCopyRight = tk.Label(self.window, text="Copyright © Basaad, Birmingham City University 2018 ",font=("Bodoni MT Condensed", 10))
        
        self.lblUserName.place(x = 250,y= 50)   
        self.txtUserName.place(x = 250,y=70)
        self.lblPassword.place(x = 250,y= 100)          
        self.txtPassword.place(x = 250,y= 120)
        self.btnLogin.place(x = (self.window.winfo_width()/2) + 50, y=195)
        self.lblCopyRight.place(x = 8,y= 275)  

        self.btnLogin.bind("<Enter>", lambda event, h=self.btnLogin: h.configure(bg="#00104E", fg="white" ))
        self.btnLogin.bind("<Leave>", lambda event, h=self.btnLogin: h.configure(bg="SystemButtonFace", fg="Black"))

        entries = [child for child in self.window.winfo_children() if isinstance(child, tk.Entry) or isinstance(child, tk.Button)]       
        for idx, entry in enumerate(entries):
            entry.bind('<Return>', lambda e, idx=idx: self.bnksys_obj.go_to_next_entry(e, entries, idx))
        
        self.bnksys_obj.uploadAdminsInfo()
        self.uploadCustomerData()
        
        tk.mainloop()
        
    def callAdminMenu(self):
        if self.txtUserName.get() != "" and self.txtPassword != "":         
            msg, admin_obj, pass_flag = self.bnksys_obj.admin_login(self.txtUserName.get(), self.txtPassword.get())
            
            if admin_obj != None:
                if pass_flag == True:             
                    usrName = self.txtUserName.get()
                
                    if os.path.isfile('tempTrans') == 1:
                        result = messagebox.askokcancel("Save updates","There are some updates unsaved, Do you wish to save it?")
                        if result == 1:
                            self.bnksys_obj.overrideFileData()
                            if os.path.isfile('tempTrans') == 1:
                                os.remove('tempTrans')
                        
                    self.window.destroy();        
                    adminForm = adminMenu(usrName, self.bnksys_obj, admin_obj)
                else:
                    messagebox.showerror("Login failed","Invalid user name or password !!..")
     
    def uploadCustomerData(self):
        self.window.fileName = 'Customer_accounts.txt';
    
        if (self.window.fileName):
            countImported,countUnimported = self.bnksys_obj.import_customer_information(self.window.fileName)
            
gui = Login()
        
        
        


