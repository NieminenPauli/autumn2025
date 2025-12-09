LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(ch: str, alphabets: str) -> str:
 
    index = alphabets.index(ch)
    return alphabets[(index + 13) % 26]


def rot13(text: str) -> str:

    result = ""

    for ch in text:
        if ch in LOWER_ALPHABETS:
            result += shiftCharacter(ch, LOWER_ALPHABETS)
        elif ch in UPPER_ALPHABETS:
            result += shiftCharacter(ch, UPPER_ALPHABETS)
        else:
            result += ch  # numbers, punctuation, space unchanged

    return result


def collect_plaintext() -> list[str]:
   
    print("\nCollecting plain text rows for ciphering.")
    rows = []

    while True:
        text = input("Insert row(empty stops): ")
        if text == "":
            break
        rows.append(text)

    return rows


def cipher_rows(rows: list[str]) -> list[str]:
  
    return [rot13(r) for r in rows]


def display_ciphered(rows: list[str]):

    print("\n#### Ciphered text ####")
    for r in rows:
        print(r)


def writeFile(filename: str, content: str):
   
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(content)


def save_ciphered(rows: list[str]):
   
    filename = input("Insert filename to save: ")
    content = "\n".join(rows) + "\n" 
    writeFile(filename, content)
    print("Ciphered text saved!")


def main():
    print("Program starting.")

    plain = collect_plaintext()
    ciphered = cipher_rows(plain)

    if len(ciphered) == 0:
        print("No rows entered. Program ending.")
        return

    print("\nShow ciphered text or save it?")
    choice = input("Type S to show, F to save: ").lower()

    if choice == "f":
        save_ciphered(ciphered)
    else:
        display_ciphered(ciphered)

    print("Program ending.")


if __name__ == "__main__":
    main()