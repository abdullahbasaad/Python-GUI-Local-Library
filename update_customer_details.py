from tkinter import messagebox
import tkinter as tk

class updCustDtls:
    def __init__(self, name="",cust_obj="",bnksys_obj = "",opr = ""):
        self.name = name
        self.cust_obj = cust_obj
        self.bnksys_obj = bnksys_obj
        self.opr = opr
        
        self.window = tk.Tk()
        self.window.after(1, lambda: self.window.focus_force())
        self.window.wm_iconbitmap('BCU.ico')
        
        self.window.geometry("400x350")
        self.window.resizable(width=False, height=False)
        welString = "Welcom "+ self.name +"- Update the details"
        self.window.title(welString)
        
        self.lblCustFname   = tk.Label(self.window, text="Admin first name:",font=("Helvetica", 9))
        self.lblCustLname   = tk.Label(self.window, text="Admin last name:",font=("Helvetica", 9))
        self.lblCustAddress = tk.Label(self.window, text="Address",font='Helvetica 11 bold',fg="#3D1D7D")
        self.lblCustAdd0    = tk.Label(self.window, text="Door number:",font=("Helvetica", 9))
        self.lblCustAdd1    = tk.Label(self.window, text="Road:",font=("Helvetica", 9))
        self.lblCustAdd2    = tk.Label(self.window, text="City:",font=("Helvetica", 9))   
        self.lblCustAdd3    = tk.Label(self.window, text="Postcode:",font=("Helvetica", 9))  
        self.btnCommit      = tk.Button(self.window,text = "Submitt", width = 30, height = 2, command = self.btnupdateCust)  
        
        self.txtCustFname   = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtCustLname   = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtCustAdd0    = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtCustAdd1    = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtCustAdd2    = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtCustAdd3    = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
                  
        self.lblCustFname.place(x = 20,y= 30)
        self.lblCustLname.place(x = 20,y= 60)
        self.lblCustAddress.place(x = 20,y= 90)
        self.lblCustAdd0.place(x = 20,y= 120)
        self.lblCustAdd1.place(x = 20,y= 150)
        self.lblCustAdd2.place(x = 20,y= 180)
        self.lblCustAdd3.place(x = 20,y= 210)            
        self.txtCustFname.place(x = 150,y= 30)
        self.txtCustLname.place(x = 150,y= 60)
        self.txtCustAdd0.place(x = 150,y= 120)
        self.txtCustAdd1.place(x = 150,y= 150)
        self.txtCustAdd2.place(x = 150,y= 180)
        self.txtCustAdd3.place(x = 150,y= 210) 
        self.btnCommit.place(x = 100,y= 265) 
        
        self.txtCustFname.delete(0, tk.END)
        self.txtCustFname.insert(0, self.cust_obj.fname)
        self.txtCustLname.delete(0, tk.END) 
        self.txtCustLname.insert(0, self.cust_obj.lname)
        self.txtCustAdd0.delete(0, tk.END)
        self.txtCustAdd0.insert(0, self.cust_obj.address[0])
        self.txtCustAdd1.delete(0, tk.END) 
        self.txtCustAdd1.insert(0, self.cust_obj.address[1])       
        self.txtCustAdd2.delete(0, tk.END) 
        self.txtCustAdd2.insert(0, self.cust_obj.address[2])
        self.txtCustAdd3.delete(0, tk.END) 
        self.txtCustAdd3.insert(0, self.cust_obj.address[3])
        
        self.enableDisableFields()
        tk.mainloop()      
        
    def btnupdateCust(self):
        result = messagebox.askyesno("Confirm", "Are you sure?")    
        
        if result == True:
            
            if self.opr == 1:
                if (self.txtCustFname.get() != self.cust_obj.get_first_name()) or (self.txtCustLname.get() != self.cust_obj.get_last_name()):
                    self.cust_obj.update_first_name(self.txtCustFname.get())
                    self.cust_obj.update_last_name(self.txtCustLname.get())
                    
                    messagebox.showinfo("Success!","The operation completed successfully ..")
                    self.bnksys_obj.tempTransactions(self.cust_obj.get_account_no(), self.cust_obj.get_account_type(), self.cust_obj)
                    self.window.destroy()
                else:                  
                    messagebox.showinfo("!!","No changes !!..")                  
            else:
                if (self.txtCustAdd0.get() != self.cust_obj.address[0]) or(self.txtCustAdd1.get() != self.cust_obj.address[1]) or (self.txtCustAdd2.get() != self.cust_obj.address[2]) or (self.txtCustAdd3.get() != self.cust_obj.address[3]):
                    addr = self.txtCustAdd0.get()+','+self.txtCustAdd1.get()+','+self.txtCustAdd2.get()+','+self.txtCustAdd3.get()
                    self.cust_obj.update_address(addr)
                    messagebox.showinfo("Success!","The operation completed successfully ..")
                    self.bnksys_obj.tempTransactions(self.cust_obj.get_account_no(), self.cust_obj.get_account_type(), self.cust_obj)
                    self.window.destroy()
                else:
                    messagebox.showinfo("!!","No changes !!..")
                    
    def enableDisableFields(self):
        if self.opr == 1:      
            self.txtCustFname.config(state='normal')
            self.txtCustLname.config(state='normal')
            self.txtCustAdd0.config(state='disabled')
            self.txtCustAdd1.config(state='disabled')
            self.txtCustAdd2.config(state='disabled')
            self.txtCustAdd3.config(state='disabled')
        else:
            self.txtCustFname.config(state='disabled')
            self.txtCustLname.config(state='disabled')
            self.txtCustAdd0.config(state='normal')
            self.txtCustAdd1.config(state='normal')
            self.txtCustAdd2.config(state='normal')
            self.txtCustAdd3.config(state='normal')
            
            
       

        
        

        
        
            
            
        
        

        
        
        


