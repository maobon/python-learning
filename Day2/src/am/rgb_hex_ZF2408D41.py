def convert_to_hex(r, g, b):
    """
    convert RGB to HEX
    :param r: red
    :param g: green
    :param b: blue
    :return: string HEX color
    """
    return "#{:02X}{:02X}{:02X}".format(r, g, b)


def create_tuple(r, g, b) -> tuple[int, int, int]:
    """
    convert three elements in RGB to tuple
    :param r: red
    :param g: green
    :param b: blue
    :return: tuple
    """
    return int(r), int(g), int(b)


def hex_to_rgb(hex_color):
    """
    hex value to RGB color
    :param hex_color: string hex color
    :return: tuple[int, int, int]
    """
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        raise ValueError("hex_color must be 6 characters long")
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return r, g, b


if __name__ == '__main__':

    color_input = input("Please input your color:\n")

    if '#' in color_input:
        print("HEX color convert to RGB color:", hex_to_rgb(color_input))
    else:
        while True:
            rgb_elements = color_input.split(',')
            for i, rgb_element in enumerate(rgb_elements):
                rgb_element_val = int(rgb_element)
                if rgb_element_val < 0 or rgb_element_val > 255:
                    print("RGB value out of range")
                    continue

            ret = convert_to_hex(*create_tuple(*rgb_elements))
            print(f"RGB color {create_tuple(*rgb_elements)} convert to HEX color:", ret)
            break
