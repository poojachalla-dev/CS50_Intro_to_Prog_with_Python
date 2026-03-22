def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 1. Length check
    if len(s) < 2 or len(s) > 6:
        return False

    # 2. First two must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # 3. Only letters and numbers allowed
    if not s.isalnum():
        return False

    # 4. Numbers rules
    number_started = False

    for char in s:
        if char.isdigit():
            if not number_started:
                number_started = True
                # First number cannot be '0'
                if char == '0':
                    return False
        else:
            # If letter appears after number → invalid
            if number_started:
                return False

    return True


if __name__ == "__main__":
    main()
