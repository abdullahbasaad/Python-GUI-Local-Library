import tkinter as tk

class managmentReport:
    def __init__(self, name, bnksys_obj):
        self.name = name
        self.bnksys_obj = bnksys_obj
        self.window = tk.Tk()
        self.window.wm_iconbitmap('BCU.ico')
        self.window.geometry("1000x500")
        self.window.resizable(width=False, height=False)
        welString = "Managment report"
        self.window.title(welString)   
        
        txt_frm = tk.Frame(self.window , width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        txt_frm.grid_propagate(False)
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

        self.txtManagReport = tk.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txtManagReport.config(font=("consolas", 12), undo=True, wrap='word')
        self.txtManagReport.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        scrollb = tk.Scrollbar(txt_frm, command=self.txtManagReport.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txtManagReport['yscrollcommand'] = scrollb.set

        self.get_manag_report()
        self.txtManagReport.config(state = 'disabled') 
        
        tk.mainloop()   
  
    def get_manag_report(self):
        lineStr = "======================================================================================================\n"
        bankHeader = "BCU- Birmingham City University Bank\n"
        self.txtManagReport.tag_add(bankHeader,1.0,5.0)
        self.txtManagReport.tag_config(bankHeader, font=('times', 16, 'underline','bold')) 
        self.txtManagReport.insert(tk.END, bankHeader)
        self.txtManagReport.insert(tk.END, lineStr)
        tableHeader = "Customer name\t Account number\t Acount balance\t Interest rate\t\tOverdraft amount\tInterest rate payable\n\n"
        self.txtManagReport.insert(tk.END, tableHeader)

        sum_money = 0
        totalOverdraft = 0
        totalInterestPayable = 0
        interest_rate_payable = 0
        
        i = 0
        for c in self.bnksys_obj.accounts_list:
            strBalance = self.bnksys_obj.formatString(str(c.balance))
            if c.account_type == "2":
                custObj = self.bnksys_obj.search_customers_by_name(c.lname)             
                interest_rate_payable = (float(c.balance) * float(custObj.get_interest_rate()))/100
                interest_rate_payable = self.bnksys_obj.formatString(str(interest_rate_payable))
                custstr = c.fname+" "+c.lname+"\t\t"+c.account_no+"\t\t"+"£"+strBalance+"\t\t"+self.bnksys_obj.formatString(str(custObj.get_interest_rate()))+"%"+"\t\t"+"£"+self.bnksys_obj.formatString(str(custObj.get_overdraft_amount()))+"\t\t"+self.bnksys_obj.formatString(str(interest_rate_payable))+"\n"        
                totalOverdraft = totalOverdraft + float(custObj.get_overdraft_amount())
                totalInterestPayable = float(totalInterestPayable) + float(interest_rate_payable)            
            else:
                custstr = c.fname+" "+c.lname+"\t\t"+c.account_no+"\t\t"+"£"+strBalance+"\t\t"+"£0.00"+"\t\t"+"£0.00"+"\t\t"+"£0.00"+"\n"
                
            self.txtManagReport.insert(tk.END, custstr)
            i+=1
            
            sum_money = sum_money + float(c.get_balance())
    
        totalCustomerstr = "\n\n\nThe Bank has "+str(i)+" customers. "
        self.txtManagReport.insert(tk.END, totalCustomerstr)

        totalAmountBalance = "\n\nThe total amount balance is £"+ str(sum_money)
        self.txtManagReport.insert(tk.END, self.bnksys_obj.formatString(totalAmountBalance))
        
        totalRatePay = "\n\nThe total interest rate payable to all customers for one year is £"+ str(totalInterestPayable)
        self.txtManagReport.insert(tk.END, self.bnksys_obj.formatString(totalRatePay))

        totalAmountDraftstr = "\n\nTotal amount of overdrafts currently taken by all customers is £"+ str(totalOverdraft)     
        self.txtManagReport.insert(tk.END, self.bnksys_obj.formatString(totalAmountDraftstr))
        
    
