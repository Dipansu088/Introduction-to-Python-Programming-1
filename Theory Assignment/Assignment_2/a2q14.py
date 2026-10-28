# Write a simple ATM program that takes the PIN as user input and execute as per the for the following:
# i. Check whether the PIN is correct.
# ii. If PIN is correct, check whether sufficient balance is available. (set minimum balance as ₹5000/-)
# iii. If sufficient balance is available, allow withdrawal. (Just print the message as: “Withdrawal allowed”)

correct_Pin=2026
min_Balance=5000
available_Balance=7000

pin=int(input("Enter your PIN: "))

if pin==correct_Pin:
    print("Hola Amigo!!!")
    if available_Balance>=min_Balance:
        print("Sufficient Balance")
        print("Withdrawal allowed")
    else:
        print("Insufficient balance")
else:
    print("Enter correct PIN")