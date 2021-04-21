
class Admin:
    
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def set_address(self, addr):
        self.address[0],self.address[1],self.address[2],self.address[3] = str(addr).split(',')
    
    def set_username(self, uname):
        self.user_name = uname
        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address      
    
    def update_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def print_details(self):        
        print("\nFirst name: %s" %self.fname)         
        print("Last name:  %s" %self.lname)                 
        print("Address:    %s" %self.address[0])         
        print("            %s" %self.address[1])         
        print("            %s" %self.address[2])         
        print("            %s" %self.address[3]) 
        print("Privilege   %s" %self.full_admin_rights) 
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self.full_admin_rights

