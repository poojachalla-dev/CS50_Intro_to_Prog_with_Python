user_prompt = input("camelCase: ")

def camel_to_snake(camel_str):
    snake_str = ""
    for char in camel_str:
        if char.isupper():
            snake_str += "_" + char.lower()
        else:
            snake_str += char
    return snake_str
snake_case = camel_to_snake(user_prompt)
print("snake_case:", snake_case)
