conti = "c"
while conti == "c":
    a = float(input("\nEnter the first number: "))
    b = float(input("Enter the second number: "))
    oper = input("Enter the operation (+, -, *, /,^): ")

    match oper:
        case "+":
            result = a+b
        case "-":
            result = a-b
        case "*":
            result = a*b
        case "/":
            result = a/b
        case "^":
            result = a**b

    print(f"\nKet qua = {result:.2f}")

    conti = input("\n\tTiep tuc(c/k)? - ")
