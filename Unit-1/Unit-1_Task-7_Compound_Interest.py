principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time in years: "))
amount = principal * (1 + rate / 100) ** time
print("Compound interest =", amount - principal)
print("Total amount =", amount)
