balance = 1000

def deposit(amount):
    global balance
    balance += amount

def show_local_balance():
    balance = 500
    print("Local balance:", balance)

print("Initial balance:", balance)
deposit(250)
print("Balance after deposit:", balance)
show_local_balance()
print("Account balance:", balance)
