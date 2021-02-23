invalid_msg = "Invalid value."


# RGB TO HEX CONVERTER
def rgb_hex():
    red = int(input("Enter the Red value: "))
    if red < 0 or red > 255:
        print(invalid_msg)
        return
    green = int(input("Enter the Green value: "))
    if green < 0 or green > 255:
        print(invalid_msg)
        return
    blue = int(input("Enter the Blue value: "))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return

    val = (red << 16) + (green << 8) + blue
    print(f"{hex(val[2:]).upper()}")


# HEX TO RGB CONVERTER
def hex_rgb():
    hex_val = input("Enter a hexadecimal input: ")
    if len(hex_val) != 6:
        print(invalid_msg)
        return
    else:
        hex_val = int(hex_val, 16)

    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits

    print(f"R: {red}  G: {green}  B: {blue} \n")


# USER OPTIONS
def convert():
    while True:
        option = input("1 : RGB to HEX\n2: HEX to RGB\nX: Exit\nYour choice: ")

        if option == '1':
            print("RGB to Hex...")
            rgb_hex()
        elif option == '2':
            print("Hex to RGB")
            hex_rgb()
        elif option == 'X':
            break
        else:
            print("Error.")
