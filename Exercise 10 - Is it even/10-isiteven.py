def check_even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

# Main function
def main():
    num = int(input("Enter a number: "))   # ask user
    message = check_even_odd(num)          # call function
    print(num, "is", message)              # print result

# Run the program
if __name__ == "__main__":
    main()
