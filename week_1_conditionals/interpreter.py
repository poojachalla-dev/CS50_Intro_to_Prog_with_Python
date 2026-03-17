user_prompt = input("Expression: ")

x, operator, y = user_prompt.split()

x = float(x)
y = float(y)

if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y

print(result)
