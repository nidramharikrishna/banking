# ====================banking===========================

import random
class bank:
    holder_details=[]
    def create_acc(self):
        self.new_acc={}
        self.new_acc["holder_name"]=input("enter your name:")
        self.new_acc["your_aadhar"]=int(input("enter ypur aadhar no:"))
        self.new_acc["mobile:"]=int(input ("enter your number:"))
        self.new_acc["IFSC_code"]="SBI01234"
        self.new_acc["account_number"]=random.randint(0000000000,9999999999)

        n1=input("select the type of your bank saving/zero:")
        while True:
            if n1=="saving":
                n2=int(input("add ammount above 1000/-:"))
                if n2>=1000:
                    self.new_acc["bank_balance"]=n2
                    break
                else:
                    print("add amount above 1000/-:")
            elif n1=="zero":
                n3=int(input("add amount above 500/-"))
                if n3>=500:
                    self.new_acc["bank_balance"]=n3
                    break
                else:
                    print("enter amount above 500/-")
        print("====================YOUR ACCOUNT CREATED SUCCESFULLY=========================")
        bank.holder_details.append(self.new_acc)
        print(bank.holder_details)

    def deposit(self):
        print("===============WELCOME TO DIPOSITE OPTION")
        while True:
            name=input("enter your name:")
            account_number=int(input("enter your account number:"))
            amount=int(input("enter amount :"))

            for x in bank.holder_details:
                if x["holder_name"]==name and x["account_number"]==account_number:
                    x["bank_balance"]+=amount
                    print("===========diposit successfull")
                    print("updated balance=",x["bank_balance"])
                    return
                print("====invalid credentials==== \n TRY AGAIN...!!!!")


    def withdraw(self):
        print("==============WELCOME TO WITHDRAW OPTION====================")
        while True:
            name=input("enter your name")
            account=int(input("enter your account number"))
            amount=int(input("enter amount"))

            for x in bank.holder_details:
                if x["holder_name"]==name and x["account_number"]==account:
                    x["bank_balance"]-=amount
                    print("===WITHDRAW SUCCESFULL===")
                    print(" REMAINING BALANCE=",x["bank_balance"])
                    return
                print("===ENTER VALID CREDENTIALS...===")

    def check_details(self):
        print("=================WELCOME TO CHECK DETAILS OPTION=====================")
        while True:
            name=input("enter your name:")
            account=int(input("enter account number:"))
            for x in bank.holder_details:
                if x["holder_name"]==name and x["account_number"]==account:
                    for x in bank.holder_details:
                        print(x,end="")
                        break
                else:
                    print("--------ENTER VALID CREDENTIALS-------")
    def check_balance(self):
        print("=============WELCOME TO CHECK BALANCE OPTION==============")
        while True:
            name=input("enter your name:")
            account_no=int(input("enter your account number:"))
            for x in bank.holder_details:
                if x["holder_name"]==name and x["account_number"]==account_no:
                    print(x["bank_balance"])
                    break
                else:
                    print("-------enter valid credentials---------")

       
obj=bank()
while True:
    n4=int(input("==========select your choice===========\n "
    "1.for create a new account \n"
    " 2.deposit amount \n"
    " 3.withdraw \n" 
    " 4.check details \n"
    " 5.exit :"))
    if n4==1:
        obj.create_acc()
    elif n4==2:
        obj.deposit()
    elif n4==3:
        obj.withdraw()
    elif n4==4:
        obj.check_details()
    elif n4==5:
        obj.check_balance()
    else:
        break
