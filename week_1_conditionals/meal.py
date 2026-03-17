def main():
    time = input("What time is it? ")
    t = convert(time)

    if t >= 7.0 and t < 8.0:
        print("Breakfast time")
    elif t >= 12.0 and t < 13.0:
        print("Lunch time")
    elif t >= 18.0 and t < 19.0:
        print("Dinner time")
    else:
        print("Invalid time")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
