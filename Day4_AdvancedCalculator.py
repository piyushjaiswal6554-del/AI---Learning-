# Loop Calculator (Fixed)

while True:
    print("\nSelect operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Calculator is closed")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == '1':
        print("Result:", a + b)

    elif choice == '2':
        print("Result:", a - b)

    elif choice == '3':
        print("Result:", a * b)

    elif choice == '4':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid choice")