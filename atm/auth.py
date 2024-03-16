class authent:
    def autho(self,username,password):
        self.username=username
        self.password=password
        if self.username==self.password:
            return True
        else:
            return False
    
