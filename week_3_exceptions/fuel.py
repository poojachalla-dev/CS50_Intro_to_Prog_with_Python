def main():
    percent = fuel()
    
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")


def fuel():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0 or x > y:
                continue

            percent = round((x / y) * 100)
            return percent

        except (ValueError, ZeroDivisionError):
            continue


main()
