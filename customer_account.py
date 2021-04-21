class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance, account_type):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.account_type = account_type
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address[0],self.address[1],self.address[2],self.address[3] = str(addr).split(',')
        
    def get_address(self):
        return self.address
    
    def deposit(self, amount):
        self.balance+=amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance = self.get_balance() - amount
            return True
        
    def get_balance(self):
        return self.balance
    
    def set_balance(self, newAmount):
        self.balance = newAmount
    
    def get_account_no(self):
        return self.account_no
    
    def get_account_type(self):
        return self.account_type
        
class CustomerAccount2(CustomerAccount):
    def __init__(self, fname, lname, address, account_no, balance, account_type,interest_rate, overdraft_limit, overdraft_amount ):
        CustomerAccount.__init__(self, fname, lname, address, account_no, balance, account_type)
        self.interest_rate = interest_rate
        self.overdraft_limit = overdraft_limit
        self.overdraft_amount = overdraft_amount
        
    def get_overdraft_amount(self):
        return self.overdraft_amount
    
    def get_interest_rate(self):
        return self.interest_rate
    
    def get_overdraft_limit(self):
        return self.overdraft_limit
    
    def withdrawOver(self, amount):
        if amount <= float(self.balance):
            self.set_balance(float(self.get_balance()) - amount)
            return True
        else:
            over_remain = float(self.overdraft_limit) - float(self.overdraft_amount)
            
            if (amount > over_remain + float(self.get_balance())) or (float(self.overdraft_amount) == float(self.overdraft_limit)):
                return False
            else:
                amount = abs(float(self.balance) - amount)
                self.set_balance(0)
                self.overdraft_amount = float(self.overdraft_amount) + float(amount)
                return True

            
        