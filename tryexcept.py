try:
    age=int(input("Age ?"))
    c=age/0
    print(c)
except ValueError:
    print("Check Again")
except ZeroDivisionError:
    print("No number can be divided by 0")
