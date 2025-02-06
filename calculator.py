import math

while True:
    print("Select any operation : ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Logarithm")
    print("6. Trigonometry")
    print("7. Exponentiation")
    print("8. Calculate distance between two coordinates")
    print("9. Calculate area of circle")
    print("10. Calculate area of rectangle")
    print("11. Calculate area of triangle")
    print("12. Calculate area of square")
    print("13. Calculate area of ellipse")
    print("14. Calculate factorial")
    print("15. Calculate distance between two points")
    print("16. Find number is prime or not")
    print("17. Exit")
    
    try:
        choose = int(input())
    except:
        print("Invalid input. Please enter a number.")
        continue

    match choose:
        case 1:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
            total_sum = num1+num2
            while True:
                num2 = float(input("Enter a number (for no more number enter zero): "))
                if num2 == 0:
                    print("Total Sum is: ", total_sum)
                    break
                else:
                    total_sum += num2

        case 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            sub = num1 - num2
            if(num2>num1):
                a='-'
            while True:
                #sub = math.fabs(sub)  fabs function is use to make negative number into positive number
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
           # print(product)
            while True:
                num2 = float(input("Enter next number (for no more number enter zero): "))
                if num2 == 0:
                    print("Result is: ", product)
                    break
                else:
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

        case 6:     #study about angle, degree, radian and their convator also which value is to print.
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
            number = float(input("Enter the number whose power is to find "))
            power = float(input("Enter the power "))
            number = pow(number,power)
            print("Number : ",number)

        case 8:
            x1 = float(input("Enter the starting x coordinate "))
            x2 = float(input("Enter the ending x coordinate "))
            y1 = float(input("Enter the starting y coordinate "))
            y2 = float(input("Enter the ending y coordinate "))
            dis=math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
            print("Distance between the given coordinate = ",dis)
        
        case 9:
            radius = float(input("Enter the radius of the circle "))
            print("Area of the circle = ",math.pi*pow(radius,2))        #math.pi give pi value = 3.14

        case 10:
            length = float(input("Enter length of the rectangle "))
            breadth = float(input("Enter breadth of the rectangle "))
            area= length*breadth
            print("Area of rectangle = ",area)
            print("Perimeter of rectangle = ",2*(length+breadth))

        case 14:
            num = int(input("Enter the number upto which factorial series has to print "))
            factorial = math.factorial(num)
            print("Factorial number = ",factorial)

        case 16:
            num = int(input("Enter the number to check whether it is prime or not "))
            if num == 1:
                print("Given number is not prime number\n")
            else:
                for i in range(2, int(math.sqrt(num))+1):
                    if num %i==0:
                        print("Number is not a prime number")
                    else:
                        print("Number is prime number")

        case 17:
            print("Exiting...")
            break

        case default:
            print("Invalid choice. Please select a valid operation.")
