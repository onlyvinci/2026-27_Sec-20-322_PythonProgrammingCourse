def simple_interest(principal, time, rate=5):
    return principal * time * rate / 100

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
print("Interest with default rate:", simple_interest(p, t))
r = float(input("Enter explicit rate: "))
print("Interest with explicit rate:", simple_interest(p, t, r))
