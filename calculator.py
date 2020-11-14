num1 = input("Please insert the first number:\n")
signal = input("Operator(+, -, *, /):\n")
num2 = input("Second number:\n")

num1 = float(num1)
num2 = float(num2)

result = None

if signal == "+":
    result = num1 + num2
elif signal == "-":
    result = num1 - num2
elif signal == "*":
    result = num1 * num2
elif signal == "/":
    result = num1 / num2
else:
    print("Invalid input, please revise.")

print("Answer: " + str(result))