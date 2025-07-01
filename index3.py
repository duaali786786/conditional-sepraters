num=int(input("Enter your number"))

if num>15:
    print(f"{num} is greater than 15")
    num=int(input("Enter your number"))


elif num==15:
    print(f"{num} is a neither a greater or smaller than 15")


else:
    print(f"{num} is a smaller number")