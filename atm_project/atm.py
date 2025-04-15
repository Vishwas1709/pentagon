from Bank import Account
from datetime import datetime

a1= Account("Vishwas",123,10000)

# print(a1.name)
# print(a1.balance)

# a1.deposit(500)
# print(a1.balance)

# a1.withdrawal(5000)
# print(a1.balance)



while (True):

    print("Wlcome to canara Bank ATM" )

    if not a1.pin:
        a1.setPin()
    if a1.verifyPin():

        print(
            """
        1. Deposit
        2. Withdraw
        3. Mini Statement
        4. Change Pin
        """
        )

        #John@Pentagonspace.in


        option  = int (input("Select any one of the option "))


        if option ==1:
            amot=int(input("Enter the amount to deposit "))
            a1.deposit(amot)
            a1.transaction.append(amot)
            print('Avalable balance :',a1.balance)

        if option ==2:
            amount=int(input("Enter the amount to withdraw "))
            a1.withdrawal(amount)
            a1.transaction.append(-amount)
            print('Available Balance :',a1.balance)

        if option == 3:
            dt = datetime.now()
            date=dt.strftime("%d-%m-%y")
            time=dt.strftime("%I :%M %p")

            print(
                f"""
                        Canara Bank
            Data:{date}             Time:{time}

            Last Transaction : 
                
                """
            )
            for transaction in a1.transaction:
                print(transaction)
            print("Available Balance : ",a1.balance)
        if option == 4:
                a1.changePin
            
        