import math

while True:
    print("Select any operation : \n")
    print("1. Addition\n")
    print("2. Subtraction\n")
    print("3. Multiplication\n")
    print("4. Division\n")
    print("5. Logarithm\n")
    print("6. Trigonometry\n")
    print("7. Exit\n")
    
    try:
        choose = int(input())
    except:
        print("Invalid input. Please enter a number.")
        continue

    match choose:
        case 1:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
            total_sum = 0
            while True:
                if num == 0:
                    print("Total Sum is: ", total_sum)
                    break
                num = float(input("Enter a number (for no more number enter zero): "))
                total_sum += num

        case 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            sub = num1 - num2
            while True:
                num2 = float(input("Enter next number (for no more number enter zero): "))
                if num2 == 0:
                    print("Result is: ", sub)
                    break
                sub -= num2

        case 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            product = num1 * num2
            while True:
                if num2 == 0:
                    print("Result is: ", product)
                    break
                num2 = float(input("Enter next number (for no more number enter zero): "))
                product *= num2

        case 4:
            num1 = float(input("Enter numerator: "))
            num2 = float(input("Enter denominator: "))
            if num2 != 0:
                division_result = num1 / num2
                print("Result is: ", division_result)
            else:
                print("Error: Division by zero.")

        case 5:
            num = float(input("Enter a number for logarithm: "))
            base = int(input("Enter the base of logarithm: "))
            if num > 0:
                log_result = math.log(num,base)
                print("Logarithm is: ", log_result)
            else:
                print("Error: Logarithm of non-positive number.")

        case 6:
            angle = float(input("Enter angle in degrees: "))
            radians = math.radians(angle)
            tri = str(input("Enter the trigonometric function (sin, cos, tan): "))
            if(tri=="sin"):
                print("Sine: ", math.sin(radians))
            elif(tri=="cos"):
                print("Cosine: ", math.cos(radians))
            elif(tri=="tan"):
                print("Tangent: ", math.tan(radians))

        case 7:
            print("Exiting...")
            break

        case default:
            print("Invalid choice. Please select a valid operation.")