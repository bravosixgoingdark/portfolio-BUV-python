def integers(a, b): # function to swap two integers
    list = [a, b]
    reversed = list[::-1] # Return the reversed list
    return reversed

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Before swapping: ", a, b)
    a, b = integers(a, b)
    print("After swapping: ", a, b)

if __name__ == "__main__":
    main()

    