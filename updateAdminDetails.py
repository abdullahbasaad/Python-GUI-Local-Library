from tkinter import messagebox
import tkinter as tk

class updAdmnDtls():
    def __init__(self, name="",adm_obj="",bank_obj = "",opr = ""):
        self.name = name
        self.admin_obj = adm_obj
        self.bank_obj = bank_obj
        self.opr = opr
        
        self.window = tk.Tk()
        self.window.after(1, lambda: self.window.focus_force())
        self.window.geometry("400x350")
        self.window.resizable(width=False, height=False)
        self.window.wm_iconbitmap('BCU.ico')
        welString = "Welcom "+ self.name +"- Update the names"
        self.window.title(welString)
        
        self.lblAdminFname   = tk.Label(self.window, text="Admin first name:",font=("Helvetica", 9))
        self.lblAdminLname   = tk.Label(self.window, text="Admin last name:",font=("Helvetica", 9))
        self.lblAdminAddress = tk.Label(self.window, text="Address",font='Helvetica 11 bold',fg="#3D1D7D")
        self.lblAdminAdd0    = tk.Label(self.window, text="Door number:",font=("Helvetica", 9))
        self.lblAdminAdd1    = tk.Label(self.window, text="Road:",font=("Helvetica", 9))
        self.lblAdminAdd2    = tk.Label(self.window, text="City:",font=("Helvetica", 9))   
        self.lblAdminAdd3    = tk.Label(self.window, text="Postcode:",font=("Helvetica", 9))  
        self.btnCommit       = tk.Button(self.window,text = "Submit", width = 30, height = 2, command = self.btnupdateAdmin)    
        
        self.txtAdminFname   = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtAdminLname   = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtAdminAdd0    = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtAdminAdd1    = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtAdminAdd2    = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
        self.txtAdminAdd3    = tk.Entry(self.window, width = 30,font=("Helvetica", 9))
                  
        self.lblAdminFname.place(x = 20,y= 30)
        self.lblAdminLname.place(x = 20,y= 60)
        self.lblAdminAddress.place(x = 20,y= 90)
        self.lblAdminAdd0.place(x = 20,y= 120)
        self.lblAdminAdd1.place(x = 20,y= 150)
        self.lblAdminAdd2.place(x = 20,y= 180)
        self.lblAdminAdd3.place(x = 20,y= 210)            
        self.txtAdminFname.place(x = 150,y= 30)
        self.txtAdminLname.place(x = 150,y= 60)
        self.txtAdminAdd0.place(x = 150,y= 120)
        self.txtAdminAdd1.place(x = 150,y= 150)
        self.txtAdminAdd2.place(x = 150,y= 180)
        self.txtAdminAdd3.place(x = 150,y= 210) 
        self.btnCommit.place(x = 100,y= 265) 
        
        self.txtAdminFname.delete(0, tk.END)
        self.txtAdminFname.insert(0, self.admin_obj.fname)
        self.txtAdminLname.delete(0, tk.END) 
        self.txtAdminLname.insert(0, self.admin_obj.lname)
        self.txtAdminAdd0.delete(0, tk.END)
        self.txtAdminAdd0.insert(0, self.admin_obj.address[0])
        self.txtAdminAdd1.delete(0, tk.END) 
        self.txtAdminAdd1.insert(0, self.admin_obj.address[1])       
        self.txtAdminAdd2.delete(0, tk.END) 
        self.txtAdminAdd2.insert(0, self.admin_obj.address[2])
        self.txtAdminAdd3.delete(0, tk.END) 
        self.txtAdminAdd3.insert(0, self.admin_obj.address[3])
        self.enableDisableFields()
        tk.mainloop()  
        
        
    def btnupdateAdmin(self):
        result = messagebox.askyesno("Confirm", "Are you sure?")    
        
        if result == True:                        
            if self.opr == 1:
                if (self.txtAdminFname.get() != self.admin_obj.get_first_name()) or (self.txtAdminLname.get() != self.admin_obj.get_last_name()):
                    self.admin_obj.update_first_name(self.txtAdminFname.get())
                    self.admin_obj.update_last_name(self.txtAdminLname.get())
                    self.bank_obj.exportAdminInfo()
                    messagebox.showinfo("Success!","The operation completed successfully ..")
                    self.window.destroy()
                else:                  
                    messagebox.showinfo("!!","No changes !!..")                  
            else:
                if (self.txtAdminAdd0.get() != self.admin_obj.address[0]) or(self.txtAdminAdd1.get() != self.admin_obj.address[1]) or (self.txtAdminAdd2.get() != self.admin_obj.address[2]) or (self.txtAdminAdd3.get() != self.admin_obj.address[3]):
                    addr = self.txtAdminAdd0.get()+','+self.txtAdminAdd1.get()+','+self.txtAdminAdd2.get()+','+self.txtAdminAdd3.get()
                    self.admin_obj.set_address(addr)
                    self.bank_obj.exportAdminInfo()
                    messagebox.showinfo("Success!","The operation completed successfully ..")
                    self.window.destroy()
                else:
                    messagebox.showinfo("!!","No changes !!..")
                    
    def enableDisableFields(self):
        if self.opr == 1:
            self.txtAdminFname.config(state='normal')
            self.txtAdminLname.config(state='normal')
            self.txtAdminAdd0.config(state='disabled')
            self.txtAdminAdd1.config(state='disabled')
            self.txtAdminAdd2.config(state='disabled')
            self.txtAdminAdd3.config(state='disabled')
        else:
            welString = "Welcom "+ self.name +"- Update the address"
            self.window.title(welString)
            self.txtAdminFname.config(state='disabled')
            self.txtAdminLname.config(state='disabled')
            self.txtAdminAdd0.config(state='normal')
            self.txtAdminAdd1.config(state='normal')
            self.txtAdminAdd2.config(state='normal')
            self.txtAdminAdd3.config(state='normal')

            
            
       

        
        

        
        
            
            
        
        

        
        
        


