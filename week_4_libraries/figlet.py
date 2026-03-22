import sys
from pyfiglet import Figlet
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Case 1: No arguments → random font
    if len(sys.argv) == 1:
        font = random.choice(fonts)

    # Case 2: Two arguments → specific font
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

        if sys.argv[2] not in fonts:
            sys.exit("Invalid font")

        font = sys.argv[2]

    # Invalid number of arguments
    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=font)

    text = input("Input: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
