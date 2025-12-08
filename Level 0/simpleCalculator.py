print("--- SIMPLE CALCULATOR ---")

while True:
    print("\n===Main Menu===")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

    choice = input("Enter Your Choice (1-5)")

    if choice == "1":
        print("\n---- ADDITION ----")
        number1 = int(input("Enter First Number: "))
        number2 = int(input("Enter Second Number: "))
        result = number1 + number2
        print(f"Answer is: {result}")

    elif choice == "2":
        print("\n---- SUBTRACTION ----")
        number1 = int(input("Enter First Number: "))
        number2 = int(input("Enter Second Number: "))
        result = number1 - number2
        print(f"Answer is: {result}")

    elif choice == "3":
        print("\n---- MULTIPLICATION ----")
        number1 = int(input("Enter First Number: "))
        number2 = int(input("Enter Second Number: "))
        result = number1 * number2
        print(f"Answer is: {result}")

    elif choice == "4":
        print("\n---- DIVISION ----")
        number1 = int(input("Enter First Number: "))
        number2 = int(input("Enter Second Number: "))

        if number2 == 0:
            print("Can not divide by 0")
        else:
            result = number1 / number2
            print(f"Answer is: {result}")

    elif choice == "5":
        print("Exiting Program...")  
        break
    
    else:
        print("Invalid Choice. Please Enter (1-5)")