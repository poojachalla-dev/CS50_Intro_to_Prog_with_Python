def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Format 1: MM/DD/YYYY
            if "/" in date:
                month, day, year = date.split("/")

                month = int(month)
                day = int(day)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

            # Format 2: Month Day, Year
            elif "," in date:
                parts = date.split()
                month_name = parts[0]
                day = parts[1].replace(",", "")
                year = parts[2]

                if month_name in months:
                    month = months.index(month_name) + 1
                    day = int(day)

                    if 1 <= day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break

        except (ValueError, IndexError):
            pass  # invalid input → ask again


if __name__ == "__main__":
    main()
