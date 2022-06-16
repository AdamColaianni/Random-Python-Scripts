# This is a python script for you to select and then print out special text.
# At the end it prints out the specially formatted string that can be copied and used in other scripts.
# This was build off the information in this website https://stackabuse.com/how-to-print-colored-text-in-python/
# I recommend reading it yourself as there is a lot more that can be done with this.

def text_style():
    print("""Please select the styles of the text you want. If you want more than one seperate them by a space.
    \x1b[0mNormal\x1b[0;0m: 0
    \x1b[1mBold\x1b[0;0m: 1
    \x1b[2mLight\x1b[0;0m: 2
    \x1b[3mItlicized\x1b[0;0m: 3
    \x1b[4mUnderline\x1b[0;0m: 4
    \x1b[5mBlink\x1b[0;0m: 5""")

    user_selection = input("Your selection (default = 0): ")
    if not(user_selection): user_selection = '0'

    output = ""
    user_list = user_selection.split()
    for i, v in enumerate(user_list):
        output += "\x1b["
        match v:
            case '0':
                output += '0'
            case '1':
                output += '1'
            case '2':
                output += '2'
            case '3':
                output += '3'
            case '4':
                output += '4'
            case '5':
                output += '5'
            case _:
                print(f"{i} is not a valid option")
        if i+1 == len(user_list):
            output += ';'
        else:
            output += 'm'
    return output

def text_color():
    print("""Please select the text color you want.
    \x1b[0;30mBlack\x1b[0;0m: 0
    \x1b[0;31mRed\x1b[0;0m: 1
    \x1b[0;32mGreen\x1b[0;0m: 2
    \x1b[0;33mYellow\x1b[0;0m: 3
    \x1b[0;34mBlue\x1b[0;0m: 4
    \x1b[0;35mPurple\x1b[0;0m: 5
    \x1b[0;36mCyan\x1b[0;0m: 6
    \x1b[0;37mWhite\x1b[0;0m: 7""")

    while True:
        try:
            user_selection = input("Your selection (default = 7): ")
            if not(user_selection): user_selection = '7'
            user_selection = int(user_selection)
            break
        except ValueError:
            print("Invalid Input")

    output = ""
    match user_selection:
        case 0:
            output += "30"
        case 1:
            output += "31"
        case 2:
            output += "32"
        case 3:
            output += "33"
        case 4:
            output += "34"
        case 5:
            output += "35"
        case 6:
            output += "36"
        case 7:
            output += "37"
        case _:
            print(f"{i} is not a valid option")
    return output

def text_bg_color():
    print("""Please select the text color you want.
    \x1b[0;37;40mBlack\x1b[0;0m: 0
    \x1b[0;30;41mRed\x1b[0;0m: 1
    \x1b[0;30;42mGreen\x1b[0;0m: 2
    \x1b[0;30;43mYellow\x1b[0;0m: 3
    \x1b[0;30;44mBlue\x1b[0;0m: 4
    \x1b[0;30;45mPurple\x1b[0;0m: 5
    \x1b[0;30;46mCyan\x1b[0;0m: 6
    \x1b[0;30;47mWhite\x1b[0;0m: 7""")

    while True:
        try:
            user_selection = input("Your selection (default = None): ")
            if not(user_selection): user_selection = '-1'
            user_selection = int(user_selection)
            break
        except ValueError:
            print("Invalid Input")

    output = ""
    match user_selection:
        case -1:
            output += "m"
        case 0:
            output += ";40m"
        case 1:
            output += ";41m"
        case 2:
            output += ";42m"
        case 3:
            output += ";43m"
        case 4:
            output += ";44m"
        case 5:
            output += ";45m"
        case 6:
            output += ";46m"
        case 7:
            output += ";47m"
        case _:
            print(f"{i} is not a valid option")
    return output

def main():
    print("\n\x1b[1m\x1b[3m\x1b[4;32;44mWelcome to the automatic text colorizer\x1b[0;0m\n")
    style = text_style()
    print()
    color = text_color()
    print()
    bg_color = text_bg_color()
    print()

    user_string = input("Enter you text: ")
    print()

    end = "\x1b[0;0m"
    final = style + color + bg_color
    print(f"{final}{user_string}{end}")

    print(f"\nHere is the string that makes it all happen\n{repr(final + user_string + end)}")

if __name__=="__main__":
    main()
