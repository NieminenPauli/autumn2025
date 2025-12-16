def main() -> None:
    print("Program starting.")

    try:
        # RED
        r_in = input("Insert red: ")
        if not r_in.isdigit():
            print(f"\"{r_in}\" is non-numeric value.")
            raise ValueError
        r = int(r_in)
        if not (0 <= r <= 255):
            print(f"Value \"{r}\" is out of the range 0-255.")
            raise ValueError

        # GREEN
        g_in = input("Insert green: ")
        if not g_in.isdigit():
            print(f"\"{g_in}\" is non-numeric value.")
            raise ValueError
        g = int(g_in)
        if not (0 <= g <= 255):
            print(f"Value \"{g}\" is out of the range 0-255.")
            raise ValueError

        # BLUE
        b_in = input("Insert blue: ")
        if not b_in.isdigit():
            print(f"\"{b_in}\" is non-numeric value.")
            raise ValueError
        b = int(b_in)
        if not (0 <= b <= 255):
            print(f"Value \"{b}\" is out of the range 0-255.")
            raise ValueError

        # ==========================
        #   RGB WAS VALID → PRINT
        # ==========================
        print("RGB Details:")
        print(f"- Red {r}")
        print(f"- Green {g}")
        print(f"- Blue {b}")

        # Hex formatting {:02x}
        hex_value = f"#{r:02x}{g:02x}{b:02x}"
        print(f"- Hex {hex_value}")

        # Binary 8-bit formatting {:08b}
        print(f"- R-byte(base-2): {r:08b}")
        print(f"- G-byte(base-2): {g:08b}")
        print(f"- B-byte(base-2): {b:08b}")

    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")
