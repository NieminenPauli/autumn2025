
DELIMITER = ","


def collectWords() -> str:
    words = []

    while True:
        w = input("Insert word(empty stops): ")
        if w == "":
            break
        words.append(w)

    return DELIMITER.join(words)


def analyseWords(PWords: str) -> None:
        
        word_list = PWords.split(DELIMITER)

        
        amount = len(word_list)

    
        characters = sum(len(w) for w in word_list)

        
        Avg = characters / amount if amount > 0 else 0

        print(f"- {amount} Words")
        print(f"- {characters} Characters")
        print("- {:.2f} Average word length".format(Avg))


def main() -> None:
    print("Program starting.")

    collected = collectWords()
    analyseWords(collected)

    print("Program ending.")



main()