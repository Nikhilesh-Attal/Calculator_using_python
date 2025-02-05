import math

while True:
    print("Select any operation : \n")
    print("1. Addition\n")
    print("2. Subtraction\n")
    print("3. Multiplication\n")
    print("4. Division\n")
    print("5. Logarithm\n")
    print("6. Trigonometry\n")
    print("7. Exponentiation\n")
    print("8. Calculate distance between two number\n")
    print("9. Exit\n")
    
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
            if(num2>num1):
                a='-'
            while True:
                #sub = math.fabs(sub)
                num2 = float(input("Enter next number (for no more number enter zero): "))
                if num2 == 0:
                    if(a=='-'):
                        print("Result is: ",a,"",sub)
                        break
                    else:
                        print("Subtraction is: ", sub)
                        break
                else:
                    if(sub<num2):
                        a= '-'
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
            tri = str(input("Enter the trigonometric function (sin, cos, tan, cot, sec, cosec): "))
            if(tri=="sin"):
                print("Sine: ", math.sin(radians))
            elif(tri=="cos"):
                print("Cosine: ", math.cos(radians))
            elif(tri=="tan"):
                print("Tangent: ", math.tan(radians))
            elif(tri=="cot"):
                print("Cotangent: ", 1/math.tan(radians))
            elif(tri=="sec"):
                print("Secant: ", 1/math.cos(radians))
            elif(tri=="cosec"):
                print("Cosecant: ", 1/math.sin(radians))
            else:
                print("Error: Invalid trigonometric function.")

        case 7:
            number = float(input("Enter the number whose power is to find"))
            power = float(input("Enter the power"))
            number = pow(number,power)
            print("Number : ",number)

        case 8:
            x1 = float(input("Enter the starting x coordinate"))
            x2 = float(input("Enter the ending x coordinate"))
            y1 = float(input("Enter the starting y coordinate"))
            y2 = float(input("Enter the ending y coordinate"))
            dis=math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
            print("Distance between the given coordinate = ",dis)
        
        case 9:
            print("Exiting...")
            break

        case default:
            print("Invalid choice. Please select a valid operation.")
