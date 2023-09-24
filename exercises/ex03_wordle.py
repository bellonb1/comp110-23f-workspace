"""Hit web game Wordle."""

__author__: str = "730656976"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(string_searched: str, search_char: str) -> bool:
    """Returns true if the second string is found at any index of the first."""
    assert len(search_char) == 1
    index: int = 0
    hasChar: bool = False
    while index < len(string_searched):
        if string_searched[index] == search_char:
            hasChar = True
        index += 1
    return hasChar

def emojified(guess: str, secret: str) -> str:
    """Converts character logic into printable string of emojis."""
    assert len(guess) == len(secret)
    emoji_str: str = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            emoji_str += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX
    return emoji_str

def input_guess(expected_length:int) -> str:
    """Allows the user to input a valid guess."""
    input_word: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(input_word) != expected_length:
        input_word = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return input_word

def main() -> None:
    """Main function, starts game."""
    turn: int = 1
    secret: str = "python"

    while turn < len(secret) + 1:
        print("=== Turn " + str(turn) + "/" + str(len(secret)) + " ===")
        user_input = input_guess(len(secret))
        print(emojified(user_input, secret))
        if user_input == secret:
            print("You won in " + str(turn) + "/" + str(len(secret)) + " turns!")
            exit()
        turn += 1
    print("X/" + str(len(secret)) + " - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()




# print(box_string)

# if input_guess == secret:   
#     print("Woo! You got it!")
# else:
#     print("Not quite. Play again soon!")