balance = 1000



print("Welcome to the ATM")
print("1. Check Balance")
print("2. Withdraw Money")
print("3. Exit")

choice = input("Enter your choice: ")

if choice == '1':
    print(f"Your current balance is: ${balance}")
elif choice == '2':
    amount = float(input("Enter withdrawal amount: "))
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"${amount} withdrawn successfully. Remaining balance: ${balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid withdrawal amount.")

elif choice == '3':
    print("Thank you for using the ATM. Goodbye!")

else:
    print("Invalid choice. Please try again.")



        
    