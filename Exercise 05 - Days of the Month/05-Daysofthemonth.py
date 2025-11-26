days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
        7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

m = int(input("Enter month number (1-12): "))

if 1 <= m <= 12:
    if m == 2:  
        leap = input("Is it a leap year? (yes/no): ").lower()
        if leap == "yes":
            print(f"Month {m} has 29 days")
        else:
            print(f"Month {m} has 28 days")
    else:
        print(f"Month {m} has {days[m]} days")
else:
    print("Invalid month number")



