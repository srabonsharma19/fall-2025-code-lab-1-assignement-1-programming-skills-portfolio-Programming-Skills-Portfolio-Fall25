Name = input("Enter Name")
Hometown = input("Enter Hometown")
while True:
    Age_input = input("Enter Age: ")
    if Age_input.isdigit():                     
        Age = int(Age_input)                   
        break
    else:
        print("Invalid input. ")
 
Bio = {"Name": Name , "Hometown": Hometown , "Age": Age}

print (f"{Bio ['Name']} \n {Bio ['Hometown']} \n {Bio ['Age']}")

  