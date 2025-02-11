print("welcome to tip caluculator!")

total_bill = float(input("what was the total bill?$\n"))
bil_percentage = int(input("how much percentage would you like to give 10,12,15 ?$\n"))
bill_people = int(input("how many person would you like to split the bill? \n"))


percentage = (bil_percentage / 100) * total_bill

add_percentage = total_bill + percentage

split_the_bill = round(add_percentage /bill_people,2)

print(f"each peron should pay {split_the_bill}")
