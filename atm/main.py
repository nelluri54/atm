#create atm system
#displaying the remaining amount in the atm
#rupay,mastercard,visa
#authentication of user
#auth then give him the following options to choose
#ccheck balence
#class withdrawl(show balence)
#cash deposit(show balance)
#ministatement of last three transactions\
#card renewal

from balance import Balance
from auth import authent

class cards():
    def __init__(self, initial_balance):
        self.balance = Balance(initial_balance)
        self.auth = authent()
        self.transactions = []

    def display(self):
        print("the amount present in atm:",self.balance.bals())

    def check_balance(self):
        return self.balance.bals()

    def withdraw(self,amount):
        res=self.balance.withdraw(amount)
        if res:
            self.transactions.append(("Withdrawal", amount))
        return res

    def deposit(self, amount):
        res1=self.balance.cash_deposit(amount)
        if res1:
            self.transactions.append(("credited",amount))
        return res1
    
    def mini_statement(self):
        print("Mini Statement:")
        for transaction in self.transactions[-3:]:
            print(f"{transaction[0]}: {transaction[1]}")
        
    def renew_card(self):
        pass
    
    def display1(self):
        print("1.rupay 2.mastercard 3.visa")
        while True:
            self.ch=input("enter your choice:")
            if(self.ch=="1" or self.ch=="rupay"):
                while True:
                    self.ch1=int(input("enter amount:"))
                    if(self.ch1<2000):
                        return
                    else:
                        print("amount limit is crossed")
            elif(self.ch=="2" or self.ch=="mastercard"):
                while True:
                    self.ch2=int(input("enter amount:"))
                    if(self.ch2<5000):
                        return
                    else:
                        print("amount limit is crossed")
            elif(self.ch=="3" or self.ch=="visa"):
                while True:
                    self.ch3=int(input("enter amount:"))
                    if(self.ch3<8000):
                        return
                    else:

                        print("amount limit is exceeded")
            else:
                print("invalid option")

class auth(cards):
    def __init__(self, cards_instance):
        self.cards = cards_instance
    def display3(self):
        while True:
            self.authenticator=authent()
            self.username=input("enter username:")
            self.password=input("enter password:")
            if self.authenticator.autho(self.username, self.password):
                while True:
                    print("\nOptions:")
                    print("1.checkbalance")
                    print("2. Withdraw")
                    print("3. CashDeposit")
                    print("4. MiniStatement")
                    print("5. RenewCard")
                    self.ch=input("")
                    if self.ch == "1" or self.ch=="checkbalance":
                        print("Your balance is:", self.cards.check_balance())
                    elif self.ch == "2" or self.ch=="withdraw":
                        self.amount = int(input("Enter amount to withdraw: "))
                        if self.amount<self.cards.check_balance():
                            if self.cards.withdraw(self.amount):
                                print("Withdrawal successful.")
                                print(self.cards.check_balance())
                        else:
                            print("Insufficient balance.")
                    elif self.ch=="3" or self.ch=="cash deposit":
                        self.amount1=int(input("enter amount to deposit:"))
                        if self.cards.deposit(self.amount1):
                            print("deposited successfully")
                            print(self.cards.check_balance())
                        else:
                            print("invalid amount")
                    elif (self.ch=="4" or self.ch=="MiniStatement"):
                        print(self.cards.mini_statement())
                    elif(self.ch=="5" or self.ch=="RenewCard"):
                        print(self.cards.renew_card())
                    else:
                        print("invalid choice. please enter a valid option")

            else:
                print("please enter valid credentials")
                    

ob1=cards(100000)
ob2=auth(ob1)
ob1.display()
ob1.display1()
ob2.display3()






