from customer_account import CustomerAccount
from customer_account import CustomerAccount2
from admin import Admin
from tkinter import messagebox
import datetime

accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.currentAdmin = ""

    def search_admins_by_name(self, admin_username):
        
        found_admin = None 
        for a in self.admins_list:     
            username = a.get_username()     
            
            if username == admin_username:         
                found_admin = a         
                break 
        if found_admin == None:
            errmessage = "The Admin "+admin_username+" does not exist! Try again..."
            messagebox.showerror("Error !!",errmessage)     
        return found_admin  
        
    def search_customers_by_name(self, customer_lname):
        found_customer = None     
        for a in self.accounts_list:
            if a.get_last_name() == customer_lname:         
                found_customer = a
                break 
            
        if found_customer == None:  
            errmessage = "The customer "+customer_lname+" does not exist! Try again..."
            messagebox.showerror("Error !!",errmessage)     
 
        return found_customer 
    
    def search_customers_by_account(self, account_no):
        found_customer = None     
        for a in self.accounts_list:
            if a.get_account_no() == account_no:         
                found_customer = a
                break
            
        return found_customer 
            
    def admin_login(self, username, password):
        found_admin = self.search_admins_by_name(username)
        
        msg = "\n Login failed" 
        pass_flag = True
        print()
        
        if found_admin != None:
            if found_admin.get_password() == password:
                msg = "\n Login successful"
            else:
                pass_flag = False
        return msg, found_admin, pass_flag 
    
    def import_customer_information(self, fileName):
        file = open(fileName,"r")   
        i = 0 # All records
        j = 0 # Miised records
        for line in file:
            custObj = "customer_"+str(i)
            i += 1
            try:       
                if line[0] == "1":
                    accType,fname,lname,address,account_no,balance = line.split(',')
                    accType = accType.lstrip()
                    accType = accType.rstrip()
                    fname = fname.lstrip()
                    fname = fname.rstrip()
                    lname = lname.lstrip()
                    lname = lname.rstrip()          
                    address = address.lstrip()
                    address = address.rstrip()               
                    account_no = account_no.lstrip()
                    account_no = account_no.rstrip()        
                    balance = balance.lstrip()
                    balance = balance.rstrip() 
                    add0,add1,add2,add3 = address.split('&')
                    custObj = CustomerAccount(fname,lname,[add0,add1,add2,add3],account_no,balance,accType)
                    self.accounts_list.append(custObj)
                else:
                    accType,fname,lname,address,account_no,balance,interest_rate,overdraft_limit,overdraft_amount = line.split(',')
                    accType = accType.lstrip()
                    accType = accType.rstrip()
                    fname = fname.lstrip()
                    fname = fname.rstrip()
                    lname = lname.lstrip()
                    lname = lname.rstrip()          
                    address = address.lstrip()
                    address = address.rstrip()               
                    account_no = account_no.lstrip()
                    account_no = account_no.rstrip()        
                    balance = balance.lstrip()
                    balance = balance.rstrip() 
                    interest_rate = interest_rate.lstrip()
                    interest_rate = interest_rate.rstrip() 
                    overdraft_limit = overdraft_limit.lstrip()
                    overdraft_limit = overdraft_limit.rstrip() 
                    overdraft_amount = overdraft_amount.lstrip()
                    overdraft_amount = overdraft_amount.rstrip() 
                    add0,add1,add2,add3 = address.split('&')
                    custObj = CustomerAccount2(fname,lname,[add0,add1,add2,add3],account_no,balance,accType,interest_rate,overdraft_limit,overdraft_amount)
                    self.accounts_list.append(custObj)
            except ValueError:
                j += 1
                fileExport = open("exportLogFile","+a")
                fileExport.write(line)
                fileExport.close() 
                
        return i,j
    
    def uploadAdminsInfo(self):
        file = open("Admins","r")   
        i = 0 # All records
        for line in file:
            admObj = "admin_"+str(i)
            i += 1
            try:
                fname, lname, address, user_name, password, full_rights = line.split(',')
                fname = fname.lstrip()
                fname = fname.rstrip()
                lname = lname.lstrip()
                lname = lname.rstrip()          
                address = address.lstrip()
                address = address.rstrip()               
                user_name = user_name.lstrip()
                user_name = user_name.rstrip()        
                password = password.lstrip()
                password = password.rstrip()
                full_rights = full_rights.lstrip()
                full_rights = full_rights.rstrip()
                
                add0,add1,add2,add3 = address.split('&')
                admObj = Admin(fname,lname,[add0,add1,add2,add3],user_name, password, full_rights)
                self.admins_list.append(admObj)
            except ValueError:
                fileExport = open("exportLogFile","+a")
                fileExport.write(line)
                fileExport.close() 
    
    def export_customer_informations(self):
        now = datetime.datetime.now()
        fileDate = now.strftime("%Y-%m-%d-%H-%M")

        fileExported = "Bankcustomers"+fileDate 
        customerData = open(fileExported,'w')
        i = 0       
        if not(self.accounts_list):
            messagebox.showerror("Error","Database is empty !!..")
        else:
            for data in self.accounts_list:
                
                if data.get_account_type() == "1":
                    holder = str(data.get_account_type())+","+data.get_first_name()+","+data.get_last_name()+","+data.address[0]+"&"+data.address[1]+"&"+data.address[2]+"&"+data.address[3]+","+str(data.get_account_no())+","+str(data.get_balance())+"\n"
                else:
                    custObj = self.search_customers_by_name(data.lname)
                    holder = data.get_account_type()+","+data.get_first_name()+","+data.get_last_name()+","+data.address[0]+"&"+data.address[1]+"&"+data.address[2]+"&"+data.address[3]+","+data.get_account_no()+","+str(data.get_balance())+","+str(custObj.interest_rate)+","+str(custObj.overdraft_limit)+","+str(custObj.overdraft_amount)+"\n"
                customerData.write(holder)
                i += 1
            customerData.close()
        return i
        
    def exportAdminInfo(self):
        fileExported = "Admins"
        adminsData = open(fileExported,'w')
        i = 0       
        if not(self.admins_list):
            messagebox.showerror("Error","Database is empty !!..")
        else:
            for data in self.admins_list:
                holder = data.get_first_name()+","+data.get_last_name()+","+data.address[0]+"&"+data.address[1]+"&"+data.address[2]+"&"+data.address[3]+","+str(data.get_username())+","+str(data.get_password())+","+str(data.has_full_admin_right())+"\n"
                adminsData.write(holder)
                i += 1
            adminsData.close()
        return i
    
    def exportAllData(self):
        fileExported = "Customer_accounts.txt"
        customerData = open(fileExported,'w')
        i = 0       
        if not(self.accounts_list):
            messagebox.showerror("Error","Database is empty !!..")
        else:
            for data in self.accounts_list:              
                if data.get_account_type() == "1":
                    holder = str(data.get_account_type())+","+data.get_first_name()+","+data.get_last_name()+","+data.address[0]+"&"+data.address[1]+"&"+data.address[2]+"&"+data.address[3]+","+str(data.get_account_no())+","+str(data.get_balance())+"\n"
                else:
                    custObj = self.search_customers_by_name(data.lname)
                    holder = data.get_account_type()+","+data.get_first_name()+","+data.get_last_name()+","+data.address[0]+"&"+data.address[1]+"&"+data.address[2]+"&"+data.address[3]+","+data.get_account_no()+","+str(data.get_balance())+","+str(custObj.interest_rate)+","+str(custObj.overdraft_limit)+","+str(custObj.overdraft_amount)+"\n"
                customerData.write(holder)
                i += 1
            customerData.close()
        return i
    
    def validateAmount(self, value):
        try:        
            if value:
                value = float(value)
            return value
        except ValueError:
            messagebox.showerror("Error!!","Amount transfer should be number !!..")
            return "None"
            
    def validateAccntNo(self, value):
        try:
            if value:
                value = int(value)
            return value
        except ValueError:
            messagebox.showerror("Error!!","Account number should be integer number !!..")
            return "None"
        
    def formatString(self,no):
        try:
            if len(no) - (no.index('.')+1) == 1:
                no = no+"0"
            elif len(no) - (no.index('.')+1) == 0:
                no = no+"00"
            elif len(no) - (no.index('.')+1) == 2:
                no = no
            else:
                no = round(float(no),2)
                
            return no
        except ValueError:
            return no+".00"
        
    def go_to_next_entry(self, event, entry_list, this_index):
        next_index = (this_index + 1) % len(entry_list)
        entry_list[next_index].focus_set()
        
    def tempTransactions(self,accNo, accType, custObj):
        for data in self.accounts_list:
            if data.get_account_no() == accNo:
                if accType == "1":
                    holder = str(data.get_account_type())+","+data.get_first_name()+","+data.get_last_name()+","+data.address[0]+"&"+data.address[1]+"&"+data.address[2]+"&"+data.address[3]+","+str(data.get_account_no())+","+str(data.get_balance())+"\n"
                else:
                    holder = data.get_account_type()+","+data.get_first_name()+","+data.get_last_name()+","+data.address[0]+"&"+data.address[1]+"&"+data.address[2]+"&"+data.address[3]+","+data.get_account_no()+","+str(data.get_balance())+","+str(custObj.interest_rate)+","+str(custObj.overdraft_limit)+","+str(custObj.overdraft_amount)+"\n"
                
                fileExportTrans = open("tempTrans","+a")
                fileExportTrans.write(holder)
                fileExportTrans.close() 
                
    def overrideFileData(self):
        file = open("tempTrans","r")
        customer_object = ""
        
        for line in file:
            try:       
                if line[0] == "1":
                    accType,fname,lname,address,account_no,balance = line.split(',')
                    accType = accType.lstrip()
                    accType = accType.rstrip()
                    fname = fname.lstrip()
                    fname = fname.rstrip()
                    lname = lname.lstrip()
                    lname = lname.rstrip()          
                    address = address.lstrip()
                    address = address.rstrip()               
                    account_no = account_no.lstrip()
                    account_no = account_no.rstrip()        
                    balance = balance.lstrip()
                    balance = balance.rstrip() 
                    add0,add1,add2,add3 = address.split('&')       
                    
                    for data in self.accounts_list:
                        if data.get_account_no() == str(account_no):
                            cust_obj = self.search_customers_by_account(account_no)
                            customer_object = cust_obj
                            break;

                    if customer_object != None:
                        customer_object.fname = fname
                        customer_object.lname = lname
                        addr = add0+','+add1+','+add2+','+add3
                        customer_object.update_address(addr)
                        customer_object.balance = balance        
                else:
                    accType,fname,lname,address,account_no,balance,interest_rate,overdraft_limit,overdraft_amount = line.split(',')
                    accType = accType.lstrip()
                    accType = accType.rstrip()
                    fname = fname.lstrip()
                    fname = fname.rstrip()
                    lname = lname.lstrip()
                    lname = lname.rstrip()          
                    address = address.lstrip()
                    address = address.rstrip()               
                    account_no = account_no.lstrip()
                    account_no = account_no.rstrip()        
                    balance = balance.lstrip()
                    balance = balance.rstrip() 
                    interest_rate = interest_rate.lstrip()
                    interest_rate = interest_rate.rstrip() 
                    overdraft_limit = overdraft_limit.lstrip()
                    overdraft_limit = overdraft_limit.rstrip() 
                    overdraft_amount = overdraft_amount.lstrip()
                    overdraft_amount = overdraft_amount.rstrip() 
                    add0,add1,add2,add3 = address.split('&')
                    
                    for data in self.accounts_list:
                        if data.get_account_no() == str(account_no):
                            cust_obj = self.search_customers_by_account(account_no)
                            customer_object = cust_obj
                            break;
                            
                    if customer_object != None:
                        customer_object.fname = fname
                        customer_object.lname = lname
                        addr = add0+','+add1+','+add2+','+add3
                        customer_object.update_address(addr)
                        customer_object.balance = balance 
                        customer_object.interest_rate = interest_rate
                        customer_object.overdraft_limit = overdraft_limit
                        customer_object.overdraft_amount = overdraft_amount
            except ValueError:
                messagebox.showerror("Error","Error has happened while updating data!!..")
                
 