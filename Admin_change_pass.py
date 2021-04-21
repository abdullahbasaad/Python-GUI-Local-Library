import tkinter as tk
from tkinter import messagebox

class AdminChangePass:
    def __init__(self, name="",bnk_obj = "", adm_obj=""):
        self.name = name
        self.adm_obj = adm_obj 
        self.bnk_obj = bnk_obj
        
        self.window = tk.Tk()
        self.window.geometry("365x150")
        self.window.resizable(width=False, height=False)
        welString = "Welcom "+ self.name +"- Change password"
        self.window.wm_iconbitmap('BCU.ico')
        self.window.title(welString)
        self.window.after(1, lambda: self.window.focus_force())
        
        self.lblOldPass = tk.Label(self.window,  text="Please enter the old password : ",font=("Helvetica", 9))
        self.txtOldPass = tk.Entry(self.window,  width = 19,font=("Helvetica", 9),show = "*")      
        self.lblNewPass1 = tk.Label(self.window, text="Please enter the new password : ",font=("Helvetica", 9))
        self.txtNewPass1 = tk.Entry(self.window, width = 19,font=("Helvetica", 9),show = "*")  
        self.lblNewPass2 = tk.Label(self.window, text="Re-type the new password : ",font=("Helvetica", 9))
        self.txtNewPass2 = tk.Entry(self.window, width = 19,font=("Helvetica", 9),show = "*")
        
        self.btnCommit = tk.Button(self.window,text = "Submit..", width = 12, height = 1, command = self.commit)     
            
        self.lblOldPass.place(x = 10,y= 15)
        self.txtOldPass.place(x = 200,y= 15)
        self.lblNewPass1.place(x = 10,y= 35)
        self.txtNewPass1.place(x = 200,y= 35)
        self.lblNewPass2.place(x = 10,y= 55)
        self.txtNewPass2.place(x = 200,y= 55)

        self.btnCommit.place(x = 140,y= 100) 
        
        tk.mainloop()      
        
    def commit(self):     
        oldPass = self.adm_obj.get_password()
        if oldPass != self.txtOldPass.get():
            messagebox.showerror("Error","Invalid old password !!")
        else:
            if self.txtNewPass1.get()== "" or self.txtNewPass2.get()=="":
                messagebox.showerror("Error","invalid new password !!")
            else:
                if self.txtNewPass1.get() != self.txtNewPass2.get():
                    messagebox.showerror("Error","New passwords are not identocal !!")
                else:
                    result = messagebox.askokcancel("Confirmation","Are you sure ..")
                    if result == True:
                        self.adm_obj.update_password(self.txtNewPass1.get())
                        self.bnk_obj.exportAdminInfo()
                        messagebox.showinfo("Confirmation","The password has been changed.")
                    self.window.destroy()
     